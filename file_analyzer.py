import re
from collections import Counter

SUPPORTED_LANGUAGES = {
    "py": "Python",
    "js": "JavaScript",
    "java": "Java",
    "cpp": "C++",
    "c": "C",
    "html": "HTML",
    "css": "CSS",
    "php": "PHP",
    "json": "JSON",
    "txt": "Text File",
    "md": "Markdown",
    "xml": "XML"
}


def detect_language(filename):
    ext = filename.split('.')[-1].lower()
    return SUPPORTED_LANGUAGES.get(ext, "Unknown")


def analyze_code(content, filename):
    language = detect_language(filename)
    lines = content.splitlines()

    analysis = {
        "filename": filename,
        "language": language,
        "total_lines": len(lines),
        "empty_lines": sum(1 for l in lines if not l.strip()),
        "comment_lines": sum(1 for l in lines if l.strip().startswith(("#", "//", "/*"))),
        "function_count": len(re.findall(r'\bdef\b|\bfunction\b|\bvoid\b', content)),
        "class_count": len(re.findall(r'\bclass\b', content)),
        "import_count": len(re.findall(r'\bimport\b|\brequire\b', content)),
        "top_words": dict(Counter(re.findall(r'\w+', content.lower())).most_common(10)),
    }

    # Simple AI Summary
    analysis["summary"] = generate_summary(analysis)

    return analysis


def generate_summary(data):
    return (
        f"This {data['language']} file contains "
        f"{data['total_lines']} lines, "
        f"{data['function_count']} functions, "
        f"and {data['class_count']} classes."
    )