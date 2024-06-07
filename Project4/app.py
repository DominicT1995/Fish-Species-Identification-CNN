from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__, template_folder='templates')

# Load your model (make sure to adjust the path to your model file)
model = load_model('models/fish_identifier_model.h5')

def predict_fish(image_path, model):
    img = image.load_img(image_path, target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    print("Image array shape:", img_array.shape)

    prediction = model.predict(img_array)
    predicted_class_index = np.argmax(prediction, axis=1)[0]
    class_labels = ['Red', 'Trout', 'Flounder','largemouth_bass','smallmouth_bass','Black Crappie','Cobia','King Mackerel','Snook','Tarpon','Tripletail',]

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

if __name__ == '__main__':
    app.run(debug=True)
