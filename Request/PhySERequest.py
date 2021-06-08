import requests
import csv

# user_info_physics = (requests.get("https://api.stackexchange.com/2.2/users/690/questions?pagesize=100&order=desc&sort=activity&site=physics")).json()
#user_info_tex = (requests.get("https://api.stackexchange.com/2.2/users/66024/questions?pagesize=100&order=desc&sort=activity&site=tex")).json()


def request_for_questions(user_id, se_site):
    """

    Parameters
    ----------
    user_id : int
        equal 690 for physics.se
        equal 66024 for tex.se
    se_site : string
        physics for physics.se
        tex for TeX.se

    Returns
    -------
    json
        Data about user questions.

    """
    return (requests.get(f"https://api.stackexchange.com/2.2/users/{user_id}/questions?pagesize=100&order=desc&sort=activity&site={se_site}")).json()


def create_user_data_files(user_info, type):
    """

    Parameters
    ----------
    user_info : json
        Data about user questions.
    type : string
                physics for physics.se
        tex for TeX.se

    Returns
    -------
    None.

    Creates
    -------
    .csv-file with user questions (title, link and score)
    """
    csv_user_data_file = open(f"user{type}.csv", "w",
                              newline="", encoding="utf-8")
    writer = csv.writer(csv_user_data_file, delimiter=";")
    writer.writerow(["title", "link", "score"])
    for i in range(len(user_info['items'])):
        writer.writerow([user_info['items'][i]['title'],
                         user_info['items'][i]['link'],
                         user_info['items'][i]['score']])
    csv_user_data_file.close()


user_info_tex = request_for_questions(66024, 'tex')
create_user_data_files(user_info_tex, 'tex')
