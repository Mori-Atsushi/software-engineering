# -*- coding:utf-8 -*-

import sys
import numpy as np
import copy

class IssueCell:
    def __init__(self, data):
        self.__data = data

    def get(self):
        return self.__data

class Issue:
    def __init__(self, issueUp, issueLeft):
        self.__up = np.array(map(lambda line:map(lambda data:IssueCell(data), line), issueUp))
        self.__left = np.array(map(lambda line:map(lambda data:IssueCell(data), line), issueLeft))

    def get(self, target, flag):
        if flag == 0:
            return self.__up[:, target]
        else:
           return self.__left[target, :]

class AnswerCell:
    def __init__(self):
        self.__label = ['  ', 'x ', '\x1b[40m  \x1b[49m']
        self.__data = 0

    def get(self):
        return self.__data

    def getString(self):
        return self.__label[self.get()]

    def set(self, data):
        self.__data = data

class Answer:
    def __init__(self, m, n):
        npdata = np.empty((n, m))
        self.__data = np.array(map(lambda line:map(lambda cell:AnswerCell(), line), npdata))

    def show(self):
        for line in self.__data:
            print '|',
            for item in line:
                sys.stdout.write(item.getString())
            print '|'

    def get(self, target, flag):
        if flag == 0:
            return self.__data[:, target]
        else:
            return self.__data[target, :]

class Line:
    def __init__(self, num):
        npdata = np.empty(num)
        answer = np.array(map(lambda cell:AnswerCell(), npdata))
        self.__candidateInit = self.__candidate(answer, True)

    def calc(self, issueLine, answerLine):
        sum = 0
        candidate = self.__candidate(answerLine)
        match = filter(lambda line:self.__match(line, issueLine), candidate)
        confirm = self.__confirm(match)
        for i in range(len(answerLine)):
            if answerLine[i].get() != confirm[i].get():
                answerLine[i] = confirm[i]
                sum += 1

        return sum

    def __candidate(self, answerLine, force=False):
        candidateArray = []
        sum = 0
        for cell in answerLine:
            sum += cell.get()
        if sum == 0 and not force:
            return self.__candidateInit

        for cell in answerLine:
            if cell.get() == 0:
                cell.set(1)
                duplicate = map(lambda cell:copy.deepcopy(cell), answerLine)
                candidateArray += self.__candidate(duplicate)
                cell.set(2)
                duplicate = map(lambda cell:copy.deepcopy(cell), answerLine)
                candidateArray += self.__candidate(duplicate)
                cell.set(0)
                return candidateArray

        return [answerLine]

    def __match(self, line, issueLine):
        ans = [0]
        for cell in line:
            if cell.get() == 2:
                ans[-1] += 1
            elif cell.get() == 1 and ans[-1] != 0:
                ans.append(0)

        ans = filter(lambda data: data != 0, ans)
        issue = map(lambda cell: cell.get(), issueLine)
        issue = filter(lambda data: data != 0, issue)
        return ans == issue

    def __confirm(self, match):
        temp = copy.deepcopy(match[0])
        for line in match:
            for i in range(len(line)):
                if temp[i].get() != line[i].get():
                    temp[i].set(0)
        return temp