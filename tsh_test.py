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
    single_patient(patient_data)


def single_patient(data_input):
    # name, age, gender, TSH: numbers
    name = data_input[0]
    age = data_input[1]
    sex = data_input[2]
    tsh = data_input[3]
    new_patient = {"name": name,
                   "age": age,
                   "sex": sex,
                   "TSH results": tsh}
    print(new_patient)


if __name__ == "__main__":
    read_txt()
