import sys
from pathlib import Path

import pymupdf  # PyMuPDF

# Target Page Size (Change this if needed)
PAGE_WIDTH = 595  # A4 width in points
PAGE_HEIGHT = 842  # A4 height in points


def split_pdf(
    input_pdf: Path,
    output_folder: Path,
    page_width: int = PAGE_WIDTH,
    page_height: int = PAGE_HEIGHT,
) -> None:
    """Split a PDF into multiple pages, resizing each to a fixed size while maintaining aspect ratio."""
    doc = pymupdf.open(input_pdf)

    # Ensure output folder exists
    output_folder.mkdir(parents=True, exist_ok=True)

    for page_num in range(len(doc)):
        # Create a new blank A4-sized document
        resized_doc = pymupdf.open()
        resized_page = resized_doc.new_page(width=page_width, height=page_height)

        # Extract the original page (keeps digital signature intact)
        original_page = doc.load_page(page_num)
        orig_rect = original_page.rect

        # Scale while maintaining aspect ratio
        scale = min(page_width / orig_rect.width, page_height / orig_rect.height)
        new_width = orig_rect.width * scale
        new_height = orig_rect.height * scale

        # Center the content on the new page
        x_offset = (page_width - new_width) / 2
        y_offset = (page_height - new_height) / 2

        # Insert the original page as a "stamp" (preserves signatures)
        resized_page.show_pdf_page(
            pymupdf.Rect(x_offset, y_offset, x_offset + new_width, y_offset + new_height),
            doc,
            page_num,
        )

        # Save the resized page as a new PDF
        output_pdf = output_folder / f"page_{page_num + 1}.pdf"
        resized_doc.save(output_pdf)
        resized_doc.close()

        print(
            f"Saved: {output_pdf}",
            f"(Resized to {page_width}x{page_height} points)"
            if page_width != orig_rect.width or page_height != orig_rect.height
            else "",
        )

    doc.close()
    print("PDF successfully split and resized!")


def main() -> None:
    input_pdf = Path(sys.argv[1])
    output_folder = Path(sys.argv[2] if len(sys.argv) >= 3 else ".")

    # Replace with your own input and output file paths
    split_pdf(input_pdf, output_folder, page_width=PAGE_WIDTH, page_height=PAGE_HEIGHT)


if __name__ == "__main__":
    main()
