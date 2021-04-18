import unittest
from unittest import TestCase
import json
import requests

base_url = "https://remoteproject.hauntedvideosvi.repl.co"

class TestBookDB(TestCase):
    def get_count_api(self):
        """Test case for count API."""
        expected_output = {
                          "books": [
                            {
                              "author": "Yvonne Vera", 
                              "authors": "Yvonne Vera, Yvonne Vera", 
                              "dimensions": "5.07 (w) x 7.78 (h) x 0.42 (d)", 
                              "id": 1, 
                              "isbn10": "435910108", 
                              "isbn13": "9.78044E+12", 
                              "lexile": "", 
                              "pages": "186", 
                              "price": "$14.52", 
                              "publisher": "Heinemann", 
                              "pubyear": "1999", 
                              "subjects": "General & Miscellaneous Literature Anthologies, Anthologies", 
                              "title": "Opening Spaces: An Anthology of Contemporary African Women's Writing"
                            }
                          ]
                        }
        url = base_url + "/show?count=1"
        header = {'Content-Type': 'application/json'}
        res = requests.get(url, headers=header).json()
        self.assertEqual(res, expected_output)

    def test_find_api(self):
        """Test case for find API."""
        expected_output =  {
                          "books": [
                            {
                              "author": "Yvonne Vera", 
                              "authors": "Yvonne Vera, Yvonne Vera", 
                              "dimensions": "5.07 (w) x 7.78 (h) x 0.42 (d)", 
                              "id": 1, 
                              "isbn10": "435910108", 
                              "isbn13": "9.78044E+12", 
                              "lexile": "", 
                              "pages": "186", 
                              "price": "$14.52", 
                              "publisher": "Heinemann", 
                              "pubyear": "1999", 
                              "subjects": "General & Miscellaneous Literature Anthologies, Anthologies", 
                              "title": "Opening Spaces: An Anthology of Contemporary African Women's Writing"
                            }
                          ]
                        }
        url = base_url + "/find"
        body = {"authors": "Yvonne Vera, Yvonne Vera"}
        header = {'Content-Type': 'application/json'}
        res = requests.post(url, json=body, headers=header).json()
        self.assertEqual(res, expected_output)

def suite():
        """Function for run testcase."""
        suite = unittest.TestSuite()
        suite.addTest(TestBookDB('get_count_api'))
        suite.addTest(TestBookDB('test_find_api'))
        return suite

result = unittest.TextTestRunner(verbosity=2).run(suite())
failures = [str(each[0]) + str(each[1]) for each in result.failures]
errors = [str(each[0]) + str(each[1]) for each in result.errors]
final_result = json.dumps({"test passed": result.testsRun, "failures": len(failures), "errors": len(errors)})
