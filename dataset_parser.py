import pandas as pd
from abc import ABCMeta, abstractmethod
import os
class DataserParser(metaclass=ABCMeta):

    def __init__(self):
        path = os.path.join(os.getcwd(),"data","a_example.in")#
        df = pd.read_csv(path, header=None, sep=" ")
        matrix = df.as_matrix()
        self.rows, self.cols, self.n_vehicles, self.rides, self.bonus, self.steps = matrix[0]
        self.ride_information = matrix[1:,:]
if __name__ == '__main__':
    dr = DataserParser()
    print(dr.rows)
    print(dr.ride_information)