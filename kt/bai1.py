import re
from collections import OrderedDict

def filter_words(text):
    """
    Filters special characters, removes duplicate words, and returns a list of lowercase words 
    maintaining the original order of appearance.
    """
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)  
    words = text.lower().split()

    # Remove duplicates while preserving order
    return list(OrderedDict.fromkeys(words))


input_text = "The cat is chasing the rat. The dog is also chasing the rat."
output = filter_words(input_text)
print(output)  # Output: ['the', 'cat', 'is', 'chasing', 'rat', 'dog', 'also']

