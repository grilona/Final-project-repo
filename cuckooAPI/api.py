from flask import Flask, request

app = Flask(__name__)

@app.route('/api/uploadfile', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file found in the request!', 400

    file = request.files['file']

    # Process the file or save it to a desired location
    # Here, we are simply printing the file name
    print('Received file:', file.filename)

    return 'File uploaded successfully!'

if __name__ == '__main__':
    app.run()