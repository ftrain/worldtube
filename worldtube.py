from flask import Flask
from flask import render_template, request
import youtube

app = Flask(__name__)

@app.route("/")
def worldtube():
    search_term = request.args.get('q') or "water parks"
    results = youtube.search_countries(search_term)
    return render_template('index.html',
                           search_term=search_term,
                           results=results)

if __name__ == "__main__":
    app.run(debug=True)
