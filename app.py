from flask import Flask
#this imports the variable "views" from the file views
from views import views

app = Flask(__name__)

# # you can do it like this but it's better to put it
# # into a seperate file so it's more organized
# @app.route("/")
# def home():
#     # usually html is returned but in this case it is just a string
#     return "this is the home page"

app.register_blueprint(views, url_prefix="/views")

if __name__ == '__main__':
    app.run(debug=True, port=8000)

