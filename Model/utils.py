import pickle
import json
import numpy as np
import pandas as pd
import config

class AutoData() :
    def __init__ (self,symboling,normalized_losses,make,fuel_type,aspiration,num_of_doors,body_style,
        drive_wheels,engine_location,wheel_base,length,width,height,curb_weight,engine_type,
        num_of_cylinders,engine_size,fuel_system,bore,stroke,compression_ratio,horsepower,peak_rpm,
        city_mpg,highway_mpg) :
        
        self.symboling = symboling
        self.normalized_losses = normalized_losses
        self.make = "make_" + make
        self.fuel_type = fuel_type
        self.aspiration = aspiration
        self.num_of_doors = num_of_doors
        self.body_style = "body-style_" + body_style
        self.drive_wheels = drive_wheels
        self.engine_location = engine_location
        self.wheel_base = wheel_base
        self.length = length
        self.width = width
        self.height = height
        self.curb_weight = curb_weight
        self.engine_type = "engine-type_" + engine_type
        self.num_of_cylinders = num_of_cylinders
        self.engine_size = engine_size
        self.fuel_system = "fuel-system_" + fuel_system
        self.bore = bore
        self.stroke = stroke
        self.compression_ratio = compression_ratio
        self.horsepower = horsepower
        self.peak_rpm = peak_rpm
        self.city_mpg = city_mpg
        self.highway_mpg = highway_mpg

    def load_model (self) :
        with open (config.Auto_MODEL_FILE_PATH,"rb") as f:
            self.model = pickle.load(f)
        with open (config.Auto_JSON_FILE_PATH) as f:
            self.json_data = json.load(f)

    def get_predicted_price (self) :
        self.load_model()

        make_index = self.json_data["columns"].index(self.make)
        body_style_index = self.json_data["columns"].index(self.body_style)
        engine_type_index = self.json_data["columns"].index(self.engine_type)
        fuel_system_index = self.json_data["columns"].index(self.fuel_system)

        array = np.zeros(len(self.json_data["columns"]))

        array[0] = self.symboling
        array[1] = self.normalized_losses
        array[2] = self.json_data["fuel-type"][self.fuel_type]
        array[3] = self.json_data["aspiration"][self.aspiration]
        array[4] = self.json_data["num-of-doors"][self.num_of_doors]
        array[5] = self.json_data["drive-wheels"][self.drive_wheels]
        array[6] = self.json_data["engine-location"][self.engine_location]
        array[7] = self.wheel_base
        array[8] = self.length
        array[9] = self.width
        array[10] = self.height
        array[11] = self.curb_weight
        array[12] = self.json_data["num-of-cylinders"][self.num_of_cylinders]
        array[13] = self.engine_size
        array[14] = self.bore
        array[15] = self.stroke
        array[16] = self.compression_ratio
        array[17] = self.horsepower
        array[18] = self.peak_rpm
        array[19] = self.city_mpg
        array[20] = self.highway_mpg
        array[make_index] = 1
        array[body_style_index] = 1
        array[engine_type_index] = 1
        array[fuel_system_index] = 1

        print ("Test Array :\n",array)
        predicted_price = self.model.predict([array])[0]
        print ("Predicted Price :",predicted_price)
        return np.around(predicted_price,2)

if __name__ == "__main__" :
    symboling = 2
    normalized_losses = 192
    make = "honda"
    fuel_type = "gas"
    aspiration = "turbo"
    num_of_doors = "four"
    body_style = "sedan"
    drive_wheels = "rwd"
    engine_location = "front"
    wheel_base = 95.7
    length = 170.7
    width = 71.4
    height = 52
    curb_weight = 1889
    engine_type = "ohc"
    num_of_cylinders = "eight"
    engine_size = 141
    fuel_system = "spfi"
    bore = 3.31
    stroke = 3.1
    compression_ratio = 10
    horsepower = 70
    peak_rpm = 5000
    city_mpg = 24
    highway_mpg = 29

    Autos_data = AutoData(symboling,normalized_losses,make,fuel_type,aspiration,num_of_doors,body_style,
        drive_wheels,engine_location,wheel_base,length,width,height,curb_weight,engine_type,
        num_of_cylinders,engine_size,fuel_system,bore,stroke,compression_ratio,horsepower,peak_rpm,
        city_mpg,highway_mpg)
    price = Autos_data.get_predicted_price()
    print ()
    print (f"Sales of Respective Outlet is {price}")