#!/usr/bin/python3

for k in range(ord('a'), ord('z') + 1):
    if chr(k) != 'e' and chr(k) != 'q':
        print('{:c}'.format(k), end='')
