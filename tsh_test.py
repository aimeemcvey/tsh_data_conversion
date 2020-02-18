# TSH_test.py


def read_txt(input_txt):
    """Read text file of patient data

    Patient data file contains information for an unspecified
    number of patients, including name, age, gender, and TSH
    test results.

    Args:
        input_txt (.txt): text file of patient data

    Returns:
        list: all patient data without newlines
    """
    with open(input_txt, "r+") as f:
        lines = f.readlines()
    patient_data = edit_txt(lines)
    single_patient(patient_data)
    return patient_data


def edit_txt(lines):
    """Edit text file of patient data to remove \n

    Patient data file contains information for an unspecified
    number of patients with each line of text separated by a
    newline.

    Args:
        lines (list): all patient data

    Returns:
        list: all patient data without newlines
    """
    patient_data = list()
    for line in lines:
        words = line.rstrip()
        patient_data.append(words)
    return patient_data


def single_patient(data_input):
    """Parse patient data into specified categories

    Patient data file must be separated into First Name, Last
    Name, Age, Gender, Diagnosis, and TSH test results.

    Args:
        data_input (list): all patient data

    Returns:
        dict: organized patient data separated by patient
        JSON: categorized data and test results for each patient
    """
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
    return new_patient


def extract_tsh(line):
    """Cleans TSH txt line to remove 'header' and convert data type

    TSH test results include levels of Thyroid Stimulating
    Hormone (TSH) in the blood. Several levels were collected
    for each patient.

    Args:
        line (str): TSH txt file with format "tsh, 1, 2, 3, etc"

    Returns:
        list: TSH test results as list of floats
    """
    line = line.split(",")
    line.pop(0)  # get rid of TSH
    line = [float(i) for i in line]
    line.sort()
    return line


def diagnose_tsh(line):
    """Uses TSH data to diagnose hypo- and hyperthyroidism

    Any test result < 1.0 indicates hyperthyroidism, while any
    test result > 4.0 indicates hypothyroidism. Normal thyroid
    function is defined as all blood TSH levels between
    1.0 and 4.0, inclusive.

    Args:
        line (list): blood TSH levels as floats

    Returns:
        string: TSH diagnosis
    """
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
    """Saves each patient's data in JSON format

    Patient data is saved under 'FirstName-LastName.json'
    format with the following info: First Name (str), Last
    Name (str), Age (int), Gender (str), Diagnosis (str),
    TSH (list of floats).

    Args:
        patient (dict): Patient information separated into keys-value pairs

    Returns:
        JSON: categorized data and test results for each patient
    """
    import json
    first_name = patient.get("First Name")
    last_name = patient.get("Last Name")
    filename = "{}-{}.json" .format(first_name, last_name)
    out_file = open(filename, 'w')
    json.dump(patient, out_file)
    out_file.close


if __name__ == "__main__":
    input_txt = input("Enter .txt filename: ")
    read_txt(input_txt)
