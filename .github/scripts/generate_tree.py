import os
import json
import re

def count_questions(file_path):
    """JSON फ़ाइल के अंदर प्रश्नों की संख्या गिनता है।"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return len(data) if isinstance(data, list) else 0
    except Exception:
        return 0

def get_pretty_name(filename):
    """ट्री में दिखाने के लिए सुंदर और संक्षिप्त नाम प्रदान करता है।"""
    # यहाँ आप अपनी पसंद के अनुसार मैपिंग जोड़ सकते हैं
    mapping = {
        "govt_schemes.json": "सरकारी योजनाएं (SC/ST/OBC)",
        "programming_ai.json": "प्रोग्रामिंग एवं AI परिचय",
        "Ecosystem  पारिस्थितिकी तंत्र.json": "पारिस्थितिकी तंत्र",
        "औषधियाँ एवं प्रबंधन  Medicines & Management.json": "औषधियाँ एवं प्रबंधन"
    }
    
    if filename in mapping:
        return mapping[filename]
    
    # अन्य फ़ाइलों के लिए एक्सटेंशन हटाएँ और नाम छोटा करें
    name = filename.replace('.json', '')
    return name[:30] + "..." if len(name) > 33 else name

def generate_tree(startpath):
    """प्रश्नों की संख्या के साथ फ़ाइल ट्री बनाता है।"""
    tree_lines = ["."]
    ignore_dirs = {'.git', '.github', 'tree.bak'}
    
    for root, dirs, files in os.walk(startpath):
        dirs[:] = [d for d in sorted(dirs) if d not in ignore_dirs]
        level = root.replace(startpath, '').count(os.sep)
        
        if level > 0:
            indent = '│   ' * (level - 1) + '├── '
            tree_lines.append(f"{indent}{os.path.basename(root)}")
        
        sub_indent = '│   ' * level + '├── '
        for f in sorted(files):
            if f.endswith('.json') and f != 'topics.json':
                q_count = count_questions(os.path.join(root, f))
                short_name = get_pretty_name(f)
                tree_lines.append(f"{sub_indent}{short_name} ({q_count} Qs)")
            elif f in ['topics.json', 'README.md'] and level == 0:
                tree_lines.append(f"├── {f}")

    return "\n".join(tree_lines)

def update_readme(tree_string):
    """README.md में ट्री अपडेट करता है।"""
    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = r"().*?()"
    replacement = f"\\1\n```\n{tree_string}\n```\n\\2"
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == "__main__":
    tree = generate_tree('.')
    update_readme(tree)
