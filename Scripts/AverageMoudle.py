from traceback import print_list
import pandas as pd
import matplotlib.pyplot as plt
import DrawerMoudle

class Average:

    def __init__(self):
        self.Chosen_Cell_List = []

    def print_list(self):
        ls = []
        for c in self.Chosen_Cell_List:
            ls.append(c.get_Dictonary()["cell_id"])
        print(ls)

    def remove_cell(self, cell):
        new_cell_id = cell.get_Dictonary()["cell_id"]
        for c in self.Chosen_Cell_List:
            if c.get_Dictonary()["cell_id"] == new_cell_id:
                 self.Chosen_Cell_List.remove(c)
        self.print_list()

    def save_cell(self, cell):
        new_cell_id = cell.get_Dictonary()["cell_id"]
        for c in self.Chosen_Cell_List:
            if c.get_Dictonary()["cell_id"] == new_cell_id:
                return
        self.Chosen_Cell_List.append(cell)
        self.print_list()
    
    def convert_Final_df_to_csv(self, df):
        df.to_csv('Final_DF.csv')

    def calculate_average(self):
        div_factor = len(self.Chosen_Cell_List)
        Main_DF = self.Chosen_Cell_List[0].get_normalize_cunductivity_df()
        print(type(Main_DF))
        self.Chosen_Cell_List.remove(self.Chosen_Cell_List[0])

        for c in self.Chosen_Cell_List:
            Main_DF.add(c.get_normalize_cunductivity_df())

        Main_DF.div(div_factor)

        DrawerMoudle.draw_final_avarage_df(Main_DF)
        self.convert_Final_df_to_csv(Main_DF)
