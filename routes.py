from flask import Flask, render_template, redirect, url_for, request
import pickle as pk

# Import processed datas from folder

infile = open("codes/Stored Data/sample_aspect_info.pickle", "rb")
aspect_info = pk.load(infile)
infile.close()

app = Flask(__name__)

hotels=[
    ["Hotel Arena"," s Gravesandestraat 55 Oost 1092 AA Amsterdam Netherlands", 52.3605759, 4.9159683],
    ["K K Hotel George","1 15 Templeton Place Earl s Court Kensington and Chelsea London SW5 9NB United Kingdom", 51.4918878, -0.1949706],
    ["Apex Temple Court Hotel","1 2 Serjeant s Inn Fleet Street City of London London EC4Y 1LL United Kingdom", 51.5137335, -0.1087512],
    ["The Park Grand London Paddington","1 3 Queens Garden Westminster Borough London W2 3BA United Kingdom", 51.5142184, -0.1809032],
    ["The Principal London","1 8 Russell Square Camden London WC1B 5BE United Kingdom", 51.5226217, -0.1251602]
]

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