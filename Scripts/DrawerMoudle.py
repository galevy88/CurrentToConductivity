
import pandas as pd
import matplotlib.pyplot as plt

VOLT_ARR = [-90, -80, -70, -60, -50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50, 60 ,70, 80] ######### CHECK FOR CORRECTION #########
MAJOR_FACTOR = 10
MINOR_FACTOR = 5

MINVALUE1 = -0.05
MINVALUE2 = 0


def draw_subplot(dF1, dF2, dF3, dF4, dF5, cell_id, temperature):

    y1_max = dF1.iloc[5000][80]
    y2_max = dF2.iloc[5000][80]
    y3_max = dF3.iloc[5000][80]
    epsilon1 = y1_max/MINOR_FACTOR
    epsilon2 = y2_max/MINOR_FACTOR
    epsilon3 = y3_max/MAJOR_FACTOR


    fig, axs = plt.subplots(2, 2)
    fig.set_size_inches(13, 7.5)
    axs[0, 0].plot(dF1)
    axs[0, 0].set_title("current dF")
    if temperature == '15':
        axs[0, 0].set_ylim(MINVALUE1, y1_max + epsilon1)

    axs[1, 0].plot(dF2)
    axs[1, 0].set_title("current dF after subtract")
    if temperature == '15':
        axs[1, 0].set_ylim(MINVALUE1, y2_max + epsilon2)

    axs[0, 1].plot(dF3)
    axs[0, 1].set_title("cunductivity dF")
    if temperature == '15':
        axs[0, 1].set_ylim(MINVALUE2, y3_max + epsilon3)

    axs[1, 1].plot(dF4, color = 'red', label = 'Historical data')
    axs[1, 1].plot(dF5, color = 'red', label = 'Historical data')
    axs[1, 1].set_title("cut")
    default_x_ticks = range(len(dF4))
    axs[1, 1].plot(default_x_ticks, dF4)
    plt.xticks(default_x_ticks, VOLT_ARR)

    fig.tight_layout()
    fig.suptitle(f'id: {cell_id} temp: {temperature}')
    plt.show()







# def draw_one_dataframe(dF, cell_id, factor, min_value):
#     y_max = dF.iloc[5000][80]
#     print(y_max)
#     epsilon = y_max/factor
#     dF.plot(title = f'Current DataFrame {cell_id}')
#     ax = plt.gca()
#     ax.set_ylim([min_value, y_max + epsilon])
#     plt.show()