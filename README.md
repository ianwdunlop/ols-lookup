# Ontology Lookup

Uses the [Ontology Lookup Service](https://www.ebi.ac.uk/ols4) from the EBI to discover details about a particular ontology.

## How to use

Create a virtual env based on Python 3.13. Other versions may work. If you are using Mac or Linux use pyenv to install 3.13 with
```bash
pyenv install 3.13
pyenv local 3.13
```
```bash
python3 -m venv
```

Install the requirements

```bash
pip install -r requirements.txt
```

Pick the identifer for your favourite ontology eg `efo` and then run
```bash
python -m src/ols_lookup.py
```
Which will ask you to enter the ontology ID

```bash
Enter ontology ID: efo
```

And if successful will return the details

```bash
Ontology ID: efo
Full Title: Experimental Factor Ontology
Description: The Experimental Factor Ontology (EFO) provides a systematic description of many experimental variables available in EBI databases, and for external projects such as the NHGRI GWAS catalogue. It combines parts of several biological ontologies, such as anatomy, disease and chemical compounds. The scope of EFO is to support the annotation, analysis and visualization of data handled by many groups at the EBI and as the core ontology for OpenTargets.org
Number of terms: 57806
Current status: LOADED
```

## Testing
 
```bash
python -m unittest
```

## Extending
The code is contained within `src/ols_lookup.py`. Look at the method `get_ontology_details` to understand how to send a request to the OLS API and `display_ontology_info` to understand how to process the response. Go the the [OLS API docs](https://www.ebi.ac.uk/ols4/help) to view the full set of URLs you can request data from. Add more methods using these same patterns to `src/ols_lookup.py` and accompanying tests to `test\test_ols_lookup.py`.

## Licence

Licensed under the Apache License, version 2.0 <https://www.apache.org/licenses/LICENSE-2.0>.  
See the file `LICENSE.txt` for details.

