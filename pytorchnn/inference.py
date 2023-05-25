import pandas as pd
import torch
from pytorchnn.pytorchnn import MyModel


def main_inference(file_path_csv):
    # Load the saved model
    model = MyModel()
    state_dict = torch.load('pytorchnn/model.pth', map_location=torch.device('cpu'))
    model.load_state_dict(state_dict['model_state_dict'])
    model.eval()
    # Load the input data from a CSV file
    input_data = pd.read_csv(file_path_csv)

    # Preprocess the input data
    X = preprocess_input_data(input_data)

    # Make predictions on the input data
    with torch.no_grad():
        y_pred = model(X)

    # Convert the predictions to a numpy array
    y_pred = y_pred.numpy()

    # Print the predictions
    pred_tensor = torch.from_numpy(y_pred)

    print(torch.argmax(pred_tensor, dim=1))
    return torch.argmax(pred_tensor, dim=1)


    # Define a function to preprocess the input data
def preprocess_input_data(df):
    X = df.values.astype('float32')
    X = torch.tensor(X, dtype=torch.float)
    return X

