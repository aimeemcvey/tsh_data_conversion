# TSH_test.py
import json


def read_txt():
    with open("sample_data.txt", "r+") as f:
        lines = f.readlines()
    patient_data = list()
    for line in lines:
        words = line.rstrip()
        patient_data.append(words)
        #f1 = lines[0]
        #print(lines.index(line))
    print(patient_data)

    # name, age, gender, TSH: numbers


if __name__ == "__main__":
    read_txt()
