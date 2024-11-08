import unittest
from unittest.mock import patch
import requests_mock

from src.ols_lookup import get_ontology_details, display_ontology_info

class TestOntologyLookup(unittest.TestCase):

    def test_successful_fetch(self):
        with requests_mock.Mocker() as m:
            m.get("https://www.ebi.ac.uk/ols/api/ontologies/efo", json={
                "config": {
                    "id": "efo",
                    "title": "Experimental Factor Ontology",
                    "description": "An ontology of experimental factors"
                },
                "numberOfTerms": 1000,
                "status": "LOADED"
            })

            result = get_ontology_details("efo")
            self.assertIsNotNone(result)
            self.assertEqual(result['config']['id'], 'efo')
            self.assertEqual(result['config']['title'], 'Experimental Factor Ontology')

    def test_failed_fetch(self):
        with requests_mock.Mocker() as m:
            m.get("https://www.ebi.ac.uk/ols/api/ontologies/nonexistent", status_code=404)

        result = get_ontology_details("nonexistent")
        self.assertIsNone(result)

    def test_display_ontology_info(self):
        ontology_details = {
            "config": {
                    "id": "efo",
                    "title": "Experimental Factor Ontology",
                    "description": "An ontology of experimental factors"
                },
                "numberOfTerms": 1000,
                "status": "LOADED"
        }

        with unittest.mock.patch('builtins.print') as mock_print:
            display_ontology_info(ontology_details)

            mock_print.assert_has_calls([
                unittest.mock.call("Ontology ID: efo"),
                unittest.mock.call("Full Title: Experimental Factor Ontology"),
                unittest.mock.call("Description: An ontology of experimental factors"),
                unittest.mock.call("Number of terms: 1000"),
                unittest.mock.call("Current status: LOADED")
            ])

if __name__ == '__main__':
    unittest.main()