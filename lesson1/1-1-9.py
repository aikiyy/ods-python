# -*- coding: utf-8 -*-
"""
9. 入力をすべて読み取り、ランダムに並べ替えて出力せよ。どの行の内容 も書き換えてはならない。また、入力より行が増えたり減ったりしても いけない。
"""

import random


def main():
    fn = 'input_1s.txt'
    word_list = []
    with open(fn) as f:
        for line in f:
            word_list.append(line.rstrip())
    random.shuffle(word_list)
    print('\n'.join([str(i) for i in word_list]))


if __name__ == '__main__':
    main()
