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