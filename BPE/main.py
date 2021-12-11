from BPE import BPEncoder
from BPE import BPDecoder
import json

if __name__ == '__main__':

    input = open('./res/input_text.txt')
    text_to_encode = input.read()
    input.close()

    bpEncoder = BPEncoder()
    encoded_text, encoding_dict = bpEncoder.encode(text_to_encode)
    
    output = open('./out/encoded.txt', 'w')
    output.write(f'{json.dumps(encoding_dict)}\n')
    output.write(encoded_text)

    output = open('./out/encoded.txt', 'r')
    encoded_text = output.read()
    output.close()

    bpDecoder = BPDecoder()
    decoded_text = bpDecoder.decode(encoded_text)
    output_decoded = open('./out/decoded.txt', 'w')
    output_decoded.write(decoded_text)
    output_decoded.close()
