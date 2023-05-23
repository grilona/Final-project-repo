from flask import Flask, request
from cuckooAPI import postFile, getByIdJson
import os

app = Flask(__name__)


@app.route('/api/uploadfile', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file found in the request!', 400

    file = request.files['file']
    saveFileExe(file)
    # Process the file or save it to a desired location
    # Here, we are simply printing the file name
    print('Received file:', file.filename)
    sendToCuckoo(file_path)
    return str(file)


def saveFileExe(file):
    file_name = "malclass.exe"
    directory = "/home/ubuntu/Documents/Final-project-repo/"
    file_path = os.path.join(directory, file_name)
    file.save(file_path)



def sendToCuckoo(file_path):
    # while not os.path.isfile(file_path):
    #     time.sleep(1)  # Wait for 1 second before checking again
    getByIdJson(postFile(file_path), directory)

if __name__ == '__main__':
    file_name = "malclass.exe"
    directory = "/home/ubuntu/Documents/Final-project-repo/"
    file_path = os.path.join(directory, file_name)
    app.run()