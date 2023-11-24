import pandas as pd 
import numpy as np 
import pickle
import json
import warnings
warnings.filterwarnings("ignore")

import config

class BangloruClass():

    def __init__(self,area_type,availability,size,total_sqft,bath,balcony,location):
    
    
    
    
        self.area_type = area_type
        self.availability = availability
        self.size = size
        self.total_sqft = total_sqft
        self.bath = bath
        self.balcony = balcony
        self.location = "location_" + location   # user input 
        
        
    def model_load(self):
        
        with open(config.JSON_FILE,'r') as f:                      # "JSON_.json"
            self.JSON_ = json.load(f)
            
        # load model
        
        with open(config.Model_FILE,'rb') as f:
            self.Model = pickle.load(f)
            
            
    def predict_(self):
        
        self.model_load()
        
        location_index = list(self.JSON_['columns']).index(self.location)
        
        array = np.zeros(len(self.JSON_['columns']))
        
        array[0] = self.JSON_['area_type'][self.area_type]
        array[1] = self.JSON_['availability'][self.availability]
        array[2] = self.JSON_['size'][self.size]
        array[3] = self.total_sqft
        array[4] = self.bath
        array[5] = self.balcony

        array[location_index] = 1
        
        print("output__array___",array)
        
        prediction = round(self.Model.predict([array])[0],2)
        print(prediction)
        return f'final output----{prediction}'
        
if __name__=="__main__":
    area_type = "Plot  Area"
    availability = '18-Jun'
    size = '18 Bedroom'
    total_sqft = '3040Sq. Meter'
    bath = 2.00
    balcony = 1.00

    location = "Yelahanka"
   
    obj = BangloruClass(area_type,availability,size,total_sqft,bath,balcony,location)
    prediction = obj.predict_()

    print(prediction)

