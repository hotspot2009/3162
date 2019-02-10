from flask import Flask, render_template, redirect, url_for, request
import pickle as pk
import sys

sys.path.insert(0, './codes/Library/')
from normalize import normalize_data, get_location

# Import processed datas from folder

infile = open("codes/Stored Data/aspect_dict.pickle", "rb")
aspect_dict = pk.load(infile)
infile.close()

infile = open("codes/Stored Data/city_dict.pickle", "rb")
city_dict = pk.load(infile)
infile.close()

infile = open("codes/Stored Data/hotel_dict.pickle", "rb")
hotel_dict = pk.load(infile)
infile.close()

infile = open("codes/Stored Data/timeline_dict.pickle", "rb")
timeline_dict = pk.load(infile)
infile.close()

infile = open("codes/Stored Data/best_reviews_dict.pickle", "rb")
review_dict = pk.load(infile)
infile.close()

app = Flask(__name__)

     
@app.route("/")
def index():
    return render_template('index.html', 
                aspects = aspect_dict,
                cities = city_dict)

@app.route("/homepage", methods=['GET', 'POST'])
def homepage():
    if request.method == "POST":
        input_search_term = (request.form.get("input-search-term")).lower()
        input_location = request.form.get("input-location")
        data = normalize_data(input_search_term, input_location, timeline_dict)
        data = data[:20]
        if data == []:
                return render_template('error.html')
        else:
                location_data = get_location(data, hotel_dict)
                return render_template('search.html', 
                        search_term = input_search_term, 
                        location_area = input_location,
                        timeline = data,
                        hotels = hotel_dict,
                        hotel_locations = location_data,
                        best_reviews = review_dict)  

if __name__ == "__main__":
    app.run(debug=True, port=2550)