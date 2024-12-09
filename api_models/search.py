import urllib.parse

import requests


class SearchAPI:
    def __init__(self, url, logger):
        self.url = url
        self.logger = logger
        self.request = None
        self.response = None

    def send_request_to_endpoint(self, endpoint, query):
        self.request = f"{self.url}/{endpoint}?q={encode_query(query)}"
        self.send_any_request_with_logging()

    def send_request_for_book_with_title(self, query):
        self.request = f"{self.url}.json?q={encode_query(query)}&fields=title"
        self.send_any_request_with_logging()

    def send_any_request_with_logging(self):
        self.logger.info(f"The request is: {self.request}")
        self.response = requests.get(self.request)

    def check_status_code(self, expected_code):
        if self.response.status_code == int(expected_code):
            return True
        self.logger.error(f"The response code is incorrect. "
                          f"Expected code is {expected_code}, actual code is {self.response.status_code}")
        return False

    def check_number_of_results(self, expected_number):
        results = self.response.json()
        if results["numFound"] == int(expected_number):
            return True
        self.logger.error(f"The number of results in response is incorrect. "
                          f"Expected number is {expected_number}, actual number is {self.response['numFound']}")
        return False

    def check_first_title_in_results(self, expected_title):
        results = self.response.json()
        titles = results["docs"]
        first_title = titles[0]["title"]
        if first_title == expected_title:
            return True
        self.logger.error(f"The first title in response is incorrect. "
                          f"Expected title is {expected_title}, actual title is {first_title}")
        return False


def encode_query(query):
    return urllib.parse.quote_plus(query)
