from janome.tokenizer import Tokenizer
t = Tokenizer()
for token in t.tokenize('なみチャン、お疲れ様〜😃😚(^з<)（笑）今日は茨城28度だよ💔(^_^;(￣Д￣；；(◎ ＿◎;)暑いよ💔ヤケドしないように気をつけないとネ😃♥ ❗'):
    print(token)