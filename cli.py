import argparse
import sys
from calc.stats import *


argv=sys.argv[1:]

def build_razb():
    parser=argparse.ArgumentParser(prog='mathtool',allow_abbrev=False, description='crmevoe')
    subparsers=parser.add_subparsers(dest='command', help='Доступные команды')
    a = subparsers.add_parser('integrate', allow_abbrev=False)
    a.add_argument('-a', type=int, help='Аргумент а')
    a.add_argument('-b', type=int, help='Аргумент b')
    a.add_argument('-c', type=int, help='Аргумент с')

    b = subparsers.add_parser('stats', allow_abbrev=False)
    b.add_argument('--steps',type=int, required=True, help='Шаги')
    b.add_argument('--from',dest='start', required=True, help='Начало интервала')
    b.add_argument('--to',  required=True, help='Конец интервала')
    b.add_argument('--func', required=True, help='Функция')
    b.add_argument('--input', dest='vvod',type=str, help='')

    c = subparsers.add_parser('series', allow_abbrev=False)
    ser = c.add_mutually_exclusive_group(required=True)
    ser.add_argument('--terms', type=int)
    ser.add_argument('--eps', type=float)
    return parser








