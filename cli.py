import argparse
import sys
argv=sys.argv[1:]

def build_razb():
    parser=argparse.ArgumentParser(prog='mathtool',allow_abbrev=False)
    subparsers=parser.add_subparsers(dest='command', help='Доступные команды')
    a = subparsers.add_parser('integrate', allow_abbrev=False)
    a.add_argument('--steps',type=int, required=True, help='Щаги')
    a.add_argument('--from',dest='start', required=True, help='Начало интервала')
    a.add_argument('--to',  required=True, help='Конец интервала')
    a.add_argument('--func', type=int, required=True, help='Функция')
    a.add_argument('-a', type=int,  help='Number of steps')
    a.add_argument('-b', type=int, help='Number of steps')
    a.add_argument('-c', type=int, help='Number of steps')
    a.add_argument('--input', type=int, help='Number of steps')


    return parser
if __name__=='__main__':
    parser=build_razb()
    args=parser.parse_args(argv)
    if args.command is None:
        parser.print_help()
        sys.exit(0)
    if args.command == 'integrate':

