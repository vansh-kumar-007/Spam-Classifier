import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Ensure stopwords are downloaded (AUTO-FIX)
try:
    stop_words = set(stopwords.words('english'))
except LookupError:
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))

ps = PorterStemmer()

def preprocess_text(text):
    text = text.lower()
    text = re.sub('[^a-z]', ' ', text)
    words = text.split()
    
    processed_words = []
    for word in words:
        if word not in stop_words:
            processed_words.append(ps.stem(word))
    
    return " ".join(processed_words)