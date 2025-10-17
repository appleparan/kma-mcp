"""CLI module."""

import logging
from pathlib import Path

import typer

import hydra
from omegaconf import DictConfig, OmegaConf

from kma_mcp.nlp import train_boolq
from kma_mcp.tabular import train_titanic
from kma_mcp.vision import train_mnist


ROOT_DIR = Path(__file__).resolve().parents[2]

app = typer.Typer(pretty_exceptions_show_locals=False)

logger = logging.getLogger(__name__)


def load_config() -> DictConfig:
    """Load Hydra configuration using compose API."""
    hydra.initialize_config_dir(version_base='1.2', config_dir=str(ROOT_DIR / 'configs'))
    cfg = hydra.compose(config_name='config')
    return cfg


@app.command()
def hello() -> None:
    """Hello function for the CLI.

    Prints a simple "Hello, world!" message.
    """
    cfg: DictConfig = load_config()

    logger.info(OmegaConf.to_yaml(cfg))

    typer.echo('Hello, world!')


@app.command()
def nlp(
    max_epochs: int | None = 10,
    accelerator: str | None = 'auto',
    devices: str | None = 'auto',
    deterministic: bool | None = True,  # noqa: FBT001, FBT002
    random_seed: int | None = 42,
) -> None:
    """NLP training CLI entrypoint.

    This command trains an NLP model using the specified configuration options.

    Args:
        max_epochs (int, optional):
            Maximum number of training epochs. Defaults to 10.
        accelerator (str, optional):
            Accelerator type (e.g., "cpu", "gpu", "tpu"). Defaults to "auto".
        devices (str, optional):
            Number of devices to use for training. Can be an integer, a string
            ("auto"), or a list of device IDs. Defaults to "auto".
            However, due to limitation of typer, this should be a string.
        deterministic (bool, optional):
            Whether to use deterministic algorithms for reproducibility.
            Sets the `torch.backends.cudnn.deterministic` flag. Defaults to True.
        random_seed (int, optional):
            Random seed for reproducibility. Defaults to 42.
    """
    cfg: DictConfig = load_config()

    max_epochs = max_epochs if max_epochs is not None else cfg.get('max_epochs', 10)
    accelerator = accelerator if accelerator is not None else cfg.get('accelerator', 'auto')
    devices = devices if devices is not None else cfg.get('devices', 'auto')
    deterministic = deterministic if deterministic is not None else cfg.get('deterministic', True)
    random_seed = random_seed if random_seed is not None else cfg.get('random_seed', 42)

    typer.echo('Starting NLP training...')
    typer.echo(f'Project root directory: {ROOT_DIR}')

    train_boolq(
        ROOT_DIR,
        max_epochs=max_epochs,
        accelerator=accelerator,
        devices=devices,
        deterministic=deterministic,
        random_seed=random_seed,
    )



@app.command()
def tabular(
    max_epochs: int | None = 10,
    accelerator: str | None = 'auto',
    devices: str | None = 'auto',
    deterministic: bool | None = True,  # noqa: FBT001, FBT002
    random_seed: int | None = 42,
) -> None:
    """Vision training CLI entrypoint.

    This command trains a tabular model using the specified configuration options.

    Args:
        max_epochs (int, optional):
            Maximum number of training epochs. Defaults to 10.
        accelerator (str, optional):
            Accelerator type (e.g., "cpu", "gpu", "tpu"). Defaults to "auto".
        devices (str, optional):
            Number of devices to use for training. Can be an integer, a string
            ("auto"), or a list of device IDs. Defaults to "auto".
            However, due to limitation of typer, this should be a string.
        deterministic (bool, optional):
            Whether to use deterministic algorithms for reproducibility.
            Sets the `torch.backends.cudnn.deterministic` flag. Defaults to True.
        random_seed (int, optional):
            Random seed for reproducibility. Defaults to 42.
    """
    cfg: DictConfig = load_config()

    max_epochs = max_epochs if max_epochs is not None else cfg.get('max_epochs', 10)
    accelerator = accelerator if accelerator is not None else cfg.get('accelerator', 'auto')
    devices = devices if devices is not None else cfg.get('devices', 'auto')
    deterministic = deterministic if deterministic is not None else cfg.get('deterministic', True)
    random_seed = random_seed if random_seed is not None else cfg.get('random_seed', 42)

    typer.echo('Starting tabular training...')
    typer.echo(f'Project root directory: {ROOT_DIR}')

    train_titanic(
        ROOT_DIR,
        max_epochs=max_epochs,
        accelerator=accelerator,
        devices=devices,
        deterministic=deterministic,
        random_seed=random_seed,
    )



@app.command()
def vision(
    max_epochs: int | None = 10,
    accelerator: str | None = 'auto',
    devices: str | None = 'auto',
    deterministic: bool | None = True,  # noqa: FBT001, FBT002
    random_seed: int | None = 42,
) -> None:
    """Vision training CLI entrypoint.

    This command trains a vision model using the specified configuration options.

    Args:
        max_epochs (int, optional):
            Maximum number of training epochs. Defaults to 10.
        accelerator (str, optional):
            Accelerator type (e.g., "cpu", "gpu", "tpu"). Defaults to "auto".
        devices (str, optional):
            Number of devices to use for training. Can be an integer, a string
            ("auto"), or a list of device IDs. Defaults to "auto".
            However, due to limitation of typer, this should be a string.
        deterministic (bool, optional):
            Whether to use deterministic algorithms for reproducibility.
            Sets the `torch.backends.cudnn.deterministic` flag. Defaults to True.
        random_seed (int, optional):
            Random seed for reproducibility. Defaults to 42.
    """
    cfg: DictConfig = load_config()

    max_epochs = max_epochs if max_epochs is not None else cfg.get('max_epochs', 10)
    accelerator = accelerator if accelerator is not None else cfg.get('accelerator', 'auto')
    devices = devices if devices is not None else cfg.get('devices', 'auto')
    deterministic = deterministic if deterministic is not None else cfg.get('deterministic', True)
    random_seed = random_seed if random_seed is not None else cfg.get('random_seed', 42)

    typer.echo('Starting vision training...')
    typer.echo(f'Project root directory: {ROOT_DIR}')

    train_mnist(
        ROOT_DIR,
        max_epochs=max_epochs,
        accelerator=accelerator,
        devices=devices,
        deterministic=deterministic,
        random_seed=random_seed,
    )



@app.command()
def hello() -> None:
    """Say hello to the user."""
    typer.echo("Hello, user!")


def main() -> None:
    """Main entrypoint for the CLI application.

    Runs the Typer app to handle user commands.
    """
    app()


if __name__ == '__main__':
    main()
