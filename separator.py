import nltk


def separateUnspacedWords(unspacedText):
    # Download the required resources for sentence tokenization
    nltk.download('punkt')

    # Use NLTK's sent_tokenize function for basic sentence tokenization
    sentences = nltk.sent_tokenize(unspacedText)
    return sentences
