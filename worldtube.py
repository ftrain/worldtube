from flask import Flask
from flask import render_template
from youtube import youtube_search_countries

app = Flask(__name__)

@app.route("/")
def worldtube():
    search_term = "beautiful clothing"
    results = youtube_search_countries(search_term)
    return render_template('index.html',
                           search_term=search_term,
                           results=results)

if __name__ == "__main__":
    app.run(debug=True)
