#!/usr/bin/env python

"""You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the password on a sticky note, but someone threw it out.

However, they do remember a few key facts about the password:

It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
Other than the range rule, the following are true:

111111 meets these criteria (double 11, never decreases).
223450 does not meet these criteria (decreasing pair of digits 50).
123789 does not meet these criteria (no double)."""

INPUT = "264793-803935"


def part_01():

    min, max = (int(i) for i in INPUT.split('-'))
    matching = []

    for test in range(min, max + 1):
        test_str = str(test)
        if not [a for i, a in enumerate(test_str[:-1]) if test_str[i + 1] == a]:
            continue
        if any(int(test_str[i]) > int(test_str[i + 1]) for i in range(5)):
            continue

        matching.append(test)

    return len(matching)



def main():

    print(part_01())

if __name__ == '__main__':
    main()
