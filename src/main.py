from numpy.random import randint
from .script.tools import compare_guess
import argparse

class number_guesser_game():
    def __init__(self, args):
        self.args = args
    def main(self):
        random_num = randint(self.args.MinRange,self.args.max_range)
        compare_guess(random_num)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-MinRange", "--MinRange", default=1, required=False, type=int, dest="MinRange")
    parser.add_argument("-MaxRange", "--MaxRange", default=100, required=False, type=int, dest="MaxRange")

    args = parser.parse_args()
    number_guesser_game(args).main()