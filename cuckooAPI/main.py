import requests
import json

HEADERS = {"Authorization": "Bearer 7oAo3zKteYTyBDO0aj_ugQ"}


def postFile():
    REST_URL = "http://localhost:8090/tasks/create/file"
    SAMPLE_FILE = "/home/ubuntu/Downloads/putty.exe"
    with open(SAMPLE_FILE, "rb") as sample:
        files = {"file": ("temp_file_name", sample)}
        r = requests.post(REST_URL, headers=HEADERS, files=files)
    task_id = r.json()["task_id"]
    print(task_id)


def getByIdJson():
    REST_URL = "http://localhost:8090/tasks/report/11"
    r = requests.get(REST_URL, headers=HEADERS)
    out_file = open("/home/ubuntu/Documents/cuckooOutput/putty.json", "w")
    json.dump(r.json(), out_file, indent=6)
    out_file.close()
#    print(r.json())


#postFile()
getByIdJson()
