import requests
import json
import csv

# user_info_physics = (requests.get("https://api.stackexchange.com/2.2/users/690/questions?pagesize=100&order=desc&sort=activity&site=physics")).json()
user_info_tex = (requests.get("https://api.stackexchange.com/2.2/users/66024/questions?pagesize=100&order=desc&sort=activity&site=tex")).json()


# with open("usertex.json", "r") as user_data_file:
#     user_info_tex = json.load(user_data_file)


def create_user_data_files(user_info, type):
    csv_user_data_file = open(f"user{type}.csv", "w",
                              newline="", encoding="utf-8")
    writer = csv.writer(csv_user_data_file, delimiter=";")
    writer.writerow(["title", "link", "score"])
    for i in range(len(user_info['items'])):
        writer.writerow([user_info['items'][i]['title'],
                         user_info['items'][i]['link'],
                         user_info['items'][i]['score']])
    csv_user_data_file.close()


create_user_data_files(user_info_tex, 'tex')
