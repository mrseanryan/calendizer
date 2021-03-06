# :calendar: calendizer README

Generates images of calendar month tables and can paste them onto suitable photos.

A quick way to make your own calendar for printing.

![Robin in April](exampleImages/2022-04-April--P1180988-robin.small.jpg "A robin in April")

## Usage

To generate 12 images of a mini calendar:

`render_calendar_tables.py <year> <path to output directory>`

To take 12 images and use them to create a calendar:

`calendize.py <year> <path to directory with 12 images in PNG or JPEG format> <path to output directory>`

For a full list of options, just type the relevant command:

`render_calendar_tables.py`

`calendize.py`

### Tips

With an input image of size 4000 x 3000, these settings seem to work well:

`--dpi 400 -b 100 -r 100`

There is an alpha (transparency) option:

`-a 0.8`

but printing on a small size like 2L or A5 looks better with the default opaque setting.

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

# license

License is [MIT](./LICENSE)
