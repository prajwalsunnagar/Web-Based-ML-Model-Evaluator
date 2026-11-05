#!/usr/bin/env python3
"""
Convert Markdown documents to formatted Word (.docx) files.
Handles headings, bullet lists, numbered lists, markdown tables, and code blocks.
"""

import sys
import re
from pathlib import Path
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls


def set_cell_background(cell, fill_hex):
    """Set cell background color."""
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)


def set_table_borders(table, color="D3D3D3"):
    """Set subtle gray borders on a table."""
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>\n'
        f'  <w:top w:val="single" w:sz="4" w:space="0" w:color="{color}"/>\n'
        f'  <w:bottom w:val="single" w:sz="4" w:space="0" w:color="{color}"/>\n'
        f'  <w:insideH w:val="single" w:sz="4" w:space="0" w:color="{color}"/>\n'
        f'  <w:insideV w:val="single" w:sz="4" w:space="0" w:color="{color}"/>\n'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)


def add_formatted_text(paragraph, text):
    """Parse basic bold (**text**) and inline code (`code`) and add runs."""
    pattern = re.compile(r'(\*\*.*?\*\*|`.*?`)')
    parts = pattern.split(text)
    for part in parts:
        if not part:
            continue
        if part.startswith('**') and part.endswith('**') and len(part) >= 4:
            run = paragraph.add_run(part[2:-2])
            run.bold = True
        elif part.startswith('`') and part.endswith('`') and len(part) >= 2:
            run = paragraph.add_run(part[1:-1])
            run.font.name = 'Courier New'
            run.font.size = Pt(9.5)
            run.font.color.rgb = RGBColor(0x80, 0x00, 0x20)  # maroon
        else:
            paragraph.add_run(part)


def convert_md_to_docx(md_path, docx_path):
    md_file = Path(md_path)
    docx_file = Path(docx_path)

    with open(md_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    doc = docx.Document()

    # Page setup - 1 inch margins
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)

    i = 0
    in_code_block = False
    code_lines = []

    while i < len(lines):
        line = lines[i].rstrip('\r\n')

        # Check code block
        if line.startswith('```'):
            if in_code_block:
                # end code block
                code_text = '\n'.join(code_lines)
                table = doc.add_table(rows=1, cols=1)
                table.alignment = WD_TABLE_ALIGNMENT.CENTER
                cell = table.cell(0, 0)
                set_cell_background(cell, "F4F4F6")
                p = cell.paragraphs[0]
                p.paragraph_format.space_before = Pt(4)
                p.paragraph_format.space_after = Pt(4)
                run = p.add_run(code_text)
                run.font.name = 'Courier New'
                run.font.size = Pt(8.5)
                run.font.color.rgb = RGBColor(0x33, 0x33, 0x33)
                in_code_block = False
                code_lines = []
            else:
                # start code block
                in_code_block = True
                code_lines = []
            i += 1
            continue

        if in_code_block:
            code_lines.append(line)
            i += 1
            continue

        # Empty line
        if not line.strip():
            i += 1
            continue

        # Headings
        if line.startswith('# '):
            p = doc.add_heading(level=1)
            add_formatted_text(p, line[2:].strip())
            p.paragraph_format.space_before = Pt(12)
            p.paragraph_format.space_after = Pt(6)
            i += 1
            continue
        elif line.startswith('## '):
            p = doc.add_heading(level=2)
            add_formatted_text(p, line[3:].strip())
            p.paragraph_format.space_before = Pt(10)
            p.paragraph_format.space_after = Pt(4)
            i += 1
            continue
        elif line.startswith('### '):
            p = doc.add_heading(level=3)
            add_formatted_text(p, line[4:].strip())
            p.paragraph_format.space_before = Pt(8)
            p.paragraph_format.space_after = Pt(2)
            i += 1
            continue
        elif line.startswith('#### '):
            p = doc.add_heading(level=4)
            add_formatted_text(p, line[5:].strip())
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.space_after = Pt(2)
            i += 1
            continue

        # Horizontal rule
        if line.strip() in ['---', '***', '___']:
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.space_after = Pt(6)
            p_border = parse_xml(
                f'<w:pBdr {nsdecls("w")}><w:bottom w:val="single" w:sz="6" w:space="1" w:color="CCCCCC"/></w:pBdr>'
            )
            p._p.get_or_add_pPr().append(p_border)
            i += 1
            continue

        # Markdown table
        if line.strip().startswith('|') and '|' in line.strip()[1:]:
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                table_lines.append(lines[i].strip())
                i += 1

            # Parse table lines
            rows = []
            for tl in table_lines:
                cells = [c.strip() for c in tl.strip('|').split('|')]
                # skip divider row like |---|---|
                if all(re.match(r'^:?-+:?$', c) for c in cells if c):
                    continue
                rows.append(cells)

            if rows:
                num_cols = max(len(r) for r in rows)
                table = doc.add_table(rows=len(rows), cols=num_cols)
                table.alignment = WD_TABLE_ALIGNMENT.CENTER
                set_table_borders(table)

                for r_idx, row_data in enumerate(rows):
                    is_header = (r_idx == 0)
                    for c_idx in range(num_cols):
                        val = row_data[c_idx] if c_idx < len(row_data) else ""
                        cell = table.cell(r_idx, c_idx)
                        if is_header:
                            set_cell_background(cell, "EAEAEA")
                        cell.paragraphs[0].paragraph_format.space_before = Pt(3)
                        cell.paragraphs[0].paragraph_format.space_after = Pt(3)
                        cell.paragraphs[0].text = ""
                        add_formatted_text(cell.paragraphs[0], val)
                        if is_header:
                            for run in cell.paragraphs[0].runs:
                                run.bold = True
                doc.add_paragraph().paragraph_format.space_after = Pt(4)
            continue

        # Bullet list
        if line.strip().startswith('- ') or line.strip().startswith('* '):
            text = line.strip()[2:].strip()
            p = doc.add_paragraph(style='List Bullet')
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(2)
            add_formatted_text(p, text)
            i += 1
            continue

        # Numbered list
        num_match = re.match(r'^\s*(\d+)\.\s+(.*)$', line)
        if num_match:
            text = num_match.group(2).strip()
            p = doc.add_paragraph(style='List Number')
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(2)
            add_formatted_text(p, text)
            i += 1
            continue

        # Standard paragraph
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(4)
        add_formatted_text(p, line.strip())
        i += 1

    doc.save(docx_file)
    print(f"Successfully generated {docx_file}")


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: md_to_docx.py <input.md> <output.docx>")
        sys.exit(1)
    convert_md_to_docx(sys.argv[1], sys.argv[2])
