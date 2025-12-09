# Docs X-Ray

A comprehensive Python tool for scanning documents and code files for sensitive information.

## Features

- Multi-format document support (PDF, Office, LibreOffice, RTF)
- Code and configuration file analysis (90+ file types)
- Recursive directory scanning
- Customizable sensitivity word lists
- HTML report generation with multilingual support
- Statistical data export in CSV, XLSX, and JSON formats
- Configurable output directory
- Context highlighting for matches

## Supported File Types

**Documents:** PDF, DOCX, DOC, XLSX, XLS, PPTX, PPT, RTF, ODT, ODS, ODP, TXT

**Programming Languages:** Python, JavaScript, TypeScript, Java, C/C++, C#, PHP, Ruby, Go, Rust, Swift, Kotlin, Scala, R, Lua, Perl, Shell scripts, PowerShell

**Web Technologies:** HTML, CSS, SCSS, SASS, LESS, Vue, Svelte

**Configuration Files:** JSON, YAML, TOML, INI, ENV, XML

**Other:** Jupyter Notebooks, Dockerfiles, CI/CD configs, build files

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Basic Scan

```bash
python docs-x-ray.py -d /path/to/documents -s en
```

### Recursive Scan with Statistics Export

```bash
python docs-x-ray.py -d /path/to/folder -s en -r -o all
```

### Export to Specific Output Directory

```bash
python docs-x-ray.py -d /path/to/folder -s en -O ./reports -o xlsx
```

### Options

- `-d, --directory`: Directory containing files to scan (required)
- `-s, --sensitivity-list`: Sensitivity list to use (`en` or `cz`, default: `en`)
- `-r, --recursive`: Recursively scan all subdirectories
- `-l, --lang`: Report language (`en` or `cz`, default: `en`)
- `-o, --output-format`: Export statistics format (`csv`, `xlsx`, `json`, or `all` for all formats)
- `-O, --output-dir`: Output directory for all reports and statistics (default: script directory)
- `-c, --case-sensitive`: Enable case-sensitive matching (default: case-insensitive)
- `--no-html`: Disable HTML report generation

## Sensitivity Categories

The tool scans for the following categories of sensitive information:

- **Personal Identifiers**: Social security numbers, passport numbers, national IDs
- **Financial Information**: Credit cards, bank accounts, IBAN, SWIFT codes
- **Confidential Data**: Trade secrets, proprietary information
- **Credentials**: Usernames, passwords, API keys
- **Health Records**: Medical records, diagnoses, health insurance
- **Location Data**: Addresses, GPS coordinates
- **Development Secrets**: API tokens, encryption keys, database credentials, cloud provider secrets

## Output

The tool generates:

1. **Console Output**: Colored terminal output with match context
2. **HTML Report**: Comprehensive report with statistics and detailed findings (filename: `scan_report_<language>.html`)
3. **CSV Statistics**: Tabular data export with summary statistics (filename: `statistics_<language>.csv`)
4. **XLSX Statistics**: Excel workbook with formatted tables (filename: `statistics_<language>.xlsx`)
5. **JSON Statistics**: Structured data export with metadata (filename: `statistics_<language>.json`)

All output files are saved to the output directory specified with `-O`, or to the script directory by default.

## Examples

```bash
# Scan a project directory recursively with English sensitivity list
python docs-x-ray.py -d ./my-project -s en -r

# Scan with Czech sensitivity list and Czech report
python docs-x-ray.py -d ./documents -s cz -l cz

# Scan and export all statistics formats to a specific directory
python docs-x-ray.py -d ./my-project -s en -r -o all -O ./scan-results

# Export only JSON statistics without HTML report
python docs-x-ray.py -d ./files -s en -o json --no-html

# Scan with XLSX export to custom output folder
python docs-x-ray.py -d ./documents -s en -r -o xlsx -O ~/reports

# Enable case-sensitive matching (matches "Password" but not "password")
python docs-x-ray.py -d ./files -s en -c
```

## Matching Behavior

**Word Boundaries**: The tool uses word boundary matching to find whole words only. For example:
- The term "heslo" (Czech for "password") will match in "moje heslo je tajné"
- But will NOT match in "...lsIorII,respectively—arethestarting andtheslopeoftheirdependenceonF..."

**Case Sensitivity**: By default, matching is case-insensitive. Use the `-c` flag to enable case-sensitive matching.

## Customization

Edit `sensitive_words_en.json` or `sensitive_words_cz.json` to customize the sensitivity word lists for your needs.


```
================================================================================
📊 SUMMARY STATISTICS
================================================================================

+----------------------+-----------------------+---------------------+
| Category             | Sensitive Term        |   Total Occurrences |
+======================+=======================+=====================+
| confidentiality      | tajné                 |                   4 |
+----------------------+-----------------------+---------------------+
| confidentiality      | vlastnické            |                   2 |
+----------------------+-----------------------+---------------------+
| credentials          | API klíč              |                   2 |
+----------------------+-----------------------+---------------------+
| credentials          | heslo                 |                   1 |
+----------------------+-----------------------+---------------------+
| development_secrets  | seed                  |                 176 |
+----------------------+-----------------------+---------------------+
| development_secrets  | public_key            |                  33 |
+----------------------+-----------------------+---------------------+
| development_secrets  | access_token          |                  24 |
+----------------------+-----------------------+---------------------+
| development_secrets  | private_key           |                  23 |
+----------------------+-----------------------+---------------------+
| development_secrets  | client_id             |                   7 |
+----------------------+-----------------------+---------------------+
| development_secrets  | auth_token            |                   6 |
+----------------------+-----------------------+---------------------+
| development_secrets  | cookie_secret         |                   5 |
+----------------------+-----------------------+---------------------+
| development_secrets  | oauth_token           |                   4 |
+----------------------+-----------------------+---------------------+
| development_secrets  | client_secret         |                   2 |
+----------------------+-----------------------+---------------------+
| development_secrets  | consumer_key          |                   2 |
+----------------------+-----------------------+---------------------+
| development_secrets  | consumer_secret       |                   2 |
+----------------------+-----------------------+---------------------+
| development_secrets  | slack_token           |                   2 |
+----------------------+-----------------------+---------------------+
| development_secrets  | master_key            |                   1 |
+----------------------+-----------------------+---------------------+
| development_secrets  | api_token             |                   1 |
+----------------------+-----------------------+---------------------+
| development_secrets  | aws_access_key_id     |                   1 |
+----------------------+-----------------------+---------------------+
| development_secrets  | aws_secret_access_key |                   1 |
+----------------------+-----------------------+---------------------+
| development_secrets  | encryption_key        |                   1 |
+----------------------+-----------------------+---------------------+
| development_secrets  | refresh_token         |                   1 |
+----------------------+-----------------------+---------------------+
| financial            | SWIFT                 |                  18 |
+----------------------+-----------------------+---------------------+
| financial            | IBAN                  |                   8 |
+----------------------+-----------------------+---------------------+
| financial            | CVV                   |                   8 |
+----------------------+-----------------------+---------------------+
| health               | zdravotní pojištění   |                   3 |
+----------------------+-----------------------+---------------------+
| location             | GPS                   |                  26 |
+----------------------+-----------------------+---------------------+
| location             | adresa                |                  17 |
+----------------------+-----------------------+---------------------+
| location             | souřadnice            |                   8 |
+----------------------+-----------------------+---------------------+
| personal_identifiers | rodné číslo           |                  10 |
+----------------------+-----------------------+---------------------+
| personal_identifiers | datum narození        |                  10 |
+----------------------+-----------------------+---------------------+

Overall Summary:
  • Total files scanned: 23964
  • Total matches found: 409
  • Unique terms found: 31
  • Categories with findings: 7
```
