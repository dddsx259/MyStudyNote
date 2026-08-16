import string
import regex as re


test_str = """low low low low low lower lower widest widest widest newest newest newest newest newest newest"""

def pre_tokenizer(str: string)->dict:
    PAT = r"""'(?:[sdmt]|ll|ve|re)| ?\p{L}+| ?\p{N}+| ?[^\s\p{L}\p{N}]+|\s+(?!\S)|\s+"""
    words = dict()
    for word in re.finditer(PAT, str):
        if word in words:
            words[word]+=1
        else:
            words[word] = 1
        return words

print(pre_tokenizer(test_str))
    