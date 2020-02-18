# TSH_test.py


def read_txt():
    with open("sample_data.txt", "r+") as f:
        lines = f.readlines()
    patient_data = edit_txt(lines)
    return patient_data


def edit_txt(lines):
    patient_data = list()
    for line in lines:
        words = line.rstrip()
        patient_data.append(words)
    return patient_data


def single_patient(data_input):
    new_patient = {}
    patient_number = 0
    line_number = 0
    for line in data_input:
        if line_number % 4 == 0:
            if line == "END":
                continue
            new_patient[patient_number] = {}
            name = line.split()
            new_patient[patient_number]["First Name"] = name[0]
            new_patient[patient_number]["Last Name"] = name[1]
        if line_number % 4 == 1:
            new_patient[patient_number]["Age"] = int(line)
        if line_number % 4 == 2:
            new_patient[patient_number]["Gender"] = line
        if line_number % 4 == 3:
            cut_line = extract_tsh(line)
            diagnosis = diagnose_tsh(cut_line)
            new_patient[patient_number]["Diagnosis"] = diagnosis
            new_patient[patient_number]["TSH"] = cut_line
            save_json(new_patient[patient_number])
            patient_number += 1
        line_number = line_number + 1


def extract_tsh(line):
    line = line.split(",")
    line.pop(0)  # get rid of TSH
    line = [float(i) for i in line]
    line.sort()
    return line


def diagnose_tsh(line):
    max_val = max(line)
    min_val = min(line)
    if min_val < 1.0:
        diagnosis = "hyperthyroidism"
    elif max_val > 4.0:
        diagnosis = "hypothyroidism"
    elif min_val >= 1.0 and max_val <= 4.0:
        diagnosis = "normal thyroid function"
    return diagnosis


def save_json(patient):
    import json
    first_name = patient.get("First Name")
    last_name = patient.get("Last Name")
    filename = "{}-{}.json" .format(first_name, last_name)
    out_file = open(filename, 'w')
    json.dump(patient, out_file)
    out_file.close


if __name__ == "__main__":
    list_text = read_txt()
    single_patient(list_text)
