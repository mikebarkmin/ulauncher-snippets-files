import markdownify
from datetime import datetime


def safe_filename(filename: str) -> str:
    keepcharacters = (" ", ".", "_")
    return "".join(c for c in filename if c.isalnum() or c in keepcharacters).rstrip()


def html_to_md(html: str) -> str:
    return markdownify.markdownify(html)


filters = {"safe_filename": safe_filename, "html_to_md": html_to_md}
