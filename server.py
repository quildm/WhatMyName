from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("form.html")

@app.route('/users', methods=['POST'])
def create_user():
   name = request.form['name']
   print ("a winner had been made")
   return render_template('success.html', named = name )

app.run(debug=True) # run our server
