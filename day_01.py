import sys
#very hax, such bad

with open(sys.argv[1], 'r') as fh:
    input = fh.read()
input = [int(i.strip()) for i in input.splitlines()]

# Part 1
print(sum([int(m/3) - 2 for m in input]))

# Part 2
def _get_req(mass):
    print(mass)
    res = int(mass/3) - 2
    if res <= 0:
        return mass
    return mass + _get_req(res)


print(sum(_get_req(i) - i for i in input))
