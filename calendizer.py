import numpy as np
import matplotlib.pyplot as plt
import os

# config
OUTDIR = "temp"
DPI = 150
BORDER_COLOR = 'black'
TITLE_TEXT = 'January 2022'

# fig_background_color = 'white'

data = [
    ['Mon', 'Tue', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun'],
    ['',    '',    '',    '',      '',    '1',   '2'],
    ['3',   '4',   '5',   '6',     '7',   '8',   '9'],
    ['10',  '11',  '12',  '13',    '14',  '15',  '16'],
    ['17',  '18',  '19',  '20',    '21',  '22',  '23'],
    ['24',  '25',  '26',  '27',    '28',  '29',  '30'],
    ['31',  '',    '',    '',      '',    '',    '']
]

# Pop the headers from the data array
column_headers = data.pop(0)

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

plt.suptitle(TITLE_TEXT)

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
