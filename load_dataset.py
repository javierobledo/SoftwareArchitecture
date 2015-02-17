import sys
from file_io import read_dataset_from_directory
from sklearn.feature_extraction.text import TfidfVectorizer
from numpy import float32
from file import store_sparse_mat
from word_preprocesing import *

if(len(sys.argv) == 4):
    data = read_dataset_from_directory(sys.argv[1])
    data = remove_stopwords(data)
    data = stemming(data)
    mat_name = sys.argv[2]
    mat_file = sys.argv[3]
    vectorizer = TfidfVectorizer(dtype=float32)
    X = vectorizer.fit_transform(data)
store_sparse_mat(X,mat_name,mat_file)