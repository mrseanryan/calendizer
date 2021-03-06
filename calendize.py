"""
Takes 12 images and outputs copies that have calender-month table pasted onto them.

Usage: calendize.py <year> <path to input images> <path to output directory> [options]

The options are:

[-a --alpha - The transparency of the calendar (0..1)]
[-b --bottom - The bottom margin of the calendar]
[-c --borderColor - The color of the table borders]
[--dpi] - DPI to render
[-h --help]
[-m --month - Output for one month only (1..12)]
[-r --right - The right margin of the calendar]
[-t --textColor - The color of the text]

Examples:
calendize.py 2022 my-12-images temp
calendize.py 2022 my-12-images temp --dpi 150
calendize.py 2022 my-12-images temp --dpi 150 -b blue
calendize.py 2022 my-12-images temp --dpi 150 --borderColor blue --alpha 0.7
"""
from PIL import Image
from os.path import isfile, join
from os import listdir
from calendar import month
from optparse import OptionParser
import os
from pathlib import Path

import _date_utils
import _figure_renderer

# usage() - prints out the usage text, from the top of this file :-)


def usage():
    print(__doc__)


# optparse - parse the args
parser = OptionParser(
    usage='%prog <source month 1..12> [options]')
parser.add_option('-a', '--alpha', dest='alpha', default=1.0,
                  help="The transparency of the calendar (0..1). Defaults to 1 (fully opaque).")
parser.add_option('-b', '--bottom', dest='bottom_margin', default=50,
                  help="The bottom margin of the calendar. Defaults to 50")
parser.add_option('-c', '--borderColor', dest='borderColor', default="black",
                  help="The color of the table borders - for example black or red or blue")
parser.add_option('--dpi', dest='dpi', default=150,
                  help="The DPI to render (Dots Per Inch). Defaults to 150")
parser.add_option('-m', '--month', dest='month', default=-1,
                  help="Output for one month only (1..12)")
parser.add_option('-t', '--textColor', dest='textColor', default="black",
                  help="The color of the text - for example black or red or blue")
parser.add_option('-r', '--right', dest='right_margin', default=50,
                  help="The right margin of the calendar. Defaults to 50")

(options, args) = parser.parse_args()
if (len(args) != 3):
    usage()
    exit(2)

YEAR = int(args[0])
INPUTDIR = args[1]
OUTDIR = args[2]


def is_supported_file_type(filepath):
    file_extensions = [".jpg", ".jpeg", ".png"]
    return any(map(lambda ext: filepath.lower().endswith(ext), file_extensions))


def get_input_files(input_dir):
    # Assumption: files are soted already - this allows user to decide which is for which month...
    files = [f for f in listdir(input_dir) if isfile(
        join(input_dir, f)) and is_supported_file_type(f)]
    files = map((lambda f: join(input_dir, f)), files)
    return list(files)


def calculate_bottom_right_offset_for(calender_image, background_image, bottom_margin, right_margin):
    background_image_width, background_image_height = background_image.size
    calender_image_width, calender_image_height = calender_image.size

    margin_tuple_from_topleft = (background_image_width - calender_image_width -
                                 right_margin, background_image_height - calender_image_height - bottom_margin)

    return margin_tuple_from_topleft


def paste_with_transparency(fg_img, bg_img, alpha=1.0, box=(0, 0)):
    fg_img_trans = Image.new("RGBA", fg_img.size)
    fg_img_trans = Image.blend(fg_img_trans, fg_img, alpha)
    bg_img.paste(fg_img_trans, box, fg_img_trans)
    return bg_img


def paste_calendar_into_image(calendar_image_file_path, input_image_path, output_image_path, bottom_margin, right_margin, alpha):
    calender_image = Image.open(calendar_image_file_path)
    background_image = Image.open(input_image_path)
    offset = calculate_bottom_right_offset_for(
        calender_image, background_image, bottom_margin, right_margin)
    background_image = paste_with_transparency(
        calender_image, background_image, alpha, offset)
    background_image.save(output_image_path)


def generate_output_image_filename(input_image_path, month, year):
    input_image_name = os.path.basename(input_image_path)
    month_2_digits = f"{month:02d}"
    month_name = _date_utils.month_name(month)
    output_filename = f"{year}-{month_2_digits}-{month_name}--{input_image_name}"
    # output to PNG since repeatedly saving JPG will affect quality
    return Path(output_filename).with_suffix('.png')


files = get_input_files(INPUTDIR)
files_count = len(files)
if (files_count != 12):
    print(
        f"The input folder '{INPUTDIR}' should contain 12 images but found {files_count}")
    exit(3)

Path(OUTDIR).mkdir(parents=True, exist_ok=True)


def generate_for_month(month):
    # month: 1 = January
    print(f"Generating {_date_utils.month_name(month)} {YEAR} ...")
    calendar_image_file_path = _figure_renderer.render_table_for_month(
        month, YEAR, OUTDIR, options.borderColor, options.textColor, int(options.dpi))
    input_image_path = files[month - 1]
    output_image_path = os.path.join(
        OUTDIR, generate_output_image_filename(input_image_path, month, YEAR))
    paste_calendar_into_image(calendar_image_file_path, input_image_path, output_image_path, int(
        options.bottom_margin), int(options.right_margin), float(options.alpha))
    os.unlink(calendar_image_file_path)
    print(f" - calendized image saved to {output_image_path} [OK]")


if (int(options.month) >= 1):
    generate_for_month(int(options.month))
else:
    for month in range(1, 12 + 1):
        generate_for_month(month)

print("[done]")
