import csv
import json
from pathlib import Path
import os
from collections import OrderedDict

# Reason for using Ordered Dictionary
# https://www.geeksforgeeks.org/ordereddict-in-python/

def is_empty_csv(data):
    total_rows = len(data)
    #print(str(total_rows))
    return bool(total_rows == 0)

def parse_to_json(filename,outparam = None):
    current_file = open(os.curdir + '/input/' + filename, 'r')
    if outparam is not None:
        outfile_name = outparam
    else:
        outfile_name = os.path.basename(filename).split('.')[0]
        outfile_name = outfile_name + ".json"

    reader = csv.reader(current_file)
    data = list(reader)

    if is_empty_csv(data):
        print(filename + " is Empty ")
    else:
        header_keys = data[0]
        parsed = []
        for i in range(1, len(data)):
            ord_obj = OrderedDict()
            for j in range(0, len(header_keys)):
                if len(data[i][j]) > 0:
                    ord_obj[header_keys[j]] = data[i][j]
                else:
                    ord_obj[header_keys[j]] = None
            parsed.append(ord_obj)

    if Path('output/').exists():
        try:
            outputfile = open(os.curdir + '/output/' + outfile_name, 'w')
            json.dump(parsed, outputfile)
            outputfile.close()
            print("Success")
        except:
            print("Error: could not create file...")
    else:
        print("Error: Output file does not exist...")

    # Close after processing
    current_file.close()

def test_print_parsed(parsedobj):
    for obj in parsedobj:
        print(obj)
