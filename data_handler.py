import csv
import os
import pathlib
from tempfile import NamedTemporaryFile
import shutil

# DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'

DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']
proj_dir_path = pathlib.Path(__file__).parent.resolve()
DATA_FILE_PATH = os.path.join(proj_dir_path, 'data.csv')


def get_all_user_story():
    stories_list = []
    with open(DATA_FILE_PATH) as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            stories_list.append(row)
  
    return DATA_HEADER, stories_list


def update_csv_data():
    tempfile = NamedTemporaryFile(mode='w', delete=False)
    # TODO check if id exists
    id_list = []
    new_data = {'id': '2', 'title': 't', 'user_story': 'w', 'acceptance_criteria': 'good', 'business_value': 'not', 'estimation': 'yesterday', 'status': 'none'}
    with open(DATA_FILE_PATH, 'r') as csvfile, tempfile:
        reader = csv.DictReader(csvfile, fieldnames=DATA_HEADER)
        writer = csv.DictWriter(tempfile, fieldnames=DATA_HEADER)
        for row in reader:
            if row['id'] == str(new_data['id']):
                print('update row')
                writer.writerow(new_data)
            writer.writerow(row)

    shutil.move(tempfile.name, DATA_FILE_PATH)


# print(get_all_user_story())


