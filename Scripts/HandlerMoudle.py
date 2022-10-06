
import os
import csv
from CellMoudle import Cell
from AverageMoudle import Average



class Handler: 
    
    def __init__(self):
        self.Cell_List = []
        self.progress = 0
        self.Chosen_Cell_List = []
        self.Averager = Average()
        
    
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
    
    def generate_high_value_for_all_cells(self):
        for c in self.Cell_List:
            c.generate_high_value()

    def create_cunductivity_normalize_by_high_value_for_cells(self):
        for c in self.Cell_List:
            c.create_cunductivity_dF_normalize_by_high_value()

    def generate_A_Sigmoid_value_for_all_cells(self):
        for c in self.Cell_List:
            c.generate_A_sigmoid_value()

    def draw_all(self):
        i = 0
        while(True):
            self.Cell_List[i].send_to_draw()
            Ans = input("What Do You Want? b/s/r/x: ")
            if(Ans == 'b'):
                i -= 1
            if(Ans == 's'):
                self.Averager.save_cell(self.Cell_List[i])
                self.Cell_List[i].set_is_chosen('Yes')
                i += 1
            if(Ans == 'r'):
                self.Averager.remove_cell(self.Cell_List[i])
                self.Cell_List[i].set_is_chosen('No')
                i += 1
            if(Ans == 'x'):
                self.Averager.calculate_average()
                return
            
            if (i >= len(self.Cell_List)):
                i = 0

            





handler = Handler()
handler.CSV_To_List()
handler.generate_cut_for_all_cells()
handler.calc_inear_regression_for_cells()
handler.create_dots_arr_for_cells()
handler.create_dF_subtract_for_cells()
handler.create_cunductivity_for_cells()
handler.generate_high_value_for_all_cells()
handler.create_cunductivity_normalize_by_high_value_for_cells()
handler.generate_A_Sigmoid_value_for_all_cells()
handler.draw_all()


