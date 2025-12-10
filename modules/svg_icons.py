"""
SVG icons for Docs X-Ray HTML reports.
Icons can be found at: https://icon-sets.iconify.design/
"""

# Category icons - using Material Design Icons and other icon sets
CATEGORY_ICONS = {
    'health': '''<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path fill="currentColor" d="M9.616 20.846q-.667 0-1.141-.474Q8 19.897 8 19.23V16H4.77q-.667 0-1.142-.475q-.474-.474-.474-1.14V12.5h5.565l1.854 2.78q.068.105.168.162t.232.058q.173 0 .304-.094t.192-.26l1.677-5.03l1.427 2.146q.076.106.189.172T15 12.5h5.846v1.885q0 .666-.474 1.14q-.475.475-1.141.475H16v3.23q0 .667-.475 1.142q-.474.474-1.14.474zm1.238-6.961l-1.452-2.166q-.067-.104-.167-.161T9 11.5H3.154V9.616q0-.667.474-1.141Q4.103 8 4.77 8H8V4.77q0-.667.475-1.142q.474-.474 1.14-.474h4.77q.666 0 1.14.474Q16 4.103 16 4.77V8h3.23q.667 0 1.142.475q.474.474.474 1.14V11.5h-5.59L13.42 8.72q-.064-.098-.18-.159t-.245-.061q-.167 0-.285.094t-.18.26z"/></svg>''',

    'credentials': '''<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path fill="currentColor" d="M5.039 19q-.441 0-.74-.299T4 17.961v-.607q0-.62.36-1.159q.361-.54.97-.837q1.416-.68 2.834-1.018Q9.58 14 11 14q.446 0 .883.041q.436.042.883.111q.217.044.34.174t.144.347q.108.944.566 1.799t1.197 1.464q.04.03.064.073q.023.043.023.095v.127q0 .31-.23.54t-.54.229zM11 11.77q-1.246 0-2.123-.878Q8 10.016 8 8.77t.877-2.123T11 5.77t2.123.877T14 8.77t-.877 2.123T11 11.77m7.308 2.673q.31 0 .539-.239q.23-.24.23-.55q0-.309-.23-.538t-.54-.23t-.548.23t-.24.539t.24.549t.549.24m.092 6.669l-.75-.77q-.03-.03-.13-.273v-3.43q-.85-.248-1.387-.96q-.537-.71-.537-1.621q0-1.123.794-1.917q.794-.795 1.918-.795t1.907.794t.785 1.918q0 .875-.484 1.538q-.483.663-1.247.962l.67.669q.13.13.13.292t-.13.293l-.589.588q-.13.13-.13.283t.13.283l.608.588q.13.13.13.283t-.13.282l-.992.993q-.131.13-.283.13t-.283-.13"/></svg>''',

    'financial': '''<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path fill="currentColor" d="M6 20q-.825 0-1.412-.587T4 18v-2h2v2h12v-2h2v2q0 .825-.587 1.413T18 20zm-2-4v-2h2v2zm0-4v-2h2v2zm0-4V6q0-.825.588-1.412T6 4h12q.825 0 1.413.588T20 6v2h-2V6H6v2zm4 2h8q.425 0 .713.288T17 11v2q0 .425-.288.713T16 14H8q-.425 0-.712-.288T7 13v-2q0-.425.288-.712T8 10m10 10v-2h2v2zm0-8V6h2v6z"/></svg>''',

    'personal_identifiers': '''<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path fill="currentColor" d="M12 12q-1.65 0-2.825-1.175T8 8t1.175-2.825T12 4t2.825 1.175T16 8t-1.175 2.825T12 12m-8 8v-2.8q0-.85.438-1.562T5.6 14.55q1.55-.775 3.15-1.162T12 13t3.25.388t3.15 1.162q.725.375 1.163 1.088T20 17.2V20z"/></svg>''',

    'confidentiality': '''<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path fill="currentColor" d="M6 22q-.825 0-1.412-.587T4 20V10q0-.825.588-1.412T6 8h1V6q0-2.075 1.463-3.537T12 1t3.538 1.463T17 6v2h1q.825 0 1.413.588T20 10v10q0 .825-.587 1.413T18 22zm6-5q.825 0 1.413-.587T14 15t-.587-1.412T12 13t-1.412.588T10 15t.588 1.413T12 17M9 8h6V6q0-1.25-.875-2.125T12 3t-2.125.875T9 6z"/></svg>''',

    'location': '''<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path fill="currentColor" d="M12 12q.825 0 1.413-.587T14 10t-.587-1.412T12 8t-1.412.588T10 10t.588 1.413T12 12m0 10q-4.025-3.425-6.012-6.362T4 10.2q0-3.75 2.413-5.975T12 2t5.588 2.225T20 10.2q0 2.5-1.987 5.438T12 22"/></svg>''',

    'development_secrets': '''<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path fill="currentColor" d="m12 17l1.175-2.625L16 13.2l-2.825-1.175L12 9.4l-1.175 2.625L8 13.2l2.825 1.175zm0 5l-1.975-4.425L5.6 15.6l-4.425-1.975L5.6 11.65l1.975-4.425L9.55 9.2l4.425-1.975L11.975 12l2.025 4.425L18.425 18.4l4.4 1.975l-4.4 1.975l-1.975 4.425l-2.025-4.45zm4.5-9.5L18.4 9.875l2.375-1.9l-2.375-1.9L16.5 3.5l-1.875 2.575l-2.4 1.9l2.4 1.9z"/></svg>''',

    'communication': '''<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path fill="currentColor" d="M4 20q-.825 0-1.412-.587T2 18V6q0-.825.588-1.412T4 4h16q.825 0 1.413.588T22 6v12q0 .825-.587 1.413T20 20zm8-7l8-5V6l-8 5l-8-5v2z"/></svg>''',

    'legal': '''<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path fill="currentColor" d="m7 21l-.85-4.15l-3.2-3.2L7.15 13L11 11l2 6zm10 0l-4-10l2-6l3.85 1.85l3.2 3.2L17.85 13zm-5-6l-1.4-4.2l4.2-1.4l1.4 4.2zM3 7V5h10v2zm14.8 0L15 4.2L16.4 2.8L20 6.4z"/></svg>''',

    'sensitive_data': '''<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path fill="currentColor" d="M18 8h-1V6c0-2.76-2.24-5-5-5S7 3.24 7 6v2H6c-1.1 0-2 .9-2 2v10c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V10c0-1.1-.9-2-2-2m-6 9c-1.1 0-2-.9-2-2s.9-2 2-2s2 .9 2 2s-.9 2-2 2M9 8V6c0-1.66 1.34-3 3-3s3 1.34 3 3v2z"/></svg>''',

    'default': '''<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path fill="currentColor" d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10s10-4.48 10-10S17.52 2 12 2m1 15h-2v-2h2zm0-4h-2V7h2z"/></svg>''',
}


def get_category_icon(category: str, size: int = 24, color: str = 'currentColor') -> str:
    """Get SVG icon for a category"""
    # Get icon from dict, fallback to default if not found
    icon = CATEGORY_ICONS.get(category.lower(), CATEGORY_ICONS['default'])

    # Adjust size if different from default 24
    if size != 24:
        icon = icon.replace('width="24"', f'width="{size}"')
        icon = icon.replace('height="24"', f'height="{size}"')

    # Adjust color if different from default
    if color != 'currentColor':
        icon = icon.replace('fill="currentColor"', f'fill="{color}"')

    return icon


def get_all_categories() -> list:
    """Get list of all available category icons."""
    return [cat for cat in CATEGORY_ICONS.keys() if cat != 'default']


def add_custom_icon(category: str, svg_code: str) -> None:
    """Add a custom SVG icon for a category."""
    CATEGORY_ICONS[category.lower()] = svg_code


# Status/UI icons
STATUS_ICONS = {
    'success': '''<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24"><path fill="currentColor" d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10s10-4.5 10-10S17.5 2 12 2m-2 15l-5-5l1.41-1.41L10 14.17l7.59-7.59L19 8z"/></svg>''',

    'warning': '''<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24"><path fill="currentColor" d="M1 21h22L12 2zm12-3h-2v-2h2zm0-4h-2v-4h2z"/></svg>''',

    'error': '''<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24"><path fill="currentColor" d="M12 2C6.47 2 2 6.47 2 12s4.47 10 10 10s10-4.47 10-10S17.53 2 12 2m5 13.59L15.59 17L12 13.41L8.41 17L7 15.59L10.59 12L7 8.41L8.41 7L12 10.59L15.59 7L17 8.41L13.41 12z"/></svg>''',

    'info': '''<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24"><path fill="currentColor" d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10s10-4.48 10-10S17.52 2 12 2m1 15h-2v-6h2zm0-8h-2V7h2z"/></svg>''',

    'file': '''<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24"><path fill="currentColor" d="M14 2H6c-1.1 0-1.99.9-1.99 2L4 20c0 1.1.89 2 1.99 2H18c1.1 0 2-.9 2-2V8zm4 18H6V4h7v5h5z"/></svg>''',
}


def get_status_icon(status: str, size: int = 20) -> str:
    """Get status/UI icon"""
    icon = STATUS_ICONS.get(status.lower(), STATUS_ICONS['info'])

    # Adjust size if different from default 20
    if size != 20:
        icon = icon.replace('width="20"', f'width="{size}"')
        icon = icon.replace('height="20"', f'height="{size}"')

    return icon
