import os
import sys
import CsvJsonParser as csv2json
from pathlib import Path

def load_arg_files(filename,outputname = None):
    if Path('input/').exists():
        File_Found = False;
        for input in Path('input/').iterdir():
            if input.match('input/' + filename):
                print("Found: " + filename)
                File_Found = True;
                print('Loading...')
                csv2json.parse_to_json(filename, outputname)
        if File_Found is False:
            print(filename + " Not Found")
    else:
        print("Input folder missing")
        print("Exiting Program")
        sys.exit()

def recursive_load_csv():
    if Path('input/').exists():
        if len(os.listdir(Path('input/'))) == 0:
            print("Input Directory Empty...")
            print("Exiting...")
            sys.exit()
        for input in Path('input/').rglob('*.csv'):
            print("Found: " + input.name)
            csv2json.parse_to_json(input.name)
    else:
        print("Input folder not found")
        print("Exiting...")
        sys.exit()