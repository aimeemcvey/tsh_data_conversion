# test_tsh_test.py
import pytest


def test_tsh_test_hyper():
    from tsh_test import diagnose_tsh
    answer = diagnose_tsh([0.1, 0.5, 3.0, 1.6, 2.1])
    expected = "hyperthyroidism"
    assert answer == expected


def test_tsh_test_hypo():
    from tsh_test import diagnose_tsh
    answer = diagnose_tsh([4.1, 1.1, 3.0, 1.6, 2.1])
    expected = "hypothyroidism"
    assert answer == expected


@pytest.mark.parametrize("a, expected", [
    ([4.0, 1.0, 3.0, 1.6, 2.1], "normal thyroid function"),
    ([3.6, 1.5, 2.3, 2.0, 4.0], "normal thyroid function"),
    ([1.0, 1.6, 3.5, 1.2, 2.8], "normal thyroid function"),
])
def test_tsh_test_normal(a, expected):
    from tsh_test import diagnose_tsh
    answer = diagnose_tsh(a)
    assert answer == expected


def test_extract_tsh_correct():
    from tsh_test import extract_tsh
    answer = extract_tsh("TSH, 2, 4.0, 3, 5.2, 3.1")
    expected = [2.0, 3.0, 3.1, 4.0, 5.2]
    assert answer == expected


def test_extract_tsh_failed():
    from tsh_test import extract_tsh
    answer = extract_tsh("TSH, 2, 4.0, 3, 5.2, 3.1")
    expected = [4.0, 3.0, 3.1, 2.0, 5.2]
    assert answer != expected


def test_edit_txt():
    from tsh_test import edit_txt
    data_input = ['Joe Smith\n', '35\n', 'Male\n', 'TSH,4.1,6,7\n',
                  'Jane Jones\n', '20\n', 'Female\n', 'TSH,1.3,3.5,2.4\n']
    answer = edit_txt(data_input)
    expected = ['Joe Smith', '35', 'Male', 'TSH,4.1,6,7', 'Jane Jones',
                '20', 'Female', 'TSH,1.3,3.5,2.4']
    assert answer == expected


def test_single_patient_correct():
    from tsh_test import single_patient
    data_input = ['Joe Smith', '35', 'Male', 'TSH,4.1,6,7', 'Jane Jones',
                  '20', 'Female', 'TSH,1.3,3.5,2.4']
    answer = single_patient(data_input)
    expected = {
        0: {'First Name': 'Joe', 'Last Name': 'Smith', 'Age': 35, 'Gender':
            'Male', 'Diagnosis': 'hypothyroidism', 'TSH': [4.1, 6.0, 7.0]},
        1: {'First Name': 'Jane', 'Last Name': 'Jones', 'Age': 20, 'Gender':
            'Female', 'Diagnosis': 'normal thyroid function', 'TSH':
                [1.3, 2.4, 3.5]}}
    assert answer == expected


def test_single_patient_failed():
    from tsh_test import single_patient
    data_input = ['Joe Smith', '35', 'Male', 'TSH,4.1,6,7', 'Jane Jones',
                  '20', 'Female', 'TSH,1.3,3.5,2.4']
    answer = single_patient(data_input)
    expected = {
        0: {'First Name': 'Joe', 'Last Name': 'Smith', 'Age': 35, 'Gender':
            'Male', 'TSH': [4.1, 6.0, 7.0]},
        1: {'First Name': 'Jane', 'Last Name': 'Jones', 'Age': '20', 'Gender':
            'Female', 'Diagnosis': 'normal thyroid function', 'TSH':
                [1.3, 2.4, 3.5]}}
    assert answer != expected
