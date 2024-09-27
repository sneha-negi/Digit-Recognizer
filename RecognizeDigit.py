from flask import Flask, request, render_template, redirect, url_for
from keras.models import load_model
import numpy as np
from PIL import Image
import tensorflow as tf

app = Flask(__name__)


model = load_model('Trained_model.h5')  


def preprocess_image(image):
    image = image.convert('L')  
    image = image.resize((28, 28))  
    image = np.array(image)
    image = image.astype('float32') / 255  
    image = np.expand_dims(image, axis=0) 
    image = np.expand_dims(image, axis=-1)  
    return image

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Route for image upload and prediction
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        return redirect(request.url)
    
    if file:
        image = Image.open(file)
        processed_image = preprocess_image(image)
        
        prediction = model.predict(processed_image)
        predicted_digit = np.argmax(prediction, axis=1)[0]
        
        return render_template('result.html', digit=predicted_digit)

if __name__ == "__main__":
    app.run(debug=True)
