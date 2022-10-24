from distutils.command.config import config
from flask import Flask,render_template,jsonify,request
from Model.utils import AutoData
import config

app = Flask(__name__)

@app.route("/")
def hello_flask() :
    print ("Welcome to Car Price Prediction")
    return render_template ("index.html")

@app.route("/predict_price",methods = ["POST","GET"])
def Car_price () :

    if request.method == "GET" :
        print ("We are using GET Method")
        
        # data = request.form
        # symboling = int(data["symboling"])
        # normalized_losses = int(data["normalized_losses"])
        # make = data["make"]
        # fuel_type = data["fuel_type"]
        # aspiration = data["aspiration"]
        # num_of_doors = data["num_of_doors"]
        # body_style = data["body_style"]
        # drive_wheels = data["drive_wheels"]
        # engine_location = data["engine_location"]
        # wheel_base = float(data["wheel_base"])
        # length = float(data["length"])
        # width = float(data["width"])
        # height = int(data["height"])
        # curb_weight = int(data["curb_weight"])
        # engine_type = data["engine_type"]
        # num_of_cylinders = data["num_of_cylinders"]
        # engine_size = int(data["engine_size"])
        # fuel_system = data["fuel_system"]
        # bore = float(data["bore"])
        # stroke = float(data["stroke"])
        # compression_ratio = int(data["compression_ratio"])
        # horsepower = int(data["horsepower"])
        # peak_rpm = int(data["peak_rpm"])
        # city_mpg = int(data["city_mpg"])
        # highway_mpg = int(data["highway_mpg"])

        symboling = int(request.args.get("symboling"))
        normalized_losses = int(request.args.get("normalized_losses"))
        make = request.args.get("make")
        fuel_type = request.args.get("fuel_type")
        aspiration = request.args.get("aspiration")
        num_of_doors = request.args.get("num_of_doors")
        body_style = request.args.get("body_style")
        drive_wheels = request.args.get("drive_wheels")
        engine_location = request.args.get("engine_location")
        wheel_base = float(request.args.get("wheel_base"))
        length = float(request.args.get("length"))
        width = float(request.args.get("width"))
        height = int(request.args.get("height"))
        curb_weight = int(request.args.get("curb_weight"))
        engine_type = request.args.get("engine_type")
        num_of_cylinders = request.args.get("num_of_cylinders")
        engine_size = int(request.args.get("engine_size"))
        fuel_system = request.args.get("fuel_system")
        bore = float(request.args.get("bore"))
        stroke = float(request.args.get("stroke"))
        compression_ratio = int(request.args.get("compression_ratio"))
        horsepower = int(request.args.get("horsepower"))
        peak_rpm = int(request.args.get("peak_rpm"))
        city_mpg = int(request.args.get("city_mpg"))
        highway_mpg = int(request.args.get("highway_mpg"))


        print ("""symboling,normalized_losses,make,fuel_type,aspiration,
        num_of_doors,body_style,drive_wheels,engine_location,wheel_base,length,width,height,curb_weight,
        engine_type,num_of_cylinders,engine_size,fuel_system,bore,stroke,compression_ratio,horsepower,
        peak_rpm,city_mpg,highway_mpg\n""",symboling,normalized_losses,make,fuel_type,aspiration,
        num_of_doors,body_style,drive_wheels,engine_location,wheel_base,length,width,height,curb_weight,
        engine_type,num_of_cylinders,engine_size,fuel_system,bore,stroke,compression_ratio,horsepower,
        peak_rpm,city_mpg,highway_mpg)

        Autos_data = AutoData(symboling,normalized_losses,make,fuel_type,aspiration,num_of_doors,body_style,
        drive_wheels,engine_location,wheel_base,length,width,height,curb_weight,engine_type,
        num_of_cylinders,engine_size,fuel_system,bore,stroke,compression_ratio,horsepower,peak_rpm,
        city_mpg,highway_mpg)
        price = Autos_data.get_predicted_price()

        # return jsonify({"Result" : f"Predicted Price for Car is {price}/- Rs. Only"})
        return render_template("index.html",prediction = price)

    else : 
        print ("We are using Post Method")

        # data = request.form
        # symboling = int(data["symboling"])
        # normalized_losses = int(data["normalized_losses"])
        # make = data["make"]
        # fuel_type = data["fuel_type"]
        # aspiration = data["aspiration"]
        # num_of_doors = data["num_of_doors"]
        # body_style = data["body_style"]
        # drive_wheels = data["drive_wheels"]
        # engine_location = data["engine_location"]
        # wheel_base = float(data["wheel_base"])
        # length = float(data["length"])
        # width = float(data["width"])
        # height = int(data["height"])
        # curb_weight = int(data["curb_weight"])
        # engine_type = data["engine_type"]
        # num_of_cylinders = data["num_of_cylinders"]
        # engine_size = int(data["engine_size"])
        # fuel_system = data["fuel_system"]
        # bore = float(data["bore"])
        # stroke = float(data["stroke"])
        # compression_ratio = int(data["compression_ratio"])
        # horsepower = int(data["horsepower"])
        # peak_rpm = int(data["peak_rpm"])
        # city_mpg = int(data["city_mpg"])
        # highway_mpg = int(data["highway_mpg"])

        symboling = int(request.form.get("symboling"))
        normalized_losses = int(request.form.get("normalized_losses"))
        make = request.form.get("make")
        fuel_type = request.form.get("fuel_type")
        aspiration = request.form.get("aspiration")
        num_of_doors = request.form.get("num_of_doors")
        body_style = request.form.get("body_style")
        drive_wheels = request.form.get("drive_wheels")
        engine_location = request.form.get("engine_location")
        wheel_base = float(request.form.get("wheel_base"))
        length = float(request.form.get("length"))
        width = float(request.form.get("width"))
        height = int(request.form.get("height"))
        curb_weight = int(request.form.get("curb_weight"))
        engine_type = request.form.get("engine_type")
        num_of_cylinders = request.form.get("num_of_cylinders")
        engine_size = int(request.form.get("engine_size"))
        fuel_system = request.form.get("fuel_system")
        bore = float(request.form.get("bore"))
        stroke = float(request.form.get("stroke"))
        compression_ratio = int(request.form.get("compression_ratio"))
        horsepower = int(request.form.get("horsepower"))
        peak_rpm = int(request.form.get("peak_rpm"))
        city_mpg = int(request.form.get("city_mpg"))
        highway_mpg = int(request.form.get("highway_mpg"))


        print ("""symboling,normalized_losses,make,fuel_type,aspiration,
        num_of_doors,body_style,drive_wheels,engine_location,wheel_base,length,width,height,curb_weight,
        engine_type,num_of_cylinders,engine_size,fuel_system,bore,stroke,compression_ratio,horsepower,
        peak_rpm,city_mpg,highway_mpg\n""",symboling,normalized_losses,make,fuel_type,aspiration,
        num_of_doors,body_style,drive_wheels,engine_location,wheel_base,length,width,height,curb_weight,
        engine_type,num_of_cylinders,engine_size,fuel_system,bore,stroke,compression_ratio,horsepower,
        peak_rpm,city_mpg,highway_mpg)

        Autos_data = AutoData(symboling,normalized_losses,make,fuel_type,aspiration,num_of_doors,body_style,
        drive_wheels,engine_location,wheel_base,length,width,height,curb_weight,engine_type,
        num_of_cylinders,engine_size,fuel_system,bore,stroke,compression_ratio,horsepower,peak_rpm,
        city_mpg,highway_mpg)
        price = Autos_data.get_predicted_price()

        # return jsonify({"Result" : f"Predicted Price for Car is {price}/- Rs. Only"})
        return render_template("index.html",prediction = price)


if __name__ == "__main__" :
    app.run(host = "0.0.0.0",port = config.PORT_NUMBER , debug = True)