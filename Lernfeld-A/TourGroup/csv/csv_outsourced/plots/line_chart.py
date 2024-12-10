from matplotlib import pyplot
from pprint import pprint

def create_plot(data: dict, title: str, x_label: str, y_label: str) -> None:
    years = sorted(data.keys())
    values = [data[key] for key in years]

    # Create the line plot
    pyplot.plot(years, values)

    # Customize plot as needed (e.g., title, labels, legend)
    pyplot.title(title)
    pyplot.xlabel(x_label)
    pyplot.ylabel(y_label)
    pyplot.show()

def create_multi_line_plot(data: dict, title: str, x_label: str, y_label: str):
    pprint(data)
    years = sorted(data.keys())
    values: list = list()
    legend = list()
    pprint(values)
    for item in values:
        item: dict
        for key in item.keys():
            pass # was machen?

    pyplot.xlabel(x_label)
    pyplot.ylabel(y_label)
    pyplot.title(title)
    pyplot.legend(legend)
    # pyplot.show()
