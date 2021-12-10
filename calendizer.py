"""
Renders an image of a calendar month that could be pasted onto a photo
"""
from calendar import month
import os

import calendar_model
import date_utils
import figure_renderer

# config
OUTDIR = "temp"
DPI = 150
BORDER_COLOR = 'black'
YEAR = 2022

# 1 = January
for month in range(1, 12 + 1):
    print(f"Generating {date_utils.month_name(month)} {YEAR} ...")

    # note: Table data needs to be non-numeric text.
    cell_text = calendar_model.get_month_data(month, YEAR)

    column_headers = calendar_model.get_column_headers()

    title_text = calendar_model.get_month_title(month, YEAR)

    month_2_digits = f"{month:02d}"
    outpath = os.path.join(OUTDIR, f"{month_2_digits}-{date_utils.month_name(month)}-{YEAR}.png")

    figure = figure_renderer.render(cell_text, column_headers, title_text, BORDER_COLOR, DPI, outpath)
    print(f" - saved to {outpath} [OK]")

print("[done]")
