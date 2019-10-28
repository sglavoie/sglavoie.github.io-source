Title: Binary to Decimal, Decimal to Binary Converter
Date: 2019-02-18 21:30
Tags: computer science, mathematics, python, script
Slug: binary-to-decimal-decimal-to-binary-converter
Authors: Sébastien Lavoie
Summary: As part of a [course on the mathematics of Computer Science](https://www.coursera.org/learn/mathematics-for-computer-science/), I had to come up with algorithms to convert binary numbers to decimal numbers and vice versa. 
Description: As part of a course on the mathematics of Computer Science, I had to come up with algorithms to convert binary numbers to decimal numbers and vice versa. 


There is nothing new here in terms of algorithms, but it was interesting
to figure out how to apply those concepts with Python. This works for
integer numbers, but can be easily adapted to convert fractions.

### Binary to Decimal

~~~~{.python}
"""
Converts a binary number to a decimal number.
"""


def bin_to_dec(number):
    """Algorithm that converts a binary number to a decimal number.

    Receives and returns a string."""

    # get the index of power of first digit
    # e.g. 1001 → first index power is 3 (2^3)
    first_power = len(number) - 1

    total = 0  # initialize variable to store final result

    # iterate over each number and if it is '1', calculate the value
    # based on its position and add it to the total
    for index, char in enumerate(number):
        if char == '1':
            total += 2 ** (first_power - index)

    # give back the answer to the script
    return total


if __name__ == '__main__':
    # retrieve binary number from input as string to parse
    BIN_NUM = input()

    # pass binary number to algorithm and store the result
    RESULT = bin_to_dec(BIN_NUM)

    # print the solution to the console
    print(RESULT)
~~~~


### Decimal to Binary

~~~~{.python}
"""
Converts a decimal number to a binary number.
"""


def dec_to_bin(number):
    """Algorithm that converts a decimal number to a binary number.

    Receives an integer and returns a string."""

    if number == 0:  # if number is 'zero', the answer is 'zero'
        return 0

    remainders = []  # list that stores the remainders

    # iterate over the initial given decimal and divide it by two
    # until it gets to 'zero'. At each step, add the remainder in
    # the above list
    while number > 0:
        remainders.append(number % 2)
        number = number // 2

    # reverse the list of remainders, as the first remainder is the
    # right most digit in the answer
    remainders.reverse()

    # concatenate all the digits from the list of remainders from left
    # to right to display the final binary number
    answer = ''
    for digit in remainders:
        answer += str(digit)

    # give the answer back to the script
    return answer


if __name__ == '__main__':
    # retrieve decimal number from input as integer
    DEC_NUM = int(input())

    # pass decimal number to algorithm and store the result
    RESULT = dec_to_bin(DEC_NUM)

    # print the solution to the console
    print(RESULT)
~~~~


## Conclusion

This was a very quick programming session that's been useful
to make new concepts stick. The best learning strategies are
to _test yourself_ constantly in any way possible and to
_teach clearly what you know_, which is what I tried to do
in the end. By the way, I found the course [Learning How to
Learn](https://www.coursera.org/learn/learning-how-to-learn/) on
Coursera to be quite satisfying and I would invite you to have a look if
that's a topic you're interested in!
