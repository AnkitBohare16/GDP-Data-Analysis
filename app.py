from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
import pandas as pd
from analysis import perform_analysis

app = Flask(__name__)

# Configuration for file uploads
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        # Perform analysis and save results
        outputs = perform_analysis(filepath)
        return render_template('results.html', outputs=outputs)

if __name__ == '__main__':
    app.run(debug=True)
