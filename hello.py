from flask import Flask, render_template

# Create flask app
app = Flask(__name__)

'''
safe
capitalize
lower
upper
title
trim
striptags

'''

# Create flask route
@app.route('/')

def index():
	first_name = "john"
	stuff = "This is <strong>Bold</strong>"
	favourite_pizza = ['pepperoni','cheese','vegetables']
	return render_template('index.html',
		first_name=first_name,
		stuff=stuff,
		favourite_pizza = favourite_pizza
		)

@app.route('/user/<name>')

def user(name):
	return render_template('user.html',user_name=name)

# Create custom error pages

#invalid URL

@app.errorhandler(404)

def page_not_found(e):	
	return render_template('404.html'),404 

@app.errorhandler(500)

def page_not_found(e):
	return render_template('500.html'),500
