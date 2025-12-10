# SVG Icons Guide for Docs X-Ray

This guide explains how to use and customize SVG icons in Docs X-Ray HTML reports.

## Available Icons

### Category Icons

The following category icons are pre-configured:

| Category | Icon | Description |
|----------|------|-------------|
| `health` | 🏥 | Medical/health related data |
| `credentials` | 🔐 | Passwords, usernames, authentication |
| `financial` | 💳 | Credit cards, bank accounts, financial data |
| `personal_identifiers` | 👤 | Personal information (SSN, passport, etc.) |
| `confidentiality` | 🔒 | Confidential/secret information |
| `location` | 📍 | GPS coordinates, addresses |
| `development_secrets` | ✨ | API keys, tokens, secrets |
| `communication` | 📧 | Email, messages |
| `legal` | ⚖️ | Legal documents, contracts |
| `sensitive_data` | 🔐 | General sensitive data |
| `default` | ℹ️ | Fallback for unknown categories |

### Status Icons

- `success` ✓ - Successful operations
- `warning` ⚠ - Warnings
- `error` ✗ - Errors
- `info` ℹ - Information
- `file` 📄 - File references

## Using Icons in Code

### Get a Category Icon

```python
from modules.svg_icons import get_category_icon

# Get default icon (24px, currentColor)
icon = get_category_icon('health')

# Get with custom size and color
icon = get_category_icon('credentials', size=32, color='#219b95')
```

### Get a Status Icon

```python
from modules.svg_icons import get_status_icon

# Get default icon (20px)
icon = get_status_icon('success')

# Get with custom size
icon = get_status_icon('warning', size=24)
```

### List All Available Categories

```python
from modules.svg_icons import get_all_categories

categories = get_all_categories()
print(categories)
# ['health', 'credentials', 'financial', ...]
```

## Adding Custom Icons

### Finding Icons

Visit [Iconify](https://icon-sets.iconify.design/) to browse thousands of free icons:

1. Search for your desired icon (e.g., "database", "network", "cloud")
2. Click on the icon you like
3. Select "SVG" tab
4. Copy the SVG code

### Adding a New Icon

#### Method 1: Edit the svg_icons.py file directly

Edit `modules/svg_icons.py` and add your icon to the `CATEGORY_ICONS` dictionary:

```python
CATEGORY_ICONS = {
    # ... existing icons ...

    'database': '''<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path fill="currentColor" d="YOUR_SVG_PATH"/></svg>''',
}
```

#### Method 2: Add dynamically at runtime

```python
from modules.svg_icons import add_custom_icon

# Add a custom icon for a new category
svg_code = '''<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path fill="currentColor" d="YOUR_SVG_PATH"/></svg>'''

add_custom_icon('my_category', svg_code)
```

### Creating Category-Specific Sensitive Word Lists

If you create a new category in your `sensitive_words_*.json` file, consider adding a matching icon:

1. **Add your category to the JSON file:**
   ```json
   {
     "my_new_category": [
       "sensitive_word_1",
       "sensitive_word_2"
     ]
   }
   ```

2. **Find an appropriate icon on Iconify**

3. **Add the icon to `modules/svg_icons.py`:**
   ```python
   'my_new_category': '''<svg>...</svg>''',
   ```

The icon will automatically appear in the HTML reports!

## Icon Guidelines

### Best Practices

- **Size**: Default sizes are 24px for categories, 20px for status icons
- **Color**: Use `currentColor` to inherit color from parent element
- **ViewBox**: Keep viewBox as `0 0 24 24` for consistency
- **Simplicity**: Choose simple, clear icons that work at small sizes

### Recommended Icon Sets on Iconify

- **Material Design Icons** - Modern, comprehensive set
- **Font Awesome** - Popular, recognizable icons
- **Heroicons** - Clean, professional icons
- **Lucide** - Beautiful, consistent icons
- **Phosphor Icons** - Flexible, lightweight icons

## Examples

### Example 1: Healthcare Category

```python
# Find a medical icon on Iconify
# Copy the SVG code and add to svg_icons.py

'healthcare': '''<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path fill="currentColor" d="M19 3H5c-1.1 0-1.99.9-1.99 2L3 19c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2m-1 11h-4v4h-4v-4H6v-4h4V6h4v4h4z"/></svg>''',
```

### Example 2: Network Category

```python
'network': '''<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path fill="currentColor" d="M15 20a1 1 0 0 0 1-1v-3h2a1 1 0 0 0 .77-.36a1 1 0 0 0 .15-.85l-1.14-4a1 1 0 0 0-1-.79H12V8h1a1 1 0 0 0 1-1V4a1 1 0 0 0-1-1H4a1 1 0 0 0-1 1v3a1 1 0 0 0 1 1h1v2H3.18a1 1 0 0 0-1 .79l-1.14 4a1 1 0 0 0 .15.85A1 1 0 0 0 2 16h2v3a1 1 0 0 0 2 0v-3h2v3a1 1 0 0 0 2 0v-3h2v3a1 1 0 0 0 1 1z"/></svg>''',
```

## Troubleshooting

### Icon Not Showing

1. **Check category name matches**: Ensure the category name in your JSON file exactly matches the icon key
2. **Verify SVG syntax**: Make sure the SVG code is valid
3. **Check color inheritance**: If icon appears black, try using `color='currentColor'`

### Icon Too Large/Small

Adjust the size parameter:
```python
icon = get_category_icon('health', size=16)  # Smaller
icon = get_category_icon('health', size=32)  # Larger
```

### Icon Wrong Color

Specify the color explicitly:
```python
icon = get_category_icon('health', color='#219b95')
```

## Contributing

If you create useful category icons, consider contributing them back to the project!

## Resources

- [Iconify Icon Sets](https://icon-sets.iconify.design/)
- [Material Design Icons](https://pictogrammers.com/library/mdi/)
- [Heroicons](https://heroicons.com/)
- [Lucide Icons](https://lucide.dev/)
