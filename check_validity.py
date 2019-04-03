import glob
import sys
import argparse
import pypianoroll as ppr
from tqdm import tqdm


"""
This script checks the validity of all MIDI files. If a MIDI files is faulty
it will be added to a list which is printed in the end. 
"""


def check_validity(path, beat_res):

    test_files = glob.iglob(path + "**/*.mid*", recursive=True)
    nmbr_files = len(list(glob.iglob(path + "**/*.mid*", recursive=True)))
    faulty = []

    for file in tqdm(test_files, total=nmbr_files):
        try:
            ppr.Multitrack(file, beat_resolution=beat_res).get_stacked_pianoroll()
        except:
            faulty.append(file)

    print('Done.')
    if not faulty:
        print("All your MIDI files are valid.")
    else:
        print("These MIDI files are faulty: ")
        print(*faulty, sep="\n")


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Validity Checker')
    parser.add_argument("--file_path", default=None, help='Path to your MIDI files.')
    parser.add_argument("--beat_resolution", default=24, help='Beat resolution to check MIDI files with', type=int)
    args = parser.parse_args()

    if not args.file_path:
        print("You have to set the path to your MIDI files using --file_path flag")
        sys.exit()

    check_validity(args.file_path, args.beat_resolution)