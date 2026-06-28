from pathlib import Path
from uuid import uuid4


def generate_unique_filename(filename: str) -> str:
    """
    Generate a unique filename while preserving extension.
    """

    extension = Path(filename).suffix

    return f"{uuid4()}{extension}"