# :calendar: calendizer README

Generates images of calendar month tables and can paste them onto suitable photos.

A quick way to make your own calendar for printing.

## Usage

To generate 12 images of a mini calendar:

`render_calendar_tables.py <year> <path to output directory>`

To take 12 images and use them to create a calendar:

`calendize.py <year> <path to directory with 12 images in PNG or JPEG format> <path to output directory>`

### Tips

With an input image of size 4000 x 3000, these settings seem to work well:

`--dpi 450 -b 100 -r 100`

Example:

`calendize.py <year> <path to directory with 12 images in PNG or JPEG format> <path to output directory> --dpi 450 -b 100 -r 100`

## Dependencies

- Python 3.x

## Setup

1. Install Python 3.7.x and pip

- Python 3.7.9 or later
- pip 20.2.2 or later

2. Install dependencies

```
pip install -r pip.config
```

## References

https://towardsdatascience.com/simple-little-tables-with-matplotlib-9780ef5d0bc4
