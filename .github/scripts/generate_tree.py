import os
import json
import re

def count_questions(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return len(data) if isinstance(data, list) else 0
    except Exception:
        return 0

def shorten_name(name, max_len=40):
    # Remove the .json extension for the display
    display_name = name.replace('.json', '')
    if len(display_name) > max_len:
        return display_name[:max_len-3] + "..."
    return display_name

def generate_tree(startpath):
    tree_lines = ["."]
    # Define directories to ignore
    ignore_dirs = {'.git', '.github', 'tree.bak'}
    
    for root, dirs, files in os.walk(startpath):
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        level = root.replace(startpath, '').count(os.sep)
        indent = '│   ' * (level - 1) + '├── ' if level > 0 else ''
        
        if level > 0:
            tree_lines.append(f"{indent}{os.path.basename(root)}")
        
        sub_indent = '│   ' * level + '├── '
        for i, f in enumerate(sorted(files)):
            if f.endswith('.json') and f != 'topics.json':
                q_count = count_questions(os.path.join(root, f))
                short_f = shorten_name(f)
                tree_lines.append(f"{sub_indent}{short_f} ({q_count} Qs)")
            elif f == 'topics.json' or f == 'README.md':
                if level == 0: # Only show at root
                    tree_lines.append(f"├── {f}")

    return "\n".join(tree_lines)

def update_readme(tree_string):
    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find the block between the comments
    pattern = r"().*?()"
    replacement = f"\\1\n```\n{tree_string}\n```\n\\2"
    
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == "__main__":
    tree = generate_tree('.')
    update_readme(tree)
