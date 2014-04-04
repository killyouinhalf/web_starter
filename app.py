# Welcome to your first Flask app :)

# Imports usually happen at the top of the file in python. They load
# in all the other libraries that your code will be using, so that you
# can call the functions they define, or instantiate the classes they create.

# Import the main class from the "Flask" library that we need to create our
# web application, as well as the `render_template` function for returning
# HTML files as responses.
from flask import Flask, render_template

# Create the variable `app` which is an instance of the Flask class that
# we just imported. Being an "instance of a class" is something pretty
# import to any kind of software development, but you don't need to know
# exactly what it means right now.
app = Flask(__name__)


# Here, we're creating the homepage of our application. We're defining a
# function called `homepage` which doesn't take any arguments (nothing
# inside the parentheses). Above the function definiton, we're adding a
# "decorator" which tells our app which "route" (ie URL) should be mapped
# to this function. So if you wanted to add more pages to your app, you
# could add new python functions for them, and decorate them with new routes.
@app.route("/")
def homepage():
    
	# Inside this function, you can run whatever logic you want, running any python
	# code your heart desires. You could check the cookies on the request to see if
	# there's a logged in user making the requests, you could read or write to a
	# database or run any kind of functions you want.
    return "Hello World"


@app.route("/cool-page/")
def cool_page():
	# But ou don't want to have to write the HTML for your page inside python
	# string. That'd get really annoying quickly. Thankfully, most web frameworks
	# come with a "template engine" that can take basic HTML files and spit it out
	# in a response. Here, we created a file called 'cool-page.html' inside the
	# templates folder, which is where Flask looks for template files by default.
	return render_template("cool-page.html")


# Some boilerplate code that just says "if you're running this from the command
# line, start here." Again, not critical to know what this means yet.
if __name__ == "__main__":
    app.debug = True
    app.run()
