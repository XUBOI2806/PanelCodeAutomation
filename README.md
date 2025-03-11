# PDF Annotation Tool for Panels

This Python script uses **PyMuPDF** (`fitz` module) to add annotations to a PDF document based on the detection of specific text patterns. The tool identifies text in the PDF that matches predefined keywords then groups these occurrences by their coordinates on the page. After grouping, it annotates the panels with a unique label indicating their row and column positions.

## Key Features:
- **Text Detection**: Identifies specific text patterns in the PDF.
- **Coordinate Grouping**: Groups words based on their coordinates to categorise them into rows and columns with adjustable tolerance for grouping.
- **Annotations**: Adds labels to the detected panels with unique identifiers in the format `#zRxCy`, where `z` is the PDF name, `x` is the row and `y` is the column.
- **Customisation**: Adjusts annotation placement dynamically, including vertical offset adjustments for even columns.

## Dependencies:
- `PyMuPDF` (install using `pip install pymupdf`)

## How to Use:
1. Place your PDF file in the same directory as the script.
2. Set the desired base name for the PDF file in the `base_name` variable.
3. Add to the list of predfined word to find and annotate next to.
4. Run the script to add annotations to the PDF.
5. The output PDF will be saved with the suffix `_with_annotation` added to the original file name.

## Example:
- **Input file**: `file.pdf`
- **Output file**: `file_with_annotation.pdf`
