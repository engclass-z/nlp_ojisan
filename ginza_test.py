# coding: UTF-8
import spacy
import jaconv

# https://oji.netlify.app/ より
# input = 'なみチャン、お疲れ様〜😃😚(^з<)（笑）今日は茨城28度だよ💔(^_^;(￣Д￣；；(◎ ＿◎;)暑いよ💔ヤケドしないように気をつけないとネ😃♥ ❗'
# input = 'タマオﾁｬﾝ、ヤッホー（笑）😚何してるのかい⁉早く会いたいな❗😃☀ 😍(^o^)'
# input = '彩世ちゃんは、お肌がきれい✨ダネ🎵(^з<)今から寝ようと思ってたのに、目が覚めちゃったよ😃✋😃♥ どうしてくれるんダ😘😃✋(^o^)😚'
# input = 'おはよー！チュッ😃♥ (^o^)😃🎵本日のランチ🍴は奮発してサラダ付き（笑）🎵😄💗誰だメタボなんて言ったやつは(^▽^;)^^;(￣Д￣；；💦'
# input = 'エリナちゃん、可愛らしイネ❗😃ホント可愛すぎだよ〜(^_^)😆💗マッタクもう(^_^)😃☀'
input = 'えみちゃん、こんな遅い時間😤に何をしているのかな❗❓⁉❓✋❓今日も頑張ってね😃♥ 😃☀ 😚'
output = ''

nlp = spacy.load('ja_ginza')
doc = nlp(input)
for sent in doc.sents:
    for token in sent:
        target = token.orth_

        # 半角ｶﾅはキモいので全角に
        target = jaconv.h2z(target)

        if token.dep_ == 'dep' and token.head.i == 37:
            target = ''

        # それ以外の記号は！に変えちゃう
        if '記号' in token.tag_:
            target = '！'

        # よりキモそうな顔文字とかの記号だったら無視
        if '補助記号' in token.tag_:
            target = ''

        # 空白扱いの文字はよくわからないので！にしちゃう
        if '空白' in token.tag_:
            target = '！'

        # 敬称はひらがなに。そもそもチャンとかどうなのとも思うけど
        if '接尾辞-名詞的-一般' in token.tag_:
            target = jaconv.kata2hira(target)

        # 終助詞がカタカナになってたらひらがなに戻してやる
        if '終助詞' in token.tag_ or '助動詞' in token.tag_:
            target = jaconv.kata2hira(target)

        # なんとなく❗ は！に変換したい
        if '❗' == target:
            target = '！'

        # print(
        #     token.i,
        #     token.orth_,
        #     token.lemma_,
        #     token.norm_,
        #     token.morph.get("Reading"),
        #     token.pos_,
        #     token.morph.get("Inflection"),
        #     token.tag_,
        #     token.dep_,
        #     token.head.i,
        # )
        output = output + target

print('入力: ' + input)
print('出力: ' + output)
