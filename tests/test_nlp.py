import pytest
from kma_mcp.nlp import TinyBertClassifier, prepare_data, train_boolq
from pathlib import Path
import torch
from transformers import AutoTokenizer


def test_tiny_bert_classifier_init():
    """Test TinyBertClassifier initialization."""
    model = TinyBertClassifier("google/bert_uncased_L-2_H-128_A-2")
    assert model.lr == 2e-5
    assert model.model is not None


def test_tiny_bert_classifier_forward():
    """Test TinyBertClassifier forward pass."""
    model = TinyBertClassifier("google/bert_uncased_L-2_H-128_A-2")
    input_ids = torch.randint(0, 1000, (2, 10))
    attention_mask = torch.ones(2, 10)
    
    output = model(input_ids, attention_mask)
    assert output.logits.shape == (2, 2)


def test_prepare_data():
    """Test data preparation function."""
    tokenizer = AutoTokenizer.from_pretrained("google/bert_uncased_L-2_H-128_A-2")
    train_dataset, val_dataset, test_dataset = prepare_data(tokenizer, max_length=128)
    
    assert len(train_dataset) == 4000
    assert len(val_dataset) == 1000
    assert len(test_dataset) == 1000


@pytest.mark.slow
def test_train_boolq(tmp_path):
    """Test BoolQ training function."""
    train_boolq(
        root_dir=tmp_path,
        max_epochs=1,
        accelerator="cpu",
        devices=1,
        random_seed=42
    )
    # Check that model artifacts are created
    assert any(tmp_path.glob("**/*.ckpt"))