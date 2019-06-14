# -*- coding: utf-8 -*-
"""
6. 入力をすべて読み取り、短い順に並べ替えて出力せよ。同じ長さの行が あるときは、それらの行は辞書順に並べるものとする。また、重複する 行は一度だけ出力するものとする。
"""


def main():
    fn = 'input_duplicate_1s.txt'
    word_list = []
    with open(fn) as f:
        for line in f:
            word_list.append(line.rstrip())
    print('\n'.join([i for i in sorted(word_list, key=lambda x: (len(x), x))]))


if __name__ == '__main__':
    main()
