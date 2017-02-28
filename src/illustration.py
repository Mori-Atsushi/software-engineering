# -*- coding:utf-8 -*-

import various

class Illustration:
    def __init__(self, issueUp, issueLeft):
        self.__issue = various.Issue(issueUp, issueLeft)
        self.__m = len(issueUp[0])
        self.__n = len(issueLeft)
        self.__answer = various.Answer(self.__m, self.__n)

    def calc(self):
        i = 0
        lineM = various.Line(self.__m)
        lineN = various.Line(self.__n)
        while True:
            upFlag = 0
            leftFlag = 0
            for m in range(self.__m):
                issueLine = self.__issue.get(m, 0)
                answerLine = self.__answer.get(m, 0)
                upFlag += lineM.calc(issueLine, answerLine)

            for n in range(self.__n):
                issueLine = self.__issue.get(n, 1)
                answerLine = self.__answer.get(n, 1)
                leftFlag += lineN.calc(issueLine, answerLine)

            self.show()
            print ''

            if upFlag == 0 and leftFlag == 0:
                break

    def show(self):
        self.__answer.show()