import json 

with open('trash_users_and_pages.json', 'r') as file:
	data = json.load(file)

# Remove users with missing names.
for user in data['users']:
	if user['name'] == '':
		data['users'].pop(data['users'].index(user))
# Remove inactive users (users with no friends and no liked pages).
for user in data['users']:
	if user['friends'] == [] and user['liked_pages'] == []:
		data['users'].pop(data['users'].index(user))
# Remove duplicate friend entries.
for user in data['users']:
	if len(user['friends']) != len(set(user['friends'])):
	    data['users'].pop(data['users'].index(user))
# Deduplicate pages based on IDs.
for user in data['users']:
	if len(user['liked_pages']) != len(set(user['liked_pages'])):
	    data['users'].pop(data['users'].index(user))

with open('clean_users_and_pages.json', 'w') as new_file:
	json.dump(data, new_file)
	