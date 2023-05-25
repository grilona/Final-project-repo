
import torch
from torch.utils.data import Dataset, DataLoader
import pandas as pd
import torch.nn as nn

# Get cpu, gpu or mps device for training.
device = (
    "cuda"
    if torch.cuda.is_available()
    else "mps"
    if hasattr(torch.backends, "mps") and torch.backends.mps.is_available()
    else "cpu"
)
# print(f"Using {device} device")

# Define a custom dataset
class MyDataset(Dataset):
    def __init__(self, features, labels, transform=None):
        self.features = features
        self.labels = labels
        self.transform = transform

    def __len__(self):
        return len(self.features)

    def __getitem__(self, idx):
        x = self.features[idx]
        y = self.labels[idx]
        if self.transform:
            x = self.transform(x)
        return x, y

class Normalize:
    def __init__(self, mean, std):
        self.mean = mean
        self.std = std

    def __call__(self, x):
        x = (x - self.mean) / (self.std + 1e-8)
        return x

class MyModel(nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        self.fc1 = nn.Linear(56, 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 7)
        # self.relu = nn.ReLU()
        self.leakyrelu = nn.LeakyReLU(0.1)
        self.dropout = nn.Dropout(p=0.2)


    def forward(self, x):
        x = self.fc1(x)
        x = self.leakyrelu(x)
        x = self.dropout(x)
        x = self.leakyrelu(self.fc2(x))
        x = self.dropout(x)
        x = self.fc3(x)
        return x


def train(dataloader, loss_fn,  model, optimizer):
    num_epochs = 10
    for epoch in range(num_epochs):
        for batch in dataloader:
            x_batch, y_batch = batch
            # Forward pass
            y_pred = model(x_batch)
            # y_batch = torch.argmax(y_batch, dim=0)
            loss = loss_fn(y_pred, y_batch)
            # Backward pass
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        print('Epoch [{}/{}], Loss: {:.4f}'.format(epoch + 1, num_epochs, loss.item()))


def saving_model(model):
    torch.save({'model_state_dict': model.state_dict()}, 'model.pth')
    print("Saved PyTorch Model State to model.pth")


def pytorchnn():
    # Load the CSV file
    csv_file = '/home/ubuntu/Documents/Final-project-repo/pytorchnn/dataset.csv'
    # Create an instance of the CustomDataset
    # --------
    # Load the CSV file into a Pandas dataframe
    data_df = pd.read_csv(csv_file)

    # Extract the features and labels
    features = data_df.iloc[:, :-1].values
    labels = data_df.iloc[:, -1].values

    # Convert the features and labels to PyTorch tensors
    features = torch.tensor(features).float()
    labels = torch.tensor(labels).long()

    # Calculate the mean and standard deviation of the features
    mean = torch.mean(features, dim=0)
    std = torch.std(features, dim=0)

    # Define the normalization transform
    normalize_transform = Normalize(mean=mean, std=std)

    # --------
    # Create a DataLoader to load the dataset in batches
    batch_size = 10
    # Create a DataLoader with the normalized dataset
    normalized_dataset = MyDataset(features, labels, transform=normalize_transform)
    dataloader = DataLoader(normalized_dataset, batch_size, shuffle=True)
    # dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

    # Define a simple model
    model = MyModel()

    # Define a loss function
    loss_fn = nn.CrossEntropyLoss()

    # Define an optimizer
    optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

    # Train the model
    train(dataloader, loss_fn, model, optimizer)

    saving_model(model)
