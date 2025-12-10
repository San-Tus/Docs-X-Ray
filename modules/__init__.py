"""
Docs X-Ray modules.

This package contains all the modular components for document scanning:
- cli: Command-line interface and argument parsing
- constants: Configuration constants (file extensions, etc.)
- file_extractors: Text extraction from various file formats
- scanners: Sensitive word scanning logic
- exporters: Export functionality (CSV, XLSX, JSON)
- html_reporting: HTML report generation
- utils: Utility functions (warning suppression, etc.)
- svg_icons: SVG icons for HTML reports
"""

from .cli import parse_arguments, create_parser
from .constants import SUPPORTED_EXTENSIONS
from .file_extractors import extract_text_from_file
from .scanners import scan_folder, load_sensitive_words
from .exporters import export_statistics_csv, export_statistics_xlsx, export_statistics_json
from .html_reporting import generate_html_report
from .utils import suppress_warnings_and_stderr, suppress_pdf_warnings
from .svg_icons import get_category_icon, get_status_icon, get_all_categories

__all__ = [
    'parse_arguments',
    'create_parser',
    'SUPPORTED_EXTENSIONS',
    'extract_text_from_file',
    'scan_folder',
    'load_sensitive_words',
    'export_statistics_csv',
    'export_statistics_xlsx',
    'export_statistics_json',
    'generate_html_report',
    'suppress_warnings_and_stderr',
    'suppress_pdf_warnings',
    'get_category_icon',
    'get_status_icon',
    'get_all_categories',
]
