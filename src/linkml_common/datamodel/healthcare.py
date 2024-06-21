from __future__ import annotations 
from datetime import (
    datetime,
    date
)
from decimal import Decimal 
from enum import Enum 
import re
import sys
from typing import (
    Any,
    List,
    Literal,
    Dict,
    Optional,
    Union
)
from pydantic.version import VERSION  as PYDANTIC_VERSION 
if int(PYDANTIC_VERSION[0])>=2:
    from pydantic import (
        BaseModel,
        ConfigDict,
        Field,
        field_validator
    )
else:
    from pydantic import (
        BaseModel,
        Field,
        validator
    )

metamodel_version = "None"
version = "None"


class WeakRefShimBaseModel(BaseModel):
    __slots__ = '__weakref__'

class ConfiguredBaseModel(WeakRefShimBaseModel,
                validate_assignment = True,
                validate_all = True,
                underscore_attrs_are_private = True,
                extra = "forbid",
                arbitrary_types_allowed = True,
                use_enum_values = True):
    pass


class LandformEnum(str):
    pass


class RelativeTimeEnum(str, Enum):
    BEFORE = "BEFORE"
    AFTER = "AFTER"
    AT_SAME_TIME_AS = "AT_SAME_TIME_AS"


class OrganismTaxonEnum(str):
    pass


class HumanLanguageCodeEnum(str):
    """
    An enumeration of languages
    """
    pass


class PersonStatus(str, Enum):
    # the person is living
    ALIVE = "ALIVE"
    # the person is deceased
    DEAD = "DEAD"
    # the vital status is not known
    UNKNOWN = "UNKNOWN"


class OrganizationPersonnelRelationshipEnum(str):
    """
    ...
    """
    pass


class HealthcareEncounterClassification(str, Enum):
    # Person visiting hospital, at a Care Site, in bed, for duration of more than one day, with physicians and other Providers permanently available to deliver service around the clock
    Inpatient_Visit = "Inpatient Visit"
    # Person visiting dedicated healthcare institution for treating emergencies, at a Care Site, within one day, with physicians and Providers permanently available to deliver service around the clock
    Emergency_Room_Visit = "Emergency Room Visit"
    # Person visiting ER followed by a subsequent Inpatient Visit, where Emergency department is part of hospital, and transition from the ER to other hospital departments is undefined
    Emergency_Room_and_Inpatient_Visit = "Emergency Room and Inpatient Visit"
    # Person visiting dedicated institution for reasons of poor health, at a Care Site, long-term or permanently, with no physician but possibly other Providers permanently available to deliver service around the clock
    Non_hospital_institution_Visit = "Non-hospital institution Visit"
    # Person visiting dedicated ambulatory healthcare institution, at a Care Site, within one day, without bed, with physicians or medical Providers delivering service during Visit
    Outpatient_Visit = "Outpatient Visit"
    # Provider visiting Person, without a Care Site, within one day, delivering service
    Home_Visit = "Home Visit"
    # Patient engages with Provider through communication media
    Telehealth_Visit = "Telehealth Visit"
    # Person visiting pharmacy for dispensing of Drug, at a Care Site, within one day
    Pharmacy_Visit = "Pharmacy Visit"
    # Patient visiting dedicated institution, at a Care Site, within one day, for the purpose of a Measurement.
    Laboratory_Visit = "Laboratory Visit"
    # Person using transportation service for the purpose of initiating one of the other Visits, without a Care Site, within one day, potentially with Providers accompanying the Visit and delivering service
    Ambulance_Visit = "Ambulance Visit"
    # Person interacting with healthcare system, without a Care Site, within a day, with no Providers involved, for administrative purposes
    Case_Management_Visit = "Case Management Visit"


class Identified(ConfiguredBaseModel):
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")


class Typed(ConfiguredBaseModel):
    type: Literal["Typed"] = Field("Typed", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class Entity(Typed):
    """
    A physical, digital, conceptual, or other kind of thing with some common characteristics
    """
    type: Literal["Entity"] = Field("Entity", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class Intangible(Entity):
    """
    An entity that is not a physical object, process, or information
    """
    type: Literal["Intangible"] = Field("Intangible", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class PhysicalEntity(Entity, Identified):
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""")
    ontology_types: Optional[List[str]] = Field(default_factory=list, description="""A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.""")
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""")
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["PhysicalEntity"] = Field("PhysicalEntity", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class Concept(Intangible, Identified):
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["Concept"] = Field("Concept", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class InformationEntity(Intangible, Identified):
    """
    An entity that describes some information
    """
    describes: Optional[Any] = Field(None, description="""The thing that is being described""")
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["InformationEntity"] = Field("InformationEntity", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class PhysicalDevice(PhysicalEntity):
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""")
    ontology_types: Optional[List[str]] = Field(default_factory=list, description="""A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.""")
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""")
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["PhysicalDevice"] = Field("PhysicalDevice", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class StructuredValue(Intangible):
    """
    A value that is a structured collection of other values
    """
    type: Literal["StructuredValue"] = Field("StructuredValue", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class Role(Intangible):
    type: Literal["Role"] = Field("Role", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class Relationship(Intangible):
    subject: Optional[Union[Entity,Intangible,PhysicalEntity,Event,SubjectHistory,SubjectObservationHistory,ClinicalHistory,LifeEvent,Observation,HealthcareEncounter,HealthcareConditionOccurrence,Measurement,QualitativeObservation,PhysicalDevice,Place,IndividualOrganism,Organization,AutomatedAgent,CreativeWork,HealthcareOrganization,Person,VeterinaryAnimal,Landform,AstronomicalBody,HealthcareSite,Concept,InformationEntity,StructuredValue,Role,Relationship,EntitySet,Quantity,QuantityRange,TimePointOrTemporalInterval,Service,SetOfObservations,Variable,TemporalInterval,TimePoint,SimpleQuantity,Ratio,Duration,TemporalRelationship,OrganismalRelationship,PersonInRole,OrganizationPersonnelRelationship,OrganizationalRole,HealthcareRole,HealthcareProvider,Patient,Location,PostalAddress,PointLocation,GeoBoxLocation,GeoPointLocation,Specification,OrgChart,Procedure,QuantityKind,UnitConcept]] = Field(None)
    predicate: Optional[str] = Field(None)
    object: Optional[Union[Entity,Intangible,PhysicalEntity,Event,SubjectHistory,SubjectObservationHistory,ClinicalHistory,LifeEvent,Observation,HealthcareEncounter,HealthcareConditionOccurrence,Measurement,QualitativeObservation,PhysicalDevice,Place,IndividualOrganism,Organization,AutomatedAgent,CreativeWork,HealthcareOrganization,Person,VeterinaryAnimal,Landform,AstronomicalBody,HealthcareSite,Concept,InformationEntity,StructuredValue,Role,Relationship,EntitySet,Quantity,QuantityRange,TimePointOrTemporalInterval,Service,SetOfObservations,Variable,TemporalInterval,TimePoint,SimpleQuantity,Ratio,Duration,TemporalRelationship,OrganismalRelationship,PersonInRole,OrganizationPersonnelRelationship,OrganizationalRole,HealthcareRole,HealthcareProvider,Patient,Location,PostalAddress,PointLocation,GeoBoxLocation,GeoPointLocation,Specification,OrgChart,Procedure,QuantityKind,UnitConcept]] = Field(None)
    type: Literal["Relationship"] = Field("Relationship", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class Location(StructuredValue):
    type: Literal["Location"] = Field("Location", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class PointLocation(Location):
    type: Literal["PointLocation"] = Field("PointLocation", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class Specification(InformationEntity):
    """
    A specification of a thing
    """
    describes: Optional[Any] = Field(None, description="""The thing that is being described""")
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["Specification"] = Field("Specification", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class Procedure(Specification):
    """
    A canonical series of actions conducted in a certain order or manner
    """
    describes: Optional[Any] = Field(None, description="""The thing that is being described""")
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["Procedure"] = Field("Procedure", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class EntitySet(Intangible):
    """
    A group of things. The collection may be heterogeneous or homogeneous.
    """
    members: Optional[List[Union[Entity,Intangible,PhysicalEntity,Event,SubjectHistory,SubjectObservationHistory,ClinicalHistory,LifeEvent,Observation,HealthcareEncounter,HealthcareConditionOccurrence,Measurement,QualitativeObservation,PhysicalDevice,Place,IndividualOrganism,Organization,AutomatedAgent,CreativeWork,HealthcareOrganization,Person,VeterinaryAnimal,Landform,AstronomicalBody,HealthcareSite,Concept,InformationEntity,StructuredValue,Role,Relationship,EntitySet,Quantity,QuantityRange,TimePointOrTemporalInterval,Service,SetOfObservations,Variable,TemporalInterval,TimePoint,SimpleQuantity,Ratio,Duration,TemporalRelationship,OrganismalRelationship,PersonInRole,OrganizationPersonnelRelationship,OrganizationalRole,HealthcareRole,HealthcareProvider,Patient,Location,PostalAddress,PointLocation,GeoBoxLocation,GeoPointLocation,Specification,OrgChart,Procedure,QuantityKind,UnitConcept]]] = Field(default_factory=list, description="""The members of the collection""")
    type: Literal["EntitySet"] = Field("EntitySet", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class QuantityKind(Concept):
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["QuantityKind"] = Field("QuantityKind", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class Quantity(Intangible):
    has_quantity_kind: Optional[str] = Field(None, description="""The kind of quantity""")
    type: Literal["Quantity"] = Field("Quantity", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class SimpleQuantity(Quantity):
    """
    A quantity is a property that can be measured or counted
    """
    value: Optional[float] = Field(None, description="""The value of the quantity""")
    unit: Optional[str] = Field(None)
    has_quantity_kind: Optional[str] = Field(None, description="""The kind of quantity""")
    type: Literal["SimpleQuantity"] = Field("SimpleQuantity", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class Ratio(Quantity):
    """
    A tuple of two quantities
    """
    numerator: Optional[Union[Quantity,SimpleQuantity,Ratio,Duration]] = Field(None, description="""The numerator of the ratio""")
    denominator: Optional[Union[Quantity,SimpleQuantity,Ratio,Duration]] = Field(None, description="""The denominator of the ratio""")
    has_quantity_kind: Optional[str] = Field(None, description="""The kind of quantity""")
    type: Literal["Ratio"] = Field("Ratio", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class QuantityRange(Intangible):
    """
    A quantity range is a property that can be measured or counted
    """
    lower_bound: Optional[Union[Quantity,SimpleQuantity,Ratio,Duration]] = Field(None, description="""The lower bound of the range""")
    upper_bound: Optional[Union[Quantity,SimpleQuantity,Ratio,Duration]] = Field(None, description="""The upper bound of the range""")
    type: Literal["QuantityRange"] = Field("QuantityRange", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class UnitConcept(Concept):
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["UnitConcept"] = Field("UnitConcept", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class Place(PhysicalEntity):
    """
    Entities that have a somewhat fixed, physical extension.
    """
    address: Optional[PostalAddress] = Field(None)
    geolocation: Optional[GeoPointLocation] = Field(None, description="""The geolocation of the place""")
    bounding_coordinates: Optional[GeoBoxLocation] = Field(None, description="""The bounding coordinates of the place""")
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""")
    ontology_types: Optional[List[str]] = Field(default_factory=list, description="""A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.""")
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""")
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["Place"] = Field("Place", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class Landform(Place):
    """
    A natural feature of the solid surface of the Earth or other planetary body
    """
    address: Optional[PostalAddress] = Field(None)
    geolocation: Optional[GeoPointLocation] = Field(None, description="""The geolocation of the place""")
    bounding_coordinates: Optional[GeoBoxLocation] = Field(None, description="""The bounding coordinates of the place""")
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""")
    ontology_types: Optional[List[str]] = Field(default_factory=list, description="""A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.""")
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""")
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["Landform"] = Field("Landform", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class AstronomicalBody(Place):
    address: Optional[PostalAddress] = Field(None)
    geolocation: Optional[GeoPointLocation] = Field(None, description="""The geolocation of the place""")
    bounding_coordinates: Optional[GeoBoxLocation] = Field(None, description="""The bounding coordinates of the place""")
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""")
    ontology_types: Optional[List[str]] = Field(default_factory=list, description="""A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.""")
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""")
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["AstronomicalBody"] = Field("AstronomicalBody", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class PostalAddress(StructuredValue):
    """
    Represents an Address
    """
    street_address: Optional[str] = Field(None, description="""The street address""")
    street_address_additional: Optional[str] = Field(None)
    city: Optional[str] = Field(None, description="""The city""")
    state: Optional[str] = Field(None, description="""The state""")
    postal_code: Optional[str] = Field(None, description="""The postal code or zip code""")
    country: Optional[str] = Field(None, description="""The country""")
    type: Literal["PostalAddress"] = Field("PostalAddress", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class GeoPointLocation(PointLocation):
    latitude: Optional[Decimal] = Field(None, description="""The latitude of the location""")
    longitude: Optional[Decimal] = Field(None, description="""The longitude of the location""")
    altitude: Optional[Decimal] = Field(None, description="""The altitude of the location""")
    type: Literal["GeoPointLocation"] = Field("GeoPointLocation", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class GeoBoxLocation(Location):
    west_bounding_coordinate: Optional[Decimal] = Field(None, description="""The westernmost coordinate of the location""")
    east_bounding_coordinate: Optional[Decimal] = Field(None, description="""The easternmost coordinate of the location""")
    north_bounding_coordinate: Optional[Decimal] = Field(None, description="""The northernmost coordinate of the location""")
    south_bounding_coordinate: Optional[Decimal] = Field(None, description="""The southernmost coordinate of the location""")
    type: Literal["GeoBoxLocation"] = Field("GeoBoxLocation", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class Event(Entity, Identified):
    """
    A thing that happens
    """
    starts_at: Optional[TimePoint] = Field(None)
    ends_at: Optional[TimePoint] = Field(None)
    happens_at: Optional[TimePoint] = Field(None)
    has_interval: Optional[TemporalInterval] = Field(None)
    has_duration: Optional[Duration] = Field(None)
    is_ongoing_as_of: Optional[TimePoint] = Field(None)
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["Event"] = Field("Event", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class TimePointOrTemporalInterval(Intangible):
    starts_at: Optional[TimePoint] = Field(None)
    ends_at: Optional[TimePoint] = Field(None)
    type: Literal["TimePointOrTemporalInterval"] = Field("TimePointOrTemporalInterval", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class TemporalInterval(TimePointOrTemporalInterval):
    """
    A period of time
    """
    starts_at: Optional[TimePoint] = Field(None)
    ends_at: Optional[TimePoint] = Field(None)
    type: Literal["TemporalInterval"] = Field("TemporalInterval", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class TimePoint(TimePointOrTemporalInterval):
    """
    A point in time. Can be fully specified, or specified in relative terms.
    """
    year_value: Optional[int] = Field(None)
    date_value: Optional[date] = Field(None)
    time_value: Optional[str] = Field(None)
    datetime_value: Optional[datetime ] = Field(None)
    marker_event: Optional[str] = Field(None)
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""")
    starts_at: Optional[TimePoint] = Field(None)
    ends_at: Optional[TimePoint] = Field(None)
    type: Literal["TimePoint"] = Field("TimePoint", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class Duration(Quantity):
    """
    A length of time
    """
    has_quantity_kind: Optional[str] = Field(None, description="""The kind of quantity""")
    type: Literal["Duration"] = Field("Duration", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class TemporalRelationship(Relationship):
    """
    A relationship to another time point
    """
    predicate: Optional[RelativeTimeEnum] = Field(None, description="""The relationship between the two time points""")
    relative_to: Optional[Union[TemporalInterval, TimePoint, str]] = Field(None)
    subject: Optional[Union[Entity,Intangible,PhysicalEntity,Event,SubjectHistory,SubjectObservationHistory,ClinicalHistory,LifeEvent,Observation,HealthcareEncounter,HealthcareConditionOccurrence,Measurement,QualitativeObservation,PhysicalDevice,Place,IndividualOrganism,Organization,AutomatedAgent,CreativeWork,HealthcareOrganization,Person,VeterinaryAnimal,Landform,AstronomicalBody,HealthcareSite,Concept,InformationEntity,StructuredValue,Role,Relationship,EntitySet,Quantity,QuantityRange,TimePointOrTemporalInterval,Service,SetOfObservations,Variable,TemporalInterval,TimePoint,SimpleQuantity,Ratio,Duration,TemporalRelationship,OrganismalRelationship,PersonInRole,OrganizationPersonnelRelationship,OrganizationalRole,HealthcareRole,HealthcareProvider,Patient,Location,PostalAddress,PointLocation,GeoBoxLocation,GeoPointLocation,Specification,OrgChart,Procedure,QuantityKind,UnitConcept]] = Field(None)
    object: Optional[Union[Entity,Intangible,PhysicalEntity,Event,SubjectHistory,SubjectObservationHistory,ClinicalHistory,LifeEvent,Observation,HealthcareEncounter,HealthcareConditionOccurrence,Measurement,QualitativeObservation,PhysicalDevice,Place,IndividualOrganism,Organization,AutomatedAgent,CreativeWork,HealthcareOrganization,Person,VeterinaryAnimal,Landform,AstronomicalBody,HealthcareSite,Concept,InformationEntity,StructuredValue,Role,Relationship,EntitySet,Quantity,QuantityRange,TimePointOrTemporalInterval,Service,SetOfObservations,Variable,TemporalInterval,TimePoint,SimpleQuantity,Ratio,Duration,TemporalRelationship,OrganismalRelationship,PersonInRole,OrganizationPersonnelRelationship,OrganizationalRole,HealthcareRole,HealthcareProvider,Patient,Location,PostalAddress,PointLocation,GeoBoxLocation,GeoPointLocation,Specification,OrgChart,Procedure,QuantityKind,UnitConcept]] = Field(None)
    type: Literal["TemporalRelationship"] = Field("TemporalRelationship", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class SubjectHistory(Entity):
    subject: str = Field(...)
    events: Optional[List[str]] = Field(default_factory=list)
    over_interval: Optional[TemporalInterval] = Field(None)
    type: Literal["SubjectHistory"] = Field("SubjectHistory", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class IndividualOrganism(PhysicalEntity):
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""")
    ontology_types: Optional[List[str]] = Field(default_factory=list, description="""A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.""")
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""")
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["IndividualOrganism"] = Field("IndividualOrganism", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class OrganismalRelationship(Relationship):
    subject: Optional[Union[Entity,Intangible,PhysicalEntity,Event,SubjectHistory,SubjectObservationHistory,ClinicalHistory,LifeEvent,Observation,HealthcareEncounter,HealthcareConditionOccurrence,Measurement,QualitativeObservation,PhysicalDevice,Place,IndividualOrganism,Organization,AutomatedAgent,CreativeWork,HealthcareOrganization,Person,VeterinaryAnimal,Landform,AstronomicalBody,HealthcareSite,Concept,InformationEntity,StructuredValue,Role,Relationship,EntitySet,Quantity,QuantityRange,TimePointOrTemporalInterval,Service,SetOfObservations,Variable,TemporalInterval,TimePoint,SimpleQuantity,Ratio,Duration,TemporalRelationship,OrganismalRelationship,PersonInRole,OrganizationPersonnelRelationship,OrganizationalRole,HealthcareRole,HealthcareProvider,Patient,Location,PostalAddress,PointLocation,GeoBoxLocation,GeoPointLocation,Specification,OrgChart,Procedure,QuantityKind,UnitConcept]] = Field(None)
    predicate: Optional[str] = Field(None)
    object: Optional[Union[Entity,Intangible,PhysicalEntity,Event,SubjectHistory,SubjectObservationHistory,ClinicalHistory,LifeEvent,Observation,HealthcareEncounter,HealthcareConditionOccurrence,Measurement,QualitativeObservation,PhysicalDevice,Place,IndividualOrganism,Organization,AutomatedAgent,CreativeWork,HealthcareOrganization,Person,VeterinaryAnimal,Landform,AstronomicalBody,HealthcareSite,Concept,InformationEntity,StructuredValue,Role,Relationship,EntitySet,Quantity,QuantityRange,TimePointOrTemporalInterval,Service,SetOfObservations,Variable,TemporalInterval,TimePoint,SimpleQuantity,Ratio,Duration,TemporalRelationship,OrganismalRelationship,PersonInRole,OrganizationPersonnelRelationship,OrganizationalRole,HealthcareRole,HealthcareProvider,Patient,Location,PostalAddress,PointLocation,GeoBoxLocation,GeoPointLocation,Specification,OrgChart,Procedure,QuantityKind,UnitConcept]] = Field(None)
    type: Literal["OrganismalRelationship"] = Field("OrganismalRelationship", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class Agent(ConfiguredBaseModel):
    """
    Represents an Agent
    """
    pass


class Person(Agent, IndividualOrganism):
    """
    Represents a Person
    """
    primary_email: Optional[str] = Field(None, description="""The main email address of a person""")
    birth_date: Optional[date] = Field(None, description="""Date on which a person is born""")
    age_in_years: Optional[int] = Field(None, description="""Number of years since birth""")
    vital_status: Optional[PersonStatus] = Field(None, description="""living or dead status""")
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""")
    ontology_types: Optional[List[str]] = Field(default_factory=list, description="""A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.""")
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""")
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["Person"] = Field("Person", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")

    @validator('primary_email', allow_reuse=True)
    def pattern_primary_email(cls, v):
        pattern=re.compile(r"^\S+@[\S+\.]+\S+")
        if isinstance(v,list):
            for element in v:
                if not pattern.match(element):
                    raise ValueError(f"Invalid primary_email format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid primary_email format: {v}")
        return v


class VeterinaryAnimal(IndividualOrganism):
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""")
    ontology_types: Optional[List[str]] = Field(default_factory=list, description="""A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.""")
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""")
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["VeterinaryAnimal"] = Field("VeterinaryAnimal", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class Organization(Agent, PhysicalEntity):
    """
    Represents an Organization
    """
    provides_services: Optional[List[Service]] = Field(default_factory=list)
    has_person_roles: Optional[List[PersonInRole]] = Field(default_factory=list)
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""")
    ontology_types: Optional[List[str]] = Field(default_factory=list, description="""A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.""")
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""")
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["Organization"] = Field("Organization", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class OrganizationalRole(Role):
    type: Literal["OrganizationalRole"] = Field("OrganizationalRole", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class OrgChart(InformationEntity):
    for_organization: Optional[str] = Field(None)
    relationships: Optional[OrganizationPersonnelRelationship] = Field(None)
    describes: Optional[Any] = Field(None, description="""The thing that is being described""")
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["OrgChart"] = Field("OrgChart", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class PersonInRole(Relationship):
    subject_person: Optional[str] = Field(None)
    person_role: Optional[OrganizationalRole] = Field(None)
    subject: Optional[Union[Entity,Intangible,PhysicalEntity,Event,SubjectHistory,SubjectObservationHistory,ClinicalHistory,LifeEvent,Observation,HealthcareEncounter,HealthcareConditionOccurrence,Measurement,QualitativeObservation,PhysicalDevice,Place,IndividualOrganism,Organization,AutomatedAgent,CreativeWork,HealthcareOrganization,Person,VeterinaryAnimal,Landform,AstronomicalBody,HealthcareSite,Concept,InformationEntity,StructuredValue,Role,Relationship,EntitySet,Quantity,QuantityRange,TimePointOrTemporalInterval,Service,SetOfObservations,Variable,TemporalInterval,TimePoint,SimpleQuantity,Ratio,Duration,TemporalRelationship,OrganismalRelationship,PersonInRole,OrganizationPersonnelRelationship,OrganizationalRole,HealthcareRole,HealthcareProvider,Patient,Location,PostalAddress,PointLocation,GeoBoxLocation,GeoPointLocation,Specification,OrgChart,Procedure,QuantityKind,UnitConcept]] = Field(None)
    predicate: Optional[str] = Field(None)
    object: Optional[Union[Entity,Intangible,PhysicalEntity,Event,SubjectHistory,SubjectObservationHistory,ClinicalHistory,LifeEvent,Observation,HealthcareEncounter,HealthcareConditionOccurrence,Measurement,QualitativeObservation,PhysicalDevice,Place,IndividualOrganism,Organization,AutomatedAgent,CreativeWork,HealthcareOrganization,Person,VeterinaryAnimal,Landform,AstronomicalBody,HealthcareSite,Concept,InformationEntity,StructuredValue,Role,Relationship,EntitySet,Quantity,QuantityRange,TimePointOrTemporalInterval,Service,SetOfObservations,Variable,TemporalInterval,TimePoint,SimpleQuantity,Ratio,Duration,TemporalRelationship,OrganismalRelationship,PersonInRole,OrganizationPersonnelRelationship,OrganizationalRole,HealthcareRole,HealthcareProvider,Patient,Location,PostalAddress,PointLocation,GeoBoxLocation,GeoPointLocation,Specification,OrgChart,Procedure,QuantityKind,UnitConcept]] = Field(None)
    type: Literal["PersonInRole"] = Field("PersonInRole", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class OrganizationPersonnelRelationship(Relationship):
    subject: Optional[str] = Field(None)
    predicate: Optional[str] = Field(None)
    object: Optional[str] = Field(None)
    type: Literal["OrganizationPersonnelRelationship"] = Field("OrganizationPersonnelRelationship", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class AutomatedAgent(Agent, PhysicalEntity):
    """
    Represents an Automated Agent
    """
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""")
    ontology_types: Optional[List[str]] = Field(default_factory=list, description="""A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.""")
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""")
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["AutomatedAgent"] = Field("AutomatedAgent", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class LifeEvent(Event):
    starts_at: Optional[TimePoint] = Field(None)
    ends_at: Optional[TimePoint] = Field(None)
    happens_at: Optional[TimePoint] = Field(None)
    has_interval: Optional[TemporalInterval] = Field(None)
    has_duration: Optional[Duration] = Field(None)
    is_ongoing_as_of: Optional[TimePoint] = Field(None)
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["LifeEvent"] = Field("LifeEvent", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class CreationMetadata(ConfiguredBaseModel):
    title: Optional[str] = Field(None, description="""The title of the item""")
    abstract: Optional[str] = Field(None, description="""A summary of the item""")
    rights: Optional[str] = Field(None, description="""Information about rights held in and over the item""")
    creators: Optional[List[str]] = Field(default_factory=list, description="""The person or organization who created the work""")
    contributors: Optional[List[str]] = Field(default_factory=list, description="""A person or organization that contributed to the creation of the work""")
    contacts: Optional[List[str]] = Field(default_factory=list, description="""A contact point for a person or organization""")
    keywords: Optional[List[str]] = Field(default_factory=list, description="""Keywords or tags used to describe this item""")


class CreativeWork(CreationMetadata, PhysicalEntity):
    """
    The most generic kind of creative work, including books, movies, photographs, software programs, etc.
    """
    title: Optional[str] = Field(None, description="""The title of the item""")
    abstract: Optional[str] = Field(None, description="""A summary of the item""")
    rights: Optional[str] = Field(None, description="""Information about rights held in and over the item""")
    creators: Optional[List[str]] = Field(default_factory=list, description="""The person or organization who created the work""")
    contributors: Optional[List[str]] = Field(default_factory=list, description="""A person or organization that contributed to the creation of the work""")
    contacts: Optional[List[str]] = Field(default_factory=list, description="""A contact point for a person or organization""")
    keywords: Optional[List[str]] = Field(default_factory=list, description="""Keywords or tags used to describe this item""")
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""")
    ontology_types: Optional[List[str]] = Field(default_factory=list, description="""A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.""")
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""")
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["CreativeWork"] = Field("CreativeWork", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class Service(Intangible):
    """
    A service provided by an organization
    """
    type: Literal["Service"] = Field("Service", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class Observation(Event):
    """
    A statement about the state of something
    """
    observation_subject: Optional[Union[Entity,Intangible,PhysicalEntity,Event,SubjectHistory,SubjectObservationHistory,ClinicalHistory,LifeEvent,Observation,HealthcareEncounter,HealthcareConditionOccurrence,Measurement,QualitativeObservation,PhysicalDevice,Place,IndividualOrganism,Organization,AutomatedAgent,CreativeWork,HealthcareOrganization,Person,VeterinaryAnimal,Landform,AstronomicalBody,HealthcareSite,Concept,InformationEntity,StructuredValue,Role,Relationship,EntitySet,Quantity,QuantityRange,TimePointOrTemporalInterval,Service,SetOfObservations,Variable,TemporalInterval,TimePoint,SimpleQuantity,Ratio,Duration,TemporalRelationship,OrganismalRelationship,PersonInRole,OrganizationPersonnelRelationship,OrganizationalRole,HealthcareRole,HealthcareProvider,Patient,Location,PostalAddress,PointLocation,GeoBoxLocation,GeoPointLocation,Specification,OrgChart,Procedure,QuantityKind,UnitConcept]] = Field(None)
    variable_measured: Optional[Variable] = Field(None, description="""The variable being measured""")
    measured_using: Optional[str] = Field(None)
    starts_at: Optional[TimePoint] = Field(None)
    ends_at: Optional[TimePoint] = Field(None)
    happens_at: Optional[TimePoint] = Field(None)
    has_interval: Optional[TemporalInterval] = Field(None)
    has_duration: Optional[Duration] = Field(None)
    is_ongoing_as_of: Optional[TimePoint] = Field(None)
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["Observation"] = Field("Observation", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class SetOfObservations(Intangible):
    observation_subject: Optional[Union[Entity,Intangible,PhysicalEntity,Event,SubjectHistory,SubjectObservationHistory,ClinicalHistory,LifeEvent,Observation,HealthcareEncounter,HealthcareConditionOccurrence,Measurement,QualitativeObservation,PhysicalDevice,Place,IndividualOrganism,Organization,AutomatedAgent,CreativeWork,HealthcareOrganization,Person,VeterinaryAnimal,Landform,AstronomicalBody,HealthcareSite,Concept,InformationEntity,StructuredValue,Role,Relationship,EntitySet,Quantity,QuantityRange,TimePointOrTemporalInterval,Service,SetOfObservations,Variable,TemporalInterval,TimePoint,SimpleQuantity,Ratio,Duration,TemporalRelationship,OrganismalRelationship,PersonInRole,OrganizationPersonnelRelationship,OrganizationalRole,HealthcareRole,HealthcareProvider,Patient,Location,PostalAddress,PointLocation,GeoBoxLocation,GeoPointLocation,Specification,OrgChart,Procedure,QuantityKind,UnitConcept]] = Field(None)
    observations: Optional[Union[Observation,Measurement,QualitativeObservation]] = Field(None)
    type: Literal["SetOfObservations"] = Field("SetOfObservations", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class SubjectObservationHistory(SubjectHistory):
    observations: Optional[List[Union[Observation,Measurement,QualitativeObservation]]] = Field(default_factory=list)
    measurements: Optional[List[Measurement]] = Field(default_factory=list)
    interpretations: Optional[List[Union[Observation,Measurement,QualitativeObservation]]] = Field(default_factory=list)
    subject: str = Field(...)
    events: Optional[List[str]] = Field(default_factory=list)
    over_interval: Optional[TemporalInterval] = Field(None)
    type: Literal["SubjectObservationHistory"] = Field("SubjectObservationHistory", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class Measurement(Observation):
    quantity_measured: Optional[Union[Quantity,SimpleQuantity,Ratio,Duration]] = Field(None, description="""The quantity being measured""")
    observation_subject: Optional[Union[Entity,Intangible,PhysicalEntity,Event,SubjectHistory,SubjectObservationHistory,ClinicalHistory,LifeEvent,Observation,HealthcareEncounter,HealthcareConditionOccurrence,Measurement,QualitativeObservation,PhysicalDevice,Place,IndividualOrganism,Organization,AutomatedAgent,CreativeWork,HealthcareOrganization,Person,VeterinaryAnimal,Landform,AstronomicalBody,HealthcareSite,Concept,InformationEntity,StructuredValue,Role,Relationship,EntitySet,Quantity,QuantityRange,TimePointOrTemporalInterval,Service,SetOfObservations,Variable,TemporalInterval,TimePoint,SimpleQuantity,Ratio,Duration,TemporalRelationship,OrganismalRelationship,PersonInRole,OrganizationPersonnelRelationship,OrganizationalRole,HealthcareRole,HealthcareProvider,Patient,Location,PostalAddress,PointLocation,GeoBoxLocation,GeoPointLocation,Specification,OrgChart,Procedure,QuantityKind,UnitConcept]] = Field(None)
    variable_measured: Optional[Variable] = Field(None, description="""The variable being measured""")
    measured_using: Optional[str] = Field(None)
    starts_at: Optional[TimePoint] = Field(None)
    ends_at: Optional[TimePoint] = Field(None)
    happens_at: Optional[TimePoint] = Field(None)
    has_interval: Optional[TemporalInterval] = Field(None)
    has_duration: Optional[Duration] = Field(None)
    is_ongoing_as_of: Optional[TimePoint] = Field(None)
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["Measurement"] = Field("Measurement", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class QualitativeObservation(Observation):
    observation_subject: Optional[Union[Entity,Intangible,PhysicalEntity,Event,SubjectHistory,SubjectObservationHistory,ClinicalHistory,LifeEvent,Observation,HealthcareEncounter,HealthcareConditionOccurrence,Measurement,QualitativeObservation,PhysicalDevice,Place,IndividualOrganism,Organization,AutomatedAgent,CreativeWork,HealthcareOrganization,Person,VeterinaryAnimal,Landform,AstronomicalBody,HealthcareSite,Concept,InformationEntity,StructuredValue,Role,Relationship,EntitySet,Quantity,QuantityRange,TimePointOrTemporalInterval,Service,SetOfObservations,Variable,TemporalInterval,TimePoint,SimpleQuantity,Ratio,Duration,TemporalRelationship,OrganismalRelationship,PersonInRole,OrganizationPersonnelRelationship,OrganizationalRole,HealthcareRole,HealthcareProvider,Patient,Location,PostalAddress,PointLocation,GeoBoxLocation,GeoPointLocation,Specification,OrgChart,Procedure,QuantityKind,UnitConcept]] = Field(None)
    variable_measured: Optional[Variable] = Field(None, description="""The variable being measured""")
    measured_using: Optional[str] = Field(None)
    starts_at: Optional[TimePoint] = Field(None)
    ends_at: Optional[TimePoint] = Field(None)
    happens_at: Optional[TimePoint] = Field(None)
    has_interval: Optional[TemporalInterval] = Field(None)
    has_duration: Optional[Duration] = Field(None)
    is_ongoing_as_of: Optional[TimePoint] = Field(None)
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["QualitativeObservation"] = Field("QualitativeObservation", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class Variable(Intangible):
    allowed_units: Optional[List[str]] = Field(default_factory=list, description="""The units that are allowed for this variable""")
    type: Literal["Variable"] = Field("Variable", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class HealthcareSite(Place):
    address: Optional[PostalAddress] = Field(None)
    geolocation: Optional[GeoPointLocation] = Field(None, description="""The geolocation of the place""")
    bounding_coordinates: Optional[GeoBoxLocation] = Field(None, description="""The bounding coordinates of the place""")
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""")
    ontology_types: Optional[List[str]] = Field(default_factory=list, description="""A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.""")
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""")
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["HealthcareSite"] = Field("HealthcareSite", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class HealthcareEncounter(Event):
    """
    An interaction between a patient and one or more healthcare providers
    """
    patient: Optional[Patient] = Field(None)
    provider: Optional[HealthcareProvider] = Field(None)
    starts_at: Optional[TimePoint] = Field(None)
    ends_at: Optional[TimePoint] = Field(None)
    happens_at: Optional[TimePoint] = Field(None)
    has_interval: Optional[TemporalInterval] = Field(None)
    has_duration: Optional[Duration] = Field(None)
    is_ongoing_as_of: Optional[TimePoint] = Field(None)
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["HealthcareEncounter"] = Field("HealthcareEncounter", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class HealthcareOrganization(Organization):
    """
    An organization that provides healthcare services
    """
    provides_services: Optional[List[Service]] = Field(default_factory=list)
    has_person_roles: Optional[List[PersonInRole]] = Field(default_factory=list)
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""")
    ontology_types: Optional[List[str]] = Field(default_factory=list, description="""A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.""")
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""")
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["HealthcareOrganization"] = Field("HealthcareOrganization", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class HealthcareRole(Role):
    is_person: Optional[str] = Field(None)
    type: Literal["HealthcareRole"] = Field("HealthcareRole", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class HealthcareProvider(HealthcareRole):
    speciality: Optional[str] = Field(None)
    care_site: Optional[str] = Field(None)
    is_person: Optional[str] = Field(None)
    type: Literal["HealthcareProvider"] = Field("HealthcareProvider", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class HealthcareConditionOccurrence(Event):
    patient: Optional[Patient] = Field(None)
    observed_during: Optional[str] = Field(None)
    starts_at: Optional[TimePoint] = Field(None)
    ends_at: Optional[TimePoint] = Field(None)
    happens_at: Optional[TimePoint] = Field(None)
    has_interval: Optional[TemporalInterval] = Field(None)
    has_duration: Optional[Duration] = Field(None)
    is_ongoing_as_of: Optional[TimePoint] = Field(None)
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["HealthcareConditionOccurrence"] = Field("HealthcareConditionOccurrence", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class Patient(HealthcareRole):
    is_person: Optional[str] = Field(None)
    type: Literal["Patient"] = Field("Patient", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class ClinicalHistory(SubjectObservationHistory):
    subject: Optional[str] = Field(None)
    observations: Optional[List[Union[Observation,Measurement,QualitativeObservation]]] = Field(default_factory=list)
    measurements: Optional[List[Measurement]] = Field(default_factory=list)
    interpretations: Optional[List[Union[Observation,Measurement,QualitativeObservation]]] = Field(default_factory=list)
    events: Optional[List[str]] = Field(default_factory=list)
    over_interval: Optional[TemporalInterval] = Field(None)
    type: Literal["ClinicalHistory"] = Field("ClinicalHistory", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


# Update forward refs
# see https://pydantic-docs.helpmanual.io/usage/postponed_annotations/
Identified.update_forward_refs()
Typed.update_forward_refs()
Entity.update_forward_refs()
Intangible.update_forward_refs()
PhysicalEntity.update_forward_refs()
Concept.update_forward_refs()
InformationEntity.update_forward_refs()
PhysicalDevice.update_forward_refs()
StructuredValue.update_forward_refs()
Role.update_forward_refs()
Relationship.update_forward_refs()
Location.update_forward_refs()
PointLocation.update_forward_refs()
Specification.update_forward_refs()
Procedure.update_forward_refs()
EntitySet.update_forward_refs()
QuantityKind.update_forward_refs()
Quantity.update_forward_refs()
SimpleQuantity.update_forward_refs()
Ratio.update_forward_refs()
QuantityRange.update_forward_refs()
UnitConcept.update_forward_refs()
Place.update_forward_refs()
Landform.update_forward_refs()
AstronomicalBody.update_forward_refs()
PostalAddress.update_forward_refs()
GeoPointLocation.update_forward_refs()
GeoBoxLocation.update_forward_refs()
Event.update_forward_refs()
TimePointOrTemporalInterval.update_forward_refs()
TemporalInterval.update_forward_refs()
TimePoint.update_forward_refs()
Duration.update_forward_refs()
TemporalRelationship.update_forward_refs()
SubjectHistory.update_forward_refs()
IndividualOrganism.update_forward_refs()
OrganismalRelationship.update_forward_refs()
Agent.update_forward_refs()
Person.update_forward_refs()
VeterinaryAnimal.update_forward_refs()
Organization.update_forward_refs()
OrganizationalRole.update_forward_refs()
OrgChart.update_forward_refs()
PersonInRole.update_forward_refs()
OrganizationPersonnelRelationship.update_forward_refs()
AutomatedAgent.update_forward_refs()
LifeEvent.update_forward_refs()
CreationMetadata.update_forward_refs()
CreativeWork.update_forward_refs()
Service.update_forward_refs()
Observation.update_forward_refs()
SetOfObservations.update_forward_refs()
SubjectObservationHistory.update_forward_refs()
Measurement.update_forward_refs()
QualitativeObservation.update_forward_refs()
Variable.update_forward_refs()
HealthcareSite.update_forward_refs()
HealthcareEncounter.update_forward_refs()
HealthcareOrganization.update_forward_refs()
HealthcareRole.update_forward_refs()
HealthcareProvider.update_forward_refs()
HealthcareConditionOccurrence.update_forward_refs()
Patient.update_forward_refs()
ClinicalHistory.update_forward_refs()

