import requests
import json
import time

HEADERS = {"Authorization": "Bearer 7oAo3zKteYTyBDO0aj_ugQ"}


def postFile(file_path):
    REST_URL = "http://localhost:8090/tasks/create/file"
    # SAMPLE_FILE = "/home/ubuntu/Documents/Final-project-repo/malclass.exe"
    with open(file_path, "rb") as sample:
        files = {"file": ("temp_file_name", sample)}
        r = requests.post(REST_URL, headers=HEADERS, files=files)
    task_id = r.json()["task_id"]
    return task_id


def getByIdJson(id, file_path):
    REST_URL = "http://localhost:8090/tasks/report/{}".format(id)
    try:
        r = requests.get(REST_URL, headers=HEADERS)
        r.raise_for_status()  # Raise an exception if the request was not successful
        response_json = r.json()

        if response_json:
            out_file = open(file_path, "w")
            json.dump(response_json, out_file, indent=6)
            out_file.close()
            print("JSON file saved successfully.")
        else:
            print("Empty JSON response.")
    except requests.exceptions.RequestException as e:
        print("Error occurred during the request:", e)
        if r.status_code == 404:
            print("Retrying after a delay...")
            time.sleep(5)  # Wait for 5 seconds before retrying
            getByIdJson(id, file_path)  # Retry the request
# postFile()
#getByIdJson()
