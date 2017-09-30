from flask import Flask, request, render_template, redirect, url_for, make_response

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
	if request.form["name"] == "" or request.form["dorm"] == "":
		return render_template("failure.html")
	return render_template("success.html")

if __name__ == '__main__':
	app.run(debug=True, port=8080, host='0.0.0.0')
