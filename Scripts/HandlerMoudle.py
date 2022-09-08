
import os
import csv
from CellMoudle import Cell



class Handler: 
    
    def __init__(self):
        self.Cell_List = []
        self.progress = 0
        
    
    def CSV_To_List(self):
        with open(f'wantd_cell_list.csv') as csv_file:
            reader_csv = csv.reader(csv_file)
            for row in reader_csv:
                if(row != []):
                    cell_Obj = Cell(row[0], row[1], row[2], row[3], row[4])
                    cell_Obj.get_df_for_myself()
                    self.Cell_List.append(cell_Obj)
                    print(self.progress)
                    self.progress += 1


    def generate_cut_for_all_cells(self):
        for c in self.Cell_List:
            c.generate_mid_Cut()


    def calc_inear_regression_for_cells(self):
        for c in self.Cell_List:
            c.calc_linear_regression()


    def create_dots_arr_for_cells(self):
        for c in self.Cell_List:
            c.create_subtract_dots()


    def create_dF_subtract_for_cells(self):
        for c in self.Cell_List:
            c.subtract_dots_from_dF_current()

    def create_cunductivity_for_cells(self):
        for c in self.Cell_List:
            c.create_cunductivity_dF()

    def draw_all(self):
        for c in self.Cell_List:
            c.send_to_draw()
        # self.Cell_List[10].send_to_draw()
    
    
    # def fetch_cut_plot_for_cells(self):
    #     for c in self.Cell_List:
    #         c.draw_plot()
    #     # self.Cell_List[10].draw_plot()





handler = Handler()
handler.CSV_To_List()
handler.generate_cut_for_all_cells()
handler.calc_inear_regression_for_cells()
handler.create_dots_arr_for_cells()
handler.create_dF_subtract_for_cells()
handler.create_cunductivity_for_cells()
handler.draw_all()
# handler.fetch_cut_plot_for_cells()

