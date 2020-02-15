# TSH_test.py
import json


def read_txt():
    with open("sample_data.txt", "r+") as f:
        lines = f.readlines()
    patient_data = list()
    for line in lines:
        words = line.rstrip()
        patient_data.append(words)
    single_patient(patient_data)


def single_patient(data_input):
    # name, age, gender, TSH: numbers
    num_lines = len(data_input)-1
    num_patients = int((len(data_input) - 1) / 4)
    new_patient = {}
    patient_number = 0
    line_number = 0
    for line in data_input:
        if line_number % 4 == 0:
            new_patient[patient_number] = {}
            new_patient[patient_number]["name"] = line
        if line_number % 4 == 1:
            new_patient[patient_number]["age"] = line
        if line_number % 4 == 2:
            new_patient[patient_number]["sex"] = line
        if line_number % 4 == 3:
            new_patient[patient_number]["tsh"] = line
            print(new_patient[patient_number])
            patient_number += 1
        line_number = line_number + 1


if __name__ == "__main__":
    read_txt()
