from calendar import month
import numpy as np
import matplotlib.pyplot as plt
import os

import date_utils

# config
OUTDIR = "temp"
DPI = 150
BORDER_COLOR = 'black'
YEAR = 2022

# fig_background_color = 'white'


# 1 = January
month = 1

title_text = f"{date_utils.month_name(month)} {YEAR}"

column_headers = ['Mon', 'Tue', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun']

data = [
    # ['Mon', 'Tue', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun'],
]

# Generate the calendar data for the month
days_in_month = date_utils.days_in_month(YEAR, month)

row = None
for day_of_month in range(1, days_in_month + 1):
    weekday = date_utils.weekday_zero_is_monday(YEAR, month, day_of_month)
    # First row needs fillers:
    if (row == None):
        row = [''] * weekday
    row.append(str(day_of_month))
    if(weekday == 6):
        data.append(row)
        row = []

if (weekday < 6):
    data.append(row)

while(len(row) < 7):
    row.append('')

# note: Table data needs to be non-numeric text.
cell_text = data

# Get some lists of color specs for column headers
ccolors = plt.cm.BuPu(np.full(len(column_headers), 0.1))

# Create the figure. Setting a small pad on tight_layout
# seems to better regulate white space. Sometimes experimenting
# with an explicit figsize here can produce better outcome.
plt.figure(linewidth=2,
           edgecolor=BORDER_COLOR,
           tight_layout={'pad': 0.1},
           figsize=(3, 2)
           )
# Add a table at the bottom of the axes
the_table = plt.table(cellText=cell_text,
                      rowLoc='right',
                      colColours=ccolors,
                      colLabels=column_headers,
                      loc='center')
# TODO set the border color of the table cells

# Scaling is the only influence we have over top and bottom cell padding.
# Make the rows taller (i.e., make cell y scale larger).
the_table.scale(1, 1)

# Hide axes
ax = plt.gca()
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

# Hide axes border
plt.box(on=None)

plt.suptitle(title_text)

# Force the figure to update, so backends center objects correctly within the figure.
# Without plt.draw() here, the title will center on the axes and not the figure.
plt.draw()

# Create image. plt.savefig ignores figure edge and face colors, so map them.
fig = plt.gcf()
plt.savefig(os.path.join(OUTDIR, 'pyplot-table-demo.png'),
            # bbox='tight',
            edgecolor=fig.get_edgecolor(),
            dpi=DPI
            )
