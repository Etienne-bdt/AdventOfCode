import pandas as pd
import numpy as np
import re


def mul(x,y):
    return x*y

def filter_one(sentence, regex_mul, regex_digits):
    result = re.findall(regex_mul, sentence)
    sum=0
    for r in result:
        digits = re.findall(regex_digits, r)
        sum += mul(int(digits[0]), int(digits[1]))

    return sum

def filter_two(sentence, regex_mul, regex_digits, dontdo, final_regex):
    result = re.findall(dontdo, sentence)
    for r in result:
        sentence = sentence.replace(r, "")
    sentence = re.sub(final_regex, "", sentence)

    print(sentence)
    return filter_one(sentence, regex_mul, regex_digits)
    
def main():
    # Part 1
    # Find all the occurences of mul and do_not_mul in the sentence
    # and replace them with the result of the function call
    # The sentence should become:
    # x8%&mul[3,7]!@^9+2048then(88)
    # The result of the function call is the product of the two numbers
    # in the function call
    # You can assume that the function call is always correct
    # and that the numbers are always integers
    # You can use the regex module for this
    # https://docs.python.org/3/library/re.html
    # You can also use the eval function
    # https://docs.python.org/3/library/functions.html#eval
    # You can also use the re.sub function
    # https://docs.python.org/3/library/re.html#re.sub
    # You can also use the re.findall function
    # https://docs.python.org/3/library/re.html#re.findall
    # You can also use the re.split function
    # https://docs.python.org/3/library/re.html#re.split
    # You can also use the re.finditer function
    #load file into a string
    sentence= open("./Day3/file.txt").read()
    regex_mul = "mul\(\d+,\d+\)"
    regex_digits = "\d+"
    final_regex="don't\(\).*"
    sum = filter_one(sentence, regex_mul, regex_digits)
    print(sum)

    regex_dontdo = "don't\(\).*?do\(\)"
    sum2 = filter_two(sentence, regex_mul, regex_digits, regex_dontdo,final_regex)
    print(sum2)


if __name__ == '__main__':
    main()
    
