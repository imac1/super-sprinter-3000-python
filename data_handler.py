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


def update_csv_data(new_story):
    print(new_story)
    tempfile = NamedTemporaryFile(mode='w', delete=False)
    # TODO check if id exists
    if 'id' in new_story:
        print('id')
        with open(DATA_FILE_PATH, 'r') as csvfile, tempfile:
            reader = csv.DictReader(csvfile, fieldnames=DATA_HEADER)
            writer = csv.DictWriter(tempfile, fieldnames=DATA_HEADER)
            for row in reader:
                if row['id'] == str(new_story['id']):
                    print('update row')
                    writer.writerow(new_story)
                writer.writerow(row)
                csvfile.close()
                tempfile.close()
            shutil.move(tempfile.name, DATA_FILE_PATH)
    else:
        print(new_story)
        header, stories = get_all_user_story()
        new_id = int(stories[-1]['id']) + 1
        print(new_id)
        new_dict = {'id': str(new_id)}
        new_dict.update(new_story)
        print(new_dict)
        with open(DATA_FILE_PATH, 'a') as f:
            writer = csv.DictWriter(f, fieldnames=DATA_HEADER)
            writer.writerow(new_dict)

  


# new_stori = {'title': 'tit', 'user_story': 'w', 'acceptance_criteria': 'good', 'business_value': 'not', 'estimation': 'yesterday', 'status': 'none'}
# print(update_csv_data(new_stori))