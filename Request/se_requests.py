"""Get API from SE sites and return uder information."""

import requests
import pandas as pd
import re


def request_for_questions(user_id, se_site, se_method):
    """Get request for SE and return pandas data frame dict."""
    se_url = f"https://api.stackexchange.com/2.2/users/{user_id}/{se_method}"

    params = {
        "pagesize": 100,
        "site": f"{se_site}",
        "sort": "activity",
        "order": "desc",
    }

    response = requests.get(se_url, params=params)

    info_dict = response.json()

    info_pandas = pd.DataFrame(info_dict['items'])

    return info_pandas


def info_csv(se_site, se_method):
    """Create .csv-file from site request."""

    user_id_data = {
        "physics": 690,
        "mathematics": 528313,
        "tex": 66024,
        "chemistry": 12641,
        "stackoverflow": 4908648,
    }

    info = request_for_questions(user_id_data[se_site], se_site, se_method)

    if se_method == 'questions':
        info = info[['link', 'title', 'score']]
    elif se_method == 'answers':
        info = info[['answer_id', 'question_id', 'score']]
    elif se_method == 'posts':
        info = info[['post_id', 'link', 'score']]

    file_name = f'{se_site}_{se_method}.csv'
    info.to_csv(file_name, index=False, sep=";")
    clean_csv_for_LaTeX(file_name)


def clean_csv_for_LaTeX(file):
    """Clean file for LaTeX typesetting."""

    # open your csv and read as a text string
    with open(file, "r") as csv_user_data_file:
        csv_text = csv_user_data_file.read()

        # substitute
        new_csv_text = re.sub("&#39;", "'",
                              re.sub('"', "",
                                     re.sub(r"\\([\w]+)", r"\1",
                                            csv_text)
                                     )
                              )

        # open file and save
    with open(file, "w") as csv_user_data_file:
        csv_user_data_file.write(new_csv_text)


if __name__ == "__main__":

    info_csv('physics', 'questions')

    # with open("user_tex_questions.json", "r") as info_dict_file:
    #     info_dict = json.load(info_dict_file)
