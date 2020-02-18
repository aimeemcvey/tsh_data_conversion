# TSH Test Data Conversion Assignment
This code reads, analyzes, and stores patient data containing TSH test results for hypothyroidism and hyperthyroidism.

## Overview
The input file contains the following format of information for an unspecified number of patients:
```
FirstName LastName
Age
Gender
TSH, result1, result2, result3, etc
```
The end of the file is marked by a line containing ```END```.

Hyperthyroidism is defined as any test results < 1.0, and hypothyroidism is defined as any test results > 4.0. Normal thyroid function contains all test results within 1.0 and 4.0, inclusive. No patient has conflicting test results, i.e., test results of both hyper- and hypothyroidism.

## Run Instructions
To run this program with the sample file, sample_data.txt, input ```python tsh_test.py``` into the command line. A JSON file will be created for each patient (```FirstName-LastName.json```) with each patient's data in JSON format: ```First Name```, ```Last Name```, ```Age```, ```Gender```, ```Diagnosis```, and ```TSH``` test results.

More information on this assignment can be found at <https://github.com/dward2/BME547/tree/master/Assignments/TSHTestDataConversion>
