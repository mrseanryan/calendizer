"""
Takes 12 images and outputs copies that have calender-month table pasted onto them.

Usage: calendize.py <year> <path to input images> <path to output directory> [options]

The options are:

[-b --bottom - The bottom margin of the calendar]
[-c --borderColor - The color of the table borders]
[--dpi] - DPI to render
[-h --help]
[-r --right - The right margin of the calendar]

Examples:
calendize.py 2022 my-12-images temp
calendize.py 2022 my-12-images temp --dpi 150
calendize.py 2022 my-12-images temp --dpi 150 -b blue
calendize.py 2022 my-12-images temp --dpi 150 --borderColor blue
"""
from calendar import month
from optparse import OptionParser
import os

import _date_utils
import _figure_renderer

# usage() - prints out the usage text, from the top of this file :-)
def usage():
    print(__doc__)

# optparse - parse the args
parser = OptionParser(
    usage='%prog <source month 1..12> [options]')
parser.add_option('-b', '--bottom', dest='bottom_margin', default=50,
                help="The bottom margin of the calendar. Defaults to 50")
parser.add_option('-c', '--borderColor', dest='borderColor', default="black",
                  help="The color of the table borders - for example black or red or blue")
parser.add_option('--dpi', dest='dpi', default=150,
                  help="The DPI to render (Dots Per Inch). Defaults to 150")
parser.add_option('-r', '--right', dest='right_margin', default=50,
                  help="The right margin of the calendar. Defaults to 50")

(options, args) = parser.parse_args()
if (len(args) != 3):
    usage()
    exit(2)

YEAR = int(args[0])
INPUTDIR = args[1]
OUTDIR = args[2]

from os import listdir
from os.path import isfile, join
from PIL import Image

def is_supported_file_type(filepath):
    file_extensions = [".jpg", ".jpeg", ".png"]
    return any(map(lambda ext: filepath.endswith(ext), file_extensions))

def get_input_files(input_dir):
    # Assumption: files are soted already - this allows user to decide which is for which month...
    files = [f for f in listdir(input_dir) if isfile(join(input_dir, f)) and is_supported_file_type(f)]
    files = map((lambda f: join(input_dir, f)), files)
    return list(files)

def calculate_bottom_right_offset_for(calender_image, background_image, bottom_margin, right_margin):
    background_image_width, background_image_height = background_image.size
    calender_image_width, calender_image_height = calender_image.size

    margin_tuple_from_topleft = (background_image_width - calender_image_width - right_margin, background_image_height - calender_image_height - bottom_margin)

    return margin_tuple_from_topleft

def paste_calendar_into_image(calendar_image_file_path, input_image_path, output_image_path, bottom_margin, right_margin):
    calender_image = Image.open(calendar_image_file_path)
    background_image = Image.open(input_image_path)
    background_image.paste(calender_image, calculate_bottom_right_offset_for(calender_image, background_image, bottom_margin, right_margin))
    background_image.save(output_image_path) 

def generate_output_image_filename(input_image_path, month, year):
    input_image_name = os.path.basename(input_image_path)
    month_2_digits = f"{month:02d}"
    month_name = _date_utils.month_name(month)
    return f"{year}-{month_2_digits}-{month_name}--{input_image_name}"

files = get_input_files(INPUTDIR)
files_count = len(files)
if (files_count != 12):
    print(f"The input folder '{INPUTDIR}' should contain 12 images but found {files_count}")
    exit(3)

# 1 = January
for month in range(1, 12 + 1):
    print(f"Generating {_date_utils.month_name(month)} {YEAR} ...")
    calendar_image_file_path = _figure_renderer.render_table_for_month(month, YEAR, OUTDIR, options.borderColor, options.dpi)
    print(f" - calendar table saved to {calendar_image_file_path} [OK]")
    input_image_path = files[month - 1]
    output_image_path = os.path.join(OUTDIR, generate_output_image_filename(input_image_path, month, YEAR))
    paste_calendar_into_image(calendar_image_file_path, input_image_path, output_image_path, int(options.bottom_margin), int(options.right_margin))
    print(f" - calendized image saved to {output_image_path} [OK]")

print("[done]")
