import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square", type=int, help="display square of a given number")
parser.add_argument("-v", "--verbose", action="count", default=0)

args = parser.parse_args()
answer = args.square ** 2

if args.verbose >= 2:
    print("square of {} equals {}".format(args.square, answer))
else:
    print(answer)
