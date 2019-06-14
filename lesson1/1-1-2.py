# -*- coding: utf-8 -*-
"""
2. 先頭から 50 行の入力を読み、それを逆順で出力せよ。その後、続く 50 行を読み、それを逆順で出力せよ。これを読み取る行がなくなるまで繰り返し、最後に残った行(50 行未満かもしれない)もやはり逆順で出 力せよ。
つまり、出力は 50 行めから始まり、49 行め、48 行め、...、1 行めが 続く。その次は、100 行め、99 行め、...、51 行めが続く。 なお、プログラムの実行中に 50 行より多くの行を保持してはならない。
"""


def main():
    fn = 'input_1s.txt'
    word_list = []
    with open(fn) as f:
        for line in f:
            word_list.append(line.rstrip())
            if len(word_list) == 50:
                print('\n'.join([i for i in reversed(word_list)]))
                word_list = []


if __name__ == '__main__':
    main()
