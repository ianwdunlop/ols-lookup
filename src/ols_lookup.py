# Copyright 2024 Ian Dunlop
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import requests

def get_ontology_details(ontology_id: str) -> dict:
  """
  Fetches details about an ontology from the OLS API.

  Args:
      ontology_id (str): The ID of the ontology.

  Returns:
      dict: A dictionary containing the ontology details or None if not found.
  """
  url = f"https://www.ebi.ac.uk/ols/api/ontologies/{ontology_id}"
  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for non-200 status codes
    return response.json()
  except requests.exceptions.RequestException as e:
    print(f"Error fetching ontology details: {e}")
    return None

def display_ontology_info(ontology_details: dict):
  """
  Prints the ontology details in a human-readable format.

  Args:
      ontology_details (dict): A dictionary containing the ontology details.
  """
  if not ontology_details:
    print("No ontology details were found in the input.")
    return

  print(f"Ontology ID: {ontology_details['config']['id']}")
  print(f"Full Title: {ontology_details['config']['title']}")
  print(f"Description: {ontology_details['config']['description']}")
  print(f"Number of terms: {ontology_details['numberOfTerms']}")
  print(f"Current status: {ontology_details['status']}")


if __name__ == "__main__":
  """
  Allows user to enter ontology id from standard input. Fetches ontology and displays results.
  """
  ontology_id = input("Enter ontology ID: ")
  ontology_details = get_ontology_details(ontology_id)
  display_ontology_info(ontology_details)