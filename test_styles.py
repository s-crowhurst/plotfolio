import matplotlib.pyplot as plt
import numpy as np

# List of palettes
palette_start = 1
num_palettes = 8 
palettes = [f'Light-0{palette_start+i}' for i in range(num_palettes)]

# Data
x = np.linspace(0, 10, 100)
np.random.seed(42)
scatter_x = np.random.randn(100)
scatter_y = np.random.randn(100)
categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 20, 30, 40, 50]
hist_data = np.random.randn(1000)

rows = num_palettes
cols = 4  # line, scatter, bar, histogram
fig_combined = plt.figure(figsize=(24, rows*4))
gs = fig_combined.add_gridspec(rows, cols, hspace=0.5, wspace=0.4)

for row, palette in enumerate(palettes):
    plt.style.use(palette)

    # Create axes for this row with the palette's facecolor
    ax_line = fig_combined.add_subplot(gs[row, 0])
    ax_scatter = fig_combined.add_subplot(gs[row, 1])
    ax_bar = fig_combined.add_subplot(gs[row, 2])
    ax_hist = fig_combined.add_subplot(gs[row, 3])

    # Line plot
    for i in range(6):
        ax_line.plot(x, np.sin(x + i*0.5), label=f'Line {i+1}')
    ax_line.set_title('Colour Cycle Test')
    ax_line.set_ylabel('Y axis')
    ax_line.set_xlabel('X axis')
    ax_line.legend(fontsize=6)

    # Scatter
    ax_scatter.scatter(scatter_x, scatter_y)
    ax_scatter.set_title('Scatter Plot')
    ax_scatter.set_ylabel('Y axis')
    ax_scatter.set_xlabel('X axis')

    # Bar
    ax_bar.bar(categories, values)
    ax_bar.set_title('Bar Chart')
    ax_bar.set_ylabel('Value')
    ax_bar.set_xlabel('Category')

    # Histogram
    ax_hist.hist(hist_data, bins=30)
    ax_hist.set_title('Histogram')
    ax_hist.set_ylabel('Frequency')
    ax_hist.set_xlabel('Value')

    # Palette name label
    ax_line.text(-0.5, 0.5, palette, verticalalignment='center', transform=ax_line.transAxes)

plt.savefig('plot_styles.pdf', bbox_inches='tight', pad_inches=0.5)
