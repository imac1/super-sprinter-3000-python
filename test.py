import data_handler
import csv
new = {'title': 't', 'user_story': 'w', 'acceptance_criteria': 'good', 'business_value': 'not', 'estimation': 'yesterday', 'status': 'none'}

header, stories = data_handler.get_all_user_story()

id = 5
# last_item = stories[-1]
# print(last_item['id'])
# new_id = int(stories[-1]['id']) + 1
# new_dict = {'id': str(new_id)}
# new_dict.update(new)
# print(new_dict)
# with open(data_handler.DATA_FILE_PATH, 'a') as f:
#     writer = csv.DictWriter(f, fieldnames=data_handler.DATA_HEADER)
#     writer.writerow(new_dict)
for story in stories:
    if story.get('id') == str(id):
        # print(story.values())
        print(story)
        print(story['title'])
    # for key, value in story.items():
    #     if key == id:
    #         print(value)
        # print(value)
    # print(story.get('id'))

