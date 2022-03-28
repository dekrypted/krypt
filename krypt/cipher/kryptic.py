import random

class quickCipher:
    def encode(data,key=random.choice('手田水口廿卜山戈人心日尸中木大火十土竹Ｚ一難弓金月女')):
            decode = []
            for i in range(len(data)):
                    encoded = ord(data[i])
                    if encoded >= 33 and encoded <= 126:
                            decode.append(chr(33 + ((encoded + 14) % 94)))
                    else:
                            decode.append(data[i])
            return f'{key}\\\\u00x/+?{key.join(decode)}'
    def decode(data):
            data = data.split('\\u00x/+?')
            decodeChar = data[0]
            data = data[1].replace(decodeChar,'')
            decode = []
            for i in range(len(data)):
                    encoded = ord(data[i])
                    if encoded >= 33 and encoded <= 126:
                            decode.append(chr(33 + ((encoded + 14) % 94)))
                    else:
                            decode.append(data[i])
            return ''.join(decode)
