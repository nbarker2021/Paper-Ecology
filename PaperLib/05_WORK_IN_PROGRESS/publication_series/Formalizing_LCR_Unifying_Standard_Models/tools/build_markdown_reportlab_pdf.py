"""Build a readable PDF from a Markdown paper using ReportLab.

This is a lightweight fallback for Windows systems where Pandoc is available
for TeX/HTML generation but no LaTeX engine or WeasyPrint native libraries are
installed.
"""
from __future__ import annotations

import html
import re
import sys
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    PageBreak,
    Paragraph,
    Preformatted,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


def inline_markup(text: str) -> str:
    parts = re.split(r"(`[^`]+`)", text)
    rendered: list[str] = []
    for part in parts:
        if not part:
            continue
        if part.startswith("`") and part.endswith("`"):
            rendered.append(f'<font name="Courier">{html.escape(part[1:-1])}</font>')
            continue
        escaped = html.escape(part)
        escaped = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", escaped)
        escaped = re.sub(r"(?<!\w)\*([^*\n]+)\*(?!\w)", r"<i>\1</i>", escaped)
        rendered.append(escaped)
    return "".join(rendered)


def split_table_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def is_separator_row(line: str) -> bool:
    cells = split_table_row(line)
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell.strip()) for cell in cells)


def build_pdf(markdown_path: Path, pdf_path: Path) -> None:
    styles = getSampleStyleSheet()
    body = ParagraphStyle(
        "PaperBody",
        parent=styles["BodyText"],
        fontName="Times-Roman",
        fontSize=9.5,
        leading=12,
        spaceAfter=6,
        alignment=TA_LEFT,
    )
    h1 = ParagraphStyle("PaperH1", parent=styles["Heading1"], fontSize=18, leading=22, spaceAfter=12)
    h2 = ParagraphStyle("PaperH2", parent=styles["Heading2"], fontSize=14, leading=17, spaceBefore=10, spaceAfter=8)
    h3 = ParagraphStyle("PaperH3", parent=styles["Heading3"], fontSize=11.5, leading=14, spaceBefore=8, spaceAfter=6)
    code = ParagraphStyle(
        "PaperCode",
        parent=styles["Code"],
        fontName="Courier",
        fontSize=7.3,
        leading=9,
        leftIndent=8,
        rightIndent=8,
        borderColor=colors.lightgrey,
        borderWidth=0.5,
        borderPadding=5,
        backColor=colors.whitesmoke,
        spaceAfter=8,
    )
    table_cell = ParagraphStyle("PaperTableCell", parent=body, fontSize=7.0, leading=8.3, spaceAfter=0)
    table_head = ParagraphStyle("PaperTableHead", parent=table_cell, fontName="Helvetica-Bold")

    lines = markdown_path.read_text(encoding="utf-8").splitlines()
    story = []
    i = 0
    in_code = False
    code_lines: list[str] = []

    while i < len(lines):
        line = lines[i].rstrip()

        if line.startswith("```"):
            if in_code:
                story.append(Preformatted("\n".join(code_lines), code))
                code_lines = []
                in_code = False
            else:
                in_code = True
            i += 1
            continue

        if in_code:
            code_lines.append(line)
            i += 1
            continue

        if not line.strip():
            story.append(Spacer(1, 0.06 * inch))
            i += 1
            continue

        if line.startswith("|") and "|" in line[1:]:
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                if not is_separator_row(lines[i]):
                    table_lines.append(split_table_row(lines[i]))
                i += 1
            if table_lines:
                max_cols = max(len(row) for row in table_lines)
                normalized = [row + [""] * (max_cols - len(row)) for row in table_lines]
                data = []
                for r_idx, row in enumerate(normalized):
                    style = table_head if r_idx == 0 else table_cell
                    data.append([Paragraph(inline_markup(cell), style) for cell in row])
                width = 7.0 * inch
                col_widths = [width / max_cols] * max_cols
                table = Table(data, colWidths=col_widths, repeatRows=1, hAlign="LEFT")
                table.setStyle(
                    TableStyle(
                        [
                            ("GRID", (0, 0), (-1, -1), 0.25, colors.lightgrey),
                            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#f2f2f2")),
                            ("VALIGN", (0, 0), (-1, -1), "TOP"),
                            ("LEFTPADDING", (0, 0), (-1, -1), 3),
                            ("RIGHTPADDING", (0, 0), (-1, -1), 3),
                            ("TOPPADDING", (0, 0), (-1, -1), 3),
                            ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
                        ]
                    )
                )
                story.append(table)
                story.append(Spacer(1, 0.08 * inch))
            continue

        if line.startswith("# "):
            if story:
                story.append(PageBreak())
            story.append(Paragraph(inline_markup(line[2:].strip()), h1))
        elif line.startswith("## "):
            story.append(Paragraph(inline_markup(line[3:].strip()), h2))
        elif line.startswith("### "):
            story.append(Paragraph(inline_markup(line[4:].strip()), h3))
        elif line.startswith("- "):
            story.append(Paragraph("&bull; " + inline_markup(line[2:].strip()), body))
        elif re.match(r"^\d+\. ", line):
            story.append(Paragraph(inline_markup(line), body))
        else:
            story.append(Paragraph(inline_markup(line), body))
        i += 1

    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(pdf_path),
        pagesize=LETTER,
        rightMargin=0.65 * inch,
        leftMargin=0.65 * inch,
        topMargin=0.65 * inch,
        bottomMargin=0.65 * inch,
        title=markdown_path.stem,
        author="FLCR publication series",
    )
    doc.build(story)


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: build_markdown_reportlab_pdf.py input.md output.pdf", file=sys.stderr)
        return 2
    build_pdf(Path(sys.argv[1]), Path(sys.argv[2]))
    print(str(Path(sys.argv[2])))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
