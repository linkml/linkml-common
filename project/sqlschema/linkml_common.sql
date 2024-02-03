

CREATE TABLE "Agent" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	subtype TEXT, 
	ontology_types TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "AutomatedAgent" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	subtype TEXT, 
	ontology_types TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "BasicFoodType" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	subtype TEXT, 
	ontology_types TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "ClinicalCohortDefinition" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	subtype TEXT, 
	ontology_types TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Collection" (
	type TEXT, 
	members TEXT, 
	PRIMARY KEY (type, members)
);

CREATE TABLE "CompositeFoodType" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	subtype TEXT, 
	ontology_types TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Concept" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	subtype TEXT, 
	ontology_types TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "CreativeWork" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	subtype TEXT, 
	ontology_types TEXT, 
	description TEXT, 
	title TEXT, 
	abstract TEXT, 
	rights TEXT, 
	creators TEXT, 
	contributors TEXT, 
	contacts TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Dataset" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	subtype TEXT, 
	ontology_types TEXT, 
	description TEXT, 
	title TEXT, 
	abstract TEXT, 
	rights TEXT, 
	creators TEXT, 
	contributors TEXT, 
	contacts TEXT, 
	collected_as_part_of TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "DataStructure" (
	type TEXT, 
	PRIMARY KEY (type)
);

CREATE TABLE "EngineeringSpecification" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	subtype TEXT, 
	ontology_types TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "EnvironmentalSite" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	subtype TEXT, 
	ontology_types TEXT, 
	description TEXT, 
	address TEXT, 
	geolocation TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Event" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	subtype TEXT, 
	ontology_types TEXT, 
	description TEXT, 
	starts_at TEXT, 
	ends_at TEXT, 
	happens_at TEXT, 
	has_interval TEXT, 
	has_duration TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "FoodRecipe" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	subtype TEXT, 
	ontology_types TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "FoodTypeConcept" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	subtype TEXT, 
	ontology_types TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "GeoPointLocation" (
	latitude TEXT, 
	longitude TEXT, 
	altitude TEXT, 
	PRIMARY KEY (latitude, longitude, altitude)
);

CREATE TABLE "HealthcareEncounter" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	ontology_types TEXT, 
	description TEXT, 
	starts_at TEXT, 
	ends_at TEXT, 
	happens_at TEXT, 
	has_interval TEXT, 
	has_duration TEXT, 
	patient TEXT, 
	provider TEXT, 
	subtype VARCHAR(34), 
	PRIMARY KEY (id)
);

CREATE TABLE "HealthcareOrganization" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	subtype TEXT, 
	ontology_types TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "HealthcareSite" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	subtype TEXT, 
	ontology_types TEXT, 
	description TEXT, 
	address TEXT, 
	geolocation TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "InformationEntity" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	subtype TEXT, 
	ontology_types TEXT, 
	description TEXT, 
	describes TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Intangible" (
	type TEXT, 
	PRIMARY KEY (type)
);

CREATE TABLE "Investigation" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	subtype TEXT, 
	ontology_types TEXT, 
	description TEXT, 
	objectives TEXT, 
	variables TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "InvestigativeProtocol" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	subtype TEXT, 
	ontology_types TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Landform" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	subtype TEXT, 
	ontology_types TEXT, 
	description TEXT, 
	address TEXT, 
	geolocation TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "LifeEvent" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	subtype TEXT, 
	ontology_types TEXT, 
	description TEXT, 
	starts_at TEXT, 
	ends_at TEXT, 
	happens_at TEXT, 
	has_interval TEXT, 
	has_duration TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "MathematicalOperation" (
	inputs TEXT, 
	outputs TEXT, 
	parts TEXT, 
	immediate_preceding_steps TEXT, 
	PRIMARY KEY (inputs, outputs, parts, immediate_preceding_steps)
);

CREATE TABLE "Measurement" (
	type TEXT, 
	quantity_measured TEXT, 
	variable_measured TEXT, 
	PRIMARY KEY (type, quantity_measured, variable_measured)
);

CREATE TABLE "NamedThing" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	subtype TEXT, 
	ontology_types TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Observation" (
	type TEXT, 
	PRIMARY KEY (type)
);

CREATE TABLE "Organization" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	subtype TEXT, 
	ontology_types TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Person" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	subtype TEXT, 
	ontology_types TEXT, 
	description TEXT, 
	primary_email TEXT, 
	birth_date DATE, 
	age_in_years INTEGER, 
	vital_status VARCHAR(7), 
	PRIMARY KEY (id)
);

CREATE TABLE "PhysicalDevice" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	subtype TEXT, 
	ontology_types TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Place" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	subtype TEXT, 
	ontology_types TEXT, 
	description TEXT, 
	address TEXT, 
	geolocation TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "PostalAddress" (
	type TEXT, 
	street_address TEXT, 
	street_address_additional TEXT, 
	city TEXT, 
	state TEXT, 
	postal_code TEXT, 
	country TEXT, 
	PRIMARY KEY (type, street_address, street_address_additional, city, state, postal_code, country)
);

CREATE TABLE "Procedure" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	subtype TEXT, 
	ontology_types TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Publication" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	subtype TEXT, 
	ontology_types TEXT, 
	description TEXT, 
	title TEXT, 
	abstract TEXT, 
	rights TEXT, 
	creators TEXT, 
	contributors TEXT, 
	contacts TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "QuantityKind" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	subtype TEXT, 
	ontology_types TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "QuantityRange" (
	type TEXT, 
	lower_bound TEXT, 
	upper_bound TEXT, 
	PRIMARY KEY (type, lower_bound, upper_bound)
);

CREATE TABLE "RawMaterial" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	subtype TEXT, 
	ontology_types TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "SampleMaterial" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	subtype TEXT, 
	ontology_types TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Service" (
	type TEXT, 
	PRIMARY KEY (type)
);

CREATE TABLE "Specification" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	subtype TEXT, 
	ontology_types TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "StudyDesign" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	subtype TEXT, 
	ontology_types TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "TemporalInterval" (
	type TEXT, 
	starts_at TEXT, 
	ends_at TEXT, 
	PRIMARY KEY (type, starts_at, ends_at)
);

CREATE TABLE "TemporalRelationship" (
	type TEXT, 
	predicate VARCHAR(15), 
	relative_to TEXT, 
	PRIMARY KEY (type, predicate, relative_to)
);

CREATE TABLE "TimePointOrTemporalInterval" (
	type TEXT, 
	starts_at TEXT, 
	ends_at TEXT, 
	PRIMARY KEY (type, starts_at, ends_at)
);

CREATE TABLE "UnitConcept" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	subtype TEXT, 
	ontology_types TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "UnitConversionOperation" (
	parts TEXT, 
	immediate_preceding_steps TEXT, 
	inputs TEXT, 
	outputs TEXT, 
	PRIMARY KEY (parts, immediate_preceding_steps, inputs, outputs)
);

CREATE TABLE "Variable" (
	type TEXT, 
	allowed_units TEXT, 
	PRIMARY KEY (type, allowed_units)
);

CREATE TABLE "ClinicalCohort" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	subtype TEXT, 
	ontology_types TEXT, 
	description TEXT, 
	definition TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(definition) REFERENCES "ClinicalCohortDefinition" (id)
);

CREATE TABLE "DataGenerationFromSample" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	subtype TEXT, 
	ontology_types TEXT, 
	description TEXT, 
	starts_at TEXT, 
	ends_at TEXT, 
	happens_at TEXT, 
	has_interval TEXT, 
	has_duration TEXT, 
	uses_physical_device TEXT, 
	follows_procedure TEXT, 
	part_of TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(uses_physical_device) REFERENCES "PhysicalDevice" (id), 
	FOREIGN KEY(follows_procedure) REFERENCES "InvestigativeProtocol" (id), 
	FOREIGN KEY(part_of) REFERENCES "Investigation" (id)
);

CREATE TABLE "Duration" (
	type TEXT, 
	has_quantity_kind TEXT, 
	PRIMARY KEY (type, has_quantity_kind), 
	FOREIGN KEY(has_quantity_kind) REFERENCES "QuantityKind" (id)
);

CREATE TABLE "EngineeringMaterialProcessing" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	subtype TEXT, 
	ontology_types TEXT, 
	description TEXT, 
	starts_at TEXT, 
	ends_at TEXT, 
	happens_at TEXT, 
	has_interval TEXT, 
	has_duration TEXT, 
	follows_procedure TEXT, 
	uses_physical_device TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(follows_procedure) REFERENCES "Procedure" (id), 
	FOREIGN KEY(uses_physical_device) REFERENCES "PhysicalDevice" (id)
);

CREATE TABLE "EngineeringProcess" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	subtype TEXT, 
	ontology_types TEXT, 
	description TEXT, 
	starts_at TEXT, 
	ends_at TEXT, 
	happens_at TEXT, 
	has_interval TEXT, 
	has_duration TEXT, 
	follows_procedure TEXT, 
	part_of TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(follows_procedure) REFERENCES "EngineeringSpecification" (id), 
	FOREIGN KEY(part_of) REFERENCES "EngineeringProcess" (id)
);

CREATE TABLE "FoodIngredient" (
	type TEXT, 
	has_quantity_kind TEXT, 
	"FoodRecipe_id" TEXT, 
	PRIMARY KEY (type, has_quantity_kind, "FoodRecipe_id"), 
	FOREIGN KEY(has_quantity_kind) REFERENCES "QuantityKind" (id), 
	FOREIGN KEY("FoodRecipe_id") REFERENCES "FoodRecipe" (id)
);

CREATE TABLE "FoodProcessing" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	subtype TEXT, 
	ontology_types TEXT, 
	description TEXT, 
	starts_at TEXT, 
	ends_at TEXT, 
	happens_at TEXT, 
	has_interval TEXT, 
	has_duration TEXT, 
	follows_procedure TEXT, 
	uses_physical_device TEXT, 
	"FoodRecipe_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(follows_procedure) REFERENCES "Procedure" (id), 
	FOREIGN KEY(uses_physical_device) REFERENCES "PhysicalDevice" (id), 
	FOREIGN KEY("FoodRecipe_id") REFERENCES "FoodRecipe" (id)
);

CREATE TABLE "HealthcareConditionOccurrence" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	subtype TEXT, 
	ontology_types TEXT, 
	description TEXT, 
	starts_at TEXT, 
	ends_at TEXT, 
	happens_at TEXT, 
	has_interval TEXT, 
	has_duration TEXT, 
	patient TEXT, 
	observed_during TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(observed_during) REFERENCES "HealthcareEncounter" (id)
);

CREATE TABLE "HealthcareProvider" (
	type TEXT, 
	is_person TEXT, 
	speciality TEXT, 
	care_site TEXT, 
	PRIMARY KEY (type, is_person, speciality, care_site), 
	FOREIGN KEY(is_person) REFERENCES "Person" (id), 
	FOREIGN KEY(speciality) REFERENCES "Concept" (id), 
	FOREIGN KEY(care_site) REFERENCES "HealthcareSite" (id)
);

CREATE TABLE "HealthcareRole" (
	type TEXT, 
	is_person TEXT, 
	PRIMARY KEY (type, is_person), 
	FOREIGN KEY(is_person) REFERENCES "Person" (id)
);

CREATE TABLE "InvestigativeProcess" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	subtype TEXT, 
	ontology_types TEXT, 
	description TEXT, 
	starts_at TEXT, 
	ends_at TEXT, 
	happens_at TEXT, 
	has_interval TEXT, 
	has_duration TEXT, 
	uses_physical_device TEXT, 
	follows_procedure TEXT, 
	part_of TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(uses_physical_device) REFERENCES "PhysicalDevice" (id), 
	FOREIGN KEY(follows_procedure) REFERENCES "InvestigativeProtocol" (id), 
	FOREIGN KEY(part_of) REFERENCES "Investigation" (id)
);

CREATE TABLE "MaterialCollection" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	subtype TEXT, 
	ontology_types TEXT, 
	description TEXT, 
	starts_at TEXT, 
	ends_at TEXT, 
	happens_at TEXT, 
	has_interval TEXT, 
	has_duration TEXT, 
	follows_procedure TEXT, 
	uses_physical_device TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(follows_procedure) REFERENCES "Procedure" (id), 
	FOREIGN KEY(uses_physical_device) REFERENCES "PhysicalDevice" (id)
);

CREATE TABLE "MaterialProcessing" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	subtype TEXT, 
	ontology_types TEXT, 
	description TEXT, 
	starts_at TEXT, 
	ends_at TEXT, 
	happens_at TEXT, 
	has_interval TEXT, 
	has_duration TEXT, 
	follows_procedure TEXT, 
	uses_physical_device TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(follows_procedure) REFERENCES "Procedure" (id), 
	FOREIGN KEY(uses_physical_device) REFERENCES "PhysicalDevice" (id)
);

CREATE TABLE "Patient" (
	type TEXT, 
	is_person TEXT, 
	PRIMARY KEY (type, is_person), 
	FOREIGN KEY(is_person) REFERENCES "Person" (id)
);

CREATE TABLE "PlannedProcess" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	subtype TEXT, 
	ontology_types TEXT, 
	description TEXT, 
	starts_at TEXT, 
	ends_at TEXT, 
	happens_at TEXT, 
	has_interval TEXT, 
	has_duration TEXT, 
	follows_procedure TEXT, 
	uses_physical_device TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(follows_procedure) REFERENCES "Procedure" (id), 
	FOREIGN KEY(uses_physical_device) REFERENCES "PhysicalDevice" (id)
);

CREATE TABLE "Quantity" (
	type TEXT, 
	has_quantity_kind TEXT, 
	PRIMARY KEY (type, has_quantity_kind), 
	FOREIGN KEY(has_quantity_kind) REFERENCES "QuantityKind" (id)
);

CREATE TABLE "Ratio" (
	type TEXT, 
	has_quantity_kind TEXT, 
	numerator TEXT, 
	denominator TEXT, 
	PRIMARY KEY (type, has_quantity_kind, numerator, denominator), 
	FOREIGN KEY(has_quantity_kind) REFERENCES "QuantityKind" (id)
);

CREATE TABLE "SampleCollectionProcess" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	subtype TEXT, 
	ontology_types TEXT, 
	description TEXT, 
	starts_at TEXT, 
	ends_at TEXT, 
	happens_at TEXT, 
	has_interval TEXT, 
	has_duration TEXT, 
	uses_physical_device TEXT, 
	follows_procedure TEXT, 
	part_of TEXT, 
	material_collected TEXT, 
	collected_from TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(uses_physical_device) REFERENCES "PhysicalDevice" (id), 
	FOREIGN KEY(follows_procedure) REFERENCES "InvestigativeProtocol" (id), 
	FOREIGN KEY(part_of) REFERENCES "Investigation" (id), 
	FOREIGN KEY(material_collected) REFERENCES "SampleMaterial" (id), 
	FOREIGN KEY(collected_from) REFERENCES "NamedThing" (id)
);

CREATE TABLE "SampleProcessing" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	subtype TEXT, 
	ontology_types TEXT, 
	description TEXT, 
	starts_at TEXT, 
	ends_at TEXT, 
	happens_at TEXT, 
	has_interval TEXT, 
	has_duration TEXT, 
	follows_procedure TEXT, 
	uses_physical_device TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(follows_procedure) REFERENCES "Procedure" (id), 
	FOREIGN KEY(uses_physical_device) REFERENCES "PhysicalDevice" (id)
);

CREATE TABLE "SimpleQuantity" (
	type TEXT, 
	has_quantity_kind TEXT, 
	value FLOAT, 
	unit TEXT, 
	PRIMARY KEY (type, has_quantity_kind, value, unit), 
	FOREIGN KEY(has_quantity_kind) REFERENCES "QuantityKind" (id), 
	FOREIGN KEY(unit) REFERENCES "UnitConcept" (id)
);

CREATE TABLE "TimePoint" (
	type TEXT, 
	starts_at TEXT, 
	ends_at TEXT, 
	year_value INTEGER, 
	date_value DATE, 
	time_value TIME, 
	datetime_value DATETIME, 
	marker_event TEXT, 
	description TEXT, 
	PRIMARY KEY (type, starts_at, ends_at, year_value, date_value, time_value, datetime_value, marker_event, description), 
	FOREIGN KEY(marker_event) REFERENCES "Event" (id)
);

CREATE TABLE "CreativeWork_keywords" (
	backref_id TEXT, 
	keywords TEXT, 
	PRIMARY KEY (backref_id, keywords), 
	FOREIGN KEY(backref_id) REFERENCES "CreativeWork" (id)
);

CREATE TABLE "Dataset_keywords" (
	backref_id TEXT, 
	keywords TEXT, 
	PRIMARY KEY (backref_id, keywords), 
	FOREIGN KEY(backref_id) REFERENCES "Dataset" (id)
);

CREATE TABLE "Publication_keywords" (
	backref_id TEXT, 
	keywords TEXT, 
	PRIMARY KEY (backref_id, keywords), 
	FOREIGN KEY(backref_id) REFERENCES "Publication" (id)
);

CREATE TABLE "ClinicalCohortEnrollment" (
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	subtype TEXT, 
	ontology_types TEXT, 
	description TEXT, 
	starts_at TEXT, 
	ends_at TEXT, 
	happens_at TEXT, 
	has_interval TEXT, 
	has_duration TEXT, 
	patient TEXT, 
	cohort TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(cohort) REFERENCES "ClinicalCohort" (id)
);
