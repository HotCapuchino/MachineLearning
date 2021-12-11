class BPEncoder:

    def __init__(self) -> None:
        self.encoding_dict = []
        self.allowed_chars = dict(zip([i for i in range(33, 255, 1)], [chr(i) for i in range(33, 255, 1)]))
    
    def encode(self, text: str) -> str:
        self.text = text
        # self._wipe_data()
        text = self._prepare_text()
        self._calculate_encoding_array()
        return [self.text, self.encoding_dict]

    def _prepare_text(self) -> None:
        # creating extra underscore tokens at the end of the words
        # trim extra whitespaces
        splitted = self.text.split()
        recovered = ' '.join(splitted)
        recovered = recovered.replace(' ', '_')
        # define ascii code for characters allowed for encoding
        for char in recovered:
            if char in self.allowed_chars.values():
                self.allowed_chars.pop(ord(char))
        self.text = recovered

    def _wipe_data(self) -> None:
        self.encoding_dict.clear()
        self.allowed_chars.clear()

    def _calculate_encoding_array(self) -> None:
        while True:
            freq_matrix = dict()
            for i in range(0, len(self.text), 2):
                token = self.text[i:i+2]
                if token in freq_matrix.keys():
                    amount = freq_matrix.get(token)
                    freq_matrix.update({token:amount + 1})
                else:
                    freq_matrix.update({token:1})
            freq_matrix = dict(sorted(freq_matrix.items(), key=lambda item: 0 - item[1]))
            first_token = next(iter(freq_matrix.keys()))
            if freq_matrix.get(first_token) > 1:
                if not self._exchange(first_token):
                    return
            else: 
                return

    def _exchange(self, token: str) -> bool: 
        try:
            replacer_key = next(iter(self.allowed_chars.keys()))
        except Exception as e:
            return False
        replacer = self.allowed_chars.get(replacer_key)
        self.text = self.text.replace(token, replacer)
        self.allowed_chars.pop(replacer_key)
        self.encoding_dict.append((replacer, token))
        return True
