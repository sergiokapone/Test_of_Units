import requests
import csv
import re


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
    return (requests.get(f"https://api.stackexchange.com/2.2/users/{user_id}/questions",
                         params={'pagesize': 100,
                                 'site': f'{se_site}',
                                 'sort': 'activity',
                                 'order': 'desc'})).json()

# with open("usertex.json", "r") as user_data_file:
#     user_info_tex = json.load(user_data_file)


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
    with open(f"user{type}.csv", "w",
              newline="", encoding="utf-8") as csv_user_data_file:

        # Create object responsible for converting the user’s data to .csv
        writer = csv.writer(csv_user_data_file, delimiter=";")

        # Save head to .csv-file
        writer.writerow(["title", "link", "score"])

        # Write data from user_info.json to .csv
        for i in range(len(user_info['items'])):
            writer.writerow([user_info['items'][i]['title'],
                             user_info['items'][i]['link'],
                             user_info['items'][i]['score']])

    # Cleaning file for LaTeX typesetting
    clean_csv_for_LaTeX(f"user{type}.csv")


def clean_csv_for_LaTeX(file):
    """

    Cleaning file for LaTeX typesetting
    """
    # open your csv and read as a text string
    with open(file, 'r') as csv_user_data_file:
        csv_text = csv_user_data_file.read()
        # substitute
        new_csv_text = re.sub("&#39;", "\'",
                              re.sub('\"', "",
                                     re.sub(r"\\([\w]+)", r"\1", csv_text)))
        # open file and save
    with open(file, "w") as csv_user_data_file:
        csv_user_data_file.write(new_csv_text)


if __name__ == "__main__":
    user_id_data = {66024: 'tex', 690: 'physics'}
    for user_id in user_id_data:
        create_user_data_files(
            request_for_questions(user_id, user_id_data[user_id]),
            user_id_data[user_id]
            )
