import csv
import os
import pathlib

# DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'

DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']
proj_dir_path = pathlib.Path(__file__).parent.resolve()
DATA_FILE_PATH = os.path.join(proj_dir_path, 'data.csv')

def get_all_user_story():
    
    return DATA_HEADER


def get_csv_data():
    with open(DATA_FILE_PATH) as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            print(row)


print(get_csv_data())