from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    # you can pass as many values as you want, not just name
    return render_template("index.html", name = "Fred")

# other ways to use route

#url parameters
@views.route("/profile/<username>")
def profile(username):
    return render_template("index.html", name = username)

#query parameters
# to access, use this : 
# http://127.0.0.1:8000/views/person?name=joe
@views.route("/person")
def person():
    args = request.args
    name = args.get("name")
    return render_template("index.html", name = name)

# returning json
@views.route("/json")
def get_json():
    return jsonify({"name": "Fred", "coolness": 10})


#return json data, i don't really know how to use this
@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

#redirecting to other pages
#views in this case is referring to the instantiated object
# home is the function you want to redirect to
@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.home"))

#this shows you how html inheritence works in jinja
# i think that's what it's called
@views.route("/other")
def other():
    return render_template("other.html")


