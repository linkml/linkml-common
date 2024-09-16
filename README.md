# linkml-common

LinkML Common Modeling Elements and Types (COMET)

## Web Index of Elements

[https://linkml.github.io/linkml-common](https://linkml.github.io/linkml-common)

## Why not schema.org?

The [schema.org](https://schema.org) project is a great resource for high level annotation of web pages and other
resources. LinkML-Common differs from schema.org in a number of ways

* Opinionated
   - schema.org is great for annotating data with minimum fuss
   - LinkML-Common enforces a more constrained data model, and is a *validation-first* framework
* Focused on Science, Technology, Engineering, Mathematics, and Scholarly Communication
    - schema.org has excellent broad coverage of a number of domains
    - LinkML-Common has a focus on science and adjacent domains. There is more emphasis on modeling investigations, 
      and adhering to ontologies such as the [Ontology for Biomedical Investigations](https://obofoundry.org/ontology/obi.html)

## How does it compare to FHIR/OMOP/CDISC

LinkML-Common has a broader remit than healthcare or clinical research data models. However, it is intended
to give broad coverage in these domains, and to be extensible. We aim to provide rigorous computable transformations
between COMET and these models

## How does it compare to Biolink?

Biolink is a Knowledge Graph model that emphasizes shared knowledge entities such as genes, diseases, drugs.
These are largely not modeled to any great extent in COMET, and the idea is that these models can be combined.

## Can I adapt it?

Yes! If you don't like our modeling, the idea is to use [LinkML-Map](https://github.com/linkml/linkml-map)
to profile, extend, and adapt the modeling elements here.

Note that like COMET, LinkML-Transformer is not yet mature and is under active development.

## Do I have to use LinkML?

We also provide Pydantic, OWL, JSON-Schema, and many other representations.

## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
  * [linkml_common](src/linkml_common)
    * [schema](src/linkml_common/schema) -- LinkML schema
      (edit this)
    * [datamodel](src/linkml_common/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests

## Developer Documentation

<details>
Use the `make` command to generate project artefacts:

* `make all`: make everything
* `make deploy`: deploys site
</details>

## Credits

This project was made with
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).
