import os

def read_dataset_from_directory(directory_path):
    data = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".txt"):
                f = open(os.path.join(root, file),encoding="latin-1")
                doc = ""
                for line in f:
                    doc += line
                data.append(doc)
    return data