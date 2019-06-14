# -*- coding: utf-8 -*-
"""
8. 入力をすべて読み取り、すべての偶数番めの行を出力したあとに、すべ ての奇数番めの行を出力せよ(最初の行を 0 行めと数える)。
"""


def main():
    fn = 'input_1s.txt'
    word_list = []
    with open(fn) as f:
        for line in f:
            word_list.append(line.rstrip())
    print('\n'.join([str(i) for i in range(0, len(word_list), 2)]))
    print('\n'.join([str(i) for i in range(1, len(word_list), 2)]))


if __name__ == '__main__':
    main()
