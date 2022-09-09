from janome.tokenizer import Tokenizer
t = Tokenizer()
for token in t.tokenize('月日は百代の過客にして、行かふ年も又旅人也。'):
    print(token)