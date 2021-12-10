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

from os import listdir
from os.path import isfile, join

def is_supported_file_type(filepath):
    file_extensions = [".jpg", ".jpeg", ".png"]
    return any(map(lambda ext: filepath.endswith(ext), file_extensions))

files = [f for f in listdir(INPUTDIR) if isfile(join(INPUTDIR, f) and is_supported_file_type(f))]

print(files)


# 1 = January
for month in range(1, 12 + 1):
    print(f"Generating {_date_utils.month_name(month)} {YEAR} ...")
    image_file_path = _figure_renderer.render_table_for_month(month, YEAR, OUTDIR, BORDER_COLOR, DPI)
    print(f" - saved to {image_file_path} [OK]")

print("[done]")
