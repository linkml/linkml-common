-- # Class: "Entity" Description: "A physical, digital, conceptual, or other kind of thing with some common characteristics"
--     * Slot: id Description: 
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: Collection_id Description: Autocreated FK slot
-- # Class: "NamedThing" Description: ""
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "Concept" Description: ""
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "InformationEntity" Description: "An entity that describes some information"
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: describes_id Description: The thing that is being described
-- # Class: "PhysicalDevice" Description: ""
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "Intangible" Description: "An entity that is not a physical object, process, or information"
--     * Slot: id Description: 
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
-- # Class: "Role" Description: ""
--     * Slot: id Description: 
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
-- # Class: "Relationship" Description: ""
--     * Slot: id Description: 
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
-- # Class: "Location" Description: ""
--     * Slot: id Description: 
-- # Class: "PointLocation" Description: ""
--     * Slot: id Description: 
-- # Class: "Observation" Description: "A statement about the state of something"
--     * Slot: id Description: 
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
-- # Class: "Specification" Description: "A specification of a thing"
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "Procedure" Description: "A canonical series of actions conducted in a certain order or manner"
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "MathematicalOperation" Description: "Application of a mathematical operation to one or more inputs to produce one or more outputs"
--     * Slot: id Description: 
-- # Class: "Collection" Description: "A group of things. The collection may be heterogeneous or homogeneous."
--     * Slot: id Description: 
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
-- # Class: "Any" Description: ""
--     * Slot: id Description: 
-- # Class: "Publication" Description: ""
--     * Slot: title Description: The title of the item
--     * Slot: abstract Description: A summary of the item
--     * Slot: rights Description: Information about rights held in and over the item
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "Agent" Description: "Represents an Agent"
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "Person" Description: "Represents a Person"
--     * Slot: primary_email Description: The main email address of a person
--     * Slot: birth_date Description: Date on which a person is born
--     * Slot: age_in_years Description: Number of years since birth
--     * Slot: vital_status Description: living or dead status
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "Organization" Description: "Represents an Organization"
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "AutomatedAgent" Description: "Represents an Automated Agent"
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "LifeEvent" Description: ""
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: starts_at_id Description: 
--     * Slot: ends_at_id Description: 
--     * Slot: happens_at_id Description: 
--     * Slot: has_interval_id Description: 
--     * Slot: has_duration_id Description: 
-- # Class: "CreativeWork" Description: "The most generic kind of creative work, including books, movies, photographs, software programs, etc."
--     * Slot: title Description: The title of the item
--     * Slot: abstract Description: A summary of the item
--     * Slot: rights Description: Information about rights held in and over the item
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "Service" Description: "A service provided by an organization"
--     * Slot: id Description: 
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
-- # Class: "Investigation" Description: ""
--     * Slot: objectives Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "InvestigativeProtocol" Description: ""
--     * Slot: protocols_io_url Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "StudyDesign" Description: ""
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "SampleMaterial" Description: ""
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "InvestigativeProcess" Description: ""
--     * Slot: follows_procedure Description: 
--     * Slot: part_of Description: 
--     * Slot: uses_physical_device Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: starts_at_id Description: 
--     * Slot: ends_at_id Description: 
--     * Slot: happens_at_id Description: 
--     * Slot: has_interval_id Description: 
--     * Slot: has_duration_id Description: 
-- # Class: "SampleCollectionProcess" Description: ""
--     * Slot: material_collected Description: 
--     * Slot: collected_from Description: 
--     * Slot: follows_procedure Description: 
--     * Slot: part_of Description: 
--     * Slot: uses_physical_device Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: starts_at_id Description: 
--     * Slot: ends_at_id Description: 
--     * Slot: happens_at_id Description: 
--     * Slot: has_interval_id Description: 
--     * Slot: has_duration_id Description: 
-- # Class: "SampleProcessing" Description: ""
--     * Slot: follows_procedure Description: 
--     * Slot: uses_physical_device Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: starts_at_id Description: 
--     * Slot: ends_at_id Description: 
--     * Slot: happens_at_id Description: 
--     * Slot: has_interval_id Description: 
--     * Slot: has_duration_id Description: 
-- # Class: "DataGenerationFromSample" Description: ""
--     * Slot: follows_procedure Description: 
--     * Slot: part_of Description: 
--     * Slot: uses_physical_device Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: starts_at_id Description: 
--     * Slot: ends_at_id Description: 
--     * Slot: happens_at_id Description: 
--     * Slot: has_interval_id Description: 
--     * Slot: has_duration_id Description: 
-- # Class: "Dataset" Description: ""
--     * Slot: title Description: The title of the item
--     * Slot: abstract Description: A summary of the item
--     * Slot: rights Description: Information about rights held in and over the item
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "BuiltEnvironmentFeature" Description: ""
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "Facility" Description: ""
--     * Slot: located_at_place Description: The place where the entity is located
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "Building" Description: ""
--     * Slot: located_at_place Description: The place where the entity is located
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "BuiltSystem" Description: ""
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "HealthcareSite" Description: ""
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: address_id Description: 
--     * Slot: geolocation_id Description: The geolocation of the place
--     * Slot: bounding_coordinates_id Description: The bounding coordinates of the place
-- # Class: "HealthcareEncounter" Description: "An interaction between a patient and one or more healthcare providers"
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: patient_id Description: 
--     * Slot: provider_id Description: 
--     * Slot: starts_at_id Description: 
--     * Slot: ends_at_id Description: 
--     * Slot: happens_at_id Description: 
--     * Slot: has_interval_id Description: 
--     * Slot: has_duration_id Description: 
-- # Class: "HealthcareOrganization" Description: "An organization that provides healthcare services"
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "HealthcareRole" Description: ""
--     * Slot: id Description: 
--     * Slot: is_person Description: 
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
-- # Class: "HealthcareProvider" Description: ""
--     * Slot: id Description: 
--     * Slot: speciality Description: 
--     * Slot: care_site Description: 
--     * Slot: is_person Description: 
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
-- # Class: "HealthcareConditionOccurrence" Description: ""
--     * Slot: observed_during Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: patient_id Description: 
--     * Slot: starts_at_id Description: 
--     * Slot: ends_at_id Description: 
--     * Slot: happens_at_id Description: 
--     * Slot: has_interval_id Description: 
--     * Slot: has_duration_id Description: 
-- # Class: "Patient" Description: ""
--     * Slot: id Description: 
--     * Slot: is_person Description: 
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
-- # Class: "ClinicalCohort" Description: "A group of patients who share a common set of characteristics"
--     * Slot: definition Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "ClinicalCohortDefinition" Description: "A definition of a clinical cohort"
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "ClinicalCohortEnrollment" Description: "An event relating a patient to a clinical cohort"
--     * Slot: cohort Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: patient_id Description: 
--     * Slot: starts_at_id Description: 
--     * Slot: ends_at_id Description: 
--     * Slot: happens_at_id Description: 
--     * Slot: has_interval_id Description: 
--     * Slot: has_duration_id Description: 
-- # Class: "DataStructure" Description: ""
--     * Slot: id Description: 
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
-- # Class: "EngineeringSpecification" Description: ""
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "RawMaterial" Description: ""
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "EngineeringProcess" Description: ""
--     * Slot: follows_procedure Description: 
--     * Slot: part_of Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: starts_at_id Description: 
--     * Slot: ends_at_id Description: 
--     * Slot: happens_at_id Description: 
--     * Slot: has_interval_id Description: 
--     * Slot: has_duration_id Description: 
-- # Class: "EngineeringMaterialProcessing" Description: ""
--     * Slot: follows_procedure Description: 
--     * Slot: uses_physical_device Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: starts_at_id Description: 
--     * Slot: ends_at_id Description: 
--     * Slot: happens_at_id Description: 
--     * Slot: has_interval_id Description: 
--     * Slot: has_duration_id Description: 
-- # Class: "Equipment" Description: ""
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "Place" Description: "Entities that have a somewhat fixed, physical extension."
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: address_id Description: 
--     * Slot: geolocation_id Description: The geolocation of the place
--     * Slot: bounding_coordinates_id Description: The bounding coordinates of the place
-- # Class: "Landform" Description: "A natural feature of the solid surface of the Earth or other planetary body"
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: address_id Description: 
--     * Slot: geolocation_id Description: The geolocation of the place
--     * Slot: bounding_coordinates_id Description: The bounding coordinates of the place
-- # Class: "PostalAddress" Description: "Represents an Address"
--     * Slot: id Description: 
--     * Slot: street_address Description: The street address
--     * Slot: street_address_additional Description: 
--     * Slot: city Description: The city
--     * Slot: state Description: The state
--     * Slot: postal_code Description: The postal code or zip code
--     * Slot: country Description: The country
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
-- # Class: "GeoPointLocation" Description: ""
--     * Slot: id Description: 
--     * Slot: latitude Description: The latitude of the location
--     * Slot: longitude Description: The longitude of the location
--     * Slot: altitude Description: The altitude of the location
-- # Class: "GeoBoxLocation" Description: ""
--     * Slot: id Description: 
--     * Slot: west_bounding_coordinate Description: The westernmost coordinate of the location
--     * Slot: east_bounding_coordinate Description: The easternmost coordinate of the location
--     * Slot: north_bounding_coordinate Description: The northernmost coordinate of the location
--     * Slot: south_bounding_coordinate Description: The southernmost coordinate of the location
-- # Class: "QuantityKind" Description: ""
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "Quantity" Description: ""
--     * Slot: id Description: 
--     * Slot: has_quantity_kind Description: The kind of quantity
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
-- # Class: "SimpleQuantity" Description: "A quantity is a property that can be measured or counted"
--     * Slot: id Description: 
--     * Slot: value Description: The value of the quantity
--     * Slot: unit Description: 
--     * Slot: has_quantity_kind Description: The kind of quantity
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
-- # Class: "Ratio" Description: "A tuple of two quantities"
--     * Slot: id Description: 
--     * Slot: has_quantity_kind Description: The kind of quantity
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: numerator_id Description: The numerator of the ratio
--     * Slot: denominator_id Description: The denominator of the ratio
-- # Class: "QuantityRange" Description: "A quantity range is a property that can be measured or counted"
--     * Slot: id Description: 
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: lower_bound_id Description: The lower bound of the range
--     * Slot: upper_bound_id Description: The upper bound of the range
-- # Class: "UnitConversionOperation" Description: "A unit conversion operation"
--     * Slot: id Description: 
-- # Class: "UnitConcept" Description: ""
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "MoneyQuantity" Description: "A quantity of money"
--     * Slot: id Description: 
--     * Slot: value Description: The value of the quantity
--     * Slot: unit Description: The currency of the quantity
--     * Slot: has_quantity_kind Description: The kind of quantity
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
-- # Class: "CurrencyConcept" Description: "A currency"
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "FinancialProduct" Description: "A product or service offered by a bank whereby one may deposit, withdraw or transfer money and in some cases be paid interest."
--     * Slot: id Description: 
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
-- # Class: "FinancialAccount" Description: "A bank account"
--     * Slot: id Description: 
--     * Slot: account_number Description: The account number
--     * Slot: bank Description: The bank that holds the account
--     * Slot: account_holder Description: The person or organization that holds the account
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
-- # Class: "PowerPlant" Description: "A facility for generating electrical power"
--     * Slot: plant_type Description: 
--     * Slot: location Description: 
--     * Slot: operator Description: 
--     * Slot: commissioning_date Description: 
--     * Slot: decommissioning_date Description: 
--     * Slot: located_at_place Description: The place where the entity is located
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: capacity_id Description: 
--     * Slot: capex_id Description: Capital expenditure for the plant
--     * Slot: opex_id Description: Operating expense for the plant
-- # Class: "PowerPlantType" Description: "The type of power plant"
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "FossilFuelPlant" Description: "A power plant that uses fossil fuels"
--     * Slot: fuel Description: 
--     * Slot: plant_type Description: 
--     * Slot: location Description: 
--     * Slot: operator Description: 
--     * Slot: commissioning_date Description: 
--     * Slot: decommissioning_date Description: 
--     * Slot: located_at_place Description: The place where the entity is located
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: capacity_id Description: 
--     * Slot: capex_id Description: Capital expenditure for the plant
--     * Slot: opex_id Description: Operating expense for the plant
-- # Class: "NuclearPlant" Description: "A nuclear power plant"
--     * Slot: plant_type Description: 
--     * Slot: location Description: 
--     * Slot: operator Description: 
--     * Slot: commissioning_date Description: 
--     * Slot: decommissioning_date Description: 
--     * Slot: located_at_place Description: The place where the entity is located
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: capacity_id Description: 
--     * Slot: capex_id Description: Capital expenditure for the plant
--     * Slot: opex_id Description: Operating expense for the plant
-- # Class: "RenewablePlant" Description: "A power plant that uses renewable energy sources"
--     * Slot: plant_type Description: 
--     * Slot: location Description: 
--     * Slot: operator Description: 
--     * Slot: commissioning_date Description: 
--     * Slot: decommissioning_date Description: 
--     * Slot: located_at_place Description: The place where the entity is located
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: capacity_id Description: 
--     * Slot: capex_id Description: Capital expenditure for the plant
--     * Slot: opex_id Description: Operating expense for the plant
-- # Class: "HydroelectricPlant" Description: "A hydroelectric power plant"
--     * Slot: dam Description: The dam used by the hydroelectric plant
--     * Slot: plant_type Description: 
--     * Slot: location Description: 
--     * Slot: operator Description: 
--     * Slot: commissioning_date Description: 
--     * Slot: decommissioning_date Description: 
--     * Slot: located_at_place Description: The place where the entity is located
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: capacity_id Description: 
--     * Slot: capex_id Description: Capital expenditure for the plant
--     * Slot: opex_id Description: Operating expense for the plant
-- # Class: "SolarPlant" Description: "A solar power plant"
--     * Slot: plant_type Description: 
--     * Slot: location Description: 
--     * Slot: operator Description: 
--     * Slot: commissioning_date Description: 
--     * Slot: decommissioning_date Description: 
--     * Slot: located_at_place Description: The place where the entity is located
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: capacity_id Description: 
--     * Slot: capex_id Description: Capital expenditure for the plant
--     * Slot: opex_id Description: Operating expense for the plant
-- # Class: "WindFarm" Description: "A wind farm"
--     * Slot: plant_type Description: 
--     * Slot: location Description: 
--     * Slot: operator Description: 
--     * Slot: commissioning_date Description: 
--     * Slot: decommissioning_date Description: 
--     * Slot: located_at_place Description: The place where the entity is located
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: capacity_id Description: 
--     * Slot: capex_id Description: Capital expenditure for the plant
--     * Slot: opex_id Description: Operating expense for the plant
-- # Class: "FossilFuel" Description: "A type of fossil fuel"
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "ElectricalGrid" Description: "A network of electrical transmission lines"
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "Measurement" Description: ""
--     * Slot: id Description: 
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: quantity_measured_id Description: The quantity being measured
--     * Slot: variable_measured_id Description: The variable being measured
-- # Class: "Variable" Description: ""
--     * Slot: id Description: 
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
-- # Class: "Event" Description: "A thing that happens"
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: starts_at_id Description: 
--     * Slot: ends_at_id Description: 
--     * Slot: happens_at_id Description: 
--     * Slot: has_interval_id Description: 
--     * Slot: has_duration_id Description: 
-- # Class: "TimePointOrTemporalInterval" Description: ""
--     * Slot: id Description: 
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: starts_at_id Description: 
--     * Slot: ends_at_id Description: 
-- # Class: "TemporalInterval" Description: "A period of time"
--     * Slot: id Description: 
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: starts_at_id Description: 
--     * Slot: ends_at_id Description: 
-- # Class: "TimePoint" Description: "A point in time. Can be fully specified, or specified in relative terms."
--     * Slot: id Description: 
--     * Slot: year_value Description: 
--     * Slot: date_value Description: 
--     * Slot: time_value Description: 
--     * Slot: datetime_value Description: 
--     * Slot: marker_event Description: 
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: starts_at_id Description: 
--     * Slot: ends_at_id Description: 
-- # Class: "Duration" Description: "A length of time"
--     * Slot: id Description: 
--     * Slot: has_quantity_kind Description: The kind of quantity
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
-- # Class: "TemporalRelationship" Description: "A relationship to another time point"
--     * Slot: id Description: 
--     * Slot: predicate Description: The relationship between the two time points
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: relative_to_id Description: 
-- # Class: "PlannedProcess" Description: "A process that follows a defined procedure or plan"
--     * Slot: follows_procedure Description: 
--     * Slot: uses_physical_device Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: starts_at_id Description: 
--     * Slot: ends_at_id Description: 
--     * Slot: happens_at_id Description: 
--     * Slot: has_interval_id Description: 
--     * Slot: has_duration_id Description: 
-- # Class: "MaterialCollection" Description: ""
--     * Slot: follows_procedure Description: 
--     * Slot: uses_physical_device Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: starts_at_id Description: 
--     * Slot: ends_at_id Description: 
--     * Slot: happens_at_id Description: 
--     * Slot: has_interval_id Description: 
--     * Slot: has_duration_id Description: 
-- # Class: "MaterialProcessing" Description: ""
--     * Slot: follows_procedure Description: 
--     * Slot: uses_physical_device Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: starts_at_id Description: 
--     * Slot: ends_at_id Description: 
--     * Slot: happens_at_id Description: 
--     * Slot: has_interval_id Description: 
--     * Slot: has_duration_id Description: 
-- # Class: "ExtractiveIndustryFacility" Description: "A facility where natural resources are extracted from the earth"
--     * Slot: facility_type Description: 
--     * Slot: operator Description: 
--     * Slot: located_at_place Description: The place where the entity is located
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: production_capacity_id Description: 
--     * Slot: annual_production_id Description: 
--     * Slot: reserves_id Description: 
-- # Class: "MiningFacility" Description: "A facility where mineral resources are extracted from the earth"
--     * Slot: mining_method Description: 
--     * Slot: facility_type Description: 
--     * Slot: operator Description: 
--     * Slot: located_at_place Description: The place where the entity is located
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: depth_id Description: 
--     * Slot: area_id Description: 
--     * Slot: production_capacity_id Description: 
--     * Slot: annual_production_id Description: 
--     * Slot: reserves_id Description: 
-- # Class: "WellFacility" Description: "A facility where fluid resources (e.g., oil, gas, water) are extracted from the earth"
--     * Slot: well_type Description: 
--     * Slot: facility_type Description: 
--     * Slot: operator Description: 
--     * Slot: located_at_place Description: The place where the entity is located
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: depth_id Description: 
--     * Slot: production_capacity_id Description: 
--     * Slot: annual_production_id Description: 
--     * Slot: reserves_id Description: 
-- # Class: "QuarryFacility" Description: "A facility where stone, sand, or gravel are extracted from the earth"
--     * Slot: facility_type Description: 
--     * Slot: operator Description: 
--     * Slot: located_at_place Description: The place where the entity is located
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: production_capacity_id Description: 
--     * Slot: annual_production_id Description: 
--     * Slot: reserves_id Description: 
-- # Class: "ExtractiveIndustryEquipment" Description: "The equipment used in extractive industry operations"
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "ExtractiveIndustryProduct" Description: "A product extracted from an extractive industry facility"
--     * Slot: product_type Description: 
--     * Slot: processing_method Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: ExtractiveIndustryFacility_id Description: Autocreated FK slot
--     * Slot: MiningFacility_id Description: Autocreated FK slot
--     * Slot: WellFacility_id Description: Autocreated FK slot
--     * Slot: QuarryFacility_id Description: Autocreated FK slot
--     * Slot: grade_id Description: 
-- # Class: "ExtractiveIndustryWaste" Description: "Waste material generated from extractive industry operations"
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "EnvironmentalSite" Description: "A location or site that is the subject of environmental monitoring"
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: address_id Description: 
--     * Slot: geolocation_id Description: The geolocation of the place
--     * Slot: bounding_coordinates_id Description: The bounding coordinates of the place
-- # Class: "EnvironmentalProcess" Description: ""
--     * Slot: id Description: 
-- # Class: "EnvironmentalMonitoring" Description: ""
--     * Slot: id Description: 
-- # Class: "FoodRecipe" Description: ""
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "FoodIngredient" Description: ""
--     * Slot: id Description: 
--     * Slot: has_quantity_kind Description: The kind of quantity
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
-- # Class: "FoodProcessing" Description: ""
--     * Slot: follows_procedure Description: 
--     * Slot: uses_physical_device Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: starts_at_id Description: 
--     * Slot: ends_at_id Description: 
--     * Slot: happens_at_id Description: 
--     * Slot: has_interval_id Description: 
--     * Slot: has_duration_id Description: 
-- # Class: "FoodTypeConcept" Description: ""
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "BasicFoodType" Description: ""
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "CompositeFoodType" Description: ""
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "NamedThing_ontology_types" Description: ""
--     * Slot: NamedThing_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "Concept_ontology_types" Description: ""
--     * Slot: Concept_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "InformationEntity_ontology_types" Description: ""
--     * Slot: InformationEntity_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "PhysicalDevice_ontology_types" Description: ""
--     * Slot: PhysicalDevice_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "Specification_ontology_types" Description: ""
--     * Slot: Specification_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "Procedure_ontology_types" Description: ""
--     * Slot: Procedure_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "MathematicalOperation_inputs" Description: ""
--     * Slot: MathematicalOperation_id Description: Autocreated FK slot
--     * Slot: inputs_id Description: The inputs to the operation
-- # Class: "MathematicalOperation_outputs" Description: ""
--     * Slot: MathematicalOperation_id Description: Autocreated FK slot
--     * Slot: outputs_id Description: The outputs of the operation
-- # Class: "MathematicalOperation_parts" Description: ""
--     * Slot: MathematicalOperation_id Description: Autocreated FK slot
--     * Slot: parts_id Description: The parts of the process
-- # Class: "MathematicalOperation_immediate_preceding_steps" Description: ""
--     * Slot: MathematicalOperation_id Description: Autocreated FK slot
--     * Slot: immediate_preceding_steps_id Description: The steps that immediately precede this step
-- # Class: "Publication_creators" Description: ""
--     * Slot: Publication_id Description: Autocreated FK slot
--     * Slot: creators_id Description: The person or organization who created the work
-- # Class: "Publication_contributors" Description: ""
--     * Slot: Publication_id Description: Autocreated FK slot
--     * Slot: contributors_id Description: A person or organization that contributed to the creation of the work
-- # Class: "Publication_contacts" Description: ""
--     * Slot: Publication_id Description: Autocreated FK slot
--     * Slot: contacts_id Description: A contact point for a person or organization
-- # Class: "Publication_keywords" Description: ""
--     * Slot: Publication_id Description: Autocreated FK slot
--     * Slot: keywords Description: Keywords or tags used to describe this item
-- # Class: "Publication_ontology_types" Description: ""
--     * Slot: Publication_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "Agent_ontology_types" Description: ""
--     * Slot: Agent_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "Person_ontology_types" Description: ""
--     * Slot: Person_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "Organization_ontology_types" Description: ""
--     * Slot: Organization_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "AutomatedAgent_ontology_types" Description: ""
--     * Slot: AutomatedAgent_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "LifeEvent_ontology_types" Description: ""
--     * Slot: LifeEvent_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "CreativeWork_creators" Description: ""
--     * Slot: CreativeWork_id Description: Autocreated FK slot
--     * Slot: creators_id Description: The person or organization who created the work
-- # Class: "CreativeWork_contributors" Description: ""
--     * Slot: CreativeWork_id Description: Autocreated FK slot
--     * Slot: contributors_id Description: A person or organization that contributed to the creation of the work
-- # Class: "CreativeWork_contacts" Description: ""
--     * Slot: CreativeWork_id Description: Autocreated FK slot
--     * Slot: contacts_id Description: A contact point for a person or organization
-- # Class: "CreativeWork_keywords" Description: ""
--     * Slot: CreativeWork_id Description: Autocreated FK slot
--     * Slot: keywords Description: Keywords or tags used to describe this item
-- # Class: "CreativeWork_ontology_types" Description: ""
--     * Slot: CreativeWork_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "Investigation_variables" Description: ""
--     * Slot: Investigation_id Description: Autocreated FK slot
--     * Slot: variables_id Description: 
-- # Class: "Investigation_ontology_types" Description: ""
--     * Slot: Investigation_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "InvestigativeProtocol_ontology_types" Description: ""
--     * Slot: InvestigativeProtocol_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "StudyDesign_ontology_types" Description: ""
--     * Slot: StudyDesign_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "SampleMaterial_ontology_types" Description: ""
--     * Slot: SampleMaterial_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "InvestigativeProcess_ontology_types" Description: ""
--     * Slot: InvestigativeProcess_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "SampleCollectionProcess_ontology_types" Description: ""
--     * Slot: SampleCollectionProcess_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "SampleProcessing_ontology_types" Description: ""
--     * Slot: SampleProcessing_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "DataGenerationFromSample_ontology_types" Description: ""
--     * Slot: DataGenerationFromSample_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "Dataset_collected_as_part_of" Description: ""
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: collected_as_part_of_id Description: 
-- # Class: "Dataset_creators" Description: ""
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: creators_id Description: The person or organization who created the work
-- # Class: "Dataset_contributors" Description: ""
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: contributors_id Description: A person or organization that contributed to the creation of the work
-- # Class: "Dataset_contacts" Description: ""
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: contacts_id Description: A contact point for a person or organization
-- # Class: "Dataset_keywords" Description: ""
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: keywords Description: Keywords or tags used to describe this item
-- # Class: "Dataset_ontology_types" Description: ""
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "BuiltEnvironmentFeature_ontology_types" Description: ""
--     * Slot: BuiltEnvironmentFeature_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "Facility_ontology_types" Description: ""
--     * Slot: Facility_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "Building_ontology_types" Description: ""
--     * Slot: Building_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "BuiltSystem_ontology_types" Description: ""
--     * Slot: BuiltSystem_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "HealthcareSite_ontology_types" Description: ""
--     * Slot: HealthcareSite_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "HealthcareEncounter_ontology_types" Description: ""
--     * Slot: HealthcareEncounter_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "HealthcareOrganization_ontology_types" Description: ""
--     * Slot: HealthcareOrganization_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "HealthcareConditionOccurrence_ontology_types" Description: ""
--     * Slot: HealthcareConditionOccurrence_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "ClinicalCohort_ontology_types" Description: ""
--     * Slot: ClinicalCohort_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "ClinicalCohortDefinition_ontology_types" Description: ""
--     * Slot: ClinicalCohortDefinition_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "ClinicalCohortEnrollment_ontology_types" Description: ""
--     * Slot: ClinicalCohortEnrollment_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "EngineeringSpecification_ontology_types" Description: ""
--     * Slot: EngineeringSpecification_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "RawMaterial_ontology_types" Description: ""
--     * Slot: RawMaterial_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "EngineeringProcess_ontology_types" Description: ""
--     * Slot: EngineeringProcess_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "EngineeringMaterialProcessing_ontology_types" Description: ""
--     * Slot: EngineeringMaterialProcessing_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "Equipment_ontology_types" Description: ""
--     * Slot: Equipment_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "Place_ontology_types" Description: ""
--     * Slot: Place_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "Landform_ontology_types" Description: ""
--     * Slot: Landform_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "QuantityKind_ontology_types" Description: ""
--     * Slot: QuantityKind_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "UnitConversionOperation_inputs" Description: ""
--     * Slot: UnitConversionOperation_id Description: Autocreated FK slot
--     * Slot: inputs_id Description: The input unit
-- # Class: "UnitConversionOperation_outputs" Description: ""
--     * Slot: UnitConversionOperation_id Description: Autocreated FK slot
--     * Slot: outputs_id Description: The output unit
-- # Class: "UnitConversionOperation_parts" Description: ""
--     * Slot: UnitConversionOperation_id Description: Autocreated FK slot
--     * Slot: parts_id Description: The parts of the process
-- # Class: "UnitConversionOperation_immediate_preceding_steps" Description: ""
--     * Slot: UnitConversionOperation_id Description: Autocreated FK slot
--     * Slot: immediate_preceding_steps_id Description: The steps that immediately precede this step
-- # Class: "UnitConcept_ontology_types" Description: ""
--     * Slot: UnitConcept_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "CurrencyConcept_ontology_types" Description: ""
--     * Slot: CurrencyConcept_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "PowerPlant_ontology_types" Description: ""
--     * Slot: PowerPlant_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "PowerPlantType_ontology_types" Description: ""
--     * Slot: PowerPlantType_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "FossilFuelPlant_ontology_types" Description: ""
--     * Slot: FossilFuelPlant_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "NuclearPlant_ontology_types" Description: ""
--     * Slot: NuclearPlant_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "RenewablePlant_ontology_types" Description: ""
--     * Slot: RenewablePlant_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "HydroelectricPlant_ontology_types" Description: ""
--     * Slot: HydroelectricPlant_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "SolarPlant_ontology_types" Description: ""
--     * Slot: SolarPlant_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "WindFarm_ontology_types" Description: ""
--     * Slot: WindFarm_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "FossilFuel_ontology_types" Description: ""
--     * Slot: FossilFuel_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "ElectricalGrid_plants" Description: ""
--     * Slot: ElectricalGrid_id Description: Autocreated FK slot
--     * Slot: plants_id Description: 
-- # Class: "ElectricalGrid_ontology_types" Description: ""
--     * Slot: ElectricalGrid_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "Variable_allowed_units" Description: ""
--     * Slot: Variable_id Description: Autocreated FK slot
--     * Slot: allowed_units_id Description: The units that are allowed for this variable
-- # Class: "Event_ontology_types" Description: ""
--     * Slot: Event_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "PlannedProcess_ontology_types" Description: ""
--     * Slot: PlannedProcess_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "MaterialCollection_ontology_types" Description: ""
--     * Slot: MaterialCollection_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "MaterialProcessing_ontology_types" Description: ""
--     * Slot: MaterialProcessing_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "ExtractiveIndustryFacility_ontology_types" Description: ""
--     * Slot: ExtractiveIndustryFacility_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "MiningFacility_ontology_types" Description: ""
--     * Slot: MiningFacility_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "WellFacility_ontology_types" Description: ""
--     * Slot: WellFacility_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "QuarryFacility_ontology_types" Description: ""
--     * Slot: QuarryFacility_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "ExtractiveIndustryEquipment_ontology_types" Description: ""
--     * Slot: ExtractiveIndustryEquipment_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "ExtractiveIndustryProduct_ontology_types" Description: ""
--     * Slot: ExtractiveIndustryProduct_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "ExtractiveIndustryWaste_ontology_types" Description: ""
--     * Slot: ExtractiveIndustryWaste_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "EnvironmentalSite_ontology_types" Description: ""
--     * Slot: EnvironmentalSite_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "FoodRecipe_ingredients" Description: ""
--     * Slot: FoodRecipe_id Description: Autocreated FK slot
--     * Slot: ingredients_id Description: 
-- # Class: "FoodRecipe_steps" Description: ""
--     * Slot: FoodRecipe_id Description: Autocreated FK slot
--     * Slot: steps_id Description: 
-- # Class: "FoodRecipe_ontology_types" Description: ""
--     * Slot: FoodRecipe_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "FoodProcessing_ontology_types" Description: ""
--     * Slot: FoodProcessing_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "FoodTypeConcept_ontology_types" Description: ""
--     * Slot: FoodTypeConcept_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "BasicFoodType_ontology_types" Description: ""
--     * Slot: BasicFoodType_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 
-- # Class: "CompositeFoodType_ontology_types" Description: ""
--     * Slot: CompositeFoodType_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: 

CREATE TABLE "Concept" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id)
);
CREATE TABLE "Intangible" (
	id INTEGER NOT NULL, 
	type TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Role" (
	id INTEGER NOT NULL, 
	type TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Relationship" (
	id INTEGER NOT NULL, 
	type TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Location" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "PointLocation" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Observation" (
	id INTEGER NOT NULL, 
	type TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "MathematicalOperation" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Collection" (
	id INTEGER NOT NULL, 
	type TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Any" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Service" (
	id INTEGER NOT NULL, 
	type TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "DataStructure" (
	id INTEGER NOT NULL, 
	type TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "PostalAddress" (
	id INTEGER NOT NULL, 
	street_address TEXT, 
	street_address_additional TEXT, 
	city TEXT, 
	state TEXT, 
	postal_code TEXT, 
	country TEXT, 
	type TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "GeoPointLocation" (
	id INTEGER NOT NULL, 
	latitude INTEGER, 
	longitude INTEGER, 
	altitude INTEGER, 
	PRIMARY KEY (id)
);
CREATE TABLE "GeoBoxLocation" (
	id INTEGER NOT NULL, 
	west_bounding_coordinate INTEGER, 
	east_bounding_coordinate INTEGER, 
	north_bounding_coordinate INTEGER, 
	south_bounding_coordinate INTEGER, 
	PRIMARY KEY (id)
);
CREATE TABLE "UnitConversionOperation" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "FinancialProduct" (
	id INTEGER NOT NULL, 
	type TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Variable" (
	id INTEGER NOT NULL, 
	type TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Event" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	starts_at_id INTEGER, 
	ends_at_id INTEGER, 
	happens_at_id INTEGER, 
	has_interval_id INTEGER, 
	has_duration_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(starts_at_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(ends_at_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(happens_at_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(has_interval_id) REFERENCES "TemporalInterval" (id), 
	FOREIGN KEY(has_duration_id) REFERENCES "Duration" (id)
);
CREATE TABLE "TemporalInterval" (
	id INTEGER NOT NULL, 
	type TEXT, 
	starts_at_id INTEGER, 
	ends_at_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(starts_at_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(ends_at_id) REFERENCES "TimePoint" (id)
);
CREATE TABLE "TimePoint" (
	id INTEGER NOT NULL, 
	year_value INTEGER, 
	date_value DATE, 
	time_value TIME, 
	datetime_value DATETIME, 
	marker_event TEXT, 
	description TEXT, 
	type TEXT, 
	starts_at_id INTEGER, 
	ends_at_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(marker_event) REFERENCES "Event" (id), 
	FOREIGN KEY(starts_at_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(ends_at_id) REFERENCES "TimePoint" (id)
);
CREATE TABLE "EnvironmentalProcess" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "EnvironmentalMonitoring" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Entity" (
	id INTEGER NOT NULL, 
	type TEXT, 
	"Collection_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Collection_id") REFERENCES "Collection" (id)
);
CREATE TABLE "NamedThing" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id)
);
CREATE TABLE "InformationEntity" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	describes_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(describes_id) REFERENCES "Any" (id)
);
CREATE TABLE "PhysicalDevice" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id)
);
CREATE TABLE "Specification" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id)
);
CREATE TABLE "Procedure" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id)
);
CREATE TABLE "Publication" (
	title TEXT, 
	abstract TEXT, 
	rights TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id)
);
CREATE TABLE "Agent" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id)
);
CREATE TABLE "Person" (
	primary_email TEXT, 
	birth_date DATE, 
	age_in_years INTEGER, 
	vital_status VARCHAR(7), 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id)
);
CREATE TABLE "Organization" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id)
);
CREATE TABLE "AutomatedAgent" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id)
);
CREATE TABLE "CreativeWork" (
	title TEXT, 
	abstract TEXT, 
	rights TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id)
);
CREATE TABLE "Investigation" (
	objectives TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id)
);
CREATE TABLE "InvestigativeProtocol" (
	protocols_io_url TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id)
);
CREATE TABLE "StudyDesign" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id)
);
CREATE TABLE "SampleMaterial" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id)
);
CREATE TABLE "Dataset" (
	title TEXT, 
	abstract TEXT, 
	rights TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id)
);
CREATE TABLE "BuiltEnvironmentFeature" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id)
);
CREATE TABLE "BuiltSystem" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id)
);
CREATE TABLE "HealthcareSite" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	address_id INTEGER, 
	geolocation_id INTEGER, 
	bounding_coordinates_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(address_id) REFERENCES "PostalAddress" (id), 
	FOREIGN KEY(geolocation_id) REFERENCES "GeoPointLocation" (id), 
	FOREIGN KEY(bounding_coordinates_id) REFERENCES "GeoBoxLocation" (id)
);
CREATE TABLE "HealthcareOrganization" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id)
);
CREATE TABLE "ClinicalCohortDefinition" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id)
);
CREATE TABLE "EngineeringSpecification" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id)
);
CREATE TABLE "RawMaterial" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id)
);
CREATE TABLE "Equipment" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id)
);
CREATE TABLE "Place" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	address_id INTEGER, 
	geolocation_id INTEGER, 
	bounding_coordinates_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(address_id) REFERENCES "PostalAddress" (id), 
	FOREIGN KEY(geolocation_id) REFERENCES "GeoPointLocation" (id), 
	FOREIGN KEY(bounding_coordinates_id) REFERENCES "GeoBoxLocation" (id)
);
CREATE TABLE "Landform" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	address_id INTEGER, 
	geolocation_id INTEGER, 
	bounding_coordinates_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(address_id) REFERENCES "PostalAddress" (id), 
	FOREIGN KEY(geolocation_id) REFERENCES "GeoPointLocation" (id), 
	FOREIGN KEY(bounding_coordinates_id) REFERENCES "GeoBoxLocation" (id)
);
CREATE TABLE "QuantityKind" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id)
);
CREATE TABLE "UnitConcept" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id)
);
CREATE TABLE "CurrencyConcept" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id)
);
CREATE TABLE "PowerPlantType" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id)
);
CREATE TABLE "FossilFuel" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id)
);
CREATE TABLE "ElectricalGrid" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id)
);
CREATE TABLE "TimePointOrTemporalInterval" (
	id INTEGER NOT NULL, 
	type TEXT, 
	starts_at_id INTEGER, 
	ends_at_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(starts_at_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(ends_at_id) REFERENCES "TimePoint" (id)
);
CREATE TABLE "ExtractiveIndustryEquipment" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id)
);
CREATE TABLE "ExtractiveIndustryWaste" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id)
);
CREATE TABLE "EnvironmentalSite" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	address_id INTEGER, 
	geolocation_id INTEGER, 
	bounding_coordinates_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(address_id) REFERENCES "PostalAddress" (id), 
	FOREIGN KEY(geolocation_id) REFERENCES "GeoPointLocation" (id), 
	FOREIGN KEY(bounding_coordinates_id) REFERENCES "GeoBoxLocation" (id)
);
CREATE TABLE "FoodRecipe" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id)
);
CREATE TABLE "FoodTypeConcept" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id)
);
CREATE TABLE "BasicFoodType" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id)
);
CREATE TABLE "CompositeFoodType" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id)
);
CREATE TABLE "Concept_ontology_types" (
	"Concept_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("Concept_id", ontology_types_id), 
	FOREIGN KEY("Concept_id") REFERENCES "Concept" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "MathematicalOperation_inputs" (
	"MathematicalOperation_id" INTEGER, 
	inputs_id INTEGER, 
	PRIMARY KEY ("MathematicalOperation_id", inputs_id), 
	FOREIGN KEY("MathematicalOperation_id") REFERENCES "MathematicalOperation" (id), 
	FOREIGN KEY(inputs_id) REFERENCES "Any" (id)
);
CREATE TABLE "MathematicalOperation_outputs" (
	"MathematicalOperation_id" INTEGER, 
	outputs_id INTEGER, 
	PRIMARY KEY ("MathematicalOperation_id", outputs_id), 
	FOREIGN KEY("MathematicalOperation_id") REFERENCES "MathematicalOperation" (id), 
	FOREIGN KEY(outputs_id) REFERENCES "Any" (id)
);
CREATE TABLE "MathematicalOperation_parts" (
	"MathematicalOperation_id" INTEGER, 
	parts_id INTEGER, 
	PRIMARY KEY ("MathematicalOperation_id", parts_id), 
	FOREIGN KEY("MathematicalOperation_id") REFERENCES "MathematicalOperation" (id), 
	FOREIGN KEY(parts_id) REFERENCES "MathematicalOperation" (id)
);
CREATE TABLE "MathematicalOperation_immediate_preceding_steps" (
	"MathematicalOperation_id" INTEGER, 
	immediate_preceding_steps_id INTEGER, 
	PRIMARY KEY ("MathematicalOperation_id", immediate_preceding_steps_id), 
	FOREIGN KEY("MathematicalOperation_id") REFERENCES "MathematicalOperation" (id), 
	FOREIGN KEY(immediate_preceding_steps_id) REFERENCES "MathematicalOperation" (id)
);
CREATE TABLE "UnitConversionOperation_parts" (
	"UnitConversionOperation_id" INTEGER, 
	parts_id INTEGER, 
	PRIMARY KEY ("UnitConversionOperation_id", parts_id), 
	FOREIGN KEY("UnitConversionOperation_id") REFERENCES "UnitConversionOperation" (id), 
	FOREIGN KEY(parts_id) REFERENCES "MathematicalOperation" (id)
);
CREATE TABLE "UnitConversionOperation_immediate_preceding_steps" (
	"UnitConversionOperation_id" INTEGER, 
	immediate_preceding_steps_id INTEGER, 
	PRIMARY KEY ("UnitConversionOperation_id", immediate_preceding_steps_id), 
	FOREIGN KEY("UnitConversionOperation_id") REFERENCES "UnitConversionOperation" (id), 
	FOREIGN KEY(immediate_preceding_steps_id) REFERENCES "MathematicalOperation" (id)
);
CREATE TABLE "Event_ontology_types" (
	"Event_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("Event_id", ontology_types_id), 
	FOREIGN KEY("Event_id") REFERENCES "Event" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "Facility" (
	located_at_place TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(located_at_place) REFERENCES "Place" (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id)
);
CREATE TABLE "Building" (
	located_at_place TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(located_at_place) REFERENCES "Place" (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id)
);
CREATE TABLE "HealthcareRole" (
	id INTEGER NOT NULL, 
	is_person TEXT, 
	type TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(is_person) REFERENCES "Person" (id)
);
CREATE TABLE "HealthcareProvider" (
	id INTEGER NOT NULL, 
	speciality TEXT, 
	care_site TEXT, 
	is_person TEXT, 
	type TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(speciality) REFERENCES "Concept" (id), 
	FOREIGN KEY(care_site) REFERENCES "HealthcareSite" (id), 
	FOREIGN KEY(is_person) REFERENCES "Person" (id)
);
CREATE TABLE "Patient" (
	id INTEGER NOT NULL, 
	is_person TEXT, 
	type TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(is_person) REFERENCES "Person" (id)
);
CREATE TABLE "ClinicalCohort" (
	definition TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(definition) REFERENCES "ClinicalCohortDefinition" (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id)
);
CREATE TABLE "Quantity" (
	id INTEGER NOT NULL, 
	has_quantity_kind TEXT, 
	type TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_quantity_kind) REFERENCES "QuantityKind" (id)
);
CREATE TABLE "SimpleQuantity" (
	id INTEGER NOT NULL, 
	value FLOAT, 
	unit TEXT, 
	has_quantity_kind TEXT, 
	type TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(unit) REFERENCES "UnitConcept" (id), 
	FOREIGN KEY(has_quantity_kind) REFERENCES "QuantityKind" (id)
);
CREATE TABLE "MoneyQuantity" (
	id INTEGER NOT NULL, 
	value FLOAT, 
	unit TEXT, 
	has_quantity_kind TEXT, 
	type TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(unit) REFERENCES "CurrencyConcept" (id), 
	FOREIGN KEY(has_quantity_kind) REFERENCES "QuantityKind" (id)
);
CREATE TABLE "FinancialAccount" (
	id INTEGER NOT NULL, 
	account_number TEXT, 
	bank TEXT, 
	account_holder TEXT, 
	type TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(bank) REFERENCES "Organization" (id), 
	FOREIGN KEY(account_holder) REFERENCES "Person" (id)
);
CREATE TABLE "Duration" (
	id INTEGER NOT NULL, 
	has_quantity_kind TEXT, 
	type TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_quantity_kind) REFERENCES "QuantityKind" (id)
);
CREATE TABLE "TemporalRelationship" (
	id INTEGER NOT NULL, 
	predicate VARCHAR(15), 
	type TEXT, 
	relative_to_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(relative_to_id) REFERENCES "Entity" (id)
);
CREATE TABLE "FoodIngredient" (
	id INTEGER NOT NULL, 
	has_quantity_kind TEXT, 
	type TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_quantity_kind) REFERENCES "QuantityKind" (id)
);
CREATE TABLE "NamedThing_ontology_types" (
	"NamedThing_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("NamedThing_id", ontology_types_id), 
	FOREIGN KEY("NamedThing_id") REFERENCES "NamedThing" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "InformationEntity_ontology_types" (
	"InformationEntity_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("InformationEntity_id", ontology_types_id), 
	FOREIGN KEY("InformationEntity_id") REFERENCES "InformationEntity" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "PhysicalDevice_ontology_types" (
	"PhysicalDevice_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("PhysicalDevice_id", ontology_types_id), 
	FOREIGN KEY("PhysicalDevice_id") REFERENCES "PhysicalDevice" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "Specification_ontology_types" (
	"Specification_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("Specification_id", ontology_types_id), 
	FOREIGN KEY("Specification_id") REFERENCES "Specification" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "Procedure_ontology_types" (
	"Procedure_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("Procedure_id", ontology_types_id), 
	FOREIGN KEY("Procedure_id") REFERENCES "Procedure" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "Publication_creators" (
	"Publication_id" TEXT, 
	creators_id TEXT, 
	PRIMARY KEY ("Publication_id", creators_id), 
	FOREIGN KEY("Publication_id") REFERENCES "Publication" (id), 
	FOREIGN KEY(creators_id) REFERENCES "Agent" (id)
);
CREATE TABLE "Publication_contributors" (
	"Publication_id" TEXT, 
	contributors_id TEXT, 
	PRIMARY KEY ("Publication_id", contributors_id), 
	FOREIGN KEY("Publication_id") REFERENCES "Publication" (id), 
	FOREIGN KEY(contributors_id) REFERENCES "Agent" (id)
);
CREATE TABLE "Publication_contacts" (
	"Publication_id" TEXT, 
	contacts_id TEXT, 
	PRIMARY KEY ("Publication_id", contacts_id), 
	FOREIGN KEY("Publication_id") REFERENCES "Publication" (id), 
	FOREIGN KEY(contacts_id) REFERENCES "Agent" (id)
);
CREATE TABLE "Publication_keywords" (
	"Publication_id" TEXT, 
	keywords TEXT, 
	PRIMARY KEY ("Publication_id", keywords), 
	FOREIGN KEY("Publication_id") REFERENCES "Publication" (id)
);
CREATE TABLE "Publication_ontology_types" (
	"Publication_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("Publication_id", ontology_types_id), 
	FOREIGN KEY("Publication_id") REFERENCES "Publication" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "Agent_ontology_types" (
	"Agent_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("Agent_id", ontology_types_id), 
	FOREIGN KEY("Agent_id") REFERENCES "Agent" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "Person_ontology_types" (
	"Person_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("Person_id", ontology_types_id), 
	FOREIGN KEY("Person_id") REFERENCES "Person" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "Organization_ontology_types" (
	"Organization_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("Organization_id", ontology_types_id), 
	FOREIGN KEY("Organization_id") REFERENCES "Organization" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "AutomatedAgent_ontology_types" (
	"AutomatedAgent_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("AutomatedAgent_id", ontology_types_id), 
	FOREIGN KEY("AutomatedAgent_id") REFERENCES "AutomatedAgent" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "CreativeWork_creators" (
	"CreativeWork_id" TEXT, 
	creators_id TEXT, 
	PRIMARY KEY ("CreativeWork_id", creators_id), 
	FOREIGN KEY("CreativeWork_id") REFERENCES "CreativeWork" (id), 
	FOREIGN KEY(creators_id) REFERENCES "Agent" (id)
);
CREATE TABLE "CreativeWork_contributors" (
	"CreativeWork_id" TEXT, 
	contributors_id TEXT, 
	PRIMARY KEY ("CreativeWork_id", contributors_id), 
	FOREIGN KEY("CreativeWork_id") REFERENCES "CreativeWork" (id), 
	FOREIGN KEY(contributors_id) REFERENCES "Agent" (id)
);
CREATE TABLE "CreativeWork_contacts" (
	"CreativeWork_id" TEXT, 
	contacts_id TEXT, 
	PRIMARY KEY ("CreativeWork_id", contacts_id), 
	FOREIGN KEY("CreativeWork_id") REFERENCES "CreativeWork" (id), 
	FOREIGN KEY(contacts_id) REFERENCES "Agent" (id)
);
CREATE TABLE "CreativeWork_keywords" (
	"CreativeWork_id" TEXT, 
	keywords TEXT, 
	PRIMARY KEY ("CreativeWork_id", keywords), 
	FOREIGN KEY("CreativeWork_id") REFERENCES "CreativeWork" (id)
);
CREATE TABLE "CreativeWork_ontology_types" (
	"CreativeWork_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("CreativeWork_id", ontology_types_id), 
	FOREIGN KEY("CreativeWork_id") REFERENCES "CreativeWork" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "Investigation_variables" (
	"Investigation_id" TEXT, 
	variables_id INTEGER, 
	PRIMARY KEY ("Investigation_id", variables_id), 
	FOREIGN KEY("Investigation_id") REFERENCES "Investigation" (id), 
	FOREIGN KEY(variables_id) REFERENCES "Variable" (id)
);
CREATE TABLE "Investigation_ontology_types" (
	"Investigation_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("Investigation_id", ontology_types_id), 
	FOREIGN KEY("Investigation_id") REFERENCES "Investigation" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "InvestigativeProtocol_ontology_types" (
	"InvestigativeProtocol_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("InvestigativeProtocol_id", ontology_types_id), 
	FOREIGN KEY("InvestigativeProtocol_id") REFERENCES "InvestigativeProtocol" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "StudyDesign_ontology_types" (
	"StudyDesign_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("StudyDesign_id", ontology_types_id), 
	FOREIGN KEY("StudyDesign_id") REFERENCES "StudyDesign" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "SampleMaterial_ontology_types" (
	"SampleMaterial_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("SampleMaterial_id", ontology_types_id), 
	FOREIGN KEY("SampleMaterial_id") REFERENCES "SampleMaterial" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "Dataset_collected_as_part_of" (
	"Dataset_id" TEXT, 
	collected_as_part_of_id TEXT, 
	PRIMARY KEY ("Dataset_id", collected_as_part_of_id), 
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id), 
	FOREIGN KEY(collected_as_part_of_id) REFERENCES "Investigation" (id)
);
CREATE TABLE "Dataset_creators" (
	"Dataset_id" TEXT, 
	creators_id TEXT, 
	PRIMARY KEY ("Dataset_id", creators_id), 
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id), 
	FOREIGN KEY(creators_id) REFERENCES "Agent" (id)
);
CREATE TABLE "Dataset_contributors" (
	"Dataset_id" TEXT, 
	contributors_id TEXT, 
	PRIMARY KEY ("Dataset_id", contributors_id), 
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id), 
	FOREIGN KEY(contributors_id) REFERENCES "Agent" (id)
);
CREATE TABLE "Dataset_contacts" (
	"Dataset_id" TEXT, 
	contacts_id TEXT, 
	PRIMARY KEY ("Dataset_id", contacts_id), 
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id), 
	FOREIGN KEY(contacts_id) REFERENCES "Agent" (id)
);
CREATE TABLE "Dataset_keywords" (
	"Dataset_id" TEXT, 
	keywords TEXT, 
	PRIMARY KEY ("Dataset_id", keywords), 
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);
CREATE TABLE "Dataset_ontology_types" (
	"Dataset_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("Dataset_id", ontology_types_id), 
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "BuiltEnvironmentFeature_ontology_types" (
	"BuiltEnvironmentFeature_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("BuiltEnvironmentFeature_id", ontology_types_id), 
	FOREIGN KEY("BuiltEnvironmentFeature_id") REFERENCES "BuiltEnvironmentFeature" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "BuiltSystem_ontology_types" (
	"BuiltSystem_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("BuiltSystem_id", ontology_types_id), 
	FOREIGN KEY("BuiltSystem_id") REFERENCES "BuiltSystem" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "HealthcareSite_ontology_types" (
	"HealthcareSite_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("HealthcareSite_id", ontology_types_id), 
	FOREIGN KEY("HealthcareSite_id") REFERENCES "HealthcareSite" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "HealthcareOrganization_ontology_types" (
	"HealthcareOrganization_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("HealthcareOrganization_id", ontology_types_id), 
	FOREIGN KEY("HealthcareOrganization_id") REFERENCES "HealthcareOrganization" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "ClinicalCohortDefinition_ontology_types" (
	"ClinicalCohortDefinition_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("ClinicalCohortDefinition_id", ontology_types_id), 
	FOREIGN KEY("ClinicalCohortDefinition_id") REFERENCES "ClinicalCohortDefinition" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "EngineeringSpecification_ontology_types" (
	"EngineeringSpecification_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("EngineeringSpecification_id", ontology_types_id), 
	FOREIGN KEY("EngineeringSpecification_id") REFERENCES "EngineeringSpecification" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "RawMaterial_ontology_types" (
	"RawMaterial_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("RawMaterial_id", ontology_types_id), 
	FOREIGN KEY("RawMaterial_id") REFERENCES "RawMaterial" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "Equipment_ontology_types" (
	"Equipment_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("Equipment_id", ontology_types_id), 
	FOREIGN KEY("Equipment_id") REFERENCES "Equipment" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "Place_ontology_types" (
	"Place_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("Place_id", ontology_types_id), 
	FOREIGN KEY("Place_id") REFERENCES "Place" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "Landform_ontology_types" (
	"Landform_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("Landform_id", ontology_types_id), 
	FOREIGN KEY("Landform_id") REFERENCES "Landform" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "QuantityKind_ontology_types" (
	"QuantityKind_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("QuantityKind_id", ontology_types_id), 
	FOREIGN KEY("QuantityKind_id") REFERENCES "QuantityKind" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "UnitConcept_ontology_types" (
	"UnitConcept_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("UnitConcept_id", ontology_types_id), 
	FOREIGN KEY("UnitConcept_id") REFERENCES "UnitConcept" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "CurrencyConcept_ontology_types" (
	"CurrencyConcept_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("CurrencyConcept_id", ontology_types_id), 
	FOREIGN KEY("CurrencyConcept_id") REFERENCES "CurrencyConcept" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "PowerPlantType_ontology_types" (
	"PowerPlantType_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("PowerPlantType_id", ontology_types_id), 
	FOREIGN KEY("PowerPlantType_id") REFERENCES "PowerPlantType" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "FossilFuel_ontology_types" (
	"FossilFuel_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("FossilFuel_id", ontology_types_id), 
	FOREIGN KEY("FossilFuel_id") REFERENCES "FossilFuel" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "ElectricalGrid_ontology_types" (
	"ElectricalGrid_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("ElectricalGrid_id", ontology_types_id), 
	FOREIGN KEY("ElectricalGrid_id") REFERENCES "ElectricalGrid" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "Variable_allowed_units" (
	"Variable_id" INTEGER, 
	allowed_units_id TEXT, 
	PRIMARY KEY ("Variable_id", allowed_units_id), 
	FOREIGN KEY("Variable_id") REFERENCES "Variable" (id), 
	FOREIGN KEY(allowed_units_id) REFERENCES "UnitConcept" (id)
);
CREATE TABLE "ExtractiveIndustryEquipment_ontology_types" (
	"ExtractiveIndustryEquipment_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("ExtractiveIndustryEquipment_id", ontology_types_id), 
	FOREIGN KEY("ExtractiveIndustryEquipment_id") REFERENCES "ExtractiveIndustryEquipment" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "ExtractiveIndustryWaste_ontology_types" (
	"ExtractiveIndustryWaste_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("ExtractiveIndustryWaste_id", ontology_types_id), 
	FOREIGN KEY("ExtractiveIndustryWaste_id") REFERENCES "ExtractiveIndustryWaste" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "EnvironmentalSite_ontology_types" (
	"EnvironmentalSite_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("EnvironmentalSite_id", ontology_types_id), 
	FOREIGN KEY("EnvironmentalSite_id") REFERENCES "EnvironmentalSite" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "FoodRecipe_ontology_types" (
	"FoodRecipe_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("FoodRecipe_id", ontology_types_id), 
	FOREIGN KEY("FoodRecipe_id") REFERENCES "FoodRecipe" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "FoodTypeConcept_ontology_types" (
	"FoodTypeConcept_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("FoodTypeConcept_id", ontology_types_id), 
	FOREIGN KEY("FoodTypeConcept_id") REFERENCES "FoodTypeConcept" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "BasicFoodType_ontology_types" (
	"BasicFoodType_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("BasicFoodType_id", ontology_types_id), 
	FOREIGN KEY("BasicFoodType_id") REFERENCES "BasicFoodType" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "CompositeFoodType_ontology_types" (
	"CompositeFoodType_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("CompositeFoodType_id", ontology_types_id), 
	FOREIGN KEY("CompositeFoodType_id") REFERENCES "CompositeFoodType" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "LifeEvent" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	starts_at_id INTEGER, 
	ends_at_id INTEGER, 
	happens_at_id INTEGER, 
	has_interval_id INTEGER, 
	has_duration_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(starts_at_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(ends_at_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(happens_at_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(has_interval_id) REFERENCES "TemporalInterval" (id), 
	FOREIGN KEY(has_duration_id) REFERENCES "Duration" (id)
);
CREATE TABLE "InvestigativeProcess" (
	follows_procedure TEXT, 
	part_of TEXT, 
	uses_physical_device TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	starts_at_id INTEGER, 
	ends_at_id INTEGER, 
	happens_at_id INTEGER, 
	has_interval_id INTEGER, 
	has_duration_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(follows_procedure) REFERENCES "InvestigativeProtocol" (id), 
	FOREIGN KEY(part_of) REFERENCES "Investigation" (id), 
	FOREIGN KEY(uses_physical_device) REFERENCES "PhysicalDevice" (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(starts_at_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(ends_at_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(happens_at_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(has_interval_id) REFERENCES "TemporalInterval" (id), 
	FOREIGN KEY(has_duration_id) REFERENCES "Duration" (id)
);
CREATE TABLE "SampleCollectionProcess" (
	material_collected TEXT, 
	collected_from TEXT, 
	follows_procedure TEXT, 
	part_of TEXT, 
	uses_physical_device TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	starts_at_id INTEGER, 
	ends_at_id INTEGER, 
	happens_at_id INTEGER, 
	has_interval_id INTEGER, 
	has_duration_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(material_collected) REFERENCES "SampleMaterial" (id), 
	FOREIGN KEY(collected_from) REFERENCES "NamedThing" (id), 
	FOREIGN KEY(follows_procedure) REFERENCES "InvestigativeProtocol" (id), 
	FOREIGN KEY(part_of) REFERENCES "Investigation" (id), 
	FOREIGN KEY(uses_physical_device) REFERENCES "PhysicalDevice" (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(starts_at_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(ends_at_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(happens_at_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(has_interval_id) REFERENCES "TemporalInterval" (id), 
	FOREIGN KEY(has_duration_id) REFERENCES "Duration" (id)
);
CREATE TABLE "SampleProcessing" (
	follows_procedure TEXT, 
	uses_physical_device TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	starts_at_id INTEGER, 
	ends_at_id INTEGER, 
	happens_at_id INTEGER, 
	has_interval_id INTEGER, 
	has_duration_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(follows_procedure) REFERENCES "Procedure" (id), 
	FOREIGN KEY(uses_physical_device) REFERENCES "PhysicalDevice" (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(starts_at_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(ends_at_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(happens_at_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(has_interval_id) REFERENCES "TemporalInterval" (id), 
	FOREIGN KEY(has_duration_id) REFERENCES "Duration" (id)
);
CREATE TABLE "DataGenerationFromSample" (
	follows_procedure TEXT, 
	part_of TEXT, 
	uses_physical_device TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	starts_at_id INTEGER, 
	ends_at_id INTEGER, 
	happens_at_id INTEGER, 
	has_interval_id INTEGER, 
	has_duration_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(follows_procedure) REFERENCES "InvestigativeProtocol" (id), 
	FOREIGN KEY(part_of) REFERENCES "Investigation" (id), 
	FOREIGN KEY(uses_physical_device) REFERENCES "PhysicalDevice" (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(starts_at_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(ends_at_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(happens_at_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(has_interval_id) REFERENCES "TemporalInterval" (id), 
	FOREIGN KEY(has_duration_id) REFERENCES "Duration" (id)
);
CREATE TABLE "HealthcareEncounter" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification VARCHAR(34), 
	description TEXT, 
	patient_id INTEGER, 
	provider_id INTEGER, 
	starts_at_id INTEGER, 
	ends_at_id INTEGER, 
	happens_at_id INTEGER, 
	has_interval_id INTEGER, 
	has_duration_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(patient_id) REFERENCES "Patient" (id), 
	FOREIGN KEY(provider_id) REFERENCES "HealthcareProvider" (id), 
	FOREIGN KEY(starts_at_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(ends_at_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(happens_at_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(has_interval_id) REFERENCES "TemporalInterval" (id), 
	FOREIGN KEY(has_duration_id) REFERENCES "Duration" (id)
);
CREATE TABLE "ClinicalCohortEnrollment" (
	cohort TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	patient_id INTEGER, 
	starts_at_id INTEGER, 
	ends_at_id INTEGER, 
	happens_at_id INTEGER, 
	has_interval_id INTEGER, 
	has_duration_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(cohort) REFERENCES "ClinicalCohort" (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(patient_id) REFERENCES "Patient" (id), 
	FOREIGN KEY(starts_at_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(ends_at_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(happens_at_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(has_interval_id) REFERENCES "TemporalInterval" (id), 
	FOREIGN KEY(has_duration_id) REFERENCES "Duration" (id)
);
CREATE TABLE "EngineeringProcess" (
	follows_procedure TEXT, 
	part_of TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	starts_at_id INTEGER, 
	ends_at_id INTEGER, 
	happens_at_id INTEGER, 
	has_interval_id INTEGER, 
	has_duration_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(follows_procedure) REFERENCES "EngineeringSpecification" (id), 
	FOREIGN KEY(part_of) REFERENCES "EngineeringProcess" (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(starts_at_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(ends_at_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(happens_at_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(has_interval_id) REFERENCES "TemporalInterval" (id), 
	FOREIGN KEY(has_duration_id) REFERENCES "Duration" (id)
);
CREATE TABLE "EngineeringMaterialProcessing" (
	follows_procedure TEXT, 
	uses_physical_device TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	starts_at_id INTEGER, 
	ends_at_id INTEGER, 
	happens_at_id INTEGER, 
	has_interval_id INTEGER, 
	has_duration_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(follows_procedure) REFERENCES "Procedure" (id), 
	FOREIGN KEY(uses_physical_device) REFERENCES "PhysicalDevice" (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(starts_at_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(ends_at_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(happens_at_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(has_interval_id) REFERENCES "TemporalInterval" (id), 
	FOREIGN KEY(has_duration_id) REFERENCES "Duration" (id)
);
CREATE TABLE "Ratio" (
	id INTEGER NOT NULL, 
	has_quantity_kind TEXT, 
	type TEXT, 
	numerator_id INTEGER, 
	denominator_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_quantity_kind) REFERENCES "QuantityKind" (id), 
	FOREIGN KEY(numerator_id) REFERENCES "Quantity" (id), 
	FOREIGN KEY(denominator_id) REFERENCES "Quantity" (id)
);
CREATE TABLE "QuantityRange" (
	id INTEGER NOT NULL, 
	type TEXT, 
	lower_bound_id INTEGER, 
	upper_bound_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(lower_bound_id) REFERENCES "Quantity" (id), 
	FOREIGN KEY(upper_bound_id) REFERENCES "Quantity" (id)
);
CREATE TABLE "PowerPlant" (
	plant_type TEXT, 
	location TEXT, 
	operator TEXT, 
	commissioning_date DATE, 
	decommissioning_date DATE, 
	located_at_place TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	capacity_id INTEGER, 
	capex_id INTEGER, 
	opex_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(plant_type) REFERENCES "PowerPlantType" (id), 
	FOREIGN KEY(location) REFERENCES "Place" (id), 
	FOREIGN KEY(operator) REFERENCES "Organization" (id), 
	FOREIGN KEY(located_at_place) REFERENCES "Place" (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(capacity_id) REFERENCES "SimpleQuantity" (id), 
	FOREIGN KEY(capex_id) REFERENCES "MoneyQuantity" (id), 
	FOREIGN KEY(opex_id) REFERENCES "MoneyQuantity" (id)
);
CREATE TABLE "FossilFuelPlant" (
	fuel TEXT, 
	plant_type TEXT, 
	location TEXT, 
	operator TEXT, 
	commissioning_date DATE, 
	decommissioning_date DATE, 
	located_at_place TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	capacity_id INTEGER, 
	capex_id INTEGER, 
	opex_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(fuel) REFERENCES "FossilFuel" (id), 
	FOREIGN KEY(plant_type) REFERENCES "PowerPlantType" (id), 
	FOREIGN KEY(location) REFERENCES "Place" (id), 
	FOREIGN KEY(operator) REFERENCES "Organization" (id), 
	FOREIGN KEY(located_at_place) REFERENCES "Place" (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(capacity_id) REFERENCES "SimpleQuantity" (id), 
	FOREIGN KEY(capex_id) REFERENCES "MoneyQuantity" (id), 
	FOREIGN KEY(opex_id) REFERENCES "MoneyQuantity" (id)
);
CREATE TABLE "NuclearPlant" (
	plant_type TEXT, 
	location TEXT, 
	operator TEXT, 
	commissioning_date DATE, 
	decommissioning_date DATE, 
	located_at_place TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	capacity_id INTEGER, 
	capex_id INTEGER, 
	opex_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(plant_type) REFERENCES "PowerPlantType" (id), 
	FOREIGN KEY(location) REFERENCES "Place" (id), 
	FOREIGN KEY(operator) REFERENCES "Organization" (id), 
	FOREIGN KEY(located_at_place) REFERENCES "Place" (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(capacity_id) REFERENCES "SimpleQuantity" (id), 
	FOREIGN KEY(capex_id) REFERENCES "MoneyQuantity" (id), 
	FOREIGN KEY(opex_id) REFERENCES "MoneyQuantity" (id)
);
CREATE TABLE "RenewablePlant" (
	plant_type TEXT, 
	location TEXT, 
	operator TEXT, 
	commissioning_date DATE, 
	decommissioning_date DATE, 
	located_at_place TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	capacity_id INTEGER, 
	capex_id INTEGER, 
	opex_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(plant_type) REFERENCES "PowerPlantType" (id), 
	FOREIGN KEY(location) REFERENCES "Place" (id), 
	FOREIGN KEY(operator) REFERENCES "Organization" (id), 
	FOREIGN KEY(located_at_place) REFERENCES "Place" (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(capacity_id) REFERENCES "SimpleQuantity" (id), 
	FOREIGN KEY(capex_id) REFERENCES "MoneyQuantity" (id), 
	FOREIGN KEY(opex_id) REFERENCES "MoneyQuantity" (id)
);
CREATE TABLE "HydroelectricPlant" (
	dam TEXT, 
	plant_type TEXT, 
	location TEXT, 
	operator TEXT, 
	commissioning_date DATE, 
	decommissioning_date DATE, 
	located_at_place TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	capacity_id INTEGER, 
	capex_id INTEGER, 
	opex_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(dam) REFERENCES "Landform" (id), 
	FOREIGN KEY(plant_type) REFERENCES "PowerPlantType" (id), 
	FOREIGN KEY(location) REFERENCES "Place" (id), 
	FOREIGN KEY(operator) REFERENCES "Organization" (id), 
	FOREIGN KEY(located_at_place) REFERENCES "Place" (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(capacity_id) REFERENCES "SimpleQuantity" (id), 
	FOREIGN KEY(capex_id) REFERENCES "MoneyQuantity" (id), 
	FOREIGN KEY(opex_id) REFERENCES "MoneyQuantity" (id)
);
CREATE TABLE "SolarPlant" (
	plant_type TEXT, 
	location TEXT, 
	operator TEXT, 
	commissioning_date DATE, 
	decommissioning_date DATE, 
	located_at_place TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	capacity_id INTEGER, 
	capex_id INTEGER, 
	opex_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(plant_type) REFERENCES "PowerPlantType" (id), 
	FOREIGN KEY(location) REFERENCES "Place" (id), 
	FOREIGN KEY(operator) REFERENCES "Organization" (id), 
	FOREIGN KEY(located_at_place) REFERENCES "Place" (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(capacity_id) REFERENCES "SimpleQuantity" (id), 
	FOREIGN KEY(capex_id) REFERENCES "MoneyQuantity" (id), 
	FOREIGN KEY(opex_id) REFERENCES "MoneyQuantity" (id)
);
CREATE TABLE "WindFarm" (
	plant_type TEXT, 
	location TEXT, 
	operator TEXT, 
	commissioning_date DATE, 
	decommissioning_date DATE, 
	located_at_place TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	capacity_id INTEGER, 
	capex_id INTEGER, 
	opex_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(plant_type) REFERENCES "PowerPlantType" (id), 
	FOREIGN KEY(location) REFERENCES "Place" (id), 
	FOREIGN KEY(operator) REFERENCES "Organization" (id), 
	FOREIGN KEY(located_at_place) REFERENCES "Place" (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(capacity_id) REFERENCES "SimpleQuantity" (id), 
	FOREIGN KEY(capex_id) REFERENCES "MoneyQuantity" (id), 
	FOREIGN KEY(opex_id) REFERENCES "MoneyQuantity" (id)
);
CREATE TABLE "Measurement" (
	id INTEGER NOT NULL, 
	type TEXT, 
	quantity_measured_id INTEGER, 
	variable_measured_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(quantity_measured_id) REFERENCES "Quantity" (id), 
	FOREIGN KEY(variable_measured_id) REFERENCES "Variable" (id)
);
CREATE TABLE "PlannedProcess" (
	follows_procedure TEXT, 
	uses_physical_device TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	starts_at_id INTEGER, 
	ends_at_id INTEGER, 
	happens_at_id INTEGER, 
	has_interval_id INTEGER, 
	has_duration_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(follows_procedure) REFERENCES "Procedure" (id), 
	FOREIGN KEY(uses_physical_device) REFERENCES "PhysicalDevice" (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(starts_at_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(ends_at_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(happens_at_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(has_interval_id) REFERENCES "TemporalInterval" (id), 
	FOREIGN KEY(has_duration_id) REFERENCES "Duration" (id)
);
CREATE TABLE "MaterialCollection" (
	follows_procedure TEXT, 
	uses_physical_device TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	starts_at_id INTEGER, 
	ends_at_id INTEGER, 
	happens_at_id INTEGER, 
	has_interval_id INTEGER, 
	has_duration_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(follows_procedure) REFERENCES "Procedure" (id), 
	FOREIGN KEY(uses_physical_device) REFERENCES "PhysicalDevice" (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(starts_at_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(ends_at_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(happens_at_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(has_interval_id) REFERENCES "TemporalInterval" (id), 
	FOREIGN KEY(has_duration_id) REFERENCES "Duration" (id)
);
CREATE TABLE "MaterialProcessing" (
	follows_procedure TEXT, 
	uses_physical_device TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	starts_at_id INTEGER, 
	ends_at_id INTEGER, 
	happens_at_id INTEGER, 
	has_interval_id INTEGER, 
	has_duration_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(follows_procedure) REFERENCES "Procedure" (id), 
	FOREIGN KEY(uses_physical_device) REFERENCES "PhysicalDevice" (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(starts_at_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(ends_at_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(happens_at_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(has_interval_id) REFERENCES "TemporalInterval" (id), 
	FOREIGN KEY(has_duration_id) REFERENCES "Duration" (id)
);
CREATE TABLE "ExtractiveIndustryFacility" (
	facility_type VARCHAR(15), 
	operator TEXT, 
	located_at_place TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	production_capacity_id INTEGER, 
	annual_production_id INTEGER, 
	reserves_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(operator) REFERENCES "Organization" (id), 
	FOREIGN KEY(located_at_place) REFERENCES "Place" (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(production_capacity_id) REFERENCES "Quantity" (id), 
	FOREIGN KEY(annual_production_id) REFERENCES "Quantity" (id), 
	FOREIGN KEY(reserves_id) REFERENCES "Quantity" (id)
);
CREATE TABLE "MiningFacility" (
	mining_method VARCHAR(11), 
	facility_type VARCHAR(15), 
	operator TEXT, 
	located_at_place TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	depth_id INTEGER, 
	area_id INTEGER, 
	production_capacity_id INTEGER, 
	annual_production_id INTEGER, 
	reserves_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(operator) REFERENCES "Organization" (id), 
	FOREIGN KEY(located_at_place) REFERENCES "Place" (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(depth_id) REFERENCES "Quantity" (id), 
	FOREIGN KEY(area_id) REFERENCES "Quantity" (id), 
	FOREIGN KEY(production_capacity_id) REFERENCES "Quantity" (id), 
	FOREIGN KEY(annual_production_id) REFERENCES "Quantity" (id), 
	FOREIGN KEY(reserves_id) REFERENCES "Quantity" (id)
);
CREATE TABLE "WellFacility" (
	well_type VARCHAR(9), 
	facility_type VARCHAR(15), 
	operator TEXT, 
	located_at_place TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	depth_id INTEGER, 
	production_capacity_id INTEGER, 
	annual_production_id INTEGER, 
	reserves_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(operator) REFERENCES "Organization" (id), 
	FOREIGN KEY(located_at_place) REFERENCES "Place" (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(depth_id) REFERENCES "Quantity" (id), 
	FOREIGN KEY(production_capacity_id) REFERENCES "Quantity" (id), 
	FOREIGN KEY(annual_production_id) REFERENCES "Quantity" (id), 
	FOREIGN KEY(reserves_id) REFERENCES "Quantity" (id)
);
CREATE TABLE "QuarryFacility" (
	facility_type VARCHAR(15), 
	operator TEXT, 
	located_at_place TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	production_capacity_id INTEGER, 
	annual_production_id INTEGER, 
	reserves_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(operator) REFERENCES "Organization" (id), 
	FOREIGN KEY(located_at_place) REFERENCES "Place" (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(production_capacity_id) REFERENCES "Quantity" (id), 
	FOREIGN KEY(annual_production_id) REFERENCES "Quantity" (id), 
	FOREIGN KEY(reserves_id) REFERENCES "Quantity" (id)
);
CREATE TABLE "FoodProcessing" (
	follows_procedure TEXT, 
	uses_physical_device TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	starts_at_id INTEGER, 
	ends_at_id INTEGER, 
	happens_at_id INTEGER, 
	has_interval_id INTEGER, 
	has_duration_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(follows_procedure) REFERENCES "Procedure" (id), 
	FOREIGN KEY(uses_physical_device) REFERENCES "PhysicalDevice" (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(starts_at_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(ends_at_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(happens_at_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(has_interval_id) REFERENCES "TemporalInterval" (id), 
	FOREIGN KEY(has_duration_id) REFERENCES "Duration" (id)
);
CREATE TABLE "Facility_ontology_types" (
	"Facility_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("Facility_id", ontology_types_id), 
	FOREIGN KEY("Facility_id") REFERENCES "Facility" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "Building_ontology_types" (
	"Building_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("Building_id", ontology_types_id), 
	FOREIGN KEY("Building_id") REFERENCES "Building" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "ClinicalCohort_ontology_types" (
	"ClinicalCohort_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("ClinicalCohort_id", ontology_types_id), 
	FOREIGN KEY("ClinicalCohort_id") REFERENCES "ClinicalCohort" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "UnitConversionOperation_inputs" (
	"UnitConversionOperation_id" INTEGER, 
	inputs_id INTEGER, 
	PRIMARY KEY ("UnitConversionOperation_id", inputs_id), 
	FOREIGN KEY("UnitConversionOperation_id") REFERENCES "UnitConversionOperation" (id), 
	FOREIGN KEY(inputs_id) REFERENCES "Quantity" (id)
);
CREATE TABLE "UnitConversionOperation_outputs" (
	"UnitConversionOperation_id" INTEGER, 
	outputs_id INTEGER, 
	PRIMARY KEY ("UnitConversionOperation_id", outputs_id), 
	FOREIGN KEY("UnitConversionOperation_id") REFERENCES "UnitConversionOperation" (id), 
	FOREIGN KEY(outputs_id) REFERENCES "Quantity" (id)
);
CREATE TABLE "FoodRecipe_ingredients" (
	"FoodRecipe_id" TEXT, 
	ingredients_id INTEGER, 
	PRIMARY KEY ("FoodRecipe_id", ingredients_id), 
	FOREIGN KEY("FoodRecipe_id") REFERENCES "FoodRecipe" (id), 
	FOREIGN KEY(ingredients_id) REFERENCES "FoodIngredient" (id)
);
CREATE TABLE "HealthcareConditionOccurrence" (
	observed_during TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	patient_id INTEGER, 
	starts_at_id INTEGER, 
	ends_at_id INTEGER, 
	happens_at_id INTEGER, 
	has_interval_id INTEGER, 
	has_duration_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(observed_during) REFERENCES "HealthcareEncounter" (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(patient_id) REFERENCES "Patient" (id), 
	FOREIGN KEY(starts_at_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(ends_at_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(happens_at_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(has_interval_id) REFERENCES "TemporalInterval" (id), 
	FOREIGN KEY(has_duration_id) REFERENCES "Duration" (id)
);
CREATE TABLE "ExtractiveIndustryProduct" (
	product_type VARCHAR(7), 
	processing_method TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	classification TEXT, 
	description TEXT, 
	"ExtractiveIndustryFacility_id" TEXT, 
	"MiningFacility_id" TEXT, 
	"WellFacility_id" TEXT, 
	"QuarryFacility_id" TEXT, 
	grade_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(processing_method) REFERENCES "EngineeringSpecification" (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY("ExtractiveIndustryFacility_id") REFERENCES "ExtractiveIndustryFacility" (id), 
	FOREIGN KEY("MiningFacility_id") REFERENCES "MiningFacility" (id), 
	FOREIGN KEY("WellFacility_id") REFERENCES "WellFacility" (id), 
	FOREIGN KEY("QuarryFacility_id") REFERENCES "QuarryFacility" (id), 
	FOREIGN KEY(grade_id) REFERENCES "SimpleQuantity" (id)
);
CREATE TABLE "LifeEvent_ontology_types" (
	"LifeEvent_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("LifeEvent_id", ontology_types_id), 
	FOREIGN KEY("LifeEvent_id") REFERENCES "LifeEvent" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "InvestigativeProcess_ontology_types" (
	"InvestigativeProcess_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("InvestigativeProcess_id", ontology_types_id), 
	FOREIGN KEY("InvestigativeProcess_id") REFERENCES "InvestigativeProcess" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "SampleCollectionProcess_ontology_types" (
	"SampleCollectionProcess_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("SampleCollectionProcess_id", ontology_types_id), 
	FOREIGN KEY("SampleCollectionProcess_id") REFERENCES "SampleCollectionProcess" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "SampleProcessing_ontology_types" (
	"SampleProcessing_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("SampleProcessing_id", ontology_types_id), 
	FOREIGN KEY("SampleProcessing_id") REFERENCES "SampleProcessing" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "DataGenerationFromSample_ontology_types" (
	"DataGenerationFromSample_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("DataGenerationFromSample_id", ontology_types_id), 
	FOREIGN KEY("DataGenerationFromSample_id") REFERENCES "DataGenerationFromSample" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "HealthcareEncounter_ontology_types" (
	"HealthcareEncounter_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("HealthcareEncounter_id", ontology_types_id), 
	FOREIGN KEY("HealthcareEncounter_id") REFERENCES "HealthcareEncounter" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "ClinicalCohortEnrollment_ontology_types" (
	"ClinicalCohortEnrollment_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("ClinicalCohortEnrollment_id", ontology_types_id), 
	FOREIGN KEY("ClinicalCohortEnrollment_id") REFERENCES "ClinicalCohortEnrollment" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "EngineeringProcess_ontology_types" (
	"EngineeringProcess_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("EngineeringProcess_id", ontology_types_id), 
	FOREIGN KEY("EngineeringProcess_id") REFERENCES "EngineeringProcess" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "EngineeringMaterialProcessing_ontology_types" (
	"EngineeringMaterialProcessing_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("EngineeringMaterialProcessing_id", ontology_types_id), 
	FOREIGN KEY("EngineeringMaterialProcessing_id") REFERENCES "EngineeringMaterialProcessing" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "PowerPlant_ontology_types" (
	"PowerPlant_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("PowerPlant_id", ontology_types_id), 
	FOREIGN KEY("PowerPlant_id") REFERENCES "PowerPlant" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "FossilFuelPlant_ontology_types" (
	"FossilFuelPlant_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("FossilFuelPlant_id", ontology_types_id), 
	FOREIGN KEY("FossilFuelPlant_id") REFERENCES "FossilFuelPlant" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "NuclearPlant_ontology_types" (
	"NuclearPlant_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("NuclearPlant_id", ontology_types_id), 
	FOREIGN KEY("NuclearPlant_id") REFERENCES "NuclearPlant" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "RenewablePlant_ontology_types" (
	"RenewablePlant_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("RenewablePlant_id", ontology_types_id), 
	FOREIGN KEY("RenewablePlant_id") REFERENCES "RenewablePlant" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "HydroelectricPlant_ontology_types" (
	"HydroelectricPlant_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("HydroelectricPlant_id", ontology_types_id), 
	FOREIGN KEY("HydroelectricPlant_id") REFERENCES "HydroelectricPlant" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "SolarPlant_ontology_types" (
	"SolarPlant_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("SolarPlant_id", ontology_types_id), 
	FOREIGN KEY("SolarPlant_id") REFERENCES "SolarPlant" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "WindFarm_ontology_types" (
	"WindFarm_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("WindFarm_id", ontology_types_id), 
	FOREIGN KEY("WindFarm_id") REFERENCES "WindFarm" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "ElectricalGrid_plants" (
	"ElectricalGrid_id" TEXT, 
	plants_id TEXT, 
	PRIMARY KEY ("ElectricalGrid_id", plants_id), 
	FOREIGN KEY("ElectricalGrid_id") REFERENCES "ElectricalGrid" (id), 
	FOREIGN KEY(plants_id) REFERENCES "PowerPlant" (id)
);
CREATE TABLE "PlannedProcess_ontology_types" (
	"PlannedProcess_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("PlannedProcess_id", ontology_types_id), 
	FOREIGN KEY("PlannedProcess_id") REFERENCES "PlannedProcess" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "MaterialCollection_ontology_types" (
	"MaterialCollection_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("MaterialCollection_id", ontology_types_id), 
	FOREIGN KEY("MaterialCollection_id") REFERENCES "MaterialCollection" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "MaterialProcessing_ontology_types" (
	"MaterialProcessing_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("MaterialProcessing_id", ontology_types_id), 
	FOREIGN KEY("MaterialProcessing_id") REFERENCES "MaterialProcessing" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "ExtractiveIndustryFacility_ontology_types" (
	"ExtractiveIndustryFacility_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("ExtractiveIndustryFacility_id", ontology_types_id), 
	FOREIGN KEY("ExtractiveIndustryFacility_id") REFERENCES "ExtractiveIndustryFacility" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "MiningFacility_ontology_types" (
	"MiningFacility_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("MiningFacility_id", ontology_types_id), 
	FOREIGN KEY("MiningFacility_id") REFERENCES "MiningFacility" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "WellFacility_ontology_types" (
	"WellFacility_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("WellFacility_id", ontology_types_id), 
	FOREIGN KEY("WellFacility_id") REFERENCES "WellFacility" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "QuarryFacility_ontology_types" (
	"QuarryFacility_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("QuarryFacility_id", ontology_types_id), 
	FOREIGN KEY("QuarryFacility_id") REFERENCES "QuarryFacility" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "FoodRecipe_steps" (
	"FoodRecipe_id" TEXT, 
	steps_id TEXT, 
	PRIMARY KEY ("FoodRecipe_id", steps_id), 
	FOREIGN KEY("FoodRecipe_id") REFERENCES "FoodRecipe" (id), 
	FOREIGN KEY(steps_id) REFERENCES "FoodProcessing" (id)
);
CREATE TABLE "FoodProcessing_ontology_types" (
	"FoodProcessing_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("FoodProcessing_id", ontology_types_id), 
	FOREIGN KEY("FoodProcessing_id") REFERENCES "FoodProcessing" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "HealthcareConditionOccurrence_ontology_types" (
	"HealthcareConditionOccurrence_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("HealthcareConditionOccurrence_id", ontology_types_id), 
	FOREIGN KEY("HealthcareConditionOccurrence_id") REFERENCES "HealthcareConditionOccurrence" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "ExtractiveIndustryProduct_ontology_types" (
	"ExtractiveIndustryProduct_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("ExtractiveIndustryProduct_id", ontology_types_id), 
	FOREIGN KEY("ExtractiveIndustryProduct_id") REFERENCES "ExtractiveIndustryProduct" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);