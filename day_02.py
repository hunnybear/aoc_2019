#!/usr/bin/env python
import argparse
import copy

INPUT = "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,19,6,23,2,23,6,27,2,6,27,31,2,13,31,35,1,9,35,39,2,10,39,43,1,6,43,47,1,13,47,51,2,6,51,55,2,55,6,59,1,59,5,63,2,9,63,67,1,5,67,71,2,10,71,75,1,6,75,79,1,79,5,83,2,83,10,87,1,9,87,91,1,5,91,95,1,95,6,99,2,10,99,103,1,5,103,107,1,107,6,111,1,5,111,115,2,115,6,119,1,119,6,123,1,123,10,127,1,127,13,131,1,131,2,135,1,135,5,0,99,2,14,0,0\n"

TESTS = {
    '1,0,0,0,99\n': [2, 0, 0, 0, 99],
    '1,1,1,4,99,5,6,0,99\n': [30, 1, 1, 4, 2, 5, 6, 0, 99],
    '1,9,10,3,2,3,11,0,99,30,40,50\n': [3500, 9,10,70,2,3,11,0,99,30,40,50],
    '2,4,4,5,99,0': [2,4,4,5,99,9801]
}

PART_2_TARGET = 19690720


def _stop_operation(a, b):
    raise Operation99('code 99 reached')


operations = {
    1: lambda a, b: a + b,
    2: lambda a, b: a * b,
}


def run(parsed, a=None, b=None):

    program = copy.copy(parsed)

    if a is not None:
        program[1] = a
    if b is not None:
        program[2] = b

    position = 0
    while True:
        operation = program[position]
        if operation == 99:
            break

        res = operations[program[position]](program[program[position + 1]], program[program[position + 2]])
        program[program[position + 3]] = res
        #print(program)

        position += 4

    return(program)

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true')
    args = parser.parse_args()

    if args.test:
        for test, res in TESTS.items():
            parsed_test = [int(val.strip()) for val in test.split(',')]
            print('test: '+ test)
            print('result:')
            print(run(parsed_test))
            print('expected:')
            print(res)

    else:
        parsed = [int(val.strip()) for val in INPUT.split(',')]

        print('part 01:\n')
        print(run(parsed, 12, 2))

        print('part 10:\n')
        result = None
        #print(second_part(parsed))
        for a in range(100):
            for b in range(100):
                res = run(copy.copy(parsed), a, b)
                if res[0] == PART_2_TARGET:
                    result = 100 * a + b
                    break
            else:
                continue
            break

        print(result)


class Operation99(Exception):
    """
    I feel like I should document this.
    """
    pass

if __name__ == '__main__':
    main()
