# demo9-3.py
import jieba
s = 'hello,world python aboc oedf'
s1 = s.title()
s2 = s.split('o')
print(s1, '|', s2)


text = 'hello world python'
list1 = [word.capitalize() for word in text.split()]
print(list1)


sentence = "我爱自然语言处理"
words1 = jieba.cut(sentence)
# 列表可以重复访问 words1 = list(jieba.cut(sentence))
print("/".join(words1))

for word1 in words1:  # 一旦生成器中的元素被访问过一次，就不能再次访问了
    print(word1, '1')


s3 = '''
处理文本数据：在进行文本分析或自然语言处理时，
split()方法是一个非常重要的工具。
例如，你可以使用split(' ')将一个文本字符串分割成一个单词列表，
然后进行进一步的分析或处理
'''
words2 = jieba.cut(s3)
print('/'.join(words2))


s4 = '''
https://www.bilibili.com/video/
BV1wD4y1o7AS?p=80&spm_id_from=pageDriver&vd_source
=ff66893fb81121d2b498f13bea2023e9
'''

# 首先按照斜杠 '/' 分割字符串
parts = s4.split('/')
# 然后对结果进行第二次分割，按照反斜杠 '=' 分割
parts = [part.split('=') for part in parts]
print(parts)
