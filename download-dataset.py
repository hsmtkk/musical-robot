import os
import sys
import zipfile

import dotenv
import kaggle

dotenv.load_dotenv(override=True)


def required_env_var(name: str):
    val = os.getenv(name)
    if val == "":
        print(f"env var {name} is not defined")
        sys.exit(1)


required_env_var("KAGGLE_USERNAME")
required_env_var("KAGGLE_KEY")

DATASET = "snap/amazon-fine-food-reviews"
FILENAME = "Reviews.csv"
OUTPUT_PATH = "dataset"

print("download dataset")
kaggle.api.dataset_download_file(DATASET, FILENAME, OUTPUT_PATH)

print("uncompress dataset zip")
with zipfile.ZipFile(f"{OUTPUT_PATH}/{FILENAME}.zip") as z:
    with z.open(FILENAME) as r:
        with open(f"{OUTPUT_PATH}/{FILENAME}", "wb") as w:
            w.write(r.read())
