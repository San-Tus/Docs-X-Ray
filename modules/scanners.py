"""
Scanning logic for detecting sensitive words in files.
"""

import json
import re
from pathlib import Path
from collections import defaultdict
from colorama import Fore, Style
from tabulate import tabulate

from .file_extractors import extract_text_from_file
from .constants import SUPPORTED_EXTENSIONS


def load_sensitive_words(json_path: Path, case_sensitive: bool = False):
    """Load sensitive words from JSON and compile regex patterns."""
    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    compiled = {}
    for category, words in data.items():
        compiled[category] = []
        for word in words:
            # Add word boundaries to match whole words only
            # \b matches word boundaries (between \w and \W)
            pattern = r'\b' + re.escape(word) + r'\b'
            flags = 0 if case_sensitive else re.IGNORECASE
            compiled[category].append(re.compile(pattern, flags))
    return data, compiled


def get_context(text: str, match_start: int, match_end: int, context_chars: int = 40):
    """Extract surrounding context for a match."""
    start = max(0, match_start - context_chars)
    end = min(len(text), match_end + context_chars)

    before = text[start:match_start]
    matched = text[match_start:match_end]
    after = text[match_end:end]

    # Add ellipsis if truncated
    if start > 0:
        before = "..." + before
    if end < len(text):
        after = after + "..."

    return before, matched, after


def scan_file_for_sensitive_words(file_path: Path, patterns_by_category: dict):
    """Scan any supported file type for sensitive words."""
    results = {}

    # Extract text pages from the file
    text_pages = extract_text_from_file(file_path)

    if not text_pages:
        return results

    for page_index, text in enumerate(text_pages):
        # Normalize whitespace
        text = " ".join(text.split())

        for category, patterns in patterns_by_category.items():
            for pattern in patterns:
                matches = list(pattern.finditer(text))
                if matches:
                    # Extract the actual matched text from the first match
                    # instead of trying to clean the pattern
                    word_clean = matches[0].group(0)

                    if category not in results:
                        results[category] = {}
                    if word_clean not in results[category]:
                        results[category][word_clean] = {
                            'pages': [],
                            'contexts': []
                        }

                    results[category][word_clean]['pages'].append(page_index + 1)
                    # Store first context example
                    if len(results[category][word_clean]['contexts']) == 0:
                        before, matched, after = get_context(text, matches[0].start(), matches[0].end())
                        results[category][word_clean]['contexts'].append({
                            'before': before,
                            'matched': matched,
                            'after': after,
                            'page': page_index + 1
                        })
    return results


def print_results(file_name: str, results: dict):
    """Print colored results with context."""
    print(f"\n{Fore.CYAN}{'='*80}")
    print(f"{Fore.CYAN}File: {Style.BRIGHT}{file_name}")
    print(f"{Fore.CYAN}{'='*80}{Style.RESET_ALL}")

    if not results:
        print(f"{Fore.GREEN}[OK] No sensitive terms found.{Style.RESET_ALL}")
        return

    for category, words_dict in results.items():
        print(f"\n{Fore.YELLOW}Category: {Style.BRIGHT}{category}{Style.RESET_ALL}")

        for word, data in words_dict.items():
            pages = data['pages']
            pages_str = ", ".join(map(str, sorted(set(pages))))
            count = len(pages)

            print(f"\n  {Fore.RED}[!] '{word}'{Style.RESET_ALL} - {Fore.MAGENTA}{count} occurrence(s){Style.RESET_ALL} on page(s): {pages_str}")

            # Show context example
            if data['contexts']:
                ctx = data['contexts'][0]
                print(f"  {Fore.BLUE}Context (page {ctx['page']}): {Style.RESET_ALL}", end="")
                print(f"{ctx['before']}{Fore.RED}{Style.BRIGHT}{ctx['matched']}{Style.RESET_ALL}{ctx['after']}")


def print_summary_statistics(stats: dict, total_matches: int, total_files: int):
    """Print a summary table of all findings."""
    print(f"\n{Fore.CYAN}{'='*80}")
    print(f"{Fore.CYAN}{Style.BRIGHT}SUMMARY STATISTICS")
    print(f"{Fore.CYAN}{'='*80}{Style.RESET_ALL}\n")

    if not stats:
        print(f"{Fore.GREEN}[OK] No sensitive terms found in any files.{Style.RESET_ALL}")
        return

    # Prepare table data
    table_data = []
    for category, words in sorted(stats.items()):
        for word, count in sorted(words.items(), key=lambda x: x[1], reverse=True):
            table_data.append([category, word, count])

    # Print summary table
    headers = [
        f"{Fore.YELLOW}Category{Style.RESET_ALL}",
        f"{Fore.YELLOW}Sensitive Term{Style.RESET_ALL}",
        f"{Fore.YELLOW}Total Occurrences{Style.RESET_ALL}"
    ]

    print(tabulate(table_data, headers=headers, tablefmt="grid"))

    # Overall summary
    print(f"\n{Fore.GREEN}{Style.BRIGHT}Overall Summary:{Style.RESET_ALL}")
    print(f"  • Total files scanned: {Fore.CYAN}{total_files}{Style.RESET_ALL}")
    print(f"  • Total matches found: {Fore.RED}{total_matches}{Style.RESET_ALL}")
    print(f"  • Unique terms found: {Fore.MAGENTA}{sum(len(words) for words in stats.values())}{Style.RESET_ALL}")
    print(f"  • Categories with findings: {Fore.YELLOW}{len(stats)}{Style.RESET_ALL}\n")


def scan_folder(folder: Path, sensitive_json: Path, sensitivity_list: str, generate_html: bool = True,
                report_lang: str = "en", recursive: bool = False, output_formats: list = None,
                output_dir: Path = None, case_sensitive: bool = False):
    """Scan a folder for sensitive words in all supported file types."""
    from .html_reporting import generate_html_report
    from .exporters import export_statistics_csv, export_statistics_xlsx, export_statistics_json

    _, compiled_patterns = load_sensitive_words(sensitive_json, case_sensitive=case_sensitive)

    # Collect all supported files
    all_files = []
    glob_pattern = "**/*" if recursive else "*"
    for ext in SUPPORTED_EXTENSIONS:
        all_files.extend(folder.glob(f"{glob_pattern}{ext}"))

    all_files = sorted(all_files)

    if not all_files:
        print(f"{Fore.RED}No supported files found in {folder}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Supported formats: {', '.join(SUPPORTED_EXTENSIONS)}{Style.RESET_ALL}")
        return

    # Count files by type
    file_types = defaultdict(int)
    for file in all_files:
        file_types[file.suffix.lower()] += 1

    print(f"\n{Fore.GREEN}{Style.BRIGHT}Starting scan of {len(all_files)} file(s)...{Style.RESET_ALL}")
    print(f"{Fore.CYAN}File types found: {dict(file_types)}{Style.RESET_ALL}\n")

    # Statistics tracking
    global_stats = defaultdict(lambda: defaultdict(int))
    total_matches = 0
    files_with_hits = 0
    scan_results = []  # Store results for HTML report

    for idx, file_path in enumerate(all_files, 1):
        # Print progress at the top
        print(f"{Fore.CYAN}[{idx}/{len(all_files)}]{Style.RESET_ALL}", end=" ")

        results = scan_file_for_sensitive_words(file_path, compiled_patterns)

        # Store results for HTML report
        scan_results.append({
            'file_path': str(file_path.absolute()),
            'results': results
        })

        # Update statistics
        if results:
            files_with_hits += 1
        for category, words_dict in results.items():
            for word, data in words_dict.items():
                count = len(data['pages'])
                global_stats[category][word] += count
                total_matches += count

        print_results(file_path.name, results)

    # Print summary statistics
    print_summary_statistics(global_stats, total_matches, len(all_files))

    # Determine output directory
    if output_dir is None:
        output_dir = Path(__file__).resolve().parent.parent
    else:
        output_dir.mkdir(parents=True, exist_ok=True)

    # Generate HTML report
    if generate_html:
        html_output = output_dir / f"scan_report_{sensitivity_list}.html"
        try:
            generate_html_report(
                scan_results=scan_results,
                global_stats=global_stats,
                output_path=html_output,
                sensitivity_list=sensitivity_list,
                total_files=len(all_files),
                files_with_hits=files_with_hits,
                total_matches=total_matches,
                file_types=dict(file_types),
                report_lang=report_lang
            )
            print(f"\n{Fore.GREEN}[OK] HTML report generated: {Style.BRIGHT}{html_output}{Style.RESET_ALL}")
        except Exception as e:
            print(f"\n{Fore.RED}[ERROR] Error generating HTML report: {e}{Style.RESET_ALL}")

    # Export statistics in requested formats
    if output_formats and global_stats:
        print(f"\n{Fore.CYAN}{'='*80}")
        print(f"{Fore.CYAN}{Style.BRIGHT}EXPORTING STATISTICS")
        print(f"{Fore.CYAN}{'='*80}{Style.RESET_ALL}\n")

        if 'csv' in output_formats:
            csv_output = output_dir / f"statistics_{sensitivity_list}.csv"
            export_statistics_csv(global_stats, csv_output, len(all_files), files_with_hits, total_matches)

        if 'xlsx' in output_formats:
            xlsx_output = output_dir / f"statistics_{sensitivity_list}.xlsx"
            export_statistics_xlsx(global_stats, xlsx_output, len(all_files), files_with_hits, total_matches)

        if 'json' in output_formats:
            json_output = output_dir / f"statistics_{sensitivity_list}.json"
            export_statistics_json(global_stats, json_output, len(all_files), files_with_hits, total_matches, dict(file_types))
