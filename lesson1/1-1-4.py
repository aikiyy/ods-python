# -*- coding: utf-8 -*-
"""
4.入力を 1 行ずつ読み取り、それまでに読み込んだことがある行と重複 しない行を見つけたら出力せよ。重複が多いファイルを読む場合でも、 重複なく行を保持するのに必要なメモリより多くのメモリを使わない ように注意せよ。
"""


def main():
    fn = 'input_duplicate_1s.txt'
    word_set = set([])
    with open(fn) as f:
        for line in f:
            if line.rstrip() not in word_set:
                print(line.rstrip())
                word_set.add(line.rstrip())


if __name__ == '__main__':
    main()
