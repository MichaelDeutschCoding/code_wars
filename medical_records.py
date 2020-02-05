import requests
from datetime import datetime

def fetch_records():
    patients = []
    for i in range(1, 11):
        response = requests.get(f'https://jsonmock.hackerrank.com/api/medical_records?page={i}')
        response.raise_for_status()
        serialized = response.json()
        patients.extend(serialized['data'])
    return patients


def calc(patients):
    for patient in patients:
        ts = datetime.utcfromtimestamp(patient['timestamp']//1000)
        dob = datetime.strptime(patient['userDob'], '%d-%m-%Y')
        patient['age'] = (ts -dob).days / 365
        patient['bp_diff'] = patient['vitals']['bloodPressureDiastole'] - patient['vitals']['bloodPressureSystole']


patients = fetch_records()
calc(patients)

def find_records(minAge, maxAge, bpDiff):
    matching = []
    for patient in patients:
        if (minAge <= patient['age'] <= maxAge) and patient['bp_diff'] > bpDiff:
            matching.append(patient['id'])
    return matching