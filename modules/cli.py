"""
Command-line interface for Docs X-Ray.
Enhanced argument parsing with better help text and examples.
"""

import argparse
import textwrap
from pathlib import Path


VERSION = "1.0.0"


class CustomHelpFormatter(argparse.RawDescriptionHelpFormatter):
    """Custom formatter for better help text layout."""

    def __init__(self, prog):
        super().__init__(prog, max_help_position=35, width=100)


def create_parser():
    """Create and configure the argument parser with enhanced help text."""

    description = textwrap.dedent("""
    ========================================================================
                            DOCS X-RAY v{version}
    ========================================================================
    Scan documents and code files for sensitive words and phrases
    Supports 50+ file formats including PDFs, Office docs, and code
    ========================================================================
    """.format(version=VERSION))

    epilog = textwrap.dedent("""
    EXAMPLES:
      Basic scan of current directory (English sensitivity list):
        python docs-x-ray.py -d .

      Recursive scan with Czech sensitivity list:
        python docs-x-ray.py -d /path/to/docs -s cz -r

      Generate all export formats with custom output directory:
        python docs-x-ray.py -d ./documents -o all -O ./reports

      Case-sensitive scan without HTML report:
        python docs-x-ray.py -d ./code -c --no-html

      Generate Czech language HTML report:
        python docs-x-ray.py -d ./docs -s cz -l cz -o xlsx

    SUPPORTED FILE FORMATS:
      Documents:  PDF, DOCX, XLSX, PPTX, RTF, ODT, ODS, ODP, TXT
      Code:       PY, JS, TS, JAVA, CPP, C, CS, PHP, RB, GO, RS, SWIFT, etc.
      Web:        HTML, CSS, SCSS, VUE, SVELTE
      Config:     JSON, YAML, TOML, INI, ENV, XML
      Notebooks:  IPYNB (Jupyter)
      And many more...

    OUTPUT FILES:
      HTML Report:     scan_report_<sensitivity-list>.html
      CSV Stats:       statistics_<sensitivity-list>.csv
      XLSX Stats:      statistics_<sensitivity-list>.xlsx
      JSON Stats:      statistics_<sensitivity-list>.json

    For more information and updates:
      GitHub: https://github.com/San-Tus/Docs-X-Ray
    """)

    parser = argparse.ArgumentParser(
        description=description,
        epilog=epilog,
        formatter_class=CustomHelpFormatter,
        add_help=True
    )

    # Required arguments
    required = parser.add_argument_group('REQUIRED ARGUMENTS')
    required.add_argument(
        "-d",
        "--directory",
        required=True,
        metavar="PATH",
        help="Directory containing files to scan"
    )

    # Sensitivity and language options
    sensitivity = parser.add_argument_group('SENSITIVITY & LANGUAGE OPTIONS')
    sensitivity.add_argument(
        "-s",
        "--sensitivity-list",
        choices=["cz", "en"],
        default="en",
        metavar="LANG",
        help="Sensitive words list: 'cz' (Czech) or 'en' (English) [default: en]"
    )
    sensitivity.add_argument(
        "-l",
        "--lang",
        choices=["en", "cz"],
        default="en",
        metavar="LANG",
        help="Report language: 'en' (English) or 'cz' (Czech) [default: en]"
    )
    sensitivity.add_argument(
        "-c",
        "--case-sensitive",
        action="store_true",
        help="Enable case-sensitive matching [default: case-insensitive]"
    )

    # Scanning options
    scanning = parser.add_argument_group('SCANNING OPTIONS')
    scanning.add_argument(
        "-r",
        "--recursive",
        action="store_true",
        help="Recursively scan all subdirectories"
    )

    # Output options
    output = parser.add_argument_group('OUTPUT OPTIONS')
    output.add_argument(
        "--no-html",
        action="store_true",
        help="Disable HTML report generation"
    )
    output.add_argument(
        "-o",
        "--output-format",
        choices=["csv", "xlsx", "json", "all"],
        metavar="FORMAT",
        help="Export statistics: 'csv', 'xlsx', 'json', or 'all' for all formats"
    )
    output.add_argument(
        "-O",
        "--output-dir",
        metavar="PATH",
        help="Output directory for reports and statistics [default: script directory]"
    )


    return parser


def parse_arguments():
    """Parse and validate command-line arguments."""
    parser = create_parser()
    args = parser.parse_args()

    # Validate directory
    folder_to_scan = Path(args.directory).expanduser()
    if not folder_to_scan.is_dir():
        parser.error(f"Directory not found: {folder_to_scan}")

    # Parse output formats
    output_formats = None
    if args.output_format:
        if args.output_format == "all":
            output_formats = ["csv", "xlsx", "json"]
        else:
            output_formats = [args.output_format]

    # Parse output directory
    output_dir = None
    if args.output_dir:
        output_dir = Path(args.output_dir).expanduser()

    return {
        'folder': folder_to_scan,
        'sensitivity_list': args.sensitivity_list,
        'report_lang': args.lang,
        'recursive': args.recursive,
        'generate_html': not args.no_html,
        'output_formats': output_formats,
        'output_dir': output_dir,
        'case_sensitive': args.case_sensitive
    }
