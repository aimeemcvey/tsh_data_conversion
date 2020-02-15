# TSH_test.py
import json


def read_txt():
    in_file = open("sample_data.txt", "r")
    in_file.read()
    # name, age, gender, TSH: numbers
    # new_patient.name = new_patient["first name"]
    # print(new_patient.name)
    # in_file.close()


if __name__ == "__main__":
    read_txt()
