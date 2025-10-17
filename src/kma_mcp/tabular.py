from pathlib import Path

import lightning as L  # noqa: N812
import numpy as np
import pandas as pd
import torch
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from torch import nn
from torch.utils.data import DataLoader, Dataset


class TabularDataset(Dataset):
    """Custom dataset for tabular data.

    Args:
        data (numpy.ndarray): The tabular feature data.
            Expected shape is (n_samples, n_features), where
            `n_samples` is the number of rows (observations)
            and `n_features` is the number of columns (features).
        labels (numpy.ndarray): The target labels corresponding to the data.
            Expected shape is (n_samples,), where each entry corresponds
            to the label of a row in `data`.
    """

    def __init__(self, data: np.ndarray, labels: np.ndarray):
        """Initialize the TabularDataset.

        Args:
            data (numpy.ndarray): Tabular feature data.
            labels (numpy.ndarray): Target labels.
        """
        self.data = torch.tensor(data, dtype=torch.float32)
        self.labels = torch.tensor(labels, dtype=torch.long)

    def __len__(self) -> int:
        """Return the number of samples in the dataset.

        Returns:
            int: Number of samples.
        """
        return len(self.data)

    def __getitem__(self, idx: int) -> tuple[torch.Tensor, torch.Tensor]:
        """Get a sample and its corresponding label.

        Args:
            idx (int): Index of the sample to retrieve.

        Returns:
            tuple[torch.Tensor, torch.Tensor]: A tuple containing
            the feature tensor and the corresponding label tensor.
        """
        return self.data[idx], self.labels[idx]


class TabularClassifier(L.LightningModule):
    """A PyTorch Lightning Module for tabular data classification.

    Attributes:
        input_dim (int): Number of input features.
        hidden_dim (int): Number of hidden units in the model.
        output_dim (int): Number of output classes.
        lr (float): Learning rate for the optimizer.
        model: torch NN.module instance.
        loss_fn: Loss function for the model.
    """

    def __init__(
        self,
        input_dim: int,
        hidden_dim: int = 64,
        output_dim: int = 2,
        lr: float | None = 1e-3,
    ):
        """Initialize the TabularClassifier.

        Args:
            input_dim (int): Number of input features.
            hidden_dim (int, optional):
                Number of hidden units in the model. Defaults to 64.
            output_dim (int, optional): Number of output classes. Defaults to 2.
            lr (float, optional): Learning rate for the optimizer. Defaults to 1e-3.
        """
        super().__init__()
        self.save_hyperparameters()
        self.model = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim // 2),
            nn.ReLU(),
            nn.Linear(hidden_dim // 2, output_dim),
        )
        self.loss_fn = nn.CrossEntropyLoss()
        self.lr = lr

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Perform a forward pass through the model.

        Args:
            x (torch.Tensor): Input tensor.

        Returns:
            torch.Tensor: The model output.
        """
        return self.model(x)

    def training_step(
        self,
        batch: tuple[dict[str, torch.Tensor], torch.Tensor],
        batch_idx: int,  # noqa: ARG002
    ) -> torch.Tensor:
        """Perform a training step.

        Args:
            batch (tuple[dict[str, torch.Tensor], torch.Tensor]):
                The input batch containing features and labels.
            batch_idx (int): The index of the batch.

        Returns:
            torch.Tensor: The computed training loss.
        """
        x, y = batch
        preds = self(x)
        loss = self.loss_fn(preds, y)
        self.log('train_loss', loss)
        return loss

    def validation_step(
        self,
        batch: tuple[dict[str, torch.Tensor], torch.Tensor],
        batch_idx: int,  # noqa: ARG002
    ) -> torch.Tensor:
        """Perform a validation step.

        Args:
            batch (tuple[dict[str, torch.Tensor], torch.Tensor]):
                The input batch containing features and labels.
            batch_idx (int): The index of the batch.

        Returns:
            torch.Tensor: The computed training loss.
        """
        x, y = batch
        preds = self(x)
        loss = self.loss_fn(preds, y)
        acc = (preds.argmax(dim=1) == y).float().mean()
        self.log('val_loss', loss, prog_bar=True)
        self.log('val_acc', acc, prog_bar=True)

    def test_step(
        self,
        batch: tuple[dict[str, torch.Tensor], torch.Tensor],
        batch_idx: int,  # noqa: ARG002
    ) -> torch.Tensor:
        """Perform a test step.

        Args:
            batch (tuple[dict[str, torch.Tensor], torch.Tensor]):
                The input batch containing features and labels.
            batch_idx (int): The index of the batch.

        Returns:
            torch.Tensor: The computed training loss.
        """
        x, y = batch
        preds = self(x)
        loss = self.loss_fn(preds, y)
        acc = (preds.argmax(dim=1) == y).float().mean()
        self.log('test_loss', loss, prog_bar=True)
        self.log('test_acc', acc, prog_bar=True)

    def configure_optimizers(self) -> torch.optim.Adam:
        """Configure the optimizer for the model.

        Returns:
            Adam: The Adam optimizer.
        """
        return torch.optim.Adam(self.parameters(), lr=self.lr)


def preprocess_titanic_data(random_seed: int = 42) -> None:
    """Load and preprocess the Titanic dataset.

    Args:
        random_seed (int, optional): Random seed for reproducibility. Defaults to 42.
    """
    url = 'https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv'
    data = pd.read_csv(url)

    # Drop unnecessary columns
    data = data.drop(columns=['Name'])

    # Fill missing values
    data['Age'] = data['Age'].fillna(data['Age'].median())

    # Encode categorical variables
    data['Sex'] = LabelEncoder().fit_transform(data['Sex'])

    # Split features and labels
    X = data.drop(columns=['Survived']).to_numpy()
    y = data['Survived'].to_numpy()

    # Train-test split
    X_train, X_temp, y_train, y_temp = train_test_split(
        X, y, test_size=0.3, random_state=random_seed
    )
    X_val, X_test, y_val, y_test = train_test_split(
        X_temp, y_temp, test_size=0.5, random_state=random_seed
    )

    # Standardize features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_val = scaler.transform(X_val)
    X_test = scaler.transform(X_test)

    return X_train, X_val, X_test, y_train, y_val, y_test


def train_titanic(
    root_dir: Path,
    max_epochs: int = 10,
    batch_size: int = 16,
    accelerator: str = 'auto',
    devices: int | str | list[int] = 'auto',
    deterministic: bool = True,  # noqa: FBT001, FBT002
    random_seed: int = 42,
) -> None:
    """Train titanic datasets with classification model.

    Args:
        root_dir (Path): Default path for logs and weights.
        max_epochs (int, optional):
            Stop training once this number of epochs is reached.
            Defaults to 10.
        batch_size (int, optional):
            Number of samples in a batch. Defaults to 16.
        accelerator (str, optional):
            Supports passing different accelerator types.
            Defaults to "auto".
        devices (int, optional):
            Number of devices to train on. Defaults to "auto".
        deterministic (bool, optional):
            Sets the `torch.backends.cudnn.deterministic` flag.
            Defaults to True.
        random_seed (int, optional):
            Random seed for reproducibility. Defaults to 42.
    """
    """Train the tabular classifier."""
    L.seed_everything(random_seed, workers=True)

    X_train, X_val, X_test, y_train, y_val, y_test = preprocess_titanic_data()

    # Prepare datasets and dataloaders
    train_dataset = TabularDataset(X_train, y_train)
    val_dataset = TabularDataset(X_val, y_val)
    test_dataset = TabularDataset(X_test, y_test)

    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=batch_size)
    test_loader = DataLoader(test_dataset, batch_size=batch_size)

    # Model and Trainer setup
    input_dim = X_train.shape[1]
    model = TabularClassifier(input_dim=input_dim)
    trainer = L.Trainer(
        default_root_dir=root_dir,
        max_epochs=max_epochs,
        accelerator=accelerator,
        devices=devices,
        deterministic=deterministic,
        log_every_n_steps=10,
    )
    trainer.fit(model, train_loader, val_loader)
    trainer.test(model, test_loader)
