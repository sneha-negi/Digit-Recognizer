Digit Recognition Web Application
=================================

This project is a web-based application built using **Flask** that allows users to upload images of handwritten digits and predicts the digit using a pre-trained Convolutional Neural Network (CNN). The model is trained on the popular **MNIST** dataset.

Dataset
-------

The **MNIST dataset** consists of 70,000 28x28 grayscale images of handwritten digits (0-9), split into 60,000 training images and 10,000 testing images. The dataset is widely used for training machine learning models for digit recognition.

Features
--------

*   **Image Upload**: Upload an image of a handwritten digit (JPG, PNG, etc.).
    
*   **Digit Prediction**: The application processes the uploaded image and predicts the digit using a pre-trained CNN model.
    
*   **Web Interface**: A user-friendly interface where the prediction result is displayed after the image is uploaded.
    

Machine Learning Model
----------------------

*   **Model Architecture**: A Convolutional Neural Network (CNN) with convolutional layers, pooling layers, and fully connected layers.
    
*   **Training Dataset**: The model was trained on the MNIST dataset, which contains 60,000 training images.
    
*   **Model Output**: The model outputs a prediction between 0 and 9 for the uploaded image.
    

How to Access and Use the Application
-------------------------------------

### 1\. Clone the Repository

First, clone this repository to your local machine:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   git clone   [https://github.com/sneha-negi/Digit-Recognizer](https://github.com/sneha-negi/Digit-Recognizer)  cd Digit-Recognizer   `

### 2\. Install Dependencies

Install the necessary Python packages using pip. This project requires **Flask**, **TensorFlow**, and **Pillow**:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   pip install -r requirements.txt   `

### 3\. Run the Application

Once all the dependencies are installed, you can start the Flask application by running the RecognizeDigit.py script:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python RecognizeDigit.py   `

### 4\. Access the Web Application

After running the above command, open a web browser and navigate to:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   http://127.0.0.1:5000/   `

This will bring up the homepage, where you can upload an image of a digit (0-9) and get a prediction.

### 5\. Upload an Image

*   Choose an image file from your system (make sure it's a clear image of a digit).
    
*   Click the "Predict" button, and the predicted digit will be displayed on the results page.
