from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/homepage", methods=['GET', 'POST'])
def homepage():
    if request.method == "POST":
        input_search_term = request.form.get("input-search-term")
        input_location = request.form.get("input-location")
        return render_template('search.html', search_term = input_search_term, location_area = input_location)

if __name__ == "__main__":
    app.run(debug=True, port=1000)