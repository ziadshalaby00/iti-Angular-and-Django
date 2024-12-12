################### TASK (1) ###################

from webbrowser import open
import random

def randomUrl() :
    num = random.random()
    list = [
            "https://github.com",
            "https://stackoverflow.com",
            "https://www.freecodecamp.org",
            "https://www.geeksforgeeks.org",
            "https://developer.mozilla.org",
            "https://www.hackerrank.com",
            "https://codepen.io",
            "https://dev.to",
            "https://leetcode.com",
            "https://www.w3schools.com"
        ]
    open(list[int(num * 10)])

randomUrl()

#* File Finished
#* Developed by: Ziad Ahmed Shalaby