import numpy as np
import matplotlib.pyplot as plt
import os

import _calendar_model
import _date_utils

def render_table_for_month(month, YEAR, OUTDIR, BORDER_COLOR, DPI):

    # note: Table data needs to be non-numeric text.
    cell_text = _calendar_model.get_month_data(month, YEAR)

    column_headers = _calendar_model.get_column_headers()

    title_text = _calendar_model.get_month_title(month, YEAR)

    month_2_digits = f"{month:02d}"
    outpath = os.path.join(OUTDIR, f"{YEAR}-{month_2_digits}-{_date_utils.month_name(month)}.png")

    render(cell_text, column_headers, title_text, BORDER_COLOR, DPI, outpath)
    return outpath

def render(cell_text, column_headers, title_text, border_color, dpi, outpath):
    # Get some lists of color specs for column headers
    ccolors = plt.cm.BuPu(np.full(len(column_headers), 0.1))

    # Create the figure. Setting a small pad on tight_layout
    # seems to better regulate white space. Sometimes experimenting
    # with an explicit figsize here can produce better outcome.
    plt.figure(linewidth=2,
            tight_layout={'pad': 0.1},
            figsize=(3, 2),
            edgecolor=border_color
            )
    # Add a table at the bottom of the axes
    the_table = plt.table(cellText=cell_text,
                        rowLoc='right',
                        colColours=ccolors,
                        colLabels=column_headers,
                        loc='center')
    # TODO set the border color of the table cells - border_color

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
    figure = plt.gcf()

    plt.savefig(outpath,
                # bbox='tight',
                edgecolor=figure.get_edgecolor(),
                dpi=dpi
                )
