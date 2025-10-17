import pytest
import numpy as np
import torch
from pathlib import Path
from kma_mcp.tabular import TabularDataset, TabularClassifier, preprocess_titanic_data, train_titanic


def test_tabular_dataset():
    """Test TabularDataset class."""
    data = np.random.randn(100, 5)
    labels = np.random.randint(0, 2, 100)
    
    dataset = TabularDataset(data, labels)
    assert len(dataset) == 100
    
    sample, label = dataset[0]
    assert sample.shape == (5,)
    assert isinstance(label.item(), int)


def test_tabular_classifier_init():
    """Test TabularClassifier initialization."""
    model = TabularClassifier(input_dim=5, hidden_dim=64, output_dim=2)
    assert model.lr == 1e-3
    assert model.model is not None


def test_tabular_classifier_forward():
    """Test TabularClassifier forward pass."""
    model = TabularClassifier(input_dim=5, hidden_dim=64, output_dim=2)
    x = torch.randn(10, 5)
    
    output = model(x)
    assert output.shape == (10, 2)


def test_preprocess_titanic_data():
    """Test Titanic data preprocessing."""
    X_train, X_val, X_test, y_train, y_val, y_test = preprocess_titanic_data(random_seed=42)
    
    # Check shapes
    assert X_train.shape[0] > 0
    assert X_val.shape[0] > 0  
    assert X_test.shape[0] > 0
    assert len(y_train) == X_train.shape[0]
    assert len(y_val) == X_val.shape[0]
    assert len(y_test) == X_test.shape[0]
    
    # Check that features are standardized (approximately mean 0, std 1)
    assert abs(X_train.mean()) < 0.1
    assert abs(X_train.std() - 1.0) < 0.1


@pytest.mark.slow
def test_train_titanic(tmp_path):
    """Test Titanic training function."""
    train_titanic(
        root_dir=tmp_path,
        max_epochs=1,
        batch_size=32,
        accelerator="cpu", 
        devices=1,
        random_seed=42
    )
    # Check that model artifacts are created
    assert any(tmp_path.glob("**/*.ckpt"))