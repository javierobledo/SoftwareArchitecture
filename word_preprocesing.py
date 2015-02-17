from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


def remove_stopwords(data):
    new_data = []
    tokenizer = RegexpTokenizer(r'\w+')
    for document in data:
        new_data.append(remove_document_stopwords(document,tokenizer))
    return new_data

def remove_document_stopwords(document,tokenizer):
    new_document = [" ".join(filtered_sentence) for filtered_sentence in [w for w in [tokenizer.tokenize(sentence.lower()) for sentence in sent_tokenize(document)] if not w in stopwords.words('english')]]
    return " ".join(new_document)

def stemming(data):
    stemmer = PorterStemmer()
    new_data = []
    for document in data:
        words = [stemmer.stem(word) for word in document.split()]
        new_data.append(" ".join(words))
    return new_data


