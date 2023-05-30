import requests
import json
import time

HEADERS = {"Authorization": "Bearer 7oAo3zKteYTyBDO0aj_ugQ"}
CHUNK_SIZE = 1024  # Adjust the chunk size as needed

def postFile(file_path):
    REST_URL = "http://localhost:8090/tasks/create/file"
    with open(file_path, "rb") as sample:
        files = {"file": ("temp_file_name", sample)}
        r = requests.post(REST_URL, headers=HEADERS, files=files) # Send the exe to cuckoo
    task_id = r.json()["task_id"]
    return task_id



def getByIdJson(id, file_path):
    REST_URL = "http://localhost:8090/tasks/report/{}".format(id)
    try:
        r = requests.get(REST_URL, headers=HEADERS, stream=True)
        r.raise_for_status()  # Raise an exception if the request was not successful
        # response_json = r.json()

        # Initialize an empty string to store the response content
        response_content = ''

        # Read the response content in chunks
        for chunk in r.iter_content(chunk_size=CHUNK_SIZE):
            response_content += chunk.decode('utf-8')

        # Convert the complete response content to JSON
        response_json = json.loads(response_content)

        if response_json:
            with open(file_path, "w") as out_file:
                json.dump(response_json, out_file, indent=6)
            out_file.close()
            print("JSON file saved successfully.")
        else:
            print("Empty JSON response.")
    except requests.exceptions.RequestException as e:
        print("Error occurred during the request:", e)
        if r.status_code == 404:
            print("Retrying after a delay...")
            time.sleep(10)  # Wait for 10 seconds before retrying
            getByIdJson(id, file_path)  # Retry the request
    except ValueError as e:
        print("Error: Invalid JSON response")
        print(f"Response Content: {r.content}")

# postFile()
#getByIdJson()
