# -*- coding: utf-8 -*-
"""
1. 入力を 1 行ずつ読み、その逆順で出力せよ。すなわち、最後の入力行 を最初に書き出し、最後から 2 行めを 2 番めに書き出す、というよう に出力せよ。
"""


def main():
    fn = 'input_1m.txt'
    word_list = []
    with open(fn) as f:
        for line in f:
            word_list.append(line.rstrip())
    print('\n'.join([i for i in reversed(word_list)]))


if __name__ == '__main__':
    main()
