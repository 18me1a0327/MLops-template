import os
from pathlib import Path

list_files = [

    ".github/workflows/gitkeep",
    "src/_init_.py",
    "src/_components/_init_.py",
    "src/_components/data_ingestion.py",
    "src/_components/data_transformation.py",
    "src/_components/model_trainer.py",
    "src/_components/model_evaluation.py",
    "src/pipeline/_init_.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/predictions_pipeline.py",
    "src/util/utils.py",
    "src/util/_init_.py",
    "src/logger/logger.py",
    "src/exceptions/exceptions",
    "test/unit/_init_.py",
    "test/integration/_init_.py",
    "init_setup.sh",
    "requirements_txt",
    "requirements_dev.text",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.in",
    "experiment/experiment.ipynb",
]


for filepath in list_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file