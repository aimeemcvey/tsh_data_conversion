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
            cut_line = extract_tsh(line)
            new_patient[patient_number]["TSH"] = cut_line
            diagnosis = diagnose_tsh(cut_line)
            new_patient[patient_number]["diagnosis"] = diagnosis
            print(new_patient[patient_number])
            patient_number += 1
        line_number = line_number + 1
    # print(new_patient)
    return new_patient


def extract_tsh(line):
    line = line.split(",")
    line.pop(0)  # get rid of TSH
    line = [float(i) for i in line]
    return line


def diagnose_tsh(line):
    max_val = max(line)
    min_val = min(line)
    if min_val < 1.0:
        # print("hyperthyroidism")
        diagnosis = "hyperthyroidism"
    elif max_val > 4.0:
        # print("hypothyroidism")
        diagnosis = "hypothyroidism"
    elif min_val >= 1.0 and max_val <= 4.0:
        # print("normal")
        diagnosis = "normal thyroid function"
    return diagnosis


if __name__ == "__main__":
    read_txt()
