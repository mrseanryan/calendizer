"""
Takes 12 images and outputs copies that have calender-month table pasted onto them.

Usage: calendize.py <year> <path to input images> <path to output directory> [options]

The options are:
[-b --bordercolor - The color of the table borders]
[--dpi] - DPI to render
[-h --help]

Examples:
calendize.py 2022 my-12-images temp
calendize.py 2022 my-12-images temp --dpi 150
calendize.py 2022 my-12-images temp --dpi 150 -b blue
calendize.py 2022 my-12-images temp --dpi 150 --bordercolor blue
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

# optparse - parse the args
parser = OptionParser(
    usage='%prog <source month 1..12> [options]')
parser.add_option('-b', '--bordercolor', dest='bordercolor', default="black",
                  help="The color of the table borders - for example black or red or blue")
parser.add_option('--dpi', dest='dpi', default=150,
                  help="The DPI to render (Dots Per Inch). Defaults to 150")

(options, args) = parser.parse_args()
if (len(args) != 3):
    usage()
    exit(2)

# import pdb
# pdb.set_trace()

YEAR = int(args[0])
INPUTDIR = args[1]
OUTDIR = args[2]

DPI = options.dpi
BORDER_COLOR = options.bordercolor

# TODO - Sort the images by name, to let user decide which is for which month...

# 1 = January
for month in range(1, 12 + 1):
    print(f"Generating {_date_utils.month_name(month)} {YEAR} ...")

    # note: Table data needs to be non-numeric text.
    cell_text = _calendar_model.get_month_data(month, YEAR)

    column_headers = _calendar_model.get_column_headers()

    title_text = _calendar_model.get_month_title(month, YEAR)

    month_2_digits = f"{month:02d}"
    # TODO use the original image name as a suffix
    outpath = os.path.join(OUTDIR, f"{YEAR}-{month_2_digits}-{_date_utils.month_name(month)}.png")

    figure = _figure_renderer.render(cell_text, column_headers, title_text, BORDER_COLOR, DPI, outpath)
    print(f" - saved to {outpath} [OK]")

print("[done]")
