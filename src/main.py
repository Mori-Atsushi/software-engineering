# -*- coding:utf-8 -*-

import illustration
import sys

if __name__ == '__main__':
    issueUp = []
    issueLeft = []

    print '上の出題エリアの情報を書き込んでください'
    while True:
        input = sys.stdin.readline()
        if input == '\n':
            break
        input = input.rstrip()
        issueUp.append(map(lambda data: int(data), input.split()))

    print '左の出題エリアの情報を書き込んでください'
    while True:
        input = sys.stdin.readline()
        if input == '\n':
            break
        input = input.rstrip()
        issueLeft.append(map(lambda data: int(data), input.split()))

    illustration = illustration.Illustration(issueUp, issueLeft)
    print '[Start]'
    illustration.calc()
    print '[Answer]'
    illustration.show()
