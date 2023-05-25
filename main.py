import json

import torch
from flask import Flask, request
from cuckooAPI.cuckooAPI import postFile, getByIdJson
from datasetAutomation.datasetAutomation import extract
from pytorchnn.inference import main_inference
import os
from flask_socketio import SocketIO
from flask_cors import CORS
from flask import Flask, jsonify

app = Flask(__name__)

CORS(app)  # Enable CORS for cross-origin requests

# @app.route('/api/gettensor', methods=['GET'])
# def get_tensor(argmax_value):
#     tensor = torch.tensor([argmax_value])
#     return tensor


@app.route('/api/uploadfile', methods=['POST'])
def main():
    if 'file' not in request.files:
        return 'No file found in the request!', 400

    file = request.files['file']
    saveFileExe(file)
    print('Received file:', file.filename)
    sendToCuckoo()
    extractFromJsonToCSV()
    answer = getAnswer(main_inference(file_path_csv))
    deleteCSV()
    return answer, 200


def saveFileExe(file):
    file.save(file_path_exe)


def sendToCuckoo():
    getByIdJson(postFile(file_path_exe), file_path_json)


def extractFromJsonToCSV():
    extract(file_path_json,file_path_csv)


def deleteCSV():
    try:
        os.remove(file_path_csv)
        print("CSV file deleted successfully.")
    except FileNotFoundError:
        print("The specified CSV file does not exist.")
    except Exception as e:
        print("An error occurred while deleting the CSV file:", str(e))


def getAnswer(inference_answer):
    answer = inference_answer.item()
    if answer == 1:
        print("Case 1- Ransomware")
        return "Ransomware"
    elif answer == 2:
        print("Case 2- Trojans")
        return "Trojans"
    elif answer == 3:
        print("Case 3- Adware")
        return "Adware"
    elif answer == 4:
        print("Case 4- Bots")
        return "Bots"
    elif answer == 5:
        print("Case 5- Worm")
        return "Worm"
    elif answer == 6:
        print("Case 6- Spyware")
        return "Spyware"

    else:
        print("Default case- Non-malware")
        return "Non-malware"


if __name__ == '__main__':
    file_name_exe = "malclass.exe"
    file_name_json = "malclass.json"
    file_name_csv = "malclass.csv"

    directory = "/home/ubuntu/Documents/Final-project-repo/"
    file_path_exe = os.path.join(directory, file_name_exe)
    file_path_json = os.path.join(directory, file_name_json)
    file_path_csv = os.path.join(directory, file_name_csv)

    app.run()