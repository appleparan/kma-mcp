import pytest
import torch
from pathlib import Path
from kma_mcp.vision import MNISTClassifier, train_mnist


def test_mnist_classifier_init():
    """Test MNISTClassifier initialization."""
    model = MNISTClassifier(lr=1e-3)
    assert model.lr == 1e-3
    assert model.model is not None


def test_mnist_classifier_forward():
    """Test MNISTClassifier forward pass."""
    model = MNISTClassifier()
    x = torch.randn(10, 1, 28, 28)  # MNIST image shape
    
    output = model(x)
    assert output.shape == (10, 10)  # 10 classes


def test_mnist_classifier_training_step():
    """Test MNIST classifier training step."""
    model = MNISTClassifier()
    x = torch.randn(4, 1, 28, 28)
    y = torch.randint(0, 10, (4,))
    batch = (x, y)
    
    loss = model.training_step(batch, 0)
    assert isinstance(loss, torch.Tensor)
    assert loss.item() > 0


def test_mnist_classifier_validation_step():
    """Test MNIST classifier validation step."""
    model = MNISTClassifier()
    x = torch.randn(4, 1, 28, 28)
    y = torch.randint(0, 10, (4,))
    batch = (x, y)
    
    loss = model.validation_step(batch, 0)
    assert isinstance(loss, torch.Tensor)
    assert loss.item() > 0


@pytest.mark.slow
def test_train_mnist(tmp_path):
    """Test MNIST training function."""
    train_mnist(
        root_dir=tmp_path,
        max_epochs=1,
        batch_size=32,
        accelerator="cpu",
        devices=1,
        random_seed=42
    )
    # Check that model artifacts are created
    assert any(tmp_path.glob("**/*.ckpt"))