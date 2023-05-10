
import torch
from torch.utils.data import Dataset, DataLoader
import pandas as pd

# Get cpu, gpu or mps device for training.
device = (
    "cuda"
    if torch.cuda.is_available()
    else "mps"
    if torch.backends.mps.is_available()
    else "cpu"
)
print(f"Using {device} device")


class CustomDataset(Dataset):
    def __init__(self, csv_file):
        self.data = pd.read_csv(csv_file)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        x = self.data.iloc[index, :-1].values.astype('float32')
        y = self.data.iloc[index, -1:].values.astype('float32')
        return torch.from_numpy(x), torch.from_numpy(y)


def train(dataloader, loss_fn, model, optimizer):
    num_epochs = 10
    for epoch in range(num_epochs):
        for batch in dataloader:
            x_batch, y_batch = batch
            # Forward pass
            y_pred = model(x_batch)
            loss = loss_fn(y_pred, y_batch)
            # Backward pass
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        print('Epoch [{}/{}], Loss: {:.4f}'.format(epoch + 1, num_epochs, loss.item()))


def saving_model(model):
    torch.save(model.state_dict(), "model.pth")
    print("Saved PyTorch Model State to model.pth")


def main():

    # Load the CSV file
    csv_file = 'pytorchnn\dataset.csv'
    # Create an instance of the CustomDataset
    dataset = CustomDataset(csv_file)

    # Create a DataLoader to load the dataset in batches
    batch_size = 32
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

    # Define a simple model
    model = torch.nn.Sequential(
        torch.nn.Linear(58, 10),
        torch.nn.ReLU(),
        torch.nn.Linear(10, 1),
    )

    # Define a loss function
    loss_fn = torch.nn.MSELoss()

    # Define an optimizer
    optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

    # Train the model
    train(dataloader, loss_fn, model, optimizer)

    saving_model(model)

if __name__ == '__main__':
    main()