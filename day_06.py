#!/usr/bin/env python3

import argparse
import os.path
import xml.etree.cElementTree as etree

TEST="""COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
"""

TEST2="""COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN
"""


def create_map(orbits):

    all_bodies = set(sum([list(o) for o in orbits], []))

    prospective_root_elements = set(all_bodies)

    parents = {}

    for parent, child in orbits:
        prospective_root_elements.remove(child)
        assert child not in parents
        parents[child] = parent

    assert len(prospective_root_elements) == 1
    root = next(iter(prospective_root_elements))

    assert (all_bodies - set([root])) == set(parents)


    return parents, root


def _get_parents_iter(body, orbit_map):

    while orbit_map.get(body):
        body = orbit_map[body]
        yield body

_get_parents = lambda body, orbit_map: list(_get_parents_iter(body, orbit_map))


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('input_here')

    args = parser.parse_args()

    if os.path.isfile(args.input_here):
        with open(args.input_here) as fh:
            input_val = fh.read().strip()
    elif args.input_here == 'test':
        input_val = TEST
    elif args.input_here == 'test2':
        input_val = TEST2
    else:
        input_val = args.input_here.strip()

    orbits = set([tuple(obj for obj in orbit.strip().split(')')) for orbit in input_val.splitlines()])

    orbit_map, root = create_map(orbits)

    transfers = {}

    for parent, child in orbits:
        transfers.setdefault(parent, set()).add(child)
        transfers.setdefault(child, set()).add(parent)

    if input_val != TEST2:
        # part 1 answer
        print(sum(len(_get_parents(body, orbit_map)) for body in orbit_map))

    if input_val != TEST:
        branches = sorted([_get_parents('SAN', orbit_map), _get_parents('YOU', orbit_map)], key=lambda x: len(x))
        print(branches)

        common_ancestor = next(body for body in branches[0] if body in branches[1])

        ancestor_parents = len(_get_parents(common_ancestor, orbit_map))
        santa_parents = len(_get_parents('SAN', orbit_map))
        me_parents = len(_get_parents('YOU', orbit_map))

        print('Common ancestor: {}'.format(common_ancestor))
        print('Common parents: {}, Me parents: {}, Santa parents: {}'.format(ancestor_parents, me_parents, santa_parents))

        print((me_parents + santa_parents - (ancestor_parents * 2)) + 1)






if __name__ == '__main__':
    main()
