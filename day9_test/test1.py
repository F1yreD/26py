# -*- coding: utf-8 -*-
# Author: F1yreD
# Date: 2026-01-15 23:15:40
if __name__ == '__main__':
    a = {'234': 2, '123': 1, '345': 3}
    b = sorted(a.items(), key=lambda x: x[0])
    print(b)

