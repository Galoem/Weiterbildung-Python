from matplotlib import pyplot
import numpy

# def create_plot(data: dict, title: str, x_label: str, y_label: str) -> None:
#     x_keys = sorted(data.keys())
#     y_values = [data[key] for key in x_keys]

#     # Create the line plot
#     pyplot.bar(x_keys, y_values)

#     # Customize plot as needed (e.g., title, labels, legend)
#     pyplot.title(title)
#     pyplot.xlabel(x_label)
#     pyplot.ylabel(y_label)
#     pyplot.show()

def create_plot_subplots():
    # Create some data
    x = numpy.arange(5)
    y1 = numpy.random.rand(5)
    y2 = numpy.random.rand(5)

    # Create a figure and a set of subplots
    fig, axs = pyplot.subplots(nrows=2, ncols=2, figsize=(10,8))

    # Create a bar plot on the first subplot
    axs[0, 0].bar(x, y1)
    axs[0, 0].set_title('Bar Plot 1')

    # Create a bar plot on the second subplot
    axs[0, 1].bar(x, y2)
    axs[0, 1].set_title('Bar Plot 2')

    # Create a bar plot on the first subplot
    axs[1, 0].bar(x, y1)
    axs[1, 0].set_title('Bar Plot 3')

    # Create a bar plot on the second subplot
    axs[1, 1].bar(x, y2)
    axs[1, 1].set_title('Bar Plot 4')

    # Layout so plots do not overlap
    fig.tight_layout()

    pyplot.show()
