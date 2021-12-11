"""
Renders images of calendar tables - one for each month. The table-images could be used to paste onto suitable photos.

Usage: render_calendar_tables.py <year> <path to output directory> [options]

The options are:
[-b --bordercolor - The color of the table borders]
[--dpi] - DPI to render
[-h --help]
[-t --textColor - The color of the text]

Examples:
render_calendar_tables.py 2022 temp
render_calendar_tables.py 2022 temp --dpi 150
render_calendar_tables.py 2022 temp --dpi 150 -b blue
render_calendar_tables.py 2022 temp --dpi 150 --bordercolor blue
"""
from calendar import month
from optparse import OptionParser

import _date_utils
import _figure_renderer

# usage() - prints out the usage text, from the top of this file :-)


def usage():
    print(__doc__)


# optparse - parse the args
parser = OptionParser(
    usage='%prog <source month 1..12> [options]')
parser.add_option('-b', '--borderColor', dest='borderColor', default="black",
                  help="The color of the table borders - for example black or red or blue")
parser.add_option('--dpi', dest='dpi', default=150,
                  help="The DPI to render (Dots Per Inch). Defaults to 150")
parser.add_option('-t', '--textColor', dest='textColor', default="black",
                  help="The color of the text - for example black or red or blue")

(options, args) = parser.parse_args()
if (len(args) != 2):
    usage()
    exit(2)

YEAR = int(args[0])
OUTDIR = args[1]

# 1 = January
for month in range(1, 12 + 1):
    print(f"Generating {_date_utils.month_name(month)} {YEAR} ...")

    image_file_path = _figure_renderer.render_table_for_month(
        month, YEAR, OUTDIR, options.borderColor, options.textColor, options.dpi)
    print(f" - saved to {image_file_path} [OK]")

print("[done]")
