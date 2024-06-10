from flask import Flask, request, jsonify, render_template

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

import numpy as np
import os

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///SQL/fish_info.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
fish = Base.classes.fish

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################

app = Flask(__name__, template_folder='templates')

# Load your model (make sure to adjust the path to your model file)
model = load_model('models/CNN_fish_model_final_2.h5')

def predict_fish(image_path, model):
    img = image.load_img(image_path, target_size=(256, 256))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    print("Image array shape:", img_array.shape)

    prediction = model.predict(img_array)
    predicted_class_index = np.argmax(prediction, axis=1)[0]
    #class_labels = ['Red', 'Trout', 'Flounder','largemouth_bass','smallmouth_bass','Black Crappie','Cobia','King Mackerel','Snook','Tarpon','Tripletail']
    class_labels = ['Black Crappie', 'Cobia', 'Flounder', 'King_Mackeral', 'Largemouth_Bass', 'Red', 'Smallmouth_Bass', 'Snook', 'Tarpon', 'Tripletail', 'Trout']

    predicted_class = class_labels[predicted_class_index]
    confidence = prediction[0][predicted_class_index]

    
    return predicted_class, confidence



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 401
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Save the file to a temporary location
    temp_file_path = os.path.join('temp', file.filename)
    file.save(temp_file_path)

    # Make a prediction
    predicted_class, confidence = predict_fish(temp_file_path, model)
    
    # Convert confidence to a Python native float type
    confidence = float(confidence)

    # Remove the temporary file
    os.remove(temp_file_path)
    
    return jsonify({'predicted_class': predicted_class, 'confidence': confidence})

@app.route('/api/v1.0/fishjson')
def fishjson():

    data = session.query(fish.fish_class, fish.fish, fish.daily_bag, fish.min_length, fish.max_length,
                          fish.possession, fish.exceptions, fish.image_link)

    session.close()

    json_data = []

    for a, b, c, d, e, f, g, h in data:
        data_dict = {}
        data_dict["Class"] = a
        data_dict["Fish Name"] = b
        data_dict["Daily Bag Limit"] = c
        data_dict["Minimum Length"] = d
        data_dict["Maximum Length"] = e
        data_dict["Possession Limits"] = f
        data_dict["Exceptions"] = g
        data_dict["Image Link"] = h
        json_data.append(data_dict)

    return jsonify(json_data)

if __name__ == '__main__':
    app.run(debug=True)
