#!/usr/bin/env python3
import argparse
import copy
import inspect
import pdb


def output(a):
    print('output: {}'.format(a))
    if a != 0:
        pdb.set_trace()
    return None


def stop_program():
    raise StopProgram()

INPUT_OPERATOR = 3

# First member is callable that returns value and location to put value (if
# applicable), or None if not applicable. Second member is the mode mask, an
# array of truthy and falsy values to or with the mode (to force the write pos
# value to be mode 1 always()
OPERATORS = {
    1: lambda a, b, c: (a + b, c),
    2: lambda a, b, c: (a * b, c),
    3: lambda a: (a, a),
    4: output,
    99: stop_program,
}

TEST1 = [3, 0, 4, 0, 99]
TEST2 = [1002, 4, 3, 4, 33]


def run(parsed, a=None, b=None, program_input=None):

    program = copy.copy(parsed)

    if program_input is not None:
        OPERATORS[INPUT_OPERATOR] = lambda a: (program_input, a)

    if a is not None:
        program[1] = a
    if b is not None:
        program[2] = b

    position = 0

    count = 0

    while True:

        print('iteration {}'.format(count))
        print('zero count: {}'.format(program.count(0)))
        print(program)

        count += 1

        #import pdb
        #pdb.set_trace()

        instruction = program[position]
        opcode = instruction % 100

        try:
            operation = OPERATORS[opcode]
        except KeyError as exc:
            import pdb
            pdb.set_trace()

            raise exc

        arg_count = len(inspect.signature(operation).parameters)

        # Could I just do str(instruction)[-3], [-4], etc, sure. But where would
        # be the fun in that
        modes = [(instruction // (10 ** (n + 2))) % 10 for n in range(arg_count)]
        # opcode 4 (output) only has one parameter, and it must be a reference.
        if modes and (opcode != 4):
            modes[-1] = 1

        # 1 and 0 are the only valid modes
        assert set(modes) <= set([0, 1])

        #import pdb
        #pdb.set_trace()

        try:
            res = operation(*([program[program[position + i + 1] if not modes[i] else position + i + 1] for i in range(arg_count)]))
        except StopProgram:
            print(program)
            raise

        # important that this is after anything that uses it, but before
        # anything that might `continue`
        position += arg_count + 1

        if res is None:
            continue

        val, val_pos = res

        program[val_pos] = val


    return(program)


class StopProgram(StopIteration):
    pass


def parse_input(input_val):
    parsed = [int(val.strip()) for val in input_val.split(',')]

    return parsed

