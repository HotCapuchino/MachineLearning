import json

class BPDecoder:
    
    def __init__(self) -> None:
        self.decoding_dict = []
        self.text = ''

    def decode(self, encoded_text: str) -> str:
        try: 
            self.decoding_dict = json.loads(encoded_text.split('\n')[0])
        except Exception as e:
            print('Probably encoded file was corrupted!')
        self.text = encoded_text.split('\n')[1:]
        self.text = ''.join(self.text)
        self._exchange_tokens()
        return self.text

    def _exchange_tokens(self) -> None:
        for i in range(len(self.decoding_dict) - 1, -1, -1):
            pair = self.decoding_dict[i]
            replacer, token = pair[0], pair[1]
            self.text = self.text.replace(replacer, token)
        self.text = self.text.replace('_', ' ')