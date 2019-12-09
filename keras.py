import json
import flask as fl
import numpy as np
import base64
import logging
import keras.models as model_from_json
from PIL import ImageOps, Image
from flask import render_template
#from keras.models import model_from_json


HEIGHT, WIDTH = 28,28
DIMENTIONS = HEIGHT, WIDTH



# Flask instance
app = fl.Flask(__name__)

# Home route for WebApp
@app.route('/')
def home():
  return render_template('webpage.html')


# Post route for uploading an image
@app.route('/uploadimage', methods=['GET', 'POST'])
def uploadimage():
  # Get the image from the request.
  theimage = fl.request.values['imageData']

  # Print to the console.
  print(theimage)

  # Decode the string to an image, from byte 22 on
  decodedimage = base64.b64decode(theimage[22:])

  # Try to save the image
  with open ("drawing.png", "wb") as f:
  	f.write(decodedimage)
  
  model = load_model()
  # resize image so it can be tested against the model
  image_to_predict = reshape_image()


  prediction_array = model.predict(image_to_predict)
  prediction = np.argmax(prediction_array)
  
  # Return a response
  return {"prediction": prediction}


def reshape_image():
    # Adapted from: https://dev.to/preslavrachev/python-resizing-and-fitting-an-image-to-an-exact-size-13ic
  original_image = Image.open('drawing.png').convert("L")
  original_image = ImageOps.fit(original_image, WIDTH, HEIGHT, Image.ANTIALIAS)

  img_array = np.array(original_image).reshape(1,WIDTH,HEIGHT,1)
  return img_array

def load_model():
  # import model
  json_model = open('model/model.json','r')
  load_model_json = json_model.read()
  json_model.close()
  loaded_model = model_from_json(load_model_json)

  loaded_model.load_weights('model/model.h5')
  return loaded_model

def predict(model, image_array):
  prediction_array = model.predict(image_array)
  prediction = np.argmax(prediction_array)
  return prediction