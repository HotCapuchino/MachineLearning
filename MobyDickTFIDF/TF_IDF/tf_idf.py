import re
from collections import Counter
import math

class TF_IDF:

    def __init__(self, texts: list) -> None:
        self.texts: list = self.__prepare_data(texts)
        self.frequency_array = [None] * len(self.texts)

    def __prepare_data(self, data: list) -> list:
        chars_to_delete = re.compile('[^A-Za-z\s]')
        modified_texts = []
        for text in data:
            text_words = []
            for word in str(re.sub(chars_to_delete, '', text)).split():
                if len(word) > 3:
                    text_words.append(word.lower())
            modified_texts.append(text_words)
        return modified_texts

    def calculate_tf_idf(self) -> None:
        for i in range(len(self.texts)):
            print(f'currently working at {i + 1} chapter...')
            self.frequency_array[i] = self.__calculate_tf(i)

    def __calculate_tf(self, corpus: int) -> dict:
        N = len(self.texts[corpus])
        amount_dict = Counter(self.texts[corpus])
        for word in amount_dict.keys():
            word_idf = self.__calculate_idf(word)
            amount_dict[word] = (amount_dict[word] / N) * word_idf
        return amount_dict

    def __calculate_idf(self, term: str) -> int:
        N = len(self.texts)
        amount = 0
        for text in self.texts:
            if term in text:
                amount += 1
        return math.log10(N / amount + 1)

    def get_top_words(self, corpus: int, amount: int) -> list:
        sorted_words = list({key: value for key, value in sorted(self.frequency_array[corpus].items(), key=lambda item: 1 - item[1])}.keys())
        return sorted_words[:amount]
        