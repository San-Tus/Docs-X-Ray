#!/usr/bin/env python3
# GitHub: https://github.com/San-Tus/Docs-X-Ray
"""Docs X-Ray - A tool to scan documents for sensitive information."""

import sys
from pathlib import Path
from colorama import Fore, Style, init

from modules.cli import parse_arguments
from modules.scanners import scan_folder

# Set UTF-8 encoding for console output on Windows
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except AttributeError:
        # Python < 3.7
        import codecs
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
        sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

# Initialize colorama for Windows color support
init(autoreset=True)


def main():
    """Main entry point for Docs X-Ray."""
    # Parse command-line arguments
    config = parse_arguments()

    # Locate sensitive words file
    script_dir = Path(__file__).resolve().parent
    sensitive_words_file = script_dir / f"sensitive_words_{config['sensitivity_list']}.json"

    if not sensitive_words_file.is_file():
        print(f"{Fore.RED}Sensitive words file not found: {sensitive_words_file}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Please ensure the file exists in the script directory.{Style.RESET_ALL}")
        return

    # Print configuration info
    print(f"{Fore.GREEN}Using sensitivity list: {Style.BRIGHT}{config['sensitivity_list'].upper()}{Style.RESET_ALL} ({sensitive_words_file.name})")
    if config['recursive']:
        print(f"{Fore.CYAN}Recursive mode: {Style.BRIGHT}ENABLED{Style.RESET_ALL} - scanning all subdirectories")
    if config['case_sensitive']:
        print(f"{Fore.CYAN}Case-sensitive matching: {Style.BRIGHT}ENABLED{Style.RESET_ALL}")
    if config['output_dir']:
        print(f"{Fore.CYAN}Output directory: {Style.BRIGHT}{config['output_dir']}{Style.RESET_ALL}")

    # Run the scan
    scan_folder(
        folder=config['folder'],
        sensitive_json=sensitive_words_file,
        sensitivity_list=config['sensitivity_list'],
        generate_html=config['generate_html'],
        report_lang=config['report_lang'],
        recursive=config['recursive'],
        output_formats=config['output_formats'],
        output_dir=config['output_dir'],
        case_sensitive=config['case_sensitive']
    )


if __name__ == "__main__":
    main()
