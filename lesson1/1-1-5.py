# -*- coding: utf-8 -*-
"""
5.入力を 1 行ずつ読み取り、それまでに読み込んだことがある行と同じ なら出力せよ(最終的には、ある行が入力ファイルに初めて現れた箇所 をそれぞれ除いたものが出力になる)。重複が多いファイルを読む場合 でも、重複なく行を保持するのに必要なメモリより多くのメモリを使わ ないように注意せよ。
"""


def main():
    fn = 'input_duplicate_1s.txt'
    word_set = set([])
    with open(fn) as f:
        for line in f:
            if line.rstrip() in word_set:
                print(line.rstrip())
            else:
                word_set.add(line.rstrip())


if __name__ == '__main__':
    main()
