import argparse
import re
import sys
import FileManager as Fm
import textwrap


def arg_interface_parameters():
    interface = argparse.ArgumentParser(prog='CSV to JSON converter',formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog=textwrap.dedent("Help Information: \nCase 1: No parameters specified in the program will recursively"
    " load and convert all csv files inside the input folder.\n"
    "Case 2: -i parameter followed by 'somefile.csv' with search for a file name match "
    "and convert it to 'somefile.json' in the output folder.\n"
    "Case 3: -o is specified (eg. -i somefile.csv -o newfile.json) will search"
    "for somefile.csv in the input folder and output the conversion as newfile.json"
    "\nNote: -o parameter must have a associated -i parameter"))

    interface.add_argument('-f', nargs='+', type=str, required=False, help='specify filename with the .csv extension')
    interface.add_argument('-o', nargs='+', type=str, required=False, help='specify output name with the .json extension')
    input_args = interface.parse_args()
    input_parameters = vars(input_args)
    validate_args(input_parameters)

def validate_args(input_parameters):

    # Arg Cases:
    # 1. If no parameters recursively load matching csv files.
    # 2. If -f is specified grab only unique file names.
    # 3. If -f and -o is specified then check the parameters are equal ie. input has a output name 1:1
    # 4. If -o is specified without -f then throw an error.

    if input_parameters['f'] is None and input_parameters['o'] is None:
        print("Loading any CSV files recursively from the input directory...")
        Fm.recursive_load_csv()

    if input_parameters['f'] is not None and input_parameters['o'] is None:
        print("Loading specified CSV file names inside input directory...")
        for filename in input_parameters.get('f'):
            if is_valid_csv_parameter(filename):
                Fm.load_arg_files(filename)
            else:
                print(filename + ": is not valid file name")

    if input_parameters['f'] is not None and input_parameters['o'] is not None:
        if args_size_equal(input_parameters):
            print("Loading CSV files specified inside input directory and passing output file name(s) to loader")
            param_size = len(input_parameters.get('f'))
            for i in range(0,param_size):
                filename = input_parameters.get('f')[i]
                outname = input_parameters.get('o')[i]
                if is_valid_csv_parameter(filename):
                    if is_valid_json_parameter(outname):
                        Fm.load_arg_files(filename, outname)
                    else:
                        print(outname + " is not a valid output name")
                        print("Skipping ...")
                else:
                    print(filename + ": is not valid file name")
        else:
            print("Input and output must have matching pairs")
            print("Exiting...")
            sys.exit()

    if input_parameters['f'] is None and input_parameters['o'] is not None:
        print("Invalid parameters: cannot have an out parameter without specifying an input parameter")
        print("Exiting...")
        sys.exit()

def args_size_equal(input_parameters):
    return len(input_parameters.get('f')) == len(input_parameters.get('o'))

def is_valid_csv_parameter(input_parameter):
    if re.match('\w+(\.csv)$', input_parameter):
        return True
    return False

def is_valid_json_parameter(input_parameter):
    if re.match('\w+(\.json)$', input_parameter):
        return True
    return False

def main():
    arg_interface_parameters()


if __name__ == "__main__":
    main()
