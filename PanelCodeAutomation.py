import fitz  # PyMuPDF

# Change this to match the file name
base_name = "E20"

pdf_path = f"{base_name}.pdf"  # Input PDF path
output_pdf_path = f"{base_name}_with_annotation.pdf"  # Output PDF path

# List of keywords to search for in the PDF
keywords = {"word1", "word2"}

# Tolerance for grouping words into the same column or row
TOLERANCE = 15  # Adjust this value as needed
panels = []

doc = fitz.open(pdf_path)
for page_num, page in enumerate(doc):
    words = page.get_text("words")
    for word in words:
        if word[4] in keywords:
            x0, y0, x1, y1 = word[0], word[1], word[2], word[3]
            panels.append({"text": word[4], "x0": x0, "y0": y0, "page": page_num})

def group_coordinates(cord, tolerance):
    groups = {}
    sorted_cord = sorted(cord)
    cur_group = sorted_cord[0]
    groups[sorted_cord[0]] = cur_group
    for coord in sorted_cord[1:]:
        if abs(coord - cur_group) <= tolerance:
            groups[coord] = cur_group
        else:
            cur_group = coord
            groups[coord] = cur_group
    return groups


x0_cord = [panel["x0"] for panel in panels]
y0_cord = [panel["y0"] for panel in panels]

x0_groups = group_coordinates(x0_cord, TOLERANCE)
y0_groups = group_coordinates(y0_cord, TOLERANCE)

rows = {}
cols = {}

for panel in panels:
    panel["x0_grouped"] = x0_groups[panel["x0"]]
    panel["y0_grouped"] = y0_groups[panel["y0"]]

unique_x0 = sorted(list(set(panel["x0_grouped"] for panel in panels)))
for x, x0 in enumerate(unique_x0):
    cols[x0] = x + 1

for panel in panels:
    rows[panel["y0_grouped"]] = rows.get(panel["y0_grouped"], len(rows) + 1)
    panel["row"] = rows[panel["y0_grouped"]]
    panel["col"] = cols[panel["x0_grouped"]]

for panel in panels:
    page_num = panel["page"]
    x0, y0 = panel["x0"], panel["y0"]
    row, col = panel["row"], panel["col"]
    label = f"#{base_name}R{row}C{col}"

    page = doc[page_num]

    if col % 2 == 0:
        y0 += 30

    page.insert_text(
        point=(x0 - 14, y0 - 4),  # Adjust position as needed
        text=label,
        fontsize=11,
        fontname="hebo",
        color=(1, 0, 0),
    )

doc.save(output_pdf_path)
doc.close()

print(f"Annotations added to {output_pdf_path}")
