# TSH_test.py
import json


def read_txt():
    with open("sample_data.txt", "r+") as f:
        lines = f.readlines()
    patient_data = {}
    length = len(lines)
    for line in lines:
        #f1 = lines[0]
        line = line.rstrip()
        print(line)
    # name, age, gender, TSH: numbers


if __name__ == "__main__":
    read_txt()
