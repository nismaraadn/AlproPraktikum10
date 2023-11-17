from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/')
def homes():
    return render_template('homes.html')

@app.route('/cv')
def cv():
    return render_template('cv.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/biodata')
def biodata():
    return render_template('biodata.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/recommendations')
def recommendations():
    return render_template('recommendations.html')

@app.route('/fibonacci')
def fibonacci():
    return render_template('fibonacci.html')

@app.route('/json')
def json():
    return render_template('json.html')

@app.route("/post", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("post.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>Welcome {usr}. Nice to Meet You!</h1>"

if __name__ == '__main__':
    app.run(debug=True)
