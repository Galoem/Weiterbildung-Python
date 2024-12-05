from matplotlib import pyplot

def create_plot(data: dict, title: str, x_label: str, y_label: str) -> None:
    x_keys = sorted(data.keys())
    y_values = [data[key] for key in x_keys]

    # Create the line plot
    pyplot.plot(x_keys, y_values)

    # Customize plot as needed (e.g., title, labels, legend)
    pyplot.title(title)
    pyplot.xlabel(x_label)
    pyplot.ylabel(y_label)
    pyplot.show()