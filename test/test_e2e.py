from pathlib import Path
from pypdf import PdfReader
import os


def test_e2e():
    pdf_path = Path("test/test_data/in.margins.pdf")
    pdf_path.unlink(missing_ok=True)

    os.system("./scripts/example_usage.sh")

    pdf_path = Path("test/test_data/in.margins.pdf")
    assert pdf_path.exists(), f"File {pdf_path} does not exist"

    reader = PdfReader(str(pdf_path))

    # Get the number of pages
    num_pages = len(reader.pages)

    expected = [
        {
            "Page": 1,
            "Width (pts)": 896.0,
            "Height (pts)": 1198.0,
            "Number of characters": 5444,
        },
        {
            "Page": 2,
            "Width (pts)": 896.0,
            "Height (pts)": 1198.0,
            "Number of characters": 5887,
        },
        {
            "Page": 3,
            "Width (pts)": 896.0,
            "Height (pts)": 1198.0,
            "Number of characters": 5447,
        },
        {
            "Page": 4,
            "Width (pts)": 896.0,
            "Height (pts)": 1198.0,
            "Number of characters": 5194,
        },
        {
            "Page": 5,
            "Width (pts)": 896.0,
            "Height (pts)": 1198.0,
            "Number of characters": 4591,
        },
        {
            "Page": 6,
            "Width (pts)": 896.0,
            "Height (pts)": 1198.0,
            "Number of characters": 7505,
        },
        {
            "Page": 7,
            "Width (pts)": 896.0,
            "Height (pts)": 1198.0,
            "Number of characters": 333,
        },
    ]

    actual = []

    # Loop through each page and extract the required info
    for i in range(num_pages):
        page = reader.pages[i]

        # Get page size (in points, where 1 point = 1/72 inch)
        width = page.mediabox.width
        height = page.mediabox.height

        # Extract text and count the number of characters
        text = page.extract_text()
        num_chars = len(text) if text else 0

        # Append the info to the list
        actual.append(
            {
                "Page": i + 1,
                "Width (pts)": width,
                "Height (pts)": height,
                "Number of characters": num_chars,
            }
        )

    print(actual)

    for i, (exp, act) in enumerate(zip(expected, actual)):
        assert exp == act, f"Page {i + 1} does not match"

    # TIPP: I you change the code an you have to fix this test,
    #       visually inspect the result and if it looks good to you, print
    #       the actual-list and paste it into the expected-list above.
