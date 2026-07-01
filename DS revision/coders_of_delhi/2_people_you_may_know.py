import json

with open('massive_data.json', 'r') as file:
# with open('users_and_pages.json', 'r') as file:
	data = json.load(file)

# working only on 1
id_map = {i['id']: data['users'].index(i) for i in data['users']} # here we assumed that id can be different then the index
one = data['users'][0]
ones_friends = one['friends']
most_commons = set()
for i in ones_friends:
	common = set()
	for j in data['users'][id_map[i]]['friends']:
		common.update(set(data['users'][id_map[j]]['friends'])) 
	unique_commons = common.difference(set(ones_friends))
	most_commons.update((unique_commons))
print(most_commons)

# its not completed and also i will not do it because it doesn't matter at all fuck it