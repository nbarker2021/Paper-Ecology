import re

with open(r'D:\Paper Ecology\build_paper_ecology_meta.py', 'r') as f:
    content = f.read()

old_func = '''def normalize_paper_number(pn):
    """Normalize paper number to paper-XX format."""
    if pn is None:
        return None
    if isinstance(pn, int):
        return f'paper-{pn:02d}' if pn < 100 else f'paper-{pn}'
    s = str(pn).strip().lower()
    # Remove 'paper-' prefix if present to get the number
    m = re.match(r'paper[-_]?(\\\\\\=+)', s)
    if m:
        num = int(m.group(1))
        return f'paper-{num:02d}' if num < 100 else f'paper-{num}'
    # Try to parse as raw number
    try:
        num = int(s)
        return f'paper-{num:02d}' if num < 100 else f'paper-{num}'
    except ValueError:
        return s'''

new_func = '''def normalize_paper_number(pn):
    """Normalize paper number to paper-XX format. Only accepts valid paper numbers 0-100."""
    if pn is None:
        return None
    if isinstance(pn, int):
        if 0 <= pn <= 100:
            return f'paper-{pn:02d}' if pn < 100 else f'paper-{pn}'
        return None
    s = str(pn).strip().lower()
    # Match paper-XX or paper_XX where XX is 0-100
    m = re.match(r'paper[-_]?(
    )
    if m:
        try:
            num = int(m.group(1))
            if 0 <= num <= 100:
                return f'paper-{num:02d}' if num < 100 else f'paper-{num}'
        except ValueError:
            pass
    # Try to parse as raw number 0-100
    try:
        num = int(s)
        if 0 <= num <= 100:
            return f'paper-{num:02d}' if num < 100 else f'paper-{num}'
    except ValueError:
        pass
    return None'''

if old_func in content:
    content = content.replace(old_func, new_func)
    with open(r'D:\Paper Ecology\build_paper_ecology_meta.py', 'w') as f:
        f.write(content)
    print('Replaced successfully using exact old_func')
else:
    # Fallback: find function by regex and replace
    pattern = r'def normalize_paper_number\(pn\):.*?(?=\nclass |\ndef [a-zA-Z]|\Z)'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        content = content.replace(match.group(), new_func)
        with open(r'D:\Paper Ecology\build_paper_ecology_meta.py', 'w') as f:
            f.write(content)
        print('Replaced successfully using regex fallback')
    else:
        print('Could not find function')
