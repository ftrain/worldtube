from flask import Flask
from flask import render_template, request
import youtube

app = Flask(__name__)

@app.route("/")
def worldtube():
    search_term = request.args.get('q') or "water parks"
    try:
        page_num = int(request.args.get('p')) - 1 # Human --> zero index
    except (TypeError, ValueError):
        page_num = 0
    results = youtube.search_countries(search_term, page_num)
    return render_template('index.html',
                           search_term=search_term,
                           results=results,
                           current_page_num=page_num + 1, # Zero --> human index
                           num_pages = youtube.num_pages)

if __name__ == "__main__":
    app.run(debug=True)
