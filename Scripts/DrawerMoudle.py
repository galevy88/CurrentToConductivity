
import pandas as pd
import matplotlib.pyplot as plt

VOLT_ARR = [-90, -80, -70, -60, -50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50, 60 ,70, 80] ######### CHECK FOR CORRECTION #########
MAJOR_FACTOR = 10
MINOR_FACTOR = 5

MINVALUE1 = -0.05
MINVALUE2 = 0


def draw_subplot(current_df, current_df_after_subtract, cunductivity_df, cut, dots,cunductivity_normalize_higher_value, cell_id, temperature):

    y1_max = current_df.iloc[5000][80]
    y2_max = current_df_after_subtract.iloc[5000][80]
    y3_max = cunductivity_df.iloc[5000][80]
    epsilon1 = y1_max/MINOR_FACTOR
    epsilon2 = y2_max/MINOR_FACTOR
    epsilon3 = y3_max/MAJOR_FACTOR


    fig, axs = plt.subplots(2, 3)
    fig.set_size_inches(16, 7.5)
    axs[0, 0].plot(current_df)
    axs[0, 0].set_title("current dF")
    if temperature == '15':
        axs[0, 0].set_ylim(MINVALUE1, y1_max + epsilon1)

    axs[1, 0].plot(current_df_after_subtract)
    axs[1, 0].set_title("current dF after subtract")
    if temperature == '15':
        axs[1, 0].set_ylim(MINVALUE1, y2_max + epsilon2)

    axs[0, 1].plot(cunductivity_df)
    axs[0, 1].set_title("cunductivity dF")
    if temperature == '15':
        axs[0, 1].set_ylim(MINVALUE2, y3_max + epsilon3)

    axs[1, 1].plot(cut, color = 'red', label = 'Historical data')
    axs[1, 1].plot(dots, color = 'red', label = 'Historical data')
    axs[1, 1].set_title("cut")
    default_x_ticks = range(len(cut))
    axs[1, 1].plot(default_x_ticks, cut)
    plt.xticks(default_x_ticks, VOLT_ARR)

    axs[0, 2].plot(cunductivity_normalize_higher_value)
    axs[0, 2].set_title("cunductivity_normalize_higher_value")
    if temperature == '15':
        axs[0, 2].set_ylim(-0.05, 1.05)

    
    axs[0, 2].plot(cunductivity_normalize_higher_value)
    axs[0, 2].set_title("cunductivity_normalize_higher_value")
    if temperature == '15':
        axs[0, 2].set_ylim(-0.05, 1.05)

    fig.tight_layout()
    fig.suptitle(f'id: {cell_id} temp: {temperature}\n')
    plt.show()







# def draw_one_dataframe(dF, cell_id, factor, min_value):
#     y_max = dF.iloc[5000][80]
#     print(y_max)
#     epsilon = y_max/factor
#     dF.plot(title = f'Current DataFrame {cell_id}')
#     ax = plt.gca()
#     ax.set_ylim([min_value, y_max + epsilon])
#     plt.show()