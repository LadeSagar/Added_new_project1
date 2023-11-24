from flask import Flask, jsonify, render_template, request

from Packages.utils import BangloruClass

app = Flask(__name__)

@app.route("/")
def Home():
    print("show me********")
    # return "We are on Home Page*******"
    return render_template("App.html")

@app.route("/test" , methods=["GET","POST"])
def Test():
    if request.method == "GET":
        
        print("We are in get Method ********* ")
        
        area_type = request.args.get('area_type')
        availability = request.args.get('availability')
        size = request.args.get('size')
        total_sqft = eval(request.args.get('total_sqft'))
        bath =eval(request.args.get('bath'))
        balcony = eval(request.args.get('balcony'))
        location =request.args.get('location')
       
          
        obj = BangloruClass(area_type,availability,size,total_sqft,bath,balcony,location)
        prediction = obj.predict_()

        print(prediction)
        
        return render_template("App.html", Price = prediction)
    
    


# if __name__=="__main__":
    
app.run()