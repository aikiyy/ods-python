# -*- coding: utf-8 -*-
"""
7. 直前の問題で、重複する行については現れた回数だけ出力するように変 更せよ。
"""


def main():
    fn = 'input_duplicate_1s.txt'
    word_dict = {}
    with open(fn) as f:
        for line in f:
            word_dict[line.rstrip()] = word_dict.get(line.rstrip(), 0) + 1
    sorted_word_dict = dict(sorted(word_dict.items(), key=lambda x: (len(x[0]), x[0])))
    print('\n'.join([k if v == 1 else str(v) for k, v in sorted_word_dict.items()]))


if __name__ == '__main__':
    main()
