import unittest
from unittest.mock import patch
from se_requests import *
import json


class TestRequest(unittest.TestCase):
    def test_request_for_user(self):
        with open("physics_questions.json", "r") as info_dict_file:
            fake_json = json.load(info_dict_file)
        with patch("requests.get") as mocked_get:
            mocked_get.return_value.json.return_value = fake_json


if __name__ == "__main__":
    unittest.main()
