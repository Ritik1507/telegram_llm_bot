import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s:")

project_name = "llm_Bot"

list_of_files = [
    
    f"{project_name}/__init__.py",
    f"{project_name}/Bot.py",
    f"{project_name}/filters.py",
    f"{project_name}/handlers.py",
    f"{project_name}/html_format.py",
    f"{project_name}/llm.py",
    "research/research,ipynb",
    "main.py",
    ".env",
    "Docker",
    "requirements.txt",
    
]

for filepath in list_of_files:
    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating directory; {filedir} for the file:  {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"creating empty file: {filepath}")
            
    else:
         logging.info(f"{filename} already exists ")    