import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import helper


def draw_figure(measured_new_time, calculated_new_time):
    fig = plt.figure()
    fig.subplots_adjust(bottom=0.32, top=0.91)
    ax1 = fig.add_axes(plt.subplot())
    ax1.set_title('Complexity analysis for insertion sort')
    red_patch = mpatches.Patch(color='red', label='Measured time series')
    green_patch = mpatches.Patch(color='green', label='Calculated time series')
    plt.legend(handles=[red_patch, green_patch])

    txt = "For array of %s elements: \nMeasured time - %s seconds \nCalculated time -  %s seconds." \
          % (helper.NEW_ARRAY_SIZE, measured_new_time, calculated_new_time)

    plt.text(.0, -.09, txt)
    ax1.set_xlabel('Number of elements in list')
    ax1.set_ylabel('Time, seconds')
    return ax1


def draw_measured(xlist, ylist, ax):
    ax.plot(xlist, ylist, 'ro')


def draw_calculated(xlist, ylist):
    plt.plot(xlist, ylist, 'g')


def show_plot():
    plt.show()
