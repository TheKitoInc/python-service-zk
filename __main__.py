import sys
from app import main
import argparse

parser = argparse.ArgumentParser(description='ZKDevice Proxy Service')
parser.add_argument('host', help='Device Hostname / IP Address')
parser.add_argument('--port', help='Device port', type=int, default=4370)
parser.add_argument('--timeout', help='Connection timeout',
                    type=int, default=5)
parser.add_argument('--password', help='Device password', type=int, default=0)
parser.add_argument(
    '--UDP', action=argparse.BooleanOptionalAction, default=False)
parser.add_argument(
    '--ping', action=argparse.BooleanOptionalAction, default=True)

if __name__ == '__main__':
    sys.exit(main(parser.parse_args()))
