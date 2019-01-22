from flask import Flask, render_template, redirect, url_for, request
import pickle as pk

# Import processed datas from folder

infile = open("codes/Stored Data/sample_aspect_info.pickle", "rb")
aspect_info = pk.load(infile)
infile.close()

infile = open("codes/Stored Data/sample_hotel_info.pickle", "rb")
hotels = pk.load(infile)
infile.close()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/homepage", methods=['GET', 'POST'])
def homepage():
    if request.method == "POST":
        input_search_term = (request.form.get("input-search-term")).lower()
        input_location = request.form.get("input-location")
        return render_template('search.html', search_term = input_search_term, 
                                              location_area = input_location,
                                              data = aspect_info,
                                              hotel_info = hotels)

if __name__ == "__main__":
    app.run(debug=True, port=1000)