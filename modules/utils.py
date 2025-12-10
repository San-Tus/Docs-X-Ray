"""Utility functions for Docs X-Ray."""

import sys
import warnings
from contextlib import contextmanager
from io import StringIO


@contextmanager
def suppress_warnings_and_stderr():
    """Context manager to suppress warnings and stderr output."""
    # Save the original stderr and warnings settings
    old_stderr = sys.stderr
    old_showwarning = warnings.showwarning

    try:
        # Redirect stderr to a null buffer
        sys.stderr = StringIO()

        # Suppress all warnings
        warnings.filterwarnings('ignore')

        yield

    finally:
        # Restore original stderr and warnings
        sys.stderr = old_stderr
        warnings.showwarning = old_showwarning
        warnings.filterwarnings('default')


def suppress_pdf_warnings():
    """Suppress specific warnings from PDF parsing libraries."""
    # Suppress pdfplumber/PIL warnings about color values
    warnings.filterwarnings('ignore', message='.*gray non-stroke color.*')
    warnings.filterwarnings('ignore', message='.*invalid float value.*')

    # Suppress other common PDF warnings
    warnings.filterwarnings('ignore', category=UserWarning, module='pdfplumber')
    warnings.filterwarnings('ignore', category=DeprecationWarning, module='pdfplumber')
