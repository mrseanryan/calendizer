"""
Renders image of a calendar month that can be pasted onto a photo
"""
from calendar import month
import os

import calendar_model
import figure_renderer

# config
OUTDIR = "temp"
DPI = 150
BORDER_COLOR = 'black'
YEAR = 2022

# 1 = January
month = 2

# note: Table data needs to be non-numeric text.
cell_text = calendar_model.get_month_data(month, YEAR)

print(cell_text)

column_headers = calendar_model.get_column_headers()

title_text = calendar_model.get_month_title(month, YEAR)

outpath = os.path.join(OUTDIR, 'pyplot-table-demo.png')

figure = figure_renderer.render(cell_text, column_headers, title_text, BORDER_COLOR, DPI, outpath)
