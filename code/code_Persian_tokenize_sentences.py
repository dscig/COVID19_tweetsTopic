# package import
from parsivar import Tokenizer
import re
import pandas as pd

farsi_total = pd.read_csv("farsi_total.csv")

def CleanText(readData):
    
    # Remove Retweets 
    #text = re.sub('RT @[\w_]+: ', '', readData)
 
    #text = readData

	# Remove Mentions
    #text = re.sub('@[\w_]+', '', text)

    # Remove or Replace URL 
    # text = url_re.sub('URL', text)
    #text = re.sub(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", ' ', text) # start with http
    #text = re.sub(r"[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{2,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)", ' ', text) # Don't start with http
    
    # Remove Hashtag
    # text = re.sub('[#]+[0-9a-zA-Z_]+', ' ', text)
    
    # Remove Zero-width non-joiner
    text = re.sub('\u200c' , ' ', readData)

    # Remove Garbage Words (ex. &lt, &gt, etc)
    text = re.sub(r'[^\w\s]',' ',text)
    text = re.sub('_',' ',text)
		
    # Remove Special Characters
    # text = re.sub('[^0-9a-zA-Z]', ' ', text)
    
    # Remove Numbers (If you want, activate the code)
    text = re.sub(r'\d+',' ',text)
    
    # Remove English (If you want, activate the code)
    text = re.sub('[a-zA-Z]' , ' ', text)
    
    # Remove newline
    text = text.replace('\n',' ')
    
    # Remove multi spacing & Reform sentence
    # text = ' '.join(text.split())

	# If you want to normalize Korean text, activate code below:
	# from konlpy.tag import Okt # Must use Konlpy ver 0.5.2 above
	# okt = Okt()
	# if len(text) != 0:
		# text = okt.normalize(text)
       
    return text

# Persian Stopwords Load
persian_stopwords = pd.read_csv("./persian_stopwords.txt", delimiter='\t', names=["ستون"])

# Add Custom Persian Stopwords 
my_data = []
my_persian_stopwords = pd.DataFrame(my_data, columns = ["ستون"])

# Main 

my_tokenizer = Tokenizer()

def preprocessing_parsivar(readData):
    
    #### Clean text
    sentence = CleanText(readData)
    
    #### Tokenize
    morphs = my_tokenizer.tokenize_words(sentence)
    
    
    # Remove Stopwords
    morphs[:] = (morph for morph in morphs if morph not in persian_stopwords["ستون"].tolist())
    morphs[:] = (morph for morph in morphs if morph not in my_persian_stopwords["ستون"].tolist())
    
    # Remove Numbers
    #morphs[:] = (morph for morph in morphs if morph[1] not in NUMBER)
   
    return morphs


#print(f"Before preprocessing : {farsi_total[tweet]}")
#print(f"After preprocessing : {preprocessing_parsivar(farsi_total)}")


text_file = open("Results.txt", "w")
text_file.write(preprocessing_parsivar(SAMPLE_TEXT))
text_file.close()