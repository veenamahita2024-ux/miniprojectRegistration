from flask imporst Flask,render_templete

app =flask(__name__)


@app.route("/")
def home():
    return render _templete("index.html")


@app.route("/search")
def search():
    return "train search page"




if __name__=="__main__":
    app.run(debug=True)