# from datasetAutomation.datasetAutomation import extract
# from pytorchnn.pytorchnn import pytorchnn
# from pytorchnn.inference import main_inference
# if __name__ == '__main__':
#     # extract()
#     #pytorchnn()
#     main_inference()

from flask import Flask, request
from cuckooAPI.cuckooAPI import postFile, getByIdJson
from datasetAutomation.datasetAutomation import extract
from pytorchnn.inference import main_inference
import os

app = Flask(__name__)


@app.route('/api/uploadfile', methods=['POST'])
def main():
    if 'file' not in request.files:
        return 'No file found in the request!', 400

    file = request.files['file']
    saveFileExe(file)
    # Process the file or save it to a desired location
    # Here, we are simply printing the file name
    print('Received file:', file.filename)
    sendToCuckoo()
    extractFromJsonToCSV()
    main_inference(file_path_csv)


def saveFileExe(file):
    file.save(file_path_exe)


def sendToCuckoo():
    getByIdJson(postFile(file_path_exe), file_path_json)


def extractFromJsonToCSV():
    extract(file_path_json,file_path_csv)


if __name__ == '__main__':
    file_name_exe = "malclass.exe"
    file_name_json = "malclass.json"
    file_name_csv = "malclass.csv"

    directory = "/home/ubuntu/Documents/Final-project-repo/"
    file_path_exe = os.path.join(directory, file_name_exe)
    file_path_json = os.path.join(directory, file_name_json)
    file_path_csv = os.path.join(directory, file_name_csv)

    app.run()