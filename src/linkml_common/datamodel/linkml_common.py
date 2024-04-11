# Auto generated from linkml_common.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-04-09T19:01:35
# Schema: linkml-common
#
# id: https://w3id.org/linkml/linkml-common
# description: Common Data Model Elements
# license: MIT

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from datetime import date, datetime
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Date, Datetime, Decimal, Float, Integer, String, Time, Uri, Uriorcurie
from linkml_runtime.utils.metamodelcore import Decimal, URI, URIorCURIE, XSDDate, XSDDateTime, XSDTime

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BFO = CurieNamespace('BFO', 'http://purl.obolibrary.org/obo/BFO_')
ENVO = CurieNamespace('ENVO', 'http://purl.obolibrary.org/obo/ENVO_')
IAO = CurieNamespace('IAO', 'http://purl.obolibrary.org/obo/IAO_')
OBI = CurieNamespace('OBI', 'http://purl.obolibrary.org/obo/OBI_')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
UCUM = CurieNamespace('UCUM', 'http://example.org/UNKNOWN/UCUM/')
UO = CurieNamespace('UO', 'http://example.org/UNKNOWN/UO/')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
FHIR = CurieNamespace('fhir', 'http://hl7.org/fhir/')
FIBO = CurieNamespace('fibo', 'https://spec.edmcouncil.org/fibo/ontology/FBC')
FIBO_DATESANDTIMES = CurieNamespace('fibo_DatesAndTimes', 'https://www.omg.org/spec/Commons/DatesAndTimes/')
FIBO_QUANTITIESANDUNITS = CurieNamespace('fibo_QuantitiesAndUnits', 'https://www.omg.org/spec/Commons/QuantitiesAndUnits/')
FIBO_COMMONS_PARTIESANDSITUATIONS = CurieNamespace('fibo_commons_PartiesAndSituations', 'https://spec.edmcouncil.org/fibo/ontology/FBC/ommons/PartiesAndSituations/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
LINKML_COMMON = CurieNamespace('linkml_common', 'https://w3id.org/linkml-common/')
NMDCSCHEMA = CurieNamespace('nmdcschema', 'http://example.org/UNKNOWN/nmdcschema/')
OMOPSCHEMA = CurieNamespace('omopschema', 'http://example.org/omop/')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
QUDT = CurieNamespace('qudt', 'http://qudt.org/vocab/unit/')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = LINKML_COMMON


# Types

# Class references
class NamedThingId(URIorCURIE):
    pass


class ConceptId(NamedThingId):
    pass


class InformationEntityId(NamedThingId):
    pass


class PhysicalDeviceId(NamedThingId):
    pass


class SpecificationId(NamedThingId):
    pass


class ProcedureId(SpecificationId):
    pass


class BuiltEnvironmentFeatureId(NamedThingId):
    pass


class FacilityId(BuiltEnvironmentFeatureId):
    pass


class BuildingId(FacilityId):
    pass


class BuiltSystemId(BuiltEnvironmentFeatureId):
    pass


class ClinicalCohortId(NamedThingId):
    pass


class ClinicalCohortDefinitionId(NamedThingId):
    pass


class EngineeringSpecificationId(ProcedureId):
    pass


class RawMaterialId(NamedThingId):
    pass


class EquipmentId(NamedThingId):
    pass


class PowerPlantId(BuildingId):
    pass


class PowerPlantTypeId(ConceptId):
    pass


class FossilFuelPlantId(PowerPlantId):
    pass


class NuclearPlantId(PowerPlantId):
    pass


class RenewablePlantId(PowerPlantId):
    pass


class HydroelectricPlantId(RenewablePlantId):
    pass


class SolarPlantId(RenewablePlantId):
    pass


class WindFarmId(RenewablePlantId):
    pass


class FossilFuelId(ConceptId):
    pass


class ElectricalGridId(BuiltSystemId):
    pass


class ExtractiveIndustryFacilityId(FacilityId):
    pass


class MiningFacilityId(ExtractiveIndustryFacilityId):
    pass


class WellFacilityId(ExtractiveIndustryFacilityId):
    pass


class QuarryFacilityId(ExtractiveIndustryFacilityId):
    pass


class ExtractiveIndustryEquipmentId(EquipmentId):
    pass


class ExtractiveIndustryProductId(ConceptId):
    pass


class ExtractiveIndustryWasteId(ConceptId):
    pass


class CurrencyConceptId(ConceptId):
    pass


class FoodRecipeId(ProcedureId):
    pass


class FoodTypeConceptId(ConceptId):
    pass


class BasicFoodTypeId(FoodTypeConceptId):
    pass


class CompositeFoodTypeId(FoodTypeConceptId):
    pass


class PlaceId(NamedThingId):
    pass


class EnvironmentalSiteId(PlaceId):
    pass


class LandformId(PlaceId):
    pass


class HealthcareSiteId(PlaceId):
    pass


class InvestigationId(NamedThingId):
    pass


class InvestigativeProtocolId(ProcedureId):
    pass


class StudyDesignId(ProcedureId):
    pass


class SampleMaterialId(NamedThingId):
    pass


class QuantityKindId(ConceptId):
    pass


class UnitConceptId(ConceptId):
    pass


class AgentId(NamedThingId):
    pass


class PersonId(AgentId):
    pass


class OrganizationId(AgentId):
    pass


class HealthcareOrganizationId(OrganizationId):
    pass


class AutomatedAgentId(AgentId):
    pass


class CreativeWorkId(NamedThingId):
    pass


class PublicationId(CreativeWorkId):
    pass


class DatasetId(CreativeWorkId):
    pass


class EventId(NamedThingId):
    pass


class ClinicalCohortEnrollmentId(EventId):
    pass


class EngineeringProcessId(EventId):
    pass


class HealthcareEncounterId(EventId):
    pass


class HealthcareConditionOccurrenceId(EventId):
    pass


class LifeEventId(EventId):
    pass


class PlannedProcessId(EventId):
    pass


class InvestigativeProcessId(PlannedProcessId):
    pass


class SampleCollectionProcessId(InvestigativeProcessId):
    pass


class DataGenerationFromSampleId(InvestigativeProcessId):
    pass


class MaterialCollectionId(PlannedProcessId):
    pass


class MaterialProcessingId(PlannedProcessId):
    pass


class EngineeringMaterialProcessingId(MaterialProcessingId):
    pass


class FoodProcessingId(MaterialProcessingId):
    pass


class SampleProcessingId(MaterialProcessingId):
    pass


@dataclass
class Entity(YAMLRoot):
    """
    A physical, digital, conceptual, or other kind of thing with some common characteristics
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Thing"]
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "Entity"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.Entity

    type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self.type = str(self.class_name)

        super().__post_init__(**kwargs)


    def __new__(cls, *args, **kwargs):

        type_designator = "type"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_name", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_name']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



@dataclass
class NamedThing(Entity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["NamedThing"]
    class_class_curie: ClassVar[str] = "linkml_common:NamedThing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.NamedThing

    id: Union[str, NamedThingId] = None
    name: Optional[str] = None
    type: Optional[str] = None
    classification: Optional[Union[str, ConceptId]] = None
    ontology_types: Optional[Union[Union[str, ConceptId], List[Union[str, ConceptId]]]] = empty_list()
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        self.type = str(self.class_name)

        if self.classification is not None and not isinstance(self.classification, ConceptId):
            self.classification = ConceptId(self.classification)

        if not isinstance(self.ontology_types, list):
            self.ontology_types = [self.ontology_types] if self.ontology_types is not None else []
        self.ontology_types = [v if isinstance(v, ConceptId) else ConceptId(v) for v in self.ontology_types]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


    def __new__(cls, *args, **kwargs):

        type_designator = "type"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_name", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_name']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



@dataclass
class Concept(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["Concept"]
    class_class_curie: ClassVar[str] = "linkml_common:Concept"
    class_name: ClassVar[str] = "Concept"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.Concept

    id: Union[str, ConceptId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConceptId):
            self.id = ConceptId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class InformationEntity(NamedThing):
    """
    An entity that describes some information
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["InformationEntity"]
    class_class_curie: ClassVar[str] = "linkml_common:InformationEntity"
    class_name: ClassVar[str] = "InformationEntity"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.InformationEntity

    id: Union[str, InformationEntityId] = None
    describes: Optional[Union[dict, "Any"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InformationEntityId):
            self.id = InformationEntityId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class PhysicalDevice(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["PhysicalDevice"]
    class_class_curie: ClassVar[str] = "linkml_common:PhysicalDevice"
    class_name: ClassVar[str] = "PhysicalDevice"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.PhysicalDevice

    id: Union[str, PhysicalDeviceId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PhysicalDeviceId):
            self.id = PhysicalDeviceId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


class Intangible(Entity):
    """
    An entity that is not a physical object, process, or information
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Intangible"]
    class_class_curie: ClassVar[str] = "schema:Intangible"
    class_name: ClassVar[str] = "Intangible"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.Intangible


    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


class Role(Intangible):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Role"]
    class_class_curie: ClassVar[str] = "schema:Role"
    class_name: ClassVar[str] = "Role"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.Role


    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


class Relationship(Intangible):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["Relationship"]
    class_class_curie: ClassVar[str] = "linkml_common:Relationship"
    class_name: ClassVar[str] = "Relationship"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.Relationship


    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


class Location(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["Location"]
    class_class_curie: ClassVar[str] = "linkml_common:Location"
    class_name: ClassVar[str] = "Location"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.Location


class PointLocation(Location):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["PointLocation"]
    class_class_curie: ClassVar[str] = "linkml_common:PointLocation"
    class_name: ClassVar[str] = "PointLocation"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.PointLocation


class Observation(Entity):
    """
    A statement about the state of something
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["Observation"]
    class_class_curie: ClassVar[str] = "linkml_common:Observation"
    class_name: ClassVar[str] = "Observation"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.Observation


    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class Specification(NamedThing):
    """
    A specification of a thing
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["Specification"]
    class_class_curie: ClassVar[str] = "linkml_common:Specification"
    class_name: ClassVar[str] = "Specification"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.Specification

    id: Union[str, SpecificationId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SpecificationId):
            self.id = SpecificationId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class Procedure(Specification):
    """
    A canonical series of actions conducted in a certain order or manner
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["Procedure"]
    class_class_curie: ClassVar[str] = "linkml_common:Procedure"
    class_name: ClassVar[str] = "Procedure"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.Procedure

    id: Union[str, ProcedureId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProcedureId):
            self.id = ProcedureId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class MathematicalOperation(YAMLRoot):
    """
    Application of a mathematical operation to one or more inputs to produce one or more outputs
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["MathematicalOperation"]
    class_class_curie: ClassVar[str] = "linkml_common:MathematicalOperation"
    class_name: ClassVar[str] = "MathematicalOperation"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.MathematicalOperation

    inputs: Optional[Union[Union[dict, "Any"], List[Union[dict, "Any"]]]] = empty_list()
    outputs: Optional[Union[Union[dict, "Any"], List[Union[dict, "Any"]]]] = empty_list()
    parts: Optional[Union[Union[dict, "MathematicalOperation"], List[Union[dict, "MathematicalOperation"]]]] = empty_list()
    immediate_preceding_steps: Optional[Union[Union[dict, "MathematicalOperation"], List[Union[dict, "MathematicalOperation"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.parts, list):
            self.parts = [self.parts] if self.parts is not None else []
        self.parts = [v if isinstance(v, MathematicalOperation) else MathematicalOperation(**as_dict(v)) for v in self.parts]

        if not isinstance(self.immediate_preceding_steps, list):
            self.immediate_preceding_steps = [self.immediate_preceding_steps] if self.immediate_preceding_steps is not None else []
        self.immediate_preceding_steps = [v if isinstance(v, MathematicalOperation) else MathematicalOperation(**as_dict(v)) for v in self.immediate_preceding_steps]

        super().__post_init__(**kwargs)


@dataclass
class Collection(Intangible):
    """
    A group of things. The collection may be heterogeneous or homogeneous.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["Collection"]
    class_class_curie: ClassVar[str] = "linkml_common:Collection"
    class_name: ClassVar[str] = "Collection"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.Collection

    members: Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.members, list):
            self.members = [self.members] if self.members is not None else []
        self.members = [v if isinstance(v, Entity) else Entity(**as_dict(v)) for v in self.members]

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


Any = Any

@dataclass
class BuiltEnvironmentFeature(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["BuiltEnvironmentFeature"]
    class_class_curie: ClassVar[str] = "linkml_common:BuiltEnvironmentFeature"
    class_name: ClassVar[str] = "BuiltEnvironmentFeature"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.BuiltEnvironmentFeature

    id: Union[str, BuiltEnvironmentFeatureId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BuiltEnvironmentFeatureId):
            self.id = BuiltEnvironmentFeatureId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class Facility(BuiltEnvironmentFeature):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["Facility"]
    class_class_curie: ClassVar[str] = "linkml_common:Facility"
    class_name: ClassVar[str] = "Facility"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.Facility

    id: Union[str, FacilityId] = None
    located_at_place: Optional[Union[str, PlaceId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FacilityId):
            self.id = FacilityId(self.id)

        if self.located_at_place is not None and not isinstance(self.located_at_place, PlaceId):
            self.located_at_place = PlaceId(self.located_at_place)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class Building(Facility):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["Building"]
    class_class_curie: ClassVar[str] = "linkml_common:Building"
    class_name: ClassVar[str] = "Building"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.Building

    id: Union[str, BuildingId] = None
    located_at_place: Optional[Union[str, PlaceId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BuildingId):
            self.id = BuildingId(self.id)

        if self.located_at_place is not None and not isinstance(self.located_at_place, PlaceId):
            self.located_at_place = PlaceId(self.located_at_place)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class BuiltSystem(BuiltEnvironmentFeature):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["BuiltSystem"]
    class_class_curie: ClassVar[str] = "linkml_common:BuiltSystem"
    class_name: ClassVar[str] = "BuiltSystem"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.BuiltSystem

    id: Union[str, BuiltSystemId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BuiltSystemId):
            self.id = BuiltSystemId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class ClinicalCohort(NamedThing):
    """
    A group of patients who share a common set of characteristics
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["ClinicalCohort"]
    class_class_curie: ClassVar[str] = "linkml_common:ClinicalCohort"
    class_name: ClassVar[str] = "ClinicalCohort"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.ClinicalCohort

    id: Union[str, ClinicalCohortId] = None
    definition: Optional[Union[str, ClinicalCohortDefinitionId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ClinicalCohortId):
            self.id = ClinicalCohortId(self.id)

        if self.definition is not None and not isinstance(self.definition, ClinicalCohortDefinitionId):
            self.definition = ClinicalCohortDefinitionId(self.definition)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class ClinicalCohortDefinition(NamedThing):
    """
    A definition of a clinical cohort
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["ClinicalCohortDefinition"]
    class_class_curie: ClassVar[str] = "linkml_common:ClinicalCohortDefinition"
    class_name: ClassVar[str] = "ClinicalCohortDefinition"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.ClinicalCohortDefinition

    id: Union[str, ClinicalCohortDefinitionId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ClinicalCohortDefinitionId):
            self.id = ClinicalCohortDefinitionId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


class DataStructure(Intangible):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["DataStructure"]
    class_class_curie: ClassVar[str] = "linkml_common:DataStructure"
    class_name: ClassVar[str] = "DataStructure"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.DataStructure


    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class EngineeringSpecification(Procedure):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["EngineeringSpecification"]
    class_class_curie: ClassVar[str] = "linkml_common:EngineeringSpecification"
    class_name: ClassVar[str] = "EngineeringSpecification"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.EngineeringSpecification

    id: Union[str, EngineeringSpecificationId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EngineeringSpecificationId):
            self.id = EngineeringSpecificationId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class RawMaterial(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["RawMaterial"]
    class_class_curie: ClassVar[str] = "linkml_common:RawMaterial"
    class_name: ClassVar[str] = "RawMaterial"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.RawMaterial

    id: Union[str, RawMaterialId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RawMaterialId):
            self.id = RawMaterialId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class Equipment(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["Equipment"]
    class_class_curie: ClassVar[str] = "linkml_common:Equipment"
    class_name: ClassVar[str] = "Equipment"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.Equipment

    id: Union[str, EquipmentId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EquipmentId):
            self.id = EquipmentId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class PowerPlant(Building):
    """
    A facility for generating electrical power
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["PowerPlant"]
    class_class_curie: ClassVar[str] = "linkml_common:PowerPlant"
    class_name: ClassVar[str] = "PowerPlant"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.PowerPlant

    id: Union[str, PowerPlantId] = None
    plant_type: Optional[Union[str, PowerPlantTypeId]] = None
    location: Optional[Union[str, PlaceId]] = None
    operator: Optional[Union[str, OrganizationId]] = None
    capacity: Optional[Union[dict, "SimpleQuantity"]] = None
    commissioning_date: Optional[Union[str, XSDDate]] = None
    decommissioning_date: Optional[Union[str, XSDDate]] = None
    capex: Optional[Union[dict, "MoneyQuantity"]] = None
    opex: Optional[Union[dict, "MoneyQuantity"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PowerPlantId):
            self.id = PowerPlantId(self.id)

        if self.plant_type is not None and not isinstance(self.plant_type, PowerPlantTypeId):
            self.plant_type = PowerPlantTypeId(self.plant_type)

        if self.location is not None and not isinstance(self.location, PlaceId):
            self.location = PlaceId(self.location)

        if self.operator is not None and not isinstance(self.operator, OrganizationId):
            self.operator = OrganizationId(self.operator)

        if self.capacity is not None and not isinstance(self.capacity, SimpleQuantity):
            self.capacity = SimpleQuantity(**as_dict(self.capacity))

        if self.commissioning_date is not None and not isinstance(self.commissioning_date, XSDDate):
            self.commissioning_date = XSDDate(self.commissioning_date)

        if self.decommissioning_date is not None and not isinstance(self.decommissioning_date, XSDDate):
            self.decommissioning_date = XSDDate(self.decommissioning_date)

        if self.capex is not None and not isinstance(self.capex, MoneyQuantity):
            self.capex = MoneyQuantity(**as_dict(self.capex))

        if self.opex is not None and not isinstance(self.opex, MoneyQuantity):
            self.opex = MoneyQuantity(**as_dict(self.opex))

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class PowerPlantType(Concept):
    """
    The type of power plant
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["PowerPlantType"]
    class_class_curie: ClassVar[str] = "linkml_common:PowerPlantType"
    class_name: ClassVar[str] = "PowerPlantType"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.PowerPlantType

    id: Union[str, PowerPlantTypeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PowerPlantTypeId):
            self.id = PowerPlantTypeId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class FossilFuelPlant(PowerPlant):
    """
    A power plant that uses fossil fuels
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["FossilFuelPlant"]
    class_class_curie: ClassVar[str] = "linkml_common:FossilFuelPlant"
    class_name: ClassVar[str] = "FossilFuelPlant"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.FossilFuelPlant

    id: Union[str, FossilFuelPlantId] = None
    fuel: Optional[Union[str, FossilFuelId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FossilFuelPlantId):
            self.id = FossilFuelPlantId(self.id)

        if self.fuel is not None and not isinstance(self.fuel, FossilFuelId):
            self.fuel = FossilFuelId(self.fuel)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class NuclearPlant(PowerPlant):
    """
    A nuclear power plant
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["NuclearPlant"]
    class_class_curie: ClassVar[str] = "linkml_common:NuclearPlant"
    class_name: ClassVar[str] = "NuclearPlant"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.NuclearPlant

    id: Union[str, NuclearPlantId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NuclearPlantId):
            self.id = NuclearPlantId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class RenewablePlant(PowerPlant):
    """
    A power plant that uses renewable energy sources
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["RenewablePlant"]
    class_class_curie: ClassVar[str] = "linkml_common:RenewablePlant"
    class_name: ClassVar[str] = "RenewablePlant"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.RenewablePlant

    id: Union[str, RenewablePlantId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RenewablePlantId):
            self.id = RenewablePlantId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class HydroelectricPlant(RenewablePlant):
    """
    A hydroelectric power plant
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["HydroelectricPlant"]
    class_class_curie: ClassVar[str] = "linkml_common:HydroelectricPlant"
    class_name: ClassVar[str] = "HydroelectricPlant"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.HydroelectricPlant

    id: Union[str, HydroelectricPlantId] = None
    dam: Optional[Union[str, LandformId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HydroelectricPlantId):
            self.id = HydroelectricPlantId(self.id)

        if self.dam is not None and not isinstance(self.dam, LandformId):
            self.dam = LandformId(self.dam)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class SolarPlant(RenewablePlant):
    """
    A solar power plant
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["SolarPlant"]
    class_class_curie: ClassVar[str] = "linkml_common:SolarPlant"
    class_name: ClassVar[str] = "SolarPlant"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.SolarPlant

    id: Union[str, SolarPlantId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SolarPlantId):
            self.id = SolarPlantId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class WindFarm(RenewablePlant):
    """
    A wind farm
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["WindFarm"]
    class_class_curie: ClassVar[str] = "linkml_common:WindFarm"
    class_name: ClassVar[str] = "WindFarm"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.WindFarm

    id: Union[str, WindFarmId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WindFarmId):
            self.id = WindFarmId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class FossilFuel(Concept):
    """
    A type of fossil fuel
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["FossilFuel"]
    class_class_curie: ClassVar[str] = "linkml_common:FossilFuel"
    class_name: ClassVar[str] = "FossilFuel"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.FossilFuel

    id: Union[str, FossilFuelId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FossilFuelId):
            self.id = FossilFuelId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class ElectricalGrid(BuiltSystem):
    """
    A network of electrical transmission lines
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["ElectricalGrid"]
    class_class_curie: ClassVar[str] = "linkml_common:ElectricalGrid"
    class_name: ClassVar[str] = "ElectricalGrid"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.ElectricalGrid

    id: Union[str, ElectricalGridId] = None
    plants: Optional[Union[Union[str, PowerPlantId], List[Union[str, PowerPlantId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ElectricalGridId):
            self.id = ElectricalGridId(self.id)

        if not isinstance(self.plants, list):
            self.plants = [self.plants] if self.plants is not None else []
        self.plants = [v if isinstance(v, PowerPlantId) else PowerPlantId(v) for v in self.plants]

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class ExtractiveIndustryFacility(Facility):
    """
    A facility where natural resources are extracted from the earth
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["ExtractiveIndustryFacility"]
    class_class_curie: ClassVar[str] = "linkml_common:ExtractiveIndustryFacility"
    class_name: ClassVar[str] = "ExtractiveIndustryFacility"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.ExtractiveIndustryFacility

    id: Union[str, ExtractiveIndustryFacilityId] = None
    facility_type: Optional[Union[str, "ExtractiveIndustryFacilityType"]] = None
    operator: Optional[Union[str, OrganizationId]] = None
    products: Optional[Union[Dict[Union[str, ExtractiveIndustryProductId], Union[dict, "ExtractiveIndustryProduct"]], List[Union[dict, "ExtractiveIndustryProduct"]]]] = empty_dict()
    production_capacity: Optional[Union[dict, "Quantity"]] = None
    annual_production: Optional[Union[dict, "Quantity"]] = None
    reserves: Optional[Union[dict, "Quantity"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ExtractiveIndustryFacilityId):
            self.id = ExtractiveIndustryFacilityId(self.id)

        if self.facility_type is not None and not isinstance(self.facility_type, ExtractiveIndustryFacilityType):
            self.facility_type = ExtractiveIndustryFacilityType(self.facility_type)

        if self.operator is not None and not isinstance(self.operator, OrganizationId):
            self.operator = OrganizationId(self.operator)

        self._normalize_inlined_as_list(slot_name="products", slot_type=ExtractiveIndustryProduct, key_name="id", keyed=True)

        if self.production_capacity is not None and not isinstance(self.production_capacity, Quantity):
            self.production_capacity = Quantity(**as_dict(self.production_capacity))

        if self.annual_production is not None and not isinstance(self.annual_production, Quantity):
            self.annual_production = Quantity(**as_dict(self.annual_production))

        if self.reserves is not None and not isinstance(self.reserves, Quantity):
            self.reserves = Quantity(**as_dict(self.reserves))

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class MiningFacility(ExtractiveIndustryFacility):
    """
    A facility where mineral resources are extracted from the earth
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["MiningFacility"]
    class_class_curie: ClassVar[str] = "linkml_common:MiningFacility"
    class_name: ClassVar[str] = "MiningFacility"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.MiningFacility

    id: Union[str, MiningFacilityId] = None
    mining_method: Optional[Union[str, "MiningMethod"]] = None
    depth: Optional[Union[dict, "Quantity"]] = None
    area: Optional[Union[dict, "Quantity"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MiningFacilityId):
            self.id = MiningFacilityId(self.id)

        if self.mining_method is not None and not isinstance(self.mining_method, MiningMethod):
            self.mining_method = MiningMethod(self.mining_method)

        if self.depth is not None and not isinstance(self.depth, Quantity):
            self.depth = Quantity(**as_dict(self.depth))

        if self.area is not None and not isinstance(self.area, Quantity):
            self.area = Quantity(**as_dict(self.area))

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class WellFacility(ExtractiveIndustryFacility):
    """
    A facility where fluid resources (e.g., oil, gas, water) are extracted from the earth
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["WellFacility"]
    class_class_curie: ClassVar[str] = "linkml_common:WellFacility"
    class_name: ClassVar[str] = "WellFacility"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.WellFacility

    id: Union[str, WellFacilityId] = None
    well_type: Optional[Union[str, "WellType"]] = None
    depth: Optional[Union[dict, "Quantity"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WellFacilityId):
            self.id = WellFacilityId(self.id)

        if self.well_type is not None and not isinstance(self.well_type, WellType):
            self.well_type = WellType(self.well_type)

        if self.depth is not None and not isinstance(self.depth, Quantity):
            self.depth = Quantity(**as_dict(self.depth))

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class QuarryFacility(ExtractiveIndustryFacility):
    """
    A facility where stone, sand, or gravel are extracted from the earth
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["QuarryFacility"]
    class_class_curie: ClassVar[str] = "linkml_common:QuarryFacility"
    class_name: ClassVar[str] = "QuarryFacility"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.QuarryFacility

    id: Union[str, QuarryFacilityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, QuarryFacilityId):
            self.id = QuarryFacilityId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class ExtractiveIndustryEquipment(Equipment):
    """
    The equipment used in extractive industry operations
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["ExtractiveIndustryEquipment"]
    class_class_curie: ClassVar[str] = "linkml_common:ExtractiveIndustryEquipment"
    class_name: ClassVar[str] = "ExtractiveIndustryEquipment"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.ExtractiveIndustryEquipment

    id: Union[str, ExtractiveIndustryEquipmentId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ExtractiveIndustryEquipmentId):
            self.id = ExtractiveIndustryEquipmentId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class ExtractiveIndustryProduct(Concept):
    """
    A product extracted from an extractive industry facility
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["ExtractiveIndustryProduct"]
    class_class_curie: ClassVar[str] = "linkml_common:ExtractiveIndustryProduct"
    class_name: ClassVar[str] = "ExtractiveIndustryProduct"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.ExtractiveIndustryProduct

    id: Union[str, ExtractiveIndustryProductId] = None
    product_type: Optional[Union[str, "ExtractiveIndustryProductType"]] = None
    grade: Optional[Union[dict, "SimpleQuantity"]] = None
    processing_method: Optional[Union[str, EngineeringSpecificationId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ExtractiveIndustryProductId):
            self.id = ExtractiveIndustryProductId(self.id)

        if self.product_type is not None and not isinstance(self.product_type, ExtractiveIndustryProductType):
            self.product_type = ExtractiveIndustryProductType(self.product_type)

        if self.grade is not None and not isinstance(self.grade, SimpleQuantity):
            self.grade = SimpleQuantity(**as_dict(self.grade))

        if self.processing_method is not None and not isinstance(self.processing_method, EngineeringSpecificationId):
            self.processing_method = EngineeringSpecificationId(self.processing_method)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class ExtractiveIndustryWaste(Concept):
    """
    Waste material generated from extractive industry operations
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["ExtractiveIndustryWaste"]
    class_class_curie: ClassVar[str] = "linkml_common:ExtractiveIndustryWaste"
    class_name: ClassVar[str] = "ExtractiveIndustryWaste"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.ExtractiveIndustryWaste

    id: Union[str, ExtractiveIndustryWasteId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ExtractiveIndustryWasteId):
            self.id = ExtractiveIndustryWasteId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


class EnvironmentalProcess(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["EnvironmentalProcess"]
    class_class_curie: ClassVar[str] = "linkml_common:EnvironmentalProcess"
    class_name: ClassVar[str] = "EnvironmentalProcess"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.EnvironmentalProcess


class EnvironmentalMonitoring(EnvironmentalProcess):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["EnvironmentalMonitoring"]
    class_class_curie: ClassVar[str] = "linkml_common:EnvironmentalMonitoring"
    class_name: ClassVar[str] = "EnvironmentalMonitoring"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.EnvironmentalMonitoring


@dataclass
class CurrencyConcept(Concept):
    """
    A currency
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["CurrencyConcept"]
    class_class_curie: ClassVar[str] = "linkml_common:CurrencyConcept"
    class_name: ClassVar[str] = "CurrencyConcept"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.CurrencyConcept

    id: Union[str, CurrencyConceptId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CurrencyConceptId):
            self.id = CurrencyConceptId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class FoodRecipe(Procedure):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["FoodRecipe"]
    class_class_curie: ClassVar[str] = "linkml_common:FoodRecipe"
    class_name: ClassVar[str] = "FoodRecipe"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.FoodRecipe

    id: Union[str, FoodRecipeId] = None
    ingredients: Optional[Union[Union[dict, "FoodIngredient"], List[Union[dict, "FoodIngredient"]]]] = empty_list()
    steps: Optional[Union[Union[str, FoodProcessingId], List[Union[str, FoodProcessingId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FoodRecipeId):
            self.id = FoodRecipeId(self.id)

        if not isinstance(self.ingredients, list):
            self.ingredients = [self.ingredients] if self.ingredients is not None else []
        self.ingredients = [v if isinstance(v, FoodIngredient) else FoodIngredient(**as_dict(v)) for v in self.ingredients]

        if not isinstance(self.steps, list):
            self.steps = [self.steps] if self.steps is not None else []
        self.steps = [v if isinstance(v, FoodProcessingId) else FoodProcessingId(v) for v in self.steps]

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class FoodTypeConcept(Concept):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["FoodTypeConcept"]
    class_class_curie: ClassVar[str] = "linkml_common:FoodTypeConcept"
    class_name: ClassVar[str] = "FoodTypeConcept"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.FoodTypeConcept

    id: Union[str, FoodTypeConceptId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FoodTypeConceptId):
            self.id = FoodTypeConceptId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class BasicFoodType(FoodTypeConcept):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["BasicFoodType"]
    class_class_curie: ClassVar[str] = "linkml_common:BasicFoodType"
    class_name: ClassVar[str] = "BasicFoodType"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.BasicFoodType

    id: Union[str, BasicFoodTypeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BasicFoodTypeId):
            self.id = BasicFoodTypeId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class CompositeFoodType(FoodTypeConcept):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["CompositeFoodType"]
    class_class_curie: ClassVar[str] = "linkml_common:CompositeFoodType"
    class_name: ClassVar[str] = "CompositeFoodType"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.CompositeFoodType

    id: Union[str, CompositeFoodTypeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompositeFoodTypeId):
            self.id = CompositeFoodTypeId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class Place(NamedThing):
    """
    Entities that have a somewhat fixed, physical extension.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Place"]
    class_class_curie: ClassVar[str] = "schema:Place"
    class_name: ClassVar[str] = "Place"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.Place

    id: Union[str, PlaceId] = None
    address: Optional[Union[dict, "PostalAddress"]] = None
    geolocation: Optional[Union[dict, "GeoPointLocation"]] = None
    bounding_coordinates: Optional[Union[dict, "GeoBoxLocation"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PlaceId):
            self.id = PlaceId(self.id)

        if self.address is not None and not isinstance(self.address, PostalAddress):
            self.address = PostalAddress(**as_dict(self.address))

        if self.geolocation is not None and not isinstance(self.geolocation, GeoPointLocation):
            self.geolocation = GeoPointLocation(**as_dict(self.geolocation))

        if self.bounding_coordinates is not None and not isinstance(self.bounding_coordinates, GeoBoxLocation):
            self.bounding_coordinates = GeoBoxLocation(**as_dict(self.bounding_coordinates))

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class EnvironmentalSite(Place):
    """
    A location or site that is the subject of environmental monitoring
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["EnvironmentalSite"]
    class_class_curie: ClassVar[str] = "linkml_common:EnvironmentalSite"
    class_name: ClassVar[str] = "EnvironmentalSite"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.EnvironmentalSite

    id: Union[str, EnvironmentalSiteId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EnvironmentalSiteId):
            self.id = EnvironmentalSiteId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class Landform(Place):
    """
    A natural feature of the solid surface of the Earth or other planetary body
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["Landform"]
    class_class_curie: ClassVar[str] = "linkml_common:Landform"
    class_name: ClassVar[str] = "Landform"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.Landform

    id: Union[str, LandformId] = None
    geolocation: Optional[Union[dict, "GeoPointLocation"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LandformId):
            self.id = LandformId(self.id)

        if self.geolocation is not None and not isinstance(self.geolocation, GeoPointLocation):
            self.geolocation = GeoPointLocation(**as_dict(self.geolocation))

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class PostalAddress(Entity):
    """
    Represents an Address
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["PostalAddress"]
    class_class_curie: ClassVar[str] = "schema:PostalAddress"
    class_name: ClassVar[str] = "PostalAddress"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.PostalAddress

    street_address: Optional[str] = None
    street_address_additional: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.street_address is not None and not isinstance(self.street_address, str):
            self.street_address = str(self.street_address)

        if self.street_address_additional is not None and not isinstance(self.street_address_additional, str):
            self.street_address_additional = str(self.street_address_additional)

        if self.city is not None and not isinstance(self.city, str):
            self.city = str(self.city)

        if self.state is not None and not isinstance(self.state, str):
            self.state = str(self.state)

        if self.postal_code is not None and not isinstance(self.postal_code, str):
            self.postal_code = str(self.postal_code)

        if self.country is not None and not isinstance(self.country, str):
            self.country = str(self.country)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class GeoPointLocation(PointLocation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["GeoPointLocation"]
    class_class_curie: ClassVar[str] = "linkml_common:GeoPointLocation"
    class_name: ClassVar[str] = "GeoPointLocation"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.GeoPointLocation

    latitude: Optional[Decimal] = None
    longitude: Optional[Decimal] = None
    altitude: Optional[Decimal] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.latitude is not None and not isinstance(self.latitude, Decimal):
            self.latitude = Decimal(self.latitude)

        if self.longitude is not None and not isinstance(self.longitude, Decimal):
            self.longitude = Decimal(self.longitude)

        if self.altitude is not None and not isinstance(self.altitude, Decimal):
            self.altitude = Decimal(self.altitude)

        super().__post_init__(**kwargs)


@dataclass
class GeoBoxLocation(Location):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["GeoBoxLocation"]
    class_class_curie: ClassVar[str] = "linkml_common:GeoBoxLocation"
    class_name: ClassVar[str] = "GeoBoxLocation"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.GeoBoxLocation

    west_bounding_coordinate: Optional[Decimal] = None
    east_bounding_coordinate: Optional[Decimal] = None
    north_bounding_coordinate: Optional[Decimal] = None
    south_bounding_coordinate: Optional[Decimal] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.west_bounding_coordinate is not None and not isinstance(self.west_bounding_coordinate, Decimal):
            self.west_bounding_coordinate = Decimal(self.west_bounding_coordinate)

        if self.east_bounding_coordinate is not None and not isinstance(self.east_bounding_coordinate, Decimal):
            self.east_bounding_coordinate = Decimal(self.east_bounding_coordinate)

        if self.north_bounding_coordinate is not None and not isinstance(self.north_bounding_coordinate, Decimal):
            self.north_bounding_coordinate = Decimal(self.north_bounding_coordinate)

        if self.south_bounding_coordinate is not None and not isinstance(self.south_bounding_coordinate, Decimal):
            self.south_bounding_coordinate = Decimal(self.south_bounding_coordinate)

        super().__post_init__(**kwargs)


@dataclass
class HealthcareSite(Place):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["HealthcareSite"]
    class_class_curie: ClassVar[str] = "linkml_common:HealthcareSite"
    class_name: ClassVar[str] = "HealthcareSite"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.HealthcareSite

    id: Union[str, HealthcareSiteId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HealthcareSiteId):
            self.id = HealthcareSiteId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class HealthcareRole(Role):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["HealthcareRole"]
    class_class_curie: ClassVar[str] = "linkml_common:HealthcareRole"
    class_name: ClassVar[str] = "HealthcareRole"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.HealthcareRole

    is_person: Optional[Union[str, PersonId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.is_person is not None and not isinstance(self.is_person, PersonId):
            self.is_person = PersonId(self.is_person)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class HealthcareProvider(HealthcareRole):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["HealthcareProvider"]
    class_class_curie: ClassVar[str] = "linkml_common:HealthcareProvider"
    class_name: ClassVar[str] = "HealthcareProvider"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.HealthcareProvider

    speciality: Optional[Union[str, ConceptId]] = None
    care_site: Optional[Union[str, HealthcareSiteId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.speciality is not None and not isinstance(self.speciality, ConceptId):
            self.speciality = ConceptId(self.speciality)

        if self.care_site is not None and not isinstance(self.care_site, HealthcareSiteId):
            self.care_site = HealthcareSiteId(self.care_site)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


class Patient(HealthcareRole):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["Patient"]
    class_class_curie: ClassVar[str] = "linkml_common:Patient"
    class_name: ClassVar[str] = "Patient"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.Patient


    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class Investigation(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["Investigation"]
    class_class_curie: ClassVar[str] = "linkml_common:Investigation"
    class_name: ClassVar[str] = "Investigation"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.Investigation

    id: Union[str, InvestigationId] = None
    objectives: Optional[str] = None
    variables: Optional[Union[Union[dict, "Variable"], List[Union[dict, "Variable"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InvestigationId):
            self.id = InvestigationId(self.id)

        if self.objectives is not None and not isinstance(self.objectives, str):
            self.objectives = str(self.objectives)

        if not isinstance(self.variables, list):
            self.variables = [self.variables] if self.variables is not None else []
        self.variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.variables]

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class InvestigativeProtocol(Procedure):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["InvestigativeProtocol"]
    class_class_curie: ClassVar[str] = "linkml_common:InvestigativeProtocol"
    class_name: ClassVar[str] = "InvestigativeProtocol"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.InvestigativeProtocol

    id: Union[str, InvestigativeProtocolId] = None
    protocols_io_url: Optional[Union[str, URI]] = None
    classification: Optional[Union[str, ConceptId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InvestigativeProtocolId):
            self.id = InvestigativeProtocolId(self.id)

        if self.protocols_io_url is not None and not isinstance(self.protocols_io_url, URI):
            self.protocols_io_url = URI(self.protocols_io_url)

        if self.classification is not None and not isinstance(self.classification, ConceptId):
            self.classification = ConceptId(self.classification)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class StudyDesign(Procedure):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["StudyDesign"]
    class_class_curie: ClassVar[str] = "linkml_common:StudyDesign"
    class_name: ClassVar[str] = "StudyDesign"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.StudyDesign

    id: Union[str, StudyDesignId] = None
    classification: Optional[Union[str, ConceptId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StudyDesignId):
            self.id = StudyDesignId(self.id)

        if self.classification is not None and not isinstance(self.classification, ConceptId):
            self.classification = ConceptId(self.classification)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class SampleMaterial(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["SampleMaterial"]
    class_class_curie: ClassVar[str] = "linkml_common:SampleMaterial"
    class_name: ClassVar[str] = "SampleMaterial"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.SampleMaterial

    id: Union[str, SampleMaterialId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SampleMaterialId):
            self.id = SampleMaterialId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class Measurement(Observation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["Measurement"]
    class_class_curie: ClassVar[str] = "linkml_common:Measurement"
    class_name: ClassVar[str] = "Measurement"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.Measurement

    quantity_measured: Optional[Union[dict, "Quantity"]] = None
    variable_measured: Optional[Union[dict, "Variable"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.quantity_measured is not None and not isinstance(self.quantity_measured, Quantity):
            self.quantity_measured = Quantity(**as_dict(self.quantity_measured))

        if self.variable_measured is not None and not isinstance(self.variable_measured, Variable):
            self.variable_measured = Variable(**as_dict(self.variable_measured))

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class Variable(Entity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["Variable"]
    class_class_curie: ClassVar[str] = "linkml_common:Variable"
    class_name: ClassVar[str] = "Variable"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.Variable

    allowed_units: Optional[Union[Union[str, UnitConceptId], List[Union[str, UnitConceptId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.allowed_units, list):
            self.allowed_units = [self.allowed_units] if self.allowed_units is not None else []
        self.allowed_units = [v if isinstance(v, UnitConceptId) else UnitConceptId(v) for v in self.allowed_units]

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class QuantityKind(Concept):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["QuantityKind"]
    class_class_curie: ClassVar[str] = "linkml_common:QuantityKind"
    class_name: ClassVar[str] = "QuantityKind"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.QuantityKind

    id: Union[str, QuantityKindId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, QuantityKindId):
            self.id = QuantityKindId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class Quantity(Intangible):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = FHIR["Quantity"]
    class_class_curie: ClassVar[str] = "fhir:Quantity"
    class_name: ClassVar[str] = "Quantity"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.Quantity

    has_quantity_kind: Optional[Union[str, QuantityKindId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_quantity_kind is not None and not isinstance(self.has_quantity_kind, QuantityKindId):
            self.has_quantity_kind = QuantityKindId(self.has_quantity_kind)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


class FoodIngredient(Quantity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["FoodIngredient"]
    class_class_curie: ClassVar[str] = "linkml_common:FoodIngredient"
    class_name: ClassVar[str] = "FoodIngredient"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.FoodIngredient


    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class SimpleQuantity(Quantity):
    """
    A quantity is a property that can be measured or counted
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = FHIR["SimpleQuantity"]
    class_class_curie: ClassVar[str] = "fhir:SimpleQuantity"
    class_name: ClassVar[str] = "SimpleQuantity"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.SimpleQuantity

    value: Optional[float] = None
    unit: Optional[Union[str, UnitConceptId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.value is not None and not isinstance(self.value, float):
            self.value = float(self.value)

        if self.unit is not None and not isinstance(self.unit, UnitConceptId):
            self.unit = UnitConceptId(self.unit)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class MoneyQuantity(SimpleQuantity):
    """
    A quantity of money
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = FHIR["MoneyQuantity"]
    class_class_curie: ClassVar[str] = "fhir:MoneyQuantity"
    class_name: ClassVar[str] = "MoneyQuantity"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.MoneyQuantity

    value: Optional[float] = None
    unit: Optional[Union[str, CurrencyConceptId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.value is not None and not isinstance(self.value, float):
            self.value = float(self.value)

        if self.unit is not None and not isinstance(self.unit, CurrencyConceptId):
            self.unit = CurrencyConceptId(self.unit)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class Ratio(Quantity):
    """
    A tuple of two quantities
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = FHIR["Ratio"]
    class_class_curie: ClassVar[str] = "fhir:Ratio"
    class_name: ClassVar[str] = "Ratio"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.Ratio

    numerator: Optional[Union[dict, Quantity]] = None
    denominator: Optional[Union[dict, Quantity]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.numerator is not None and not isinstance(self.numerator, Quantity):
            self.numerator = Quantity(**as_dict(self.numerator))

        if self.denominator is not None and not isinstance(self.denominator, Quantity):
            self.denominator = Quantity(**as_dict(self.denominator))

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class QuantityRange(Intangible):
    """
    A quantity range is a property that can be measured or counted
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = FHIR["Range"]
    class_class_curie: ClassVar[str] = "fhir:Range"
    class_name: ClassVar[str] = "QuantityRange"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.QuantityRange

    lower_bound: Optional[Union[dict, Quantity]] = None
    upper_bound: Optional[Union[dict, Quantity]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.lower_bound is not None and not isinstance(self.lower_bound, Quantity):
            self.lower_bound = Quantity(**as_dict(self.lower_bound))

        if self.upper_bound is not None and not isinstance(self.upper_bound, Quantity):
            self.upper_bound = Quantity(**as_dict(self.upper_bound))

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class UnitConversionOperation(MathematicalOperation):
    """
    A unit conversion operation
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["UnitConversionOperation"]
    class_class_curie: ClassVar[str] = "linkml_common:UnitConversionOperation"
    class_name: ClassVar[str] = "UnitConversionOperation"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.UnitConversionOperation

    inputs: Optional[Union[Union[dict, Quantity], List[Union[dict, Quantity]]]] = empty_list()
    outputs: Optional[Union[Union[dict, Quantity], List[Union[dict, Quantity]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.inputs, list):
            self.inputs = [self.inputs] if self.inputs is not None else []
        self.inputs = [v if isinstance(v, Quantity) else Quantity(**as_dict(v)) for v in self.inputs]

        if not isinstance(self.outputs, list):
            self.outputs = [self.outputs] if self.outputs is not None else []
        self.outputs = [v if isinstance(v, Quantity) else Quantity(**as_dict(v)) for v in self.outputs]

        super().__post_init__(**kwargs)


@dataclass
class UnitConcept(Concept):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["UnitConcept"]
    class_class_curie: ClassVar[str] = "linkml_common:UnitConcept"
    class_name: ClassVar[str] = "UnitConcept"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.UnitConcept

    id: Union[str, UnitConceptId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UnitConceptId):
            self.id = UnitConceptId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class Agent(NamedThing):
    """
    Represents an Agent
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["Agent"]
    class_class_curie: ClassVar[str] = "linkml_common:Agent"
    class_name: ClassVar[str] = "Agent"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.Agent

    id: Union[str, AgentId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AgentId):
            self.id = AgentId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class Person(Agent):
    """
    Represents a Person
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["Person"]
    class_class_curie: ClassVar[str] = "linkml_common:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.Person

    id: Union[str, PersonId] = None
    primary_email: Optional[str] = None
    birth_date: Optional[Union[str, XSDDate]] = None
    age_in_years: Optional[int] = None
    vital_status: Optional[Union[str, "PersonStatus"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonId):
            self.id = PersonId(self.id)

        if self.primary_email is not None and not isinstance(self.primary_email, str):
            self.primary_email = str(self.primary_email)

        if self.birth_date is not None and not isinstance(self.birth_date, XSDDate):
            self.birth_date = XSDDate(self.birth_date)

        if self.age_in_years is not None and not isinstance(self.age_in_years, int):
            self.age_in_years = int(self.age_in_years)

        if self.vital_status is not None and not isinstance(self.vital_status, PersonStatus):
            self.vital_status = PersonStatus(self.vital_status)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class Organization(Agent):
    """
    Represents an Organization
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["Organization"]
    class_class_curie: ClassVar[str] = "linkml_common:Organization"
    class_name: ClassVar[str] = "Organization"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.Organization

    id: Union[str, OrganizationId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrganizationId):
            self.id = OrganizationId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class HealthcareOrganization(Organization):
    """
    An organization that provides healthcare services
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["HealthcareOrganization"]
    class_class_curie: ClassVar[str] = "linkml_common:HealthcareOrganization"
    class_name: ClassVar[str] = "HealthcareOrganization"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.HealthcareOrganization

    id: Union[str, HealthcareOrganizationId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HealthcareOrganizationId):
            self.id = HealthcareOrganizationId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class AutomatedAgent(Agent):
    """
    Represents an Automated Agent
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["AutomatedAgent"]
    class_class_curie: ClassVar[str] = "linkml_common:AutomatedAgent"
    class_name: ClassVar[str] = "AutomatedAgent"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.AutomatedAgent

    id: Union[str, AutomatedAgentId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AutomatedAgentId):
            self.id = AutomatedAgentId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class CreativeWork(NamedThing):
    """
    The most generic kind of creative work, including books, movies, photographs, software programs, etc.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["CreativeWork"]
    class_class_curie: ClassVar[str] = "linkml_common:CreativeWork"
    class_name: ClassVar[str] = "CreativeWork"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.CreativeWork

    id: Union[str, CreativeWorkId] = None
    title: Optional[str] = None
    abstract: Optional[str] = None
    rights: Optional[str] = None
    creators: Optional[Union[Union[str, AgentId], List[Union[str, AgentId]]]] = empty_list()
    contributors: Optional[Union[Union[str, AgentId], List[Union[str, AgentId]]]] = empty_list()
    contacts: Optional[Union[Union[str, AgentId], List[Union[str, AgentId]]]] = empty_list()
    keywords: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CreativeWorkId):
            self.id = CreativeWorkId(self.id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.abstract is not None and not isinstance(self.abstract, str):
            self.abstract = str(self.abstract)

        if self.rights is not None and not isinstance(self.rights, str):
            self.rights = str(self.rights)

        if not isinstance(self.creators, list):
            self.creators = [self.creators] if self.creators is not None else []
        self.creators = [v if isinstance(v, AgentId) else AgentId(v) for v in self.creators]

        if not isinstance(self.contributors, list):
            self.contributors = [self.contributors] if self.contributors is not None else []
        self.contributors = [v if isinstance(v, AgentId) else AgentId(v) for v in self.contributors]

        if not isinstance(self.contacts, list):
            self.contacts = [self.contacts] if self.contacts is not None else []
        self.contacts = [v if isinstance(v, AgentId) else AgentId(v) for v in self.contacts]

        if not isinstance(self.keywords, list):
            self.keywords = [self.keywords] if self.keywords is not None else []
        self.keywords = [v if isinstance(v, str) else str(v) for v in self.keywords]

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class Publication(CreativeWork):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["Publication"]
    class_class_curie: ClassVar[str] = "linkml_common:Publication"
    class_name: ClassVar[str] = "Publication"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.Publication

    id: Union[str, PublicationId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PublicationId):
            self.id = PublicationId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class Dataset(CreativeWork):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["Dataset"]
    class_class_curie: ClassVar[str] = "linkml_common:Dataset"
    class_name: ClassVar[str] = "Dataset"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.Dataset

    id: Union[str, DatasetId] = None
    collected_as_part_of: Optional[Union[Union[str, InvestigationId], List[Union[str, InvestigationId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DatasetId):
            self.id = DatasetId(self.id)

        if not isinstance(self.collected_as_part_of, list):
            self.collected_as_part_of = [self.collected_as_part_of] if self.collected_as_part_of is not None else []
        self.collected_as_part_of = [v if isinstance(v, InvestigationId) else InvestigationId(v) for v in self.collected_as_part_of]

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


class Service(Intangible):
    """
    A service provided by an organization
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["Service"]
    class_class_curie: ClassVar[str] = "linkml_common:Service"
    class_name: ClassVar[str] = "Service"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.Service


    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


class FinancialProduct(Service):
    """
    A product or service offered by a bank whereby one may deposit, withdraw or transfer money and in some cases be
    paid interest.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["FinancialProduct"]
    class_class_curie: ClassVar[str] = "linkml_common:FinancialProduct"
    class_name: ClassVar[str] = "FinancialProduct"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.FinancialProduct


    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class FinancialAccount(FinancialProduct):
    """
    A bank account
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["FinancialAccount"]
    class_class_curie: ClassVar[str] = "linkml_common:FinancialAccount"
    class_name: ClassVar[str] = "FinancialAccount"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.FinancialAccount

    account_number: Optional[str] = None
    bank: Optional[Union[str, OrganizationId]] = None
    account_holder: Optional[Union[str, PersonId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.account_number is not None and not isinstance(self.account_number, str):
            self.account_number = str(self.account_number)

        if self.bank is not None and not isinstance(self.bank, OrganizationId):
            self.bank = OrganizationId(self.bank)

        if self.account_holder is not None and not isinstance(self.account_holder, PersonId):
            self.account_holder = PersonId(self.account_holder)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class Event(NamedThing):
    """
    A thing that happens
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["Event"]
    class_class_curie: ClassVar[str] = "linkml_common:Event"
    class_name: ClassVar[str] = "Event"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.Event

    id: Union[str, EventId] = None
    starts_at: Optional[Union[dict, "TimePoint"]] = None
    ends_at: Optional[Union[dict, "TimePoint"]] = None
    happens_at: Optional[Union[dict, "TimePoint"]] = None
    has_interval: Optional[Union[dict, "TemporalInterval"]] = None
    has_duration: Optional[Union[dict, "Duration"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EventId):
            self.id = EventId(self.id)

        if self.starts_at is not None and not isinstance(self.starts_at, TimePoint):
            self.starts_at = TimePoint(**as_dict(self.starts_at))

        if self.ends_at is not None and not isinstance(self.ends_at, TimePoint):
            self.ends_at = TimePoint(**as_dict(self.ends_at))

        if self.happens_at is not None and not isinstance(self.happens_at, TimePoint):
            self.happens_at = TimePoint(**as_dict(self.happens_at))

        if self.has_interval is not None and not isinstance(self.has_interval, TemporalInterval):
            self.has_interval = TemporalInterval(**as_dict(self.has_interval))

        if self.has_duration is not None and not isinstance(self.has_duration, Duration):
            self.has_duration = Duration(**as_dict(self.has_duration))

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class ClinicalCohortEnrollment(Event):
    """
    An event relating a patient to a clinical cohort
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["ClinicalCohortEnrollment"]
    class_class_curie: ClassVar[str] = "linkml_common:ClinicalCohortEnrollment"
    class_name: ClassVar[str] = "ClinicalCohortEnrollment"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.ClinicalCohortEnrollment

    id: Union[str, ClinicalCohortEnrollmentId] = None
    patient: Optional[Union[dict, Patient]] = None
    cohort: Optional[Union[str, ClinicalCohortId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ClinicalCohortEnrollmentId):
            self.id = ClinicalCohortEnrollmentId(self.id)

        if self.patient is not None and not isinstance(self.patient, Patient):
            self.patient = Patient(**as_dict(self.patient))

        if self.cohort is not None and not isinstance(self.cohort, ClinicalCohortId):
            self.cohort = ClinicalCohortId(self.cohort)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class EngineeringProcess(Event):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["EngineeringProcess"]
    class_class_curie: ClassVar[str] = "linkml_common:EngineeringProcess"
    class_name: ClassVar[str] = "EngineeringProcess"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.EngineeringProcess

    id: Union[str, EngineeringProcessId] = None
    follows_procedure: Optional[Union[str, EngineeringSpecificationId]] = None
    part_of: Optional[Union[str, EngineeringProcessId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EngineeringProcessId):
            self.id = EngineeringProcessId(self.id)

        if self.follows_procedure is not None and not isinstance(self.follows_procedure, EngineeringSpecificationId):
            self.follows_procedure = EngineeringSpecificationId(self.follows_procedure)

        if self.part_of is not None and not isinstance(self.part_of, EngineeringProcessId):
            self.part_of = EngineeringProcessId(self.part_of)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class HealthcareEncounter(Event):
    """
    An interaction between a patient and one or more healthcare providers
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["HealthcareEncounter"]
    class_class_curie: ClassVar[str] = "linkml_common:HealthcareEncounter"
    class_name: ClassVar[str] = "HealthcareEncounter"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.HealthcareEncounter

    id: Union[str, HealthcareEncounterId] = None
    patient: Optional[Union[dict, Patient]] = None
    provider: Optional[Union[dict, HealthcareProvider]] = None
    classification: Optional[Union[str, "HealthcareEncounterClassification"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HealthcareEncounterId):
            self.id = HealthcareEncounterId(self.id)

        if self.patient is not None and not isinstance(self.patient, Patient):
            self.patient = Patient(**as_dict(self.patient))

        if self.provider is not None and not isinstance(self.provider, HealthcareProvider):
            self.provider = HealthcareProvider(**as_dict(self.provider))

        if self.classification is not None and not isinstance(self.classification, HealthcareEncounterClassification):
            self.classification = HealthcareEncounterClassification(self.classification)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class HealthcareConditionOccurrence(Event):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["HealthcareConditionOccurrence"]
    class_class_curie: ClassVar[str] = "linkml_common:HealthcareConditionOccurrence"
    class_name: ClassVar[str] = "HealthcareConditionOccurrence"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.HealthcareConditionOccurrence

    id: Union[str, HealthcareConditionOccurrenceId] = None
    patient: Optional[Union[dict, Patient]] = None
    observed_during: Optional[Union[str, HealthcareEncounterId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HealthcareConditionOccurrenceId):
            self.id = HealthcareConditionOccurrenceId(self.id)

        if self.patient is not None and not isinstance(self.patient, Patient):
            self.patient = Patient(**as_dict(self.patient))

        if self.observed_during is not None and not isinstance(self.observed_during, HealthcareEncounterId):
            self.observed_during = HealthcareEncounterId(self.observed_during)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class LifeEvent(Event):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["LifeEvent"]
    class_class_curie: ClassVar[str] = "linkml_common:LifeEvent"
    class_name: ClassVar[str] = "LifeEvent"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.LifeEvent

    id: Union[str, LifeEventId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LifeEventId):
            self.id = LifeEventId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class TimePointOrTemporalInterval(Intangible):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["TimePointOrTemporalInterval"]
    class_class_curie: ClassVar[str] = "linkml_common:TimePointOrTemporalInterval"
    class_name: ClassVar[str] = "TimePointOrTemporalInterval"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.TimePointOrTemporalInterval

    starts_at: Optional[Union[dict, "TimePoint"]] = None
    ends_at: Optional[Union[dict, "TimePoint"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.starts_at is not None and not isinstance(self.starts_at, TimePoint):
            self.starts_at = TimePoint(**as_dict(self.starts_at))

        if self.ends_at is not None and not isinstance(self.ends_at, TimePoint):
            self.ends_at = TimePoint(**as_dict(self.ends_at))

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class TemporalInterval(TimePointOrTemporalInterval):
    """
    A period of time
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["TemporalInterval"]
    class_class_curie: ClassVar[str] = "linkml_common:TemporalInterval"
    class_name: ClassVar[str] = "TemporalInterval"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.TemporalInterval

    starts_at: Optional[Union[dict, "TimePoint"]] = None
    ends_at: Optional[Union[dict, "TimePoint"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.starts_at is not None and not isinstance(self.starts_at, TimePoint):
            self.starts_at = TimePoint(**as_dict(self.starts_at))

        if self.ends_at is not None and not isinstance(self.ends_at, TimePoint):
            self.ends_at = TimePoint(**as_dict(self.ends_at))

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class TimePoint(TimePointOrTemporalInterval):
    """
    A point in time. Can be fully specified, or specified in relative terms.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["TimePoint"]
    class_class_curie: ClassVar[str] = "linkml_common:TimePoint"
    class_name: ClassVar[str] = "TimePoint"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.TimePoint

    year_value: Optional[int] = None
    date_value: Optional[Union[str, XSDDate]] = None
    time_value: Optional[Union[str, XSDTime]] = None
    datetime_value: Optional[Union[str, XSDDateTime]] = None
    marker_event: Optional[Union[str, EventId]] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.year_value is not None and not isinstance(self.year_value, int):
            self.year_value = int(self.year_value)

        if self.date_value is not None and not isinstance(self.date_value, XSDDate):
            self.date_value = XSDDate(self.date_value)

        if self.time_value is not None and not isinstance(self.time_value, XSDTime):
            self.time_value = XSDTime(self.time_value)

        if self.datetime_value is not None and not isinstance(self.datetime_value, XSDDateTime):
            self.datetime_value = XSDDateTime(self.datetime_value)

        if self.marker_event is not None and not isinstance(self.marker_event, EventId):
            self.marker_event = EventId(self.marker_event)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


class Duration(Quantity):
    """
    A length of time
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["Duration"]
    class_class_curie: ClassVar[str] = "linkml_common:Duration"
    class_name: ClassVar[str] = "Duration"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.Duration


    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class TemporalRelationship(Relationship):
    """
    A relationship to another time point
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["TemporalRelationship"]
    class_class_curie: ClassVar[str] = "linkml_common:TemporalRelationship"
    class_name: ClassVar[str] = "TemporalRelationship"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.TemporalRelationship

    predicate: Optional[Union[str, "RelativeTimeEnum"]] = None
    relative_to: Optional[Union[dict, Entity]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.predicate is not None and not isinstance(self.predicate, RelativeTimeEnum):
            self.predicate = RelativeTimeEnum(self.predicate)

        if self.relative_to is not None and not isinstance(self.relative_to, Entity):
            self.relative_to = Entity(**as_dict(self.relative_to))

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class PlannedProcess(Event):
    """
    A process that follows a defined procedure or plan
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["PlannedProcess"]
    class_class_curie: ClassVar[str] = "linkml_common:PlannedProcess"
    class_name: ClassVar[str] = "PlannedProcess"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.PlannedProcess

    id: Union[str, PlannedProcessId] = None
    follows_procedure: Optional[Union[str, ProcedureId]] = None
    uses_physical_device: Optional[Union[str, PhysicalDeviceId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PlannedProcessId):
            self.id = PlannedProcessId(self.id)

        if self.follows_procedure is not None and not isinstance(self.follows_procedure, ProcedureId):
            self.follows_procedure = ProcedureId(self.follows_procedure)

        if self.uses_physical_device is not None and not isinstance(self.uses_physical_device, PhysicalDeviceId):
            self.uses_physical_device = PhysicalDeviceId(self.uses_physical_device)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class InvestigativeProcess(PlannedProcess):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["InvestigativeProcess"]
    class_class_curie: ClassVar[str] = "linkml_common:InvestigativeProcess"
    class_name: ClassVar[str] = "InvestigativeProcess"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.InvestigativeProcess

    id: Union[str, InvestigativeProcessId] = None
    follows_procedure: Optional[Union[str, InvestigativeProtocolId]] = None
    part_of: Optional[Union[str, InvestigationId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InvestigativeProcessId):
            self.id = InvestigativeProcessId(self.id)

        if self.follows_procedure is not None and not isinstance(self.follows_procedure, InvestigativeProtocolId):
            self.follows_procedure = InvestigativeProtocolId(self.follows_procedure)

        if self.part_of is not None and not isinstance(self.part_of, InvestigationId):
            self.part_of = InvestigationId(self.part_of)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class SampleCollectionProcess(InvestigativeProcess):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["SampleCollectionProcess"]
    class_class_curie: ClassVar[str] = "linkml_common:SampleCollectionProcess"
    class_name: ClassVar[str] = "SampleCollectionProcess"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.SampleCollectionProcess

    id: Union[str, SampleCollectionProcessId] = None
    material_collected: Optional[Union[str, SampleMaterialId]] = None
    collected_from: Optional[Union[str, NamedThingId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SampleCollectionProcessId):
            self.id = SampleCollectionProcessId(self.id)

        if self.material_collected is not None and not isinstance(self.material_collected, SampleMaterialId):
            self.material_collected = SampleMaterialId(self.material_collected)

        if self.collected_from is not None and not isinstance(self.collected_from, NamedThingId):
            self.collected_from = NamedThingId(self.collected_from)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class DataGenerationFromSample(InvestigativeProcess):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["DataGenerationFromSample"]
    class_class_curie: ClassVar[str] = "linkml_common:DataGenerationFromSample"
    class_name: ClassVar[str] = "DataGenerationFromSample"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.DataGenerationFromSample

    id: Union[str, DataGenerationFromSampleId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataGenerationFromSampleId):
            self.id = DataGenerationFromSampleId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class MaterialCollection(PlannedProcess):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["MaterialCollection"]
    class_class_curie: ClassVar[str] = "linkml_common:MaterialCollection"
    class_name: ClassVar[str] = "MaterialCollection"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.MaterialCollection

    id: Union[str, MaterialCollectionId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MaterialCollectionId):
            self.id = MaterialCollectionId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class MaterialProcessing(PlannedProcess):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["MaterialProcessing"]
    class_class_curie: ClassVar[str] = "linkml_common:MaterialProcessing"
    class_name: ClassVar[str] = "MaterialProcessing"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.MaterialProcessing

    id: Union[str, MaterialProcessingId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MaterialProcessingId):
            self.id = MaterialProcessingId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class EngineeringMaterialProcessing(MaterialProcessing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["EngineeringMaterialProcessing"]
    class_class_curie: ClassVar[str] = "linkml_common:EngineeringMaterialProcessing"
    class_name: ClassVar[str] = "EngineeringMaterialProcessing"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.EngineeringMaterialProcessing

    id: Union[str, EngineeringMaterialProcessingId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EngineeringMaterialProcessingId):
            self.id = EngineeringMaterialProcessingId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class FoodProcessing(MaterialProcessing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["FoodProcessing"]
    class_class_curie: ClassVar[str] = "linkml_common:FoodProcessing"
    class_name: ClassVar[str] = "FoodProcessing"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.FoodProcessing

    id: Union[str, FoodProcessingId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FoodProcessingId):
            self.id = FoodProcessingId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class SampleProcessing(MaterialProcessing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["SampleProcessing"]
    class_class_curie: ClassVar[str] = "linkml_common:SampleProcessing"
    class_name: ClassVar[str] = "SampleProcessing"
    class_model_uri: ClassVar[URIRef] = LINKML_COMMON.SampleProcessing

    id: Union[str, SampleProcessingId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SampleProcessingId):
            self.id = SampleProcessingId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


# Enumerations
class FossilFuelType(EnumDefinitionImpl):

    COAL = PermissibleValue(
        text="COAL",
        description="Coal")
    NATURAL_GAS = PermissibleValue(
        text="NATURAL_GAS",
        description="Natural gas")
    PETROLEUM = PermissibleValue(
        text="PETROLEUM",
        description="Petroleum")

    _defn = EnumDefinition(
        name="FossilFuelType",
    )

class ExtractiveIndustryFacilityType(EnumDefinitionImpl):

    MINING_FACILITY = PermissibleValue(
        text="MINING_FACILITY",
        description="A facility where mineral resources are extracted")
    WELL_FACILITY = PermissibleValue(
        text="WELL_FACILITY",
        description="A facility where fluid resources are extracted")
    QUARRY_FACILITY = PermissibleValue(
        text="QUARRY_FACILITY",
        description="A facility where stone, sand, or gravel are extracted")

    _defn = EnumDefinition(
        name="ExtractiveIndustryFacilityType",
    )

class ExtractiveIndustryProductType(EnumDefinitionImpl):

    MINERAL = PermissibleValue(
        text="MINERAL",
        description="A solid inorganic substance")
    METAL = PermissibleValue(
        text="METAL",
        description="A solid metallic substance")
    COAL = PermissibleValue(
        text="COAL",
        description="A combustible black or brownish-black sedimentary rock")
    OIL = PermissibleValue(
        text="OIL",
        description="A liquid petroleum resource")
    GAS = PermissibleValue(
        text="GAS",
        description="A gaseous petroleum resource")
    STONE = PermissibleValue(
        text="STONE",
        description="A solid aggregate of minerals")
    SAND = PermissibleValue(
        text="SAND",
        description="A granular material composed of finely divided rock and mineral particles")
    GRAVEL = PermissibleValue(
        text="GRAVEL",
        description="A loose aggregation of rock fragments")

    _defn = EnumDefinition(
        name="ExtractiveIndustryProductType",
    )

class MiningMethod(EnumDefinitionImpl):

    UNDERGROUND = PermissibleValue(
        text="UNDERGROUND",
        description="Extraction occurs beneath the earth's surface")
    OPEN_PIT = PermissibleValue(
        text="OPEN_PIT",
        description="Extraction occurs on the earth's surface")
    PLACER = PermissibleValue(
        text="PLACER",
        description="Extraction of valuable minerals from alluvial deposits")
    IN_SITU = PermissibleValue(
        text="IN_SITU",
        description="Extraction without removing the ore from its original location")

    _defn = EnumDefinition(
        name="MiningMethod",
    )

class WellType(EnumDefinitionImpl):

    OIL = PermissibleValue(
        text="OIL",
        description="A well that primarily extracts crude oil")
    GAS = PermissibleValue(
        text="GAS",
        description="A well that primarily extracts natural gas")
    WATER = PermissibleValue(
        text="WATER",
        description="A well that extracts water for various purposes")
    INJECTION = PermissibleValue(
        text="INJECTION",
        description="A well used to inject fluids into underground formations")

    _defn = EnumDefinition(
        name="WellType",
    )

class HealthcareEncounterClassification(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="HealthcareEncounterClassification",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Inpatient Visit",
            PermissibleValue(
                text="Inpatient Visit",
                description="""Person visiting hospital, at a Care Site, in bed, for duration of more than one day, with physicians and other Providers permanently available to deliver service around the clock"""))
        setattr(cls, "Emergency Room Visit",
            PermissibleValue(
                text="Emergency Room Visit",
                description="""Person visiting dedicated healthcare institution for treating emergencies, at a Care Site, within one day, with physicians and Providers permanently available to deliver service around the clock"""))
        setattr(cls, "Emergency Room and Inpatient Visit",
            PermissibleValue(
                text="Emergency Room and Inpatient Visit",
                description="""Person visiting ER followed by a subsequent Inpatient Visit, where Emergency department is part of hospital, and transition from the ER to other hospital departments is undefined"""))
        setattr(cls, "Non-hospital institution Visit",
            PermissibleValue(
                text="Non-hospital institution Visit",
                description="""Person visiting dedicated institution for reasons of poor health, at a Care Site, long-term or permanently, with no physician but possibly other Providers permanently available to deliver service around the clock"""))
        setattr(cls, "Outpatient Visit",
            PermissibleValue(
                text="Outpatient Visit",
                description="""Person visiting dedicated ambulatory healthcare institution, at a Care Site, within one day, without bed, with physicians or medical Providers delivering service during Visit"""))
        setattr(cls, "Home Visit",
            PermissibleValue(
                text="Home Visit",
                description="Provider visiting Person, without a Care Site, within one day, delivering service"))
        setattr(cls, "Telehealth Visit",
            PermissibleValue(
                text="Telehealth Visit",
                description="Patient engages with Provider through communication media"))
        setattr(cls, "Pharmacy Visit",
            PermissibleValue(
                text="Pharmacy Visit",
                description="Person visiting pharmacy for dispensing of Drug, at a Care Site, within one day"))
        setattr(cls, "Laboratory Visit",
            PermissibleValue(
                text="Laboratory Visit",
                description="""Patient visiting dedicated institution, at a Care Site, within one day, for the purpose of a Measurement."""))
        setattr(cls, "Ambulance Visit",
            PermissibleValue(
                text="Ambulance Visit",
                description="""Person using transportation service for the purpose of initiating one of the other Visits, without a Care Site, within one day, potentially with Providers accompanying the Visit and delivering service"""))
        setattr(cls, "Case Management Visit",
            PermissibleValue(
                text="Case Management Visit",
                description="""Person interacting with healthcare system, without a Care Site, within a day, with no Providers involved, for administrative purposes"""))

class CaseOrControlEnum(EnumDefinitionImpl):

    CASE = PermissibleValue(
        text="CASE",
        meaning=OBI["0002492"])
    CONTROL = PermissibleValue(
        text="CONTROL",
        meaning=OBI["0002493"])

    _defn = EnumDefinition(
        name="CaseOrControlEnum",
    )

class StudyDesignEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="StudyDesignEnum",
    )

class InvestigativeProtocolEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="InvestigativeProtocolEnum",
    )

class SampleProcessingEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="SampleProcessingEnum",
    )

class HumanLanguageCodeEnum(EnumDefinitionImpl):
    """
    An enumeration of languages
    """
    _defn = EnumDefinition(
        name="HumanLanguageCodeEnum",
        description="An enumeration of languages",
    )

class PersonStatus(EnumDefinitionImpl):

    ALIVE = PermissibleValue(
        text="ALIVE",
        description="the person is living",
        meaning=PATO["0001421"])
    DEAD = PermissibleValue(
        text="DEAD",
        description="the person is deceased",
        meaning=PATO["0001422"])
    UNKNOWN = PermissibleValue(
        text="UNKNOWN",
        description="the vital status is not known")

    _defn = EnumDefinition(
        name="PersonStatus",
    )

class RelativeTimeEnum(EnumDefinitionImpl):

    BEFORE = PermissibleValue(text="BEFORE")
    AFTER = PermissibleValue(text="AFTER")
    AT_SAME_TIME_AS = PermissibleValue(text="AT_SAME_TIME_AS")

    _defn = EnumDefinition(
        name="RelativeTimeEnum",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=LINKML_COMMON.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=LINKML_COMMON.name, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=LINKML_COMMON.description, domain=None, range=Optional[str])

slots.type = Slot(uri=LINKML_COMMON.type, name="type", curie=LINKML_COMMON.curie('type'),
                   model_uri=LINKML_COMMON.type, domain=None, range=Optional[str])

slots.classification = Slot(uri=LINKML_COMMON.classification, name="classification", curie=LINKML_COMMON.curie('classification'),
                   model_uri=LINKML_COMMON.classification, domain=None, range=Optional[Union[str, ConceptId]])

slots.ontology_types = Slot(uri=LINKML_COMMON.ontology_types, name="ontology_types", curie=LINKML_COMMON.curie('ontology_types'),
                   model_uri=LINKML_COMMON.ontology_types, domain=None, range=Optional[Union[Union[str, ConceptId], List[Union[str, ConceptId]]]])

slots.describes = Slot(uri=SCHEMA.describes, name="describes", curie=SCHEMA.curie('describes'),
                   model_uri=LINKML_COMMON.describes, domain=None, range=Optional[Union[dict, Any]])

slots.subject = Slot(uri=RDF.subject, name="subject", curie=RDF.curie('subject'),
                   model_uri=LINKML_COMMON.subject, domain=None, range=Optional[Union[dict, Any]])

slots.object = Slot(uri=RDF.object, name="object", curie=RDF.curie('object'),
                   model_uri=LINKML_COMMON.object, domain=None, range=Optional[Union[dict, Any]])

slots.located_at_place = Slot(uri=LINKML_COMMON.located_at_place, name="located_at_place", curie=LINKML_COMMON.curie('located_at_place'),
                   model_uri=LINKML_COMMON.located_at_place, domain=None, range=Optional[Union[str, PlaceId]])

slots.address = Slot(uri=LINKML_COMMON.address, name="address", curie=LINKML_COMMON.curie('address'),
                   model_uri=LINKML_COMMON.address, domain=None, range=Optional[Union[dict, PostalAddress]])

slots.geolocation = Slot(uri=LINKML_COMMON.geolocation, name="geolocation", curie=LINKML_COMMON.curie('geolocation'),
                   model_uri=LINKML_COMMON.geolocation, domain=None, range=Optional[Union[dict, GeoPointLocation]])

slots.bounding_coordinates = Slot(uri=LINKML_COMMON.bounding_coordinates, name="bounding_coordinates", curie=LINKML_COMMON.curie('bounding_coordinates'),
                   model_uri=LINKML_COMMON.bounding_coordinates, domain=None, range=Optional[Union[dict, GeoBoxLocation]])

slots.primary_email = Slot(uri=SCHEMA.email, name="primary_email", curie=SCHEMA.curie('email'),
                   model_uri=LINKML_COMMON.primary_email, domain=None, range=Optional[str])

slots.birth_date = Slot(uri=SCHEMA.birthDate, name="birth_date", curie=SCHEMA.curie('birthDate'),
                   model_uri=LINKML_COMMON.birth_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.age_in_years = Slot(uri=LINKML_COMMON.age_in_years, name="age_in_years", curie=LINKML_COMMON.curie('age_in_years'),
                   model_uri=LINKML_COMMON.age_in_years, domain=None, range=Optional[int])

slots.vital_status = Slot(uri=LINKML_COMMON.vital_status, name="vital_status", curie=LINKML_COMMON.curie('vital_status'),
                   model_uri=LINKML_COMMON.vital_status, domain=None, range=Optional[Union[str, "PersonStatus"]])

slots.starts_at = Slot(uri=LINKML_COMMON.starts_at, name="starts_at", curie=LINKML_COMMON.curie('starts_at'),
                   model_uri=LINKML_COMMON.starts_at, domain=None, range=Optional[Union[dict, TimePoint]])

slots.ends_at = Slot(uri=LINKML_COMMON.ends_at, name="ends_at", curie=LINKML_COMMON.curie('ends_at'),
                   model_uri=LINKML_COMMON.ends_at, domain=None, range=Optional[Union[dict, TimePoint]])

slots.happens_at = Slot(uri=LINKML_COMMON.happens_at, name="happens_at", curie=LINKML_COMMON.curie('happens_at'),
                   model_uri=LINKML_COMMON.happens_at, domain=None, range=Optional[Union[dict, TimePoint]])

slots.year_value = Slot(uri=LINKML_COMMON.year_value, name="year_value", curie=LINKML_COMMON.curie('year_value'),
                   model_uri=LINKML_COMMON.year_value, domain=None, range=Optional[int])

slots.date_value = Slot(uri=LINKML_COMMON.date_value, name="date_value", curie=LINKML_COMMON.curie('date_value'),
                   model_uri=LINKML_COMMON.date_value, domain=None, range=Optional[Union[str, XSDDate]])

slots.time_value = Slot(uri=LINKML_COMMON.time_value, name="time_value", curie=LINKML_COMMON.curie('time_value'),
                   model_uri=LINKML_COMMON.time_value, domain=None, range=Optional[Union[str, XSDTime]])

slots.datetime_value = Slot(uri=LINKML_COMMON.datetime_value, name="datetime_value", curie=LINKML_COMMON.curie('datetime_value'),
                   model_uri=LINKML_COMMON.datetime_value, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.marker_event = Slot(uri=LINKML_COMMON.marker_event, name="marker_event", curie=LINKML_COMMON.curie('marker_event'),
                   model_uri=LINKML_COMMON.marker_event, domain=None, range=Optional[Union[str, EventId]])

slots.has_interval = Slot(uri=LINKML_COMMON.has_interval, name="has_interval", curie=LINKML_COMMON.curie('has_interval'),
                   model_uri=LINKML_COMMON.has_interval, domain=None, range=Optional[Union[dict, TemporalInterval]])

slots.has_duration = Slot(uri=LINKML_COMMON.has_duration, name="has_duration", curie=LINKML_COMMON.curie('has_duration'),
                   model_uri=LINKML_COMMON.has_duration, domain=None, range=Optional[Union[dict, Duration]])

slots.mathematicalOperation__inputs = Slot(uri=LINKML_COMMON.inputs, name="mathematicalOperation__inputs", curie=LINKML_COMMON.curie('inputs'),
                   model_uri=LINKML_COMMON.mathematicalOperation__inputs, domain=None, range=Optional[Union[Union[dict, Any], List[Union[dict, Any]]]])

slots.mathematicalOperation__outputs = Slot(uri=LINKML_COMMON.outputs, name="mathematicalOperation__outputs", curie=LINKML_COMMON.curie('outputs'),
                   model_uri=LINKML_COMMON.mathematicalOperation__outputs, domain=None, range=Optional[Union[Union[dict, Any], List[Union[dict, Any]]]])

slots.mathematicalOperation__parts = Slot(uri=LINKML_COMMON.parts, name="mathematicalOperation__parts", curie=LINKML_COMMON.curie('parts'),
                   model_uri=LINKML_COMMON.mathematicalOperation__parts, domain=None, range=Optional[Union[Union[dict, MathematicalOperation], List[Union[dict, MathematicalOperation]]]])

slots.mathematicalOperation__immediate_preceding_steps = Slot(uri=LINKML_COMMON.immediate_preceding_steps, name="mathematicalOperation__immediate_preceding_steps", curie=LINKML_COMMON.curie('immediate_preceding_steps'),
                   model_uri=LINKML_COMMON.mathematicalOperation__immediate_preceding_steps, domain=None, range=Optional[Union[Union[dict, MathematicalOperation], List[Union[dict, MathematicalOperation]]]])

slots.collection__members = Slot(uri=LINKML_COMMON.members, name="collection__members", curie=LINKML_COMMON.curie('members'),
                   model_uri=LINKML_COMMON.collection__members, domain=None, range=Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]])

slots.dataset__collected_as_part_of = Slot(uri=LINKML_COMMON.collected_as_part_of, name="dataset__collected_as_part_of", curie=LINKML_COMMON.curie('collected_as_part_of'),
                   model_uri=LINKML_COMMON.dataset__collected_as_part_of, domain=None, range=Optional[Union[Union[str, InvestigationId], List[Union[str, InvestigationId]]]])

slots.clinicalCohort__definition = Slot(uri=LINKML_COMMON.definition, name="clinicalCohort__definition", curie=LINKML_COMMON.curie('definition'),
                   model_uri=LINKML_COMMON.clinicalCohort__definition, domain=None, range=Optional[Union[str, ClinicalCohortDefinitionId]])

slots.clinicalCohortEnrollment__patient = Slot(uri=LINKML_COMMON.patient, name="clinicalCohortEnrollment__patient", curie=LINKML_COMMON.curie('patient'),
                   model_uri=LINKML_COMMON.clinicalCohortEnrollment__patient, domain=None, range=Optional[Union[dict, Patient]])

slots.clinicalCohortEnrollment__cohort = Slot(uri=LINKML_COMMON.cohort, name="clinicalCohortEnrollment__cohort", curie=LINKML_COMMON.curie('cohort'),
                   model_uri=LINKML_COMMON.clinicalCohortEnrollment__cohort, domain=None, range=Optional[Union[str, ClinicalCohortId]])

slots.engineeringProcess__follows_procedure = Slot(uri=LINKML_COMMON.follows_procedure, name="engineeringProcess__follows_procedure", curie=LINKML_COMMON.curie('follows_procedure'),
                   model_uri=LINKML_COMMON.engineeringProcess__follows_procedure, domain=None, range=Optional[Union[str, EngineeringSpecificationId]])

slots.engineeringProcess__part_of = Slot(uri=LINKML_COMMON.part_of, name="engineeringProcess__part_of", curie=LINKML_COMMON.curie('part_of'),
                   model_uri=LINKML_COMMON.engineeringProcess__part_of, domain=None, range=Optional[Union[str, EngineeringProcessId]])

slots.powerPlant__plant_type = Slot(uri=LINKML_COMMON.plant_type, name="powerPlant__plant_type", curie=LINKML_COMMON.curie('plant_type'),
                   model_uri=LINKML_COMMON.powerPlant__plant_type, domain=None, range=Optional[Union[str, PowerPlantTypeId]])

slots.powerPlant__location = Slot(uri=LINKML_COMMON.location, name="powerPlant__location", curie=LINKML_COMMON.curie('location'),
                   model_uri=LINKML_COMMON.powerPlant__location, domain=None, range=Optional[Union[str, PlaceId]])

slots.powerPlant__operator = Slot(uri=LINKML_COMMON.operator, name="powerPlant__operator", curie=LINKML_COMMON.curie('operator'),
                   model_uri=LINKML_COMMON.powerPlant__operator, domain=None, range=Optional[Union[str, OrganizationId]])

slots.powerPlant__capacity = Slot(uri=LINKML_COMMON.capacity, name="powerPlant__capacity", curie=LINKML_COMMON.curie('capacity'),
                   model_uri=LINKML_COMMON.powerPlant__capacity, domain=None, range=Optional[Union[dict, SimpleQuantity]])

slots.powerPlant__commissioning_date = Slot(uri=LINKML_COMMON.commissioning_date, name="powerPlant__commissioning_date", curie=LINKML_COMMON.curie('commissioning_date'),
                   model_uri=LINKML_COMMON.powerPlant__commissioning_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.powerPlant__decommissioning_date = Slot(uri=LINKML_COMMON.decommissioning_date, name="powerPlant__decommissioning_date", curie=LINKML_COMMON.curie('decommissioning_date'),
                   model_uri=LINKML_COMMON.powerPlant__decommissioning_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.powerPlant__capex = Slot(uri=LINKML_COMMON.capex, name="powerPlant__capex", curie=LINKML_COMMON.curie('capex'),
                   model_uri=LINKML_COMMON.powerPlant__capex, domain=None, range=Optional[Union[dict, MoneyQuantity]])

slots.powerPlant__opex = Slot(uri=LINKML_COMMON.opex, name="powerPlant__opex", curie=LINKML_COMMON.curie('opex'),
                   model_uri=LINKML_COMMON.powerPlant__opex, domain=None, range=Optional[Union[dict, MoneyQuantity]])

slots.fossilFuelPlant__fuel = Slot(uri=LINKML_COMMON.fuel, name="fossilFuelPlant__fuel", curie=LINKML_COMMON.curie('fuel'),
                   model_uri=LINKML_COMMON.fossilFuelPlant__fuel, domain=None, range=Optional[Union[str, FossilFuelId]])

slots.hydroelectricPlant__dam = Slot(uri=LINKML_COMMON.dam, name="hydroelectricPlant__dam", curie=LINKML_COMMON.curie('dam'),
                   model_uri=LINKML_COMMON.hydroelectricPlant__dam, domain=None, range=Optional[Union[str, LandformId]])

slots.electricalGrid__plants = Slot(uri=LINKML_COMMON.plants, name="electricalGrid__plants", curie=LINKML_COMMON.curie('plants'),
                   model_uri=LINKML_COMMON.electricalGrid__plants, domain=None, range=Optional[Union[Union[str, PowerPlantId], List[Union[str, PowerPlantId]]]])

slots.extractiveIndustryFacility__facility_type = Slot(uri=LINKML_COMMON.facility_type, name="extractiveIndustryFacility__facility_type", curie=LINKML_COMMON.curie('facility_type'),
                   model_uri=LINKML_COMMON.extractiveIndustryFacility__facility_type, domain=None, range=Optional[Union[str, "ExtractiveIndustryFacilityType"]])

slots.extractiveIndustryFacility__operator = Slot(uri=LINKML_COMMON.operator, name="extractiveIndustryFacility__operator", curie=LINKML_COMMON.curie('operator'),
                   model_uri=LINKML_COMMON.extractiveIndustryFacility__operator, domain=None, range=Optional[Union[str, OrganizationId]])

slots.extractiveIndustryFacility__products = Slot(uri=LINKML_COMMON.products, name="extractiveIndustryFacility__products", curie=LINKML_COMMON.curie('products'),
                   model_uri=LINKML_COMMON.extractiveIndustryFacility__products, domain=None, range=Optional[Union[Dict[Union[str, ExtractiveIndustryProductId], Union[dict, ExtractiveIndustryProduct]], List[Union[dict, ExtractiveIndustryProduct]]]])

slots.extractiveIndustryFacility__production_capacity = Slot(uri=LINKML_COMMON.production_capacity, name="extractiveIndustryFacility__production_capacity", curie=LINKML_COMMON.curie('production_capacity'),
                   model_uri=LINKML_COMMON.extractiveIndustryFacility__production_capacity, domain=None, range=Optional[Union[dict, Quantity]])

slots.extractiveIndustryFacility__annual_production = Slot(uri=LINKML_COMMON.annual_production, name="extractiveIndustryFacility__annual_production", curie=LINKML_COMMON.curie('annual_production'),
                   model_uri=LINKML_COMMON.extractiveIndustryFacility__annual_production, domain=None, range=Optional[Union[dict, Quantity]])

slots.extractiveIndustryFacility__reserves = Slot(uri=LINKML_COMMON.reserves, name="extractiveIndustryFacility__reserves", curie=LINKML_COMMON.curie('reserves'),
                   model_uri=LINKML_COMMON.extractiveIndustryFacility__reserves, domain=None, range=Optional[Union[dict, Quantity]])

slots.miningFacility__mining_method = Slot(uri=LINKML_COMMON.mining_method, name="miningFacility__mining_method", curie=LINKML_COMMON.curie('mining_method'),
                   model_uri=LINKML_COMMON.miningFacility__mining_method, domain=None, range=Optional[Union[str, "MiningMethod"]])

slots.miningFacility__depth = Slot(uri=LINKML_COMMON.depth, name="miningFacility__depth", curie=LINKML_COMMON.curie('depth'),
                   model_uri=LINKML_COMMON.miningFacility__depth, domain=None, range=Optional[Union[dict, Quantity]])

slots.miningFacility__area = Slot(uri=LINKML_COMMON.area, name="miningFacility__area", curie=LINKML_COMMON.curie('area'),
                   model_uri=LINKML_COMMON.miningFacility__area, domain=None, range=Optional[Union[dict, Quantity]])

slots.wellFacility__well_type = Slot(uri=LINKML_COMMON.well_type, name="wellFacility__well_type", curie=LINKML_COMMON.curie('well_type'),
                   model_uri=LINKML_COMMON.wellFacility__well_type, domain=None, range=Optional[Union[str, "WellType"]])

slots.wellFacility__depth = Slot(uri=LINKML_COMMON.depth, name="wellFacility__depth", curie=LINKML_COMMON.curie('depth'),
                   model_uri=LINKML_COMMON.wellFacility__depth, domain=None, range=Optional[Union[dict, Quantity]])

slots.extractiveIndustryProduct__product_type = Slot(uri=LINKML_COMMON.product_type, name="extractiveIndustryProduct__product_type", curie=LINKML_COMMON.curie('product_type'),
                   model_uri=LINKML_COMMON.extractiveIndustryProduct__product_type, domain=None, range=Optional[Union[str, "ExtractiveIndustryProductType"]])

slots.extractiveIndustryProduct__grade = Slot(uri=LINKML_COMMON.grade, name="extractiveIndustryProduct__grade", curie=LINKML_COMMON.curie('grade'),
                   model_uri=LINKML_COMMON.extractiveIndustryProduct__grade, domain=None, range=Optional[Union[dict, SimpleQuantity]])

slots.extractiveIndustryProduct__processing_method = Slot(uri=LINKML_COMMON.processing_method, name="extractiveIndustryProduct__processing_method", curie=LINKML_COMMON.curie('processing_method'),
                   model_uri=LINKML_COMMON.extractiveIndustryProduct__processing_method, domain=None, range=Optional[Union[str, EngineeringSpecificationId]])

slots.moneyQuantity__value = Slot(uri=LINKML_COMMON.value, name="moneyQuantity__value", curie=LINKML_COMMON.curie('value'),
                   model_uri=LINKML_COMMON.moneyQuantity__value, domain=None, range=Optional[float])

slots.moneyQuantity__unit = Slot(uri=LINKML_COMMON.unit, name="moneyQuantity__unit", curie=LINKML_COMMON.curie('unit'),
                   model_uri=LINKML_COMMON.moneyQuantity__unit, domain=None, range=Optional[Union[str, CurrencyConceptId]])

slots.financialAccount__account_number = Slot(uri=LINKML_COMMON.account_number, name="financialAccount__account_number", curie=LINKML_COMMON.curie('account_number'),
                   model_uri=LINKML_COMMON.financialAccount__account_number, domain=None, range=Optional[str])

slots.financialAccount__bank = Slot(uri=LINKML_COMMON.bank, name="financialAccount__bank", curie=LINKML_COMMON.curie('bank'),
                   model_uri=LINKML_COMMON.financialAccount__bank, domain=None, range=Optional[Union[str, OrganizationId]])

slots.financialAccount__account_holder = Slot(uri=LINKML_COMMON.account_holder, name="financialAccount__account_holder", curie=LINKML_COMMON.curie('account_holder'),
                   model_uri=LINKML_COMMON.financialAccount__account_holder, domain=None, range=Optional[Union[str, PersonId]])

slots.foodRecipe__ingredients = Slot(uri=LINKML_COMMON.ingredients, name="foodRecipe__ingredients", curie=LINKML_COMMON.curie('ingredients'),
                   model_uri=LINKML_COMMON.foodRecipe__ingredients, domain=None, range=Optional[Union[Union[dict, FoodIngredient], List[Union[dict, FoodIngredient]]]])

slots.foodRecipe__steps = Slot(uri=LINKML_COMMON.steps, name="foodRecipe__steps", curie=LINKML_COMMON.curie('steps'),
                   model_uri=LINKML_COMMON.foodRecipe__steps, domain=None, range=Optional[Union[Union[str, FoodProcessingId], List[Union[str, FoodProcessingId]]]])

slots.postalAddress__street_address = Slot(uri=LINKML_COMMON.street_address, name="postalAddress__street_address", curie=LINKML_COMMON.curie('street_address'),
                   model_uri=LINKML_COMMON.postalAddress__street_address, domain=None, range=Optional[str])

slots.postalAddress__street_address_additional = Slot(uri=LINKML_COMMON.street_address_additional, name="postalAddress__street_address_additional", curie=LINKML_COMMON.curie('street_address_additional'),
                   model_uri=LINKML_COMMON.postalAddress__street_address_additional, domain=None, range=Optional[str])

slots.postalAddress__city = Slot(uri=LINKML_COMMON.city, name="postalAddress__city", curie=LINKML_COMMON.curie('city'),
                   model_uri=LINKML_COMMON.postalAddress__city, domain=None, range=Optional[str])

slots.postalAddress__state = Slot(uri=LINKML_COMMON.state, name="postalAddress__state", curie=LINKML_COMMON.curie('state'),
                   model_uri=LINKML_COMMON.postalAddress__state, domain=None, range=Optional[str])

slots.postalAddress__postal_code = Slot(uri=LINKML_COMMON.postal_code, name="postalAddress__postal_code", curie=LINKML_COMMON.curie('postal_code'),
                   model_uri=LINKML_COMMON.postalAddress__postal_code, domain=None, range=Optional[str])

slots.postalAddress__country = Slot(uri=LINKML_COMMON.country, name="postalAddress__country", curie=LINKML_COMMON.curie('country'),
                   model_uri=LINKML_COMMON.postalAddress__country, domain=None, range=Optional[str])

slots.geoPointLocation__latitude = Slot(uri=LINKML_COMMON.latitude, name="geoPointLocation__latitude", curie=LINKML_COMMON.curie('latitude'),
                   model_uri=LINKML_COMMON.geoPointLocation__latitude, domain=None, range=Optional[Decimal])

slots.geoPointLocation__longitude = Slot(uri=LINKML_COMMON.longitude, name="geoPointLocation__longitude", curie=LINKML_COMMON.curie('longitude'),
                   model_uri=LINKML_COMMON.geoPointLocation__longitude, domain=None, range=Optional[Decimal])

slots.geoPointLocation__altitude = Slot(uri=LINKML_COMMON.altitude, name="geoPointLocation__altitude", curie=LINKML_COMMON.curie('altitude'),
                   model_uri=LINKML_COMMON.geoPointLocation__altitude, domain=None, range=Optional[Decimal])

slots.geoBoxLocation__west_bounding_coordinate = Slot(uri=LINKML_COMMON.west_bounding_coordinate, name="geoBoxLocation__west_bounding_coordinate", curie=LINKML_COMMON.curie('west_bounding_coordinate'),
                   model_uri=LINKML_COMMON.geoBoxLocation__west_bounding_coordinate, domain=None, range=Optional[Decimal])

slots.geoBoxLocation__east_bounding_coordinate = Slot(uri=LINKML_COMMON.east_bounding_coordinate, name="geoBoxLocation__east_bounding_coordinate", curie=LINKML_COMMON.curie('east_bounding_coordinate'),
                   model_uri=LINKML_COMMON.geoBoxLocation__east_bounding_coordinate, domain=None, range=Optional[Decimal])

slots.geoBoxLocation__north_bounding_coordinate = Slot(uri=LINKML_COMMON.north_bounding_coordinate, name="geoBoxLocation__north_bounding_coordinate", curie=LINKML_COMMON.curie('north_bounding_coordinate'),
                   model_uri=LINKML_COMMON.geoBoxLocation__north_bounding_coordinate, domain=None, range=Optional[Decimal])

slots.geoBoxLocation__south_bounding_coordinate = Slot(uri=LINKML_COMMON.south_bounding_coordinate, name="geoBoxLocation__south_bounding_coordinate", curie=LINKML_COMMON.curie('south_bounding_coordinate'),
                   model_uri=LINKML_COMMON.geoBoxLocation__south_bounding_coordinate, domain=None, range=Optional[Decimal])

slots.healthcareEncounter__patient = Slot(uri=LINKML_COMMON.patient, name="healthcareEncounter__patient", curie=LINKML_COMMON.curie('patient'),
                   model_uri=LINKML_COMMON.healthcareEncounter__patient, domain=None, range=Optional[Union[dict, Patient]])

slots.healthcareEncounter__provider = Slot(uri=LINKML_COMMON.provider, name="healthcareEncounter__provider", curie=LINKML_COMMON.curie('provider'),
                   model_uri=LINKML_COMMON.healthcareEncounter__provider, domain=None, range=Optional[Union[dict, HealthcareProvider]])

slots.healthcareRole__is_person = Slot(uri=LINKML_COMMON.is_person, name="healthcareRole__is_person", curie=LINKML_COMMON.curie('is_person'),
                   model_uri=LINKML_COMMON.healthcareRole__is_person, domain=None, range=Optional[Union[str, PersonId]])

slots.healthcareProvider__speciality = Slot(uri=LINKML_COMMON.speciality, name="healthcareProvider__speciality", curie=LINKML_COMMON.curie('speciality'),
                   model_uri=LINKML_COMMON.healthcareProvider__speciality, domain=None, range=Optional[Union[str, ConceptId]])

slots.healthcareProvider__care_site = Slot(uri=LINKML_COMMON.care_site, name="healthcareProvider__care_site", curie=LINKML_COMMON.curie('care_site'),
                   model_uri=LINKML_COMMON.healthcareProvider__care_site, domain=None, range=Optional[Union[str, HealthcareSiteId]])

slots.healthcareConditionOccurrence__patient = Slot(uri=LINKML_COMMON.patient, name="healthcareConditionOccurrence__patient", curie=LINKML_COMMON.curie('patient'),
                   model_uri=LINKML_COMMON.healthcareConditionOccurrence__patient, domain=None, range=Optional[Union[dict, Patient]])

slots.healthcareConditionOccurrence__observed_during = Slot(uri=LINKML_COMMON.observed_during, name="healthcareConditionOccurrence__observed_during", curie=LINKML_COMMON.curie('observed_during'),
                   model_uri=LINKML_COMMON.healthcareConditionOccurrence__observed_during, domain=None, range=Optional[Union[str, HealthcareEncounterId]])

slots.investigation__objectives = Slot(uri=LINKML_COMMON.objectives, name="investigation__objectives", curie=LINKML_COMMON.curie('objectives'),
                   model_uri=LINKML_COMMON.investigation__objectives, domain=None, range=Optional[str])

slots.investigation__variables = Slot(uri=LINKML_COMMON.variables, name="investigation__variables", curie=LINKML_COMMON.curie('variables'),
                   model_uri=LINKML_COMMON.investigation__variables, domain=None, range=Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]])

slots.investigativeProtocol__protocols_io_url = Slot(uri=LINKML_COMMON.protocols_io_url, name="investigativeProtocol__protocols_io_url", curie=LINKML_COMMON.curie('protocols_io_url'),
                   model_uri=LINKML_COMMON.investigativeProtocol__protocols_io_url, domain=None, range=Optional[Union[str, URI]])

slots.investigativeProcess__follows_procedure = Slot(uri=LINKML_COMMON.follows_procedure, name="investigativeProcess__follows_procedure", curie=LINKML_COMMON.curie('follows_procedure'),
                   model_uri=LINKML_COMMON.investigativeProcess__follows_procedure, domain=None, range=Optional[Union[str, InvestigativeProtocolId]])

slots.investigativeProcess__part_of = Slot(uri=LINKML_COMMON.part_of, name="investigativeProcess__part_of", curie=LINKML_COMMON.curie('part_of'),
                   model_uri=LINKML_COMMON.investigativeProcess__part_of, domain=None, range=Optional[Union[str, InvestigationId]])

slots.sampleCollectionProcess__material_collected = Slot(uri=LINKML_COMMON.material_collected, name="sampleCollectionProcess__material_collected", curie=LINKML_COMMON.curie('material_collected'),
                   model_uri=LINKML_COMMON.sampleCollectionProcess__material_collected, domain=None, range=Optional[Union[str, SampleMaterialId]])

slots.sampleCollectionProcess__collected_from = Slot(uri=LINKML_COMMON.collected_from, name="sampleCollectionProcess__collected_from", curie=LINKML_COMMON.curie('collected_from'),
                   model_uri=LINKML_COMMON.sampleCollectionProcess__collected_from, domain=None, range=Optional[Union[str, NamedThingId]])

slots.measurement__quantity_measured = Slot(uri=LINKML_COMMON.quantity_measured, name="measurement__quantity_measured", curie=LINKML_COMMON.curie('quantity_measured'),
                   model_uri=LINKML_COMMON.measurement__quantity_measured, domain=None, range=Optional[Union[dict, Quantity]])

slots.measurement__variable_measured = Slot(uri=LINKML_COMMON.variable_measured, name="measurement__variable_measured", curie=LINKML_COMMON.curie('variable_measured'),
                   model_uri=LINKML_COMMON.measurement__variable_measured, domain=None, range=Optional[Union[dict, Variable]])

slots.variable__allowed_units = Slot(uri=LINKML_COMMON.allowed_units, name="variable__allowed_units", curie=LINKML_COMMON.curie('allowed_units'),
                   model_uri=LINKML_COMMON.variable__allowed_units, domain=None, range=Optional[Union[Union[str, UnitConceptId], List[Union[str, UnitConceptId]]]])

slots.quantity__has_quantity_kind = Slot(uri=LINKML_COMMON.has_quantity_kind, name="quantity__has_quantity_kind", curie=LINKML_COMMON.curie('has_quantity_kind'),
                   model_uri=LINKML_COMMON.quantity__has_quantity_kind, domain=None, range=Optional[Union[str, QuantityKindId]])

slots.simpleQuantity__value = Slot(uri=LINKML_COMMON.value, name="simpleQuantity__value", curie=LINKML_COMMON.curie('value'),
                   model_uri=LINKML_COMMON.simpleQuantity__value, domain=None, range=Optional[float])

slots.simpleQuantity__unit = Slot(uri=LINKML_COMMON.unit, name="simpleQuantity__unit", curie=LINKML_COMMON.curie('unit'),
                   model_uri=LINKML_COMMON.simpleQuantity__unit, domain=None, range=Optional[Union[str, UnitConceptId]])

slots.ratio__numerator = Slot(uri=LINKML_COMMON.numerator, name="ratio__numerator", curie=LINKML_COMMON.curie('numerator'),
                   model_uri=LINKML_COMMON.ratio__numerator, domain=None, range=Optional[Union[dict, Quantity]])

slots.ratio__denominator = Slot(uri=LINKML_COMMON.denominator, name="ratio__denominator", curie=LINKML_COMMON.curie('denominator'),
                   model_uri=LINKML_COMMON.ratio__denominator, domain=None, range=Optional[Union[dict, Quantity]])

slots.quantityRange__lower_bound = Slot(uri=LINKML_COMMON.lower_bound, name="quantityRange__lower_bound", curie=LINKML_COMMON.curie('lower_bound'),
                   model_uri=LINKML_COMMON.quantityRange__lower_bound, domain=None, range=Optional[Union[dict, Quantity]])

slots.quantityRange__upper_bound = Slot(uri=LINKML_COMMON.upper_bound, name="quantityRange__upper_bound", curie=LINKML_COMMON.curie('upper_bound'),
                   model_uri=LINKML_COMMON.quantityRange__upper_bound, domain=None, range=Optional[Union[dict, Quantity]])

slots.creativeWork__title = Slot(uri=LINKML_COMMON.title, name="creativeWork__title", curie=LINKML_COMMON.curie('title'),
                   model_uri=LINKML_COMMON.creativeWork__title, domain=None, range=Optional[str])

slots.creativeWork__abstract = Slot(uri=LINKML_COMMON.abstract, name="creativeWork__abstract", curie=LINKML_COMMON.curie('abstract'),
                   model_uri=LINKML_COMMON.creativeWork__abstract, domain=None, range=Optional[str])

slots.creativeWork__rights = Slot(uri=LINKML_COMMON.rights, name="creativeWork__rights", curie=LINKML_COMMON.curie('rights'),
                   model_uri=LINKML_COMMON.creativeWork__rights, domain=None, range=Optional[str])

slots.creativeWork__creators = Slot(uri=DCTERMS.creator, name="creativeWork__creators", curie=DCTERMS.curie('creator'),
                   model_uri=LINKML_COMMON.creativeWork__creators, domain=None, range=Optional[Union[Union[str, AgentId], List[Union[str, AgentId]]]])

slots.creativeWork__contributors = Slot(uri=DCTERMS.contributor, name="creativeWork__contributors", curie=DCTERMS.curie('contributor'),
                   model_uri=LINKML_COMMON.creativeWork__contributors, domain=None, range=Optional[Union[Union[str, AgentId], List[Union[str, AgentId]]]])

slots.creativeWork__contacts = Slot(uri=SCHEMA.contactPoint, name="creativeWork__contacts", curie=SCHEMA.curie('contactPoint'),
                   model_uri=LINKML_COMMON.creativeWork__contacts, domain=None, range=Optional[Union[Union[str, AgentId], List[Union[str, AgentId]]]])

slots.creativeWork__keywords = Slot(uri=SCHEMA.keywords, name="creativeWork__keywords", curie=SCHEMA.curie('keywords'),
                   model_uri=LINKML_COMMON.creativeWork__keywords, domain=None, range=Optional[Union[str, List[str]]])

slots.temporalRelationship__predicate = Slot(uri=LINKML_COMMON.predicate, name="temporalRelationship__predicate", curie=LINKML_COMMON.curie('predicate'),
                   model_uri=LINKML_COMMON.temporalRelationship__predicate, domain=None, range=Optional[Union[str, "RelativeTimeEnum"]])

slots.temporalRelationship__relative_to = Slot(uri=LINKML_COMMON.relative_to, name="temporalRelationship__relative_to", curie=LINKML_COMMON.curie('relative_to'),
                   model_uri=LINKML_COMMON.temporalRelationship__relative_to, domain=None, range=Optional[Union[dict, Entity]])

slots.plannedProcess__follows_procedure = Slot(uri=LINKML_COMMON.follows_procedure, name="plannedProcess__follows_procedure", curie=LINKML_COMMON.curie('follows_procedure'),
                   model_uri=LINKML_COMMON.plannedProcess__follows_procedure, domain=None, range=Optional[Union[str, ProcedureId]])

slots.plannedProcess__uses_physical_device = Slot(uri=LINKML_COMMON.uses_physical_device, name="plannedProcess__uses_physical_device", curie=LINKML_COMMON.curie('uses_physical_device'),
                   model_uri=LINKML_COMMON.plannedProcess__uses_physical_device, domain=None, range=Optional[Union[str, PhysicalDeviceId]])

slots.Landform_geolocation = Slot(uri=LINKML_COMMON.geolocation, name="Landform_geolocation", curie=LINKML_COMMON.curie('geolocation'),
                   model_uri=LINKML_COMMON.Landform_geolocation, domain=Landform, range=Optional[Union[dict, "GeoPointLocation"]])

slots.HealthcareEncounter_classification = Slot(uri=LINKML_COMMON.classification, name="HealthcareEncounter_classification", curie=LINKML_COMMON.curie('classification'),
                   model_uri=LINKML_COMMON.HealthcareEncounter_classification, domain=HealthcareEncounter, range=Optional[Union[str, "HealthcareEncounterClassification"]])

slots.InvestigativeProtocol_classification = Slot(uri=LINKML_COMMON.classification, name="InvestigativeProtocol_classification", curie=LINKML_COMMON.curie('classification'),
                   model_uri=LINKML_COMMON.InvestigativeProtocol_classification, domain=InvestigativeProtocol, range=Optional[Union[str, ConceptId]])

slots.StudyDesign_classification = Slot(uri=LINKML_COMMON.classification, name="StudyDesign_classification", curie=LINKML_COMMON.curie('classification'),
                   model_uri=LINKML_COMMON.StudyDesign_classification, domain=StudyDesign, range=Optional[Union[str, ConceptId]])

slots.UnitConversionOperation_inputs = Slot(uri=LINKML_COMMON.inputs, name="UnitConversionOperation_inputs", curie=LINKML_COMMON.curie('inputs'),
                   model_uri=LINKML_COMMON.UnitConversionOperation_inputs, domain=UnitConversionOperation, range=Optional[Union[Union[dict, Quantity], List[Union[dict, Quantity]]]])

slots.UnitConversionOperation_outputs = Slot(uri=LINKML_COMMON.outputs, name="UnitConversionOperation_outputs", curie=LINKML_COMMON.curie('outputs'),
                   model_uri=LINKML_COMMON.UnitConversionOperation_outputs, domain=UnitConversionOperation, range=Optional[Union[Union[dict, Quantity], List[Union[dict, Quantity]]]])

slots.Person_primary_email = Slot(uri=SCHEMA.email, name="Person_primary_email", curie=SCHEMA.curie('email'),
                   model_uri=LINKML_COMMON.Person_primary_email, domain=Person, range=Optional[str],
                   pattern=re.compile(r'^\S+@[\S+\.]+\S+'))