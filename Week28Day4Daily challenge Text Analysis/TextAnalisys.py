#Part 1:

import re
from collections import Counter

class Text:
    def __init__(self, text):
        self.text = text

    def word_frequency(self, word):
        return None if not word else self.text.split().count(word)

    def most_common_word(self):
        words = self.text.split()
        return Counter(words).most_common(1)[0] if words else None

    def unique_words(self):
        return list(set(self.text.split()))

    @classmethod
    def from_file(cls, filepath):
        with open(filepath, 'r') as file:
            return cls(file.read())

class TextModification(Text):
    def remove_punctuation(self):
        return re.sub(r'[^\w\s]', '', self.text)

    def remove_stop_words(self):
        stop_words = set([
            'i', 'me', 'my', 'we', 'you', 'he', 'she', 'it', 'they', 
            'a', 'an', 'the', 'and', 'but', 'if', 'or', 'not', 'is', 'are'
        ])
        return ' '.join(word for word in self.text.split() if word.lower() not in stop_words)

    def remove_special_characters(self):
        return re.sub(r'[^A-Za-z0-9\s]', '', self.text)

#Part 2:

import re
from collections import Counter

class Text:
    def __init__(self, text):
        self.text = text

    def word_frequency(self, word):
        return None if not word else self.text.split().count(word)

    def most_common_word(self):
        words = self.text.split()
        return Counter(words).most_common(1)[0] if words else None

    def unique_words(self):
        return list(set(self.text.split()))

    @classmethod
    def from_file(cls, filepath):
        with open(filepath, 'r', encoding='utf-8') as file:
            text = file.read()
        return cls(text)

class TextModification(Text):
    def remove_punctuation(self):
        return re.sub(r'[^\w\s]', '', self.text)

    def remove_stop_words(self):
        stop_words = set([
            'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 
            'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 
            'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 
            'itself', 'they', 'them', 'their', 'theirs', 'themselves', 
            'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 
            'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 
            'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 
            'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 
            'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 
            'against', 'between', 'into', 'through', 'during', 'before', 
            'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 
            'out', 'on', 'off', 'over', 'under', 'again', 'further', 
            'then', 'once', 'here', 'there', 'when', 'where', 'why', 
            'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 
            'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 
            'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 
            'just', 'don', 'should', 'now'
        ])
        words = self.text.split()
        return ' '.join(word for word in words if word.lower() not in stop_words)

    def remove_special_characters(self):
        return re.sub(r'[^A-Za-z0-9\s]', '', self.text)

