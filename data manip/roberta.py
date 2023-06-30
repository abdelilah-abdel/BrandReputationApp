from transformers import AutoModelForSequenceClassification
from transformers import TFAutoModelForSequenceClassification
from transformers import AutoTokenizer
from scipy.special import softmax

tweet ="hey @sexy_girl whatsapp , you looking good 😍 https://github.com/abdelilah-abdel/BrandReputationPlateform"

#preprocess tweet 

tweet_words = []

for word in tweet.split(' '):
    if word.startswith('@') and len(word) > 1:
        word = '@user'
    elif word.startswith('http'):
        word = '@http'
    tweet_words.append(word)

tweet_proc = " ".join(tweet_words)

print(tweet_words)
print(tweet_proc)
