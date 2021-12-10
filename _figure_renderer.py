import numpy as np
import matplotlib.pyplot as plt

def render(cell_text, column_headers, title_text, border_color, dpi, outpath):
    # Get some lists of color specs for column headers
    ccolors = plt.cm.BuPu(np.full(len(column_headers), 0.1))

    # Create the figure. Setting a small pad on tight_layout
    # seems to better regulate white space. Sometimes experimenting
    # with an explicit figsize here can produce better outcome.
    plt.figure(linewidth=2,
            tight_layout={'pad': 0.1},
            figsize=(3, 2)
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
