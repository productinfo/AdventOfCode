#!/usr/bin/python3
from __future__ import print_function

def duelGenerator(factor, init_value):
    val = init_value
    while True:
        val = (val*factor)%(2147483647)
        yield val


def generatorA(init_value):
    yield from duelGenerator(16807, init_value)

def generatorB(init_value):
    yield from duelGenerator(48271, init_value)

def generatorA2(init_value):
    for i in duelGenerator(16807, init_value):
        if i%4==0:
            yield i

def generatorB2(init_value):
    for i in duelGenerator(48271, init_value):
        if i%8==0:
            yield i

# That's handy, the Advent of Code gives unittests.
def UnitTest():
    ex_a = 65
    ex_b = 8921
    print("Unit test for Part One.")
    print("First five values of dueling generators are:")
    for _, a, b in zip(range(5), generatorA(ex_a), generatorB(ex_b)):
        print("{a:>10d}  {b:>10d}".format(a=a, b=b))

    ex1=5
    ex2=40000000
    print("First {inp} values gives a result of {res}".format(inp=ex1, res=partOne(ex_a, ex_b, ex1)))
    print("First {inp} values gives a result of {res}".format(inp=ex2, res=partOne(ex_a, ex_b, ex2)))

    print("")
    print("Unit test for Part Two.")
    print("First five values of dueling generators are:")
    for _, a, b in zip(range(5), generatorA2(ex_a), generatorB2(ex_b)):
        print("{a:>10d}  {b:>10d}".format(a=a, b=b))

    ex3=5
    ex4=5000000
    print("First {inp} values gives a result of {res}".format(inp=ex3, res=partTwo(ex_a, ex_b, ex3)))
    print("First {inp} values gives a result of {res}".format(inp=ex4, res=partTwo(ex_a, ex_b, ex4)))


def partOne(in_a, in_b, num=40000000):
    count = 0
    for _, a, b in zip(range(num), generatorA(in_a), generatorB(in_b)):
        if (a%(2**16)) == (b%(2**16)):
            count += 1
    return count

def partTwo(in_a, in_b, num=5000000):
    count = 0
    for _, a, b in zip(range(num), generatorA2(in_a), generatorB2(in_b)):
        if (a%(2**16)) == (b%(2**16)):
            count += 1
    return count

if __name__ == '__main__':
    from argparse import ArgumentParser, FileType

    args = ArgumentParser()
    args.add_argument("-t", "--test", help='Unit tests', action='store_true')
    args.add_argument("in_a", help='Starting value for A', type=int)
    args.add_argument("in_b", help='Starting value for B', type=int)
    options = args.parse_args()

    if options.test:
        UnitTest()
    else:
        print("Answer for part one is : {res}".format(res=partOne(options.in_a, options.in_b)))
        print("Answer for part two is : {res}".format(res=partTwo(options.in_a, options.in_b)))
