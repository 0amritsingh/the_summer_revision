import json
with open('users_and_pages.json', 'r') as users_and_pages:
	data = json.load(users_and_pages)

userslist = data['users'] # Users and Their Connections
pageslist = data['pages'] # Pages

print('Users and Their Connections:')
for user in userslist:	
	print(f'{user['name']} (ID: {user['id']}) - Friends: {user['friends']} - Liked Pages: {user['liked_pages']}')
print('\nPages:')
for page in pageslist:
	print(f'{page['id']}: {page['name']}')

# user_map = {u["id"]: u["name"] for u in data["users"]}
# page_map = {p["id"]: p["name"] for p in data["pages"]}
# # print(user_map)
# # print(page_map)
# for user in data["users"]:
#     friends = ", ".join(f"{user_map[fid]} (ID: {fid})" for fid in user["friends"])
#     pages = ", ".join(f"{page_map[pid]} (ID: {pid})" for pid in user["liked_pages"])
#     print(f"{user['name']} (ID: {user['id']})\nFriends: {friends}\nLiked Pages: {pages}\n")
#     # print([f"{user_map[fid]} (ID: {fid})" for fid in user["friends"]])
#     # print([f"{page_map[pid]} (ID: {pid})" for pid in user["liked_pages"]])
