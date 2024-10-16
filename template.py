import os
from pathlib import Path
import logging

#logging stream
logging.basicConfig(level=logging.INFO, format = '[%(asctime)s]: %(message)s:,')

project_name = "Medical-Chatbot"

file_list = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "app.py",
    "setup.py",
    "research/trials.ipynb"
]


for filepath in file_list:
    filepath = Path(filepath)    #for / path error
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok = True)
        logging.info(f"Created directory: {filedir} for the file: {filename}")


    if(not os.path.exists(filepath)) or (not os.path.getsize(filepath) == 0):       #if size is not 0, there could be code inside the file
        with open(filepath, "w") as f:
            pass
            logging.info(f"Created empty file: {filepath}")


    else:
         logging.info(f"{filepath} already exists!")