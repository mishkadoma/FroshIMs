from flask import flask, request, render_template, redirect, url_for, make_response

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
	if 

if __name__ == '__main__':
	app.run(debug=True, port=8080, host=0.0.0.0)