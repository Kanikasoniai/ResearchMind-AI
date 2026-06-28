import fitz


def extract_metadata(pdf_path: str):

    document = fitz.open(pdf_path)

    metadata = document.metadata

    result = {
        "title": metadata.get("title"),
        "author": metadata.get("author"),
        "pages": len(document),
    }

    document.close()

    return result