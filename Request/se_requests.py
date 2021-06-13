"""Get API from SE sites and return uder information."""

import requests
import csv
import json
import re


def request_for_questions(user_id, se_site, se_method):
    """Get request for SE and return json dict."""
    se_url = f"https://api.stackexchange.com/2.2/users/{user_id}/{se_method}"

    params = {
        "pagesize": 100,
        "site": f"{se_site}",
        "sort": "activity",
        "order": "desc",
    }

    response = requests.get(se_url, params=params)

    return response.json()


def create_user_info_data_file(info_dict, csv_filename):
    with open(csv_filename, "w", newline="", encoding="utf-8") as csv_file:
        # Create object responsible for converting the user’s data to .csv
        writer = csv.writer(csv_file, delimiter=";")
        info_dict.pop
        # writer.writeheader()
        for data in info_dict["items"]:
            writer.writerow(data)


def create_user_data_file(user_info_dict, type, method):
    """Create user data .csv-file."""
    csv_user_data_file_name = f"user_{type}_{method}.csv"

    with open(
        csv_user_data_file_name, "w", newline="", encoding="utf-8"
    ) as csv_user_data_file:
        # Create object responsible for converting the user’s data to .csv
        writer = csv.writer(csv_user_data_file, delimiter=";")

        se_api_methods = ["questions", "answers", "posts"]

        if method == se_api_methods[0]:
            csv_head_line = ["title", "link", "score"]
        elif method == se_api_methods[1]:
            csv_head_line = ["answer_id", "question_id", "score"]
        elif method == se_api_methods[2]:
            csv_head_line = ["link", "score"]

        # Write head to .csv-file
        writer.writerow(csv_head_line)

        # Write data from user_info.json to .csv
        csv_line = []
        dict_len = len(user_info_dict["items"])
        if dict_len:
            for i in range(dict_len):
                for j in csv_head_line:
                    if j in user_info_dict["items"][i].keys():
                        csv_line.append(user_info_dict["items"][i][j])
                writer.writerow(csv_line)
                csv_line.clear()

    # Cleaning file for LaTeX typesetting
    clean_csv_for_LaTeX(csv_user_data_file_name)


def clean_csv_for_LaTeX(file):
    """Clean file for LaTeX typesetting."""
    # open your csv and read as a text string
    with open(file, "r") as csv_user_data_file:
        csv_text = csv_user_data_file.read()
        # substitute
        new_csv_text = re.sub(
            "&#39;", "'", re.sub('"', "", re.sub(r"\\([\w]+)", r"\1", csv_text))
        )

        # open file and save
    with open(file, "w") as csv_user_data_file:
        csv_user_data_file.write(new_csv_text)


if __name__ == "__main__":

    se_api_methods = ["questions", "posts", "answers"]

    user_id_data = {
        "physics": 690,
        "mathematics": 528313,
        "tex": 66024,
        "chemistry": 12641,
        "stackoverflow": 4908648,
    }

    with open("user_tex_questions.json", "r") as info_dict_file:
        info_dict = json.load(info_dict_file)

    print(info_dict["items"])

    # create_user_info_data_file(info_dict, "user_tex_questions.csv")
