MAX_FILE_SIZE = 20 * 1024 * 1024  # 20 MB


def validate_pdf(file):
    """
    Validate uploaded PDF.
    """

    if file.content_type != "application/pdf":
        raise ValueError("Only PDF files are allowed.")

    return True


def validate_file_size(file):
    """
    Validate uploaded file size.
    """

    file.file.seek(0, 2)
    size = file.file.tell()
    file.file.seek(0)

    if size > MAX_FILE_SIZE:
        raise ValueError(
            f"File exceeds maximum allowed size ({MAX_FILE_SIZE // (1024 * 1024)} MB)"
        )

    return True