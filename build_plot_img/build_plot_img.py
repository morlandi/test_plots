import os
import csv
import matplotlib
import datetime
from matplotlib import pyplot as plt


def chart_colors():
    return [
        # Dygraphs defaults
        "rgb(0,85,128)",
        "rgb(85,128,0)",
        "rgb(0,0,128)",
        "rgb(0,128,0)",
        "rgb(85,0,128)",
        "rgb(0,128,85)",
        "rgb(128,0,85)",
        "rgb(128,85,0)"
    ]


def chart_color(index):
    colors = chart_colors()
    return colors[index % len(colors)]


def rgb_string_to_color_code(rgb_string):
    try:
        left_brace_position = rgb_string.find('(')
        right_brace_position = rgb_string.find(')')
        content = rgb_string[left_brace_position + 1:right_brace_position]
        tokens = [int(t) for t in content.split(',')]
        color_code = '#%02x%02x%02x' % (tokens[0], tokens[1], tokens[2], )
    except:
        color_code = '#000000'
    return color_code

def format_x_time(seconds, x):
    text = str(datetime.timedelta(seconds=seconds))
    #remove leading "0:"
    if text.startswith('0:'):
        text = text[2:]
    return text


def build_plot_img(input_filename, output_filename):
    """
    Read rectangular data from given "input_filename" CSV file, and build a bitmap with the plot;
    the result is saved in "output_filename"
    """
    data = _csv_to_plot_data(input_filename)
    x = data['x']
    num_cols = len(data['columns'])

    # Scan columns
    # for index, y in enumerate(data['columns']):
    #     # add this column to chart
    #     color = rgb_string_to_color_code(chart_color(index))
    #     plt.plot(x, y, color, linewidth=1)
    formatter = matplotlib.ticker.FuncFormatter(format_x_time)
    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(8,3), dpi=72, tight_layout=True)
    axes.xaxis.set_major_formatter(formatter)
    for index, y in enumerate(data['columns']):
        # add this column to chart
        color = rgb_string_to_color_code(chart_color(index))
        axes.plot(x, y, color, linewidth=1)

    # plt.ylabel('some numbers')
    plt.grid()
    plt.savefig(output_filename)  # , dpi=600)


# Helpers
def _csv_to_plot_data(filename):

    # Collect rows from CSV input file
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        matrix = []
        for i, row in enumerate(reader):
            matrix.append(row)

    # Prepare "data" structure
    data = {
        'labels': matrix[0],
        'x': [],
        'columns': [],
    }

    # Transpose matrix and feed "data"
    num_labels = len(data['labels'])
    for index in range(0, num_labels):
        values = [float(row[index]) if i>0 else 0 for i, row in enumerate(matrix)][1:]
        if index == 0:
            data['x'] = values
        else:
            data['columns'].append(values)

    return data


if __name__ == "__main__":

    filenames = [
        "test_145_2",
        "test_145_1",
        "test_145_3",
    ]

    for filename in filenames:
        if os.path.isfile(filename + ".png"):
            os.remove(filename + ".png")
        build_plot_img(filename + ".csv", filename + ".png")

    # for filename in filenames:
    #     os.system("open %s" % filename + ".png")
