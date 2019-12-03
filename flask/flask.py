# Adapted from: https://www.palletsprojects.com/p/flask/
# Run with: env FLASK_APP=random-wa.py flask run

# For creating the web application.
import flask as fl
from flask import render_template
# For generating random numbers.
import numpy as np
import base64
# Create the web application.
app = fl.Flask(__name__)

# Add a route for the web page.
@app.route('/')
def home():
  return render_template('webpage.html')

# Add a route for generating random numbers using POST data.
@app.route('/random', methods=['GET', 'POST'])
def random():
  # Find out how many numbers the user asked to generate.
  howmany = int(fl.request.values.get("noofnos", "1"))
  # Generate and respond with the numbers.
  return {"randomNos": np.random.random(howmany).tolist()}

# Post route for uploading an image
@app.route('/uploadimage', methods=['GET', 'POST'])
def uploadimage():
  # Get the image from the request.
  theimage = fl.request.values.get("theimage", "")
  # Print to the console.
  print(theimage)
  # Decode the string to an image
  decodedimage = base64.b64decode(theimage[22:])
  # Try to save the image
  with open ("drawing.png", "wb") as f:
  	f.write(decodedimage)
  # Return a response
  return {"message": theimage}


# Route for predict POST
  @app.route('/predict', methods=['POST'])
  def predict():
    return {"message": theimage}