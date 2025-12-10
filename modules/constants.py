"""
Constants and configuration for Docs X-Ray.
"""

# Supported file extensions
SUPPORTED_EXTENSIONS = [
    # Documents
    '.pdf', '.docx', '.doc', '.xlsx', '.xls', '.pptx', '.ppt', '.rtf', '.odt', '.ods', '.odp', '.txt',
    # Programming languages
    '.py', '.js', '.ts', '.jsx', '.tsx', '.java', '.cpp', '.c', '.h', '.hpp', '.cs', '.php', '.rb', '.go',
    '.rs', '.swift', '.kt', '.scala', '.r', '.m', '.lua', '.pl', '.sh', '.bash', '.zsh', '.fish', '.ps1',
    # Notebooks
    '.ipynb',
    # Web technologies
    '.html', '.htm', '.css', '.scss', '.sass', '.less', '.vue', '.svelte',
    # Configuration files
    '.json', '.yaml', '.yml', '.toml', '.ini', '.cfg', '.conf', '.config', '.properties', '.env',
    # Markup and data
    '.xml', '.md', '.markdown', '.rst', '.tex', '.csv', '.tsv',
    # Build and package files
    '.gradle', '.maven', '.sbt', '.rake', '.make', '.cmake',
    # Docker and container
    '.dockerfile', '.dockerignore', '.containerfile',
    # CI/CD
    '.gitlab-ci.yml', '.travis.yml', '.circleci',
    # Other config/script files
    '.gitignore', '.gitattributes', '.editorconfig', '.htaccess', '.npmrc', '.babelrc', '.eslintrc',
    '.prettierrc', '.stylelintrc', '.jshintrc', '.ansible', '.terraform', '.tf', '.tfvars'
]
