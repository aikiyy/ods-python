# -*- coding: utf-8 -*-
"""
3. 入力を 1 行ずつ読み取り、42 行め以降で空行を見つけたら、その 42 行前の行を出力せよ。例えば、242 行めが空行であれば 200 行めを出力せよ。なお、プログラムの実行中に 43 行以上の行を保持してはなら ない。
"""


def main():
    fn = 'input_random_empty_1s.txt'
    word_list = []
    with open(fn) as f:
        for line in f:
            if line.rstrip() == '' and len(word_list) == 42:
                print(word_list[0])
            if len(word_list) == 42:
                word_list.pop(0)
            word_list.append(line.rstrip())


if __name__ == '__main__':
    main()
