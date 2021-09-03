def safe_filename(filename: str) -> str:
    keepcharacters = (" ", ".", "_")
    return "".join(c for c in filename if c.isalnum() or c in keepcharacters).rstrip()


filters = {"safe_filename": safe_filename}
