#!/usr/bin/python3

import tensorflow as tf
import pandas as pd
import ml_process

class Predictor(ml_process.ML_process_class) :
    def __init__(self):
        super().__init__()
        self.predict_data_source = None # 나중에 디폴트 설정넣어놔야함

    def read_data(self, data_read_where):
        pass

    def main(self):
        self.config()




if __name__ == '__main__' :
    predictor = Predictor()
    predictor.main()
