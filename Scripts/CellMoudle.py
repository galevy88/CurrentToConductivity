
from statistics import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt
import DrawerMoudle
import numpy as np
from asyncio.windows_events import NULL
from sklearn.linear_model import LogisticRegression



def create_ls():
    ls = []
    for i in range (0,19):
        ls.append(i)
    return ls
    
def create_ls_1():
    ls = []
    for i in range (0,18):
        ls.append(i)
    return ls

CHOSEN_ROW = 3550
LEFT_VOLT_EDGE = -90
RIGHT_VOLT_EDGE = -60
VOLT_ARR = [-90, -80, -70, -60, -50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50, 60 ,70, 80] ######### CHECK FOR CORRECTION #########
VOLT_Index = [-100, -90, -80, -70, -60, -50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50, 60 ,70, 80] ######### CHECK FOR CORRECTION #########



class Cell:

    def __init__(self, channel_type, Kv_type, Kv_sub_type, temperature, cell_id):
        self.information_Dictonary = self.fetch_Dict(channel_type, Kv_type, Kv_sub_type, temperature, cell_id)
        self.path = self.generate_path()
        self.current_dF = NULL
        self.current_dF_after_substract = NULL
        self.cunductivity_dF = NULL
        self.cunductivity_dF_normalize_high_value = NULL
        self.cut = NULL
        self.high_value = NULL
        self.slope = NULL
        self.b = NULL
        self.dots = NULL
        self.Ek = self.generate_Ek()
        self.sigmoid_Values = []
        self.isChosen = 'NotDecided'

    def generate_Ek(self):
        temperature_str = self.information_Dictonary["temperature"]
        temperature = float(temperature_str)
        Ek = -0.285 * (temperature + 273)
        return Ek

    def get_df_for_myself(self):
        ls = create_ls()
        cell_id = self.information_Dictonary["cell_id"]
        self.current_dF = pd.read_csv(f'{self.path}\\{cell_id}_Activation_rep2.csv', names=VOLT_Index)
        self.current_dF = self.current_dF.iloc[: , 1:]
        self.remove_edges()
         

    def remove_edges(self):
        for i in range(0, 990):
            self.current_dF = self.current_dF.drop(i)
        
        for i in range(6000, 6990):
            self.current_dF = self.current_dF.drop(i)

    def generate_mid_Cut(self):
        cut = self.current_dF.loc[CHOSEN_ROW, :].values.tolist()
        self.cut = cut


    def calc_linear_regression(self):
        y2 = self.cut[2]
        y1 = self.cut[0]
        x2 = RIGHT_VOLT_EDGE
        x1 = LEFT_VOLT_EDGE
        slope = ((y2 - y1) / (x2 - x1))
        b = y2 - (slope * x2)
        self.slope = slope
        self.b = b


    def create_subtract_dots(self):
        dots_Arr = []
        for v in VOLT_ARR:
            I = (self.slope * v) + self.b
            dots_Arr.append(I)
        self.dots = dots_Arr


    def subtract_dots_from_dF_current(self):
        self.current_dF_after_substract =  self.current_dF.subtract(self.dots, axis = 1)
        
    def generate_path(self):
        channel_type = self.information_Dictonary["channel_type"]
        Kv_type = self.information_Dictonary["Kv_type"]
        Kv_sub_type = self.information_Dictonary["Kv_sub_type"]
        temperature = self.information_Dictonary["temperature"]
        cell_id = self.information_Dictonary["cell_id"]
        path = f'{channel_type}\\{Kv_type}\\{Kv_sub_type}\\{temperature}\\{cell_id}'
        return path

    def create_cunductivity_dF(self):
        i = 0
        self.cunductivity_dF = self.current_dF_after_substract.copy()
        for column in self.current_dF_after_substract:
            col_to_add = self.current_dF_after_substract[column]
            self.cunductivity_dF[column] = col_to_add.div(VOLT_ARR[i] - self.Ek)
            i+=1

    def generate_high_value(self):
        last_col = self.cunductivity_dF.iloc[ : , -1:].values
        self.high_value = max(last_col)
        # print(f'High Value Of Cell {self.information_Dictonary["cell_id"]} is: {self.high_value[0]}')

    def create_cunductivity_dF_normalize_by_high_value(self):
        self.cunductivity_dF_normalize_high_value = self.cunductivity_dF.div(self.high_value[0])

    def generate_A_sigmoid_value(self):
        for column in self.cunductivity_dF:
            self.sigmoid_Values.append(max(self.cunductivity_dF[column]))
        self.sigmoid_Values[1] = (self.sigmoid_Values[0] + self.sigmoid_Values[2]) / 2
        

    def get_normalize_cunductivity_df(self):
        return self.cunductivity_dF_normalize_high_value

    def set_is_chosen(self, choice):
        self.isChosen = choice
        

    # DRAW AREA
    def send_to_draw(self):
        DrawerMoudle.draw_subplot(self.current_dF, self.current_dF_after_substract, self.cunductivity_dF, self.cut, self.dots, self.cunductivity_dF_normalize_high_value, self.sigmoid_Values, self.information_Dictonary["cell_id"], self.information_Dictonary["temperature"], self.isChosen)


    # DICT AREA
    def fetch_Dict(self, channel_type, Kv_type, Kv_sub_type, temperature, cell_id):
        new_Dict = {
            "channel_type" : channel_type,
            "Kv_type" : Kv_type,
            "Kv_sub_type" : Kv_sub_type,
            "temperature" : temperature,
            "cell_id" : cell_id
        }
        return new_Dict

    def get_Dictonary(self):
        return self.information_Dictonary













    # def draw_current_dF(self):
    #     DrawerMoudle.draw_one_dataframe(self.current_dF, self.information_Dictonary["cell_id"], 5, -0.05)

    # def draw_current_dF_after_subtract(self):
    #     DrawerMoudle.draw_one_dataframe(self.current_dF_after_substract, self.information_Dictonary["cell_id"], 5, -0.05)

    # def draw_cunductivity_dF(self):
    #     DrawerMoudle.draw_one_dataframe(self.cunductivity_dF, self.information_Dictonary["cell_id"], 10, 0)

    # def draw_plot(self):
    #     plt.plot(self.cut, color = 'red', label = 'Historical data')
    #     plt.plot(self.dots, color = 'green', label = 'Historical data')
    #     default_x_ticks = range(len(self.cut))
    #     plt.plot(default_x_ticks, self.cut)
    #     plt.xticks(default_x_ticks, VOLT_ARR)
    #     plt.show()




# FOR GENERTATE SIGMOID:

        # classifier = LogisticRegression(random_state = 0)
        # fit_ls = create_ls_1()
        # fit_ls = np.array(fit_ls)
        # ls = np.array(ls)
        # fit_ls = fit_ls.reshape(len(fit_ls),1)
        # ls = ls.reshape(len(ls),1)
        # classifier.fit(fit_ls, ls)
        # print(f'COEF: {classifier.coef_}')
