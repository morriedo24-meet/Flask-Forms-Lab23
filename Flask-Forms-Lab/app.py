from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "morrie"
password = "123"
facebook_friends=["Avia","Ella","Amit", "Rona", "Saba", "Savta"]


@app.route('/', methods=['GET', 'POST'])  # '/' for the default page
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		form_name = request.form['username']
		form_password = request.form['password']
		if username == form_name and password == form_password:
			return redirect(url_for('home'))
		else:
			return render_template('login.html')



@app.route('/home')  # '/' for the default page
def home():
		return render_template('home.html', f_friends = facebook_friends)


@app.route('/friend_exists/<string:name>')
def friend_exists(name):
    return render_template('friend_exists.html', f_friends = facebook_friends, n = name)

if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		debug=True
	)
