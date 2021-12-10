"""
Renders images of calendar tables - one for each month. The table-images could be used to paste onto suitable photos.

Usage: render_calendar_tables.py <year> <path to output directory> [options]

The options are:
[-b --bordercolor - The color of the table borders]
[--dpi] - DPI to render
[-h --help]

Examples:
render_calendar_tables.py 2022 temp
render_calendar_tables.py 2022 temp --dpi 150
render_calendar_tables.py 2022 temp --dpi 150 -b blue
render_calendar_tables.py 2022 temp --dpi 150 --bordercolor blue
"""
from calendar import month
from optparse import OptionParser
import os

import _calendar_model
import _date_utils
import _figure_renderer

# usage() - prints out the usage text, from the top of this file :-)
def usage():
    print(__doc__)


def split_exlude_empty(text, separator):
    return list(filter(None, text.split(separator)))

# optparse - parse the args
parser = OptionParser(
    usage='%prog <source month 1..12> [options]')
parser.add_option('-b', '--bordercolor', dest='bordercolor', default="black",
                  help="The color of the table borders - for example black or red or blue")
parser.add_option('--dpi', dest='dpi', default=150,
                  help="The DPI to render (Dots Per Inch). Defaults to 150")

(options, args) = parser.parse_args()
if (len(args) != 2):
    usage()
    exit(2)

# import pdb
# pdb.set_trace()

YEAR = int(args[0])
OUTDIR = args[1]

DPI = options.dpi
BORDER_COLOR = options.bordercolor

# 1 = January
for month in range(1, 12 + 1):
    print(f"Generating {_date_utils.month_name(month)} {YEAR} ...")

    # note: Table data needs to be non-numeric text.
    cell_text = _calendar_model.get_month_data(month, YEAR)

    column_headers = _calendar_model.get_column_headers()

    title_text = _calendar_model.get_month_title(month, YEAR)

    month_2_digits = f"{month:02d}"
    outpath = os.path.join(OUTDIR, f"{month_2_digits}-{_date_utils.month_name(month)}-{YEAR}.png")

    figure = _figure_renderer.render(cell_text, column_headers, title_text, BORDER_COLOR, DPI, outpath)
    print(f" - saved to {outpath} [OK]")

print("[done]")