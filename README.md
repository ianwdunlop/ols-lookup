# Ontology Lookup

Uses the Ontology Lookup Service from the EBI to discover details abotu a particular ontology.

## How to use

Create a virtual env based on Python 3.13. Other versions may work. If you are using Mac or Linux use pyenv to install 3.13 with
```bash
pyenv install 3.13
pyenv local 3.13
```
```bash
python3 -m venv
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
Run `python -m unittest`.

