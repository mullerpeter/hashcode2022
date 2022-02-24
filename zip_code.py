from zipfile import ZipFile
import os
from os.path import basename

excluded_directories = ['000_practice', 'input_data', 'runs', 'submissions', '__pycache__', 'venv']


def zip_code():
    # create a ZipFile object
    with ZipFile('submission/code.zip', 'w') as zipObj:
        # Iterate over all the files in directory
        for folderName, subfolders, filenames in os.walk('.'):
            for filename in filenames:
                # Skip non python/json files
                if '.py' not in filename and '.json' not in filename:
                    continue
                # Skip excluded directories
                if any(directory in folderName for directory in excluded_directories):
                    continue

                # create complete filepath of file in directory
                filePath = os.path.join(folderName, filename)
                # Add file to zip
                zipObj.write(filePath, basename(filePath))
