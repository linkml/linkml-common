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


class RelativeTimeEnum(str, Enum):
    BEFORE = "BEFORE"
    AFTER = "AFTER"
    AT_SAME_TIME_AS = "AT_SAME_TIME_AS"


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


class Entity(ConfiguredBaseModel):
    """
    A physical, digital, conceptual, or other kind of thing with some common characteristics
    """
    type: Literal["Entity"] = Field("Entity", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class NamedThing(Entity):
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["NamedThing"] = Field("NamedThing", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""")
    ontology_types: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""")


class Concept(NamedThing):
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["Concept"] = Field("Concept", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""")
    ontology_types: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""")


class InformationEntity(NamedThing):
    """
    An entity that describes some information
    """
    describes: Optional[Any] = Field(None, description="""The thing that is being described""")
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["InformationEntity"] = Field("InformationEntity", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""")
    ontology_types: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""")


class PhysicalDevice(NamedThing):
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["PhysicalDevice"] = Field("PhysicalDevice", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""")
    ontology_types: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""")


class Intangible(Entity):
    """
    An entity that is not a physical object, process, or information
    """
    type: Literal["Intangible"] = Field("Intangible", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class Role(Intangible):
    type: Literal["Role"] = Field("Role", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class Relationship(Intangible):
    type: Literal["Relationship"] = Field("Relationship", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class Location(ConfiguredBaseModel):
    pass


class PointLocation(Location):
    pass


class Observation(Entity):
    """
    A statement about the state of something
    """
    type: Literal["Observation"] = Field("Observation", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class Specification(NamedThing):
    """
    A specification of a thing
    """
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["Specification"] = Field("Specification", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""")
    ontology_types: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""")


class Procedure(Specification):
    """
    A canonical series of actions conducted in a certain order or manner
    """
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["Procedure"] = Field("Procedure", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""")
    ontology_types: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""")


class MathematicalOperation(ConfiguredBaseModel):
    """
    Application of a mathematical operation to one or more inputs to produce one or more outputs
    """
    inputs: Optional[List[Any]] = Field(default_factory=list, description="""The inputs to the operation""")
    outputs: Optional[List[Any]] = Field(default_factory=list, description="""The outputs of the operation""")
    parts: Optional[List[MathematicalOperation]] = Field(default_factory=list, description="""The parts of the process""")
    immediate_preceding_steps: Optional[List[MathematicalOperation]] = Field(default_factory=list, description="""The steps that immediately precede this step""")


class Collection(Intangible):
    """
    A group of things. The collection may be heterogeneous or homogeneous.
    """
    members: Optional[List[Union[Entity,NamedThing,Intangible,Observation,Variable,Measurement,Role,Relationship,Collection,TimePointOrTemporalInterval,Service,Quantity,QuantityRange,Duration,SimpleQuantity,Ratio,FoodIngredient,TemporalInterval,TimePoint,TemporalRelationship,Concept,InformationEntity,PhysicalDevice,Specification,Event,Agent,CreativeWork,Person,Organization,AutomatedAgent,LifeEvent,PlannedProcess,MaterialCollection,MaterialProcessing,FoodProcessing,Procedure,FoodRecipe,QuantityKind,UnitConcept,FoodTypeConcept,BasicFoodType,CompositeFoodType]]] = Field(default_factory=list, description="""The members of the collection""")
    type: Literal["Collection"] = Field("Collection", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class Event(NamedThing):
    """
    A thing that happens
    """
    starts_at: Optional[TimePoint] = Field(None)
    ends_at: Optional[TimePoint] = Field(None)
    happens_at: Optional[TimePoint] = Field(None)
    has_interval: Optional[TemporalInterval] = Field(None)
    has_duration: Optional[Duration] = Field(None)
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["Event"] = Field("Event", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""")
    ontology_types: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""")


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


class TemporalRelationship(Relationship):
    """
    A relationship to another time point
    """
    predicate: Optional[RelativeTimeEnum] = Field(None, description="""The relationship between the two time points""")
    relative_to: Optional[Union[TemporalInterval, TimePoint, str]] = Field(None)
    type: Literal["TemporalRelationship"] = Field("TemporalRelationship", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class Agent(NamedThing):
    """
    Represents an Agent
    """
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["Agent"] = Field("Agent", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""")
    ontology_types: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""")


class Person(Agent):
    """
    Represents a Person
    """
    primary_email: Optional[str] = Field(None, description="""The main email address of a person""")
    birth_date: Optional[date] = Field(None, description="""Date on which a person is born""")
    age_in_years: Optional[int] = Field(None, description="""Number of years since birth""")
    vital_status: Optional[PersonStatus] = Field(None, description="""living or dead status""")
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["Person"] = Field("Person", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""")
    ontology_types: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""")

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


class Organization(Agent):
    """
    Represents an Organization
    """
    provides_services: Optional[List[Service]] = Field(default_factory=list)
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["Organization"] = Field("Organization", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""")
    ontology_types: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""")


class AutomatedAgent(Agent):
    """
    Represents an Automated Agent
    """
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["AutomatedAgent"] = Field("AutomatedAgent", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""")
    ontology_types: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""")


class LifeEvent(Event):
    starts_at: Optional[TimePoint] = Field(None)
    ends_at: Optional[TimePoint] = Field(None)
    happens_at: Optional[TimePoint] = Field(None)
    has_interval: Optional[TemporalInterval] = Field(None)
    has_duration: Optional[Duration] = Field(None)
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["LifeEvent"] = Field("LifeEvent", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""")
    ontology_types: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""")


class CreativeWork(NamedThing):
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
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["CreativeWork"] = Field("CreativeWork", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""")
    ontology_types: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""")


class Service(Intangible):
    """
    A service provided by an organization
    """
    type: Literal["Service"] = Field("Service", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class QuantityKind(Concept):
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["QuantityKind"] = Field("QuantityKind", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""")
    ontology_types: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""")


class Quantity(Intangible):
    has_quantity_kind: Optional[str] = Field(None, description="""The kind of quantity""")
    type: Literal["Quantity"] = Field("Quantity", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class Duration(Quantity):
    """
    A length of time
    """
    has_quantity_kind: Optional[str] = Field(None, description="""The kind of quantity""")
    type: Literal["Duration"] = Field("Duration", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


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
    numerator: Optional[Union[Quantity,Duration,SimpleQuantity,Ratio,FoodIngredient]] = Field(None, description="""The numerator of the ratio""")
    denominator: Optional[Union[Quantity,Duration,SimpleQuantity,Ratio,FoodIngredient]] = Field(None, description="""The denominator of the ratio""")
    has_quantity_kind: Optional[str] = Field(None, description="""The kind of quantity""")
    type: Literal["Ratio"] = Field("Ratio", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class QuantityRange(Intangible):
    """
    A quantity range is a property that can be measured or counted
    """
    lower_bound: Optional[Union[Quantity,Duration,SimpleQuantity,Ratio,FoodIngredient]] = Field(None, description="""The lower bound of the range""")
    upper_bound: Optional[Union[Quantity,Duration,SimpleQuantity,Ratio,FoodIngredient]] = Field(None, description="""The upper bound of the range""")
    type: Literal["QuantityRange"] = Field("QuantityRange", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class UnitConversionOperation(MathematicalOperation):
    """
    A unit conversion operation
    """
    inputs: Optional[List[Union[Quantity,Duration,SimpleQuantity,Ratio,FoodIngredient]]] = Field(default_factory=list, description="""The input unit""")
    outputs: Optional[List[Union[Quantity,Duration,SimpleQuantity,Ratio,FoodIngredient]]] = Field(default_factory=list, description="""The output unit""")
    parts: Optional[List[MathematicalOperation]] = Field(default_factory=list, description="""The parts of the process""")
    immediate_preceding_steps: Optional[List[MathematicalOperation]] = Field(default_factory=list, description="""The steps that immediately precede this step""")


class UnitConcept(Concept):
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["UnitConcept"] = Field("UnitConcept", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""")
    ontology_types: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""")


class Measurement(Observation):
    quantity_measured: Optional[Union[Quantity,Duration,SimpleQuantity,Ratio,FoodIngredient]] = Field(None, description="""The quantity being measured""")
    variable_measured: Optional[Variable] = Field(None, description="""The variable being measured""")
    type: Literal["Measurement"] = Field("Measurement", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class Variable(Entity):
    allowed_units: Optional[List[str]] = Field(default_factory=list, description="""The units that are allowed for this variable""")
    type: Literal["Variable"] = Field("Variable", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class PlannedProcess(Event):
    """
    A process that follows a defined procedure or plan
    """
    follows_procedure: Optional[str] = Field(None)
    uses_physical_device: Optional[str] = Field(None)
    starts_at: Optional[TimePoint] = Field(None)
    ends_at: Optional[TimePoint] = Field(None)
    happens_at: Optional[TimePoint] = Field(None)
    has_interval: Optional[TemporalInterval] = Field(None)
    has_duration: Optional[Duration] = Field(None)
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["PlannedProcess"] = Field("PlannedProcess", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""")
    ontology_types: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""")


class MaterialCollection(PlannedProcess):
    follows_procedure: Optional[str] = Field(None)
    uses_physical_device: Optional[str] = Field(None)
    starts_at: Optional[TimePoint] = Field(None)
    ends_at: Optional[TimePoint] = Field(None)
    happens_at: Optional[TimePoint] = Field(None)
    has_interval: Optional[TemporalInterval] = Field(None)
    has_duration: Optional[Duration] = Field(None)
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["MaterialCollection"] = Field("MaterialCollection", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""")
    ontology_types: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""")


class MaterialProcessing(PlannedProcess):
    follows_procedure: Optional[str] = Field(None)
    uses_physical_device: Optional[str] = Field(None)
    starts_at: Optional[TimePoint] = Field(None)
    ends_at: Optional[TimePoint] = Field(None)
    happens_at: Optional[TimePoint] = Field(None)
    has_interval: Optional[TemporalInterval] = Field(None)
    has_duration: Optional[Duration] = Field(None)
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["MaterialProcessing"] = Field("MaterialProcessing", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""")
    ontology_types: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""")


class FoodRecipe(Procedure):
    ingredients: Optional[List[FoodIngredient]] = Field(default_factory=list)
    steps: Optional[List[str]] = Field(default_factory=list)
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["FoodRecipe"] = Field("FoodRecipe", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""")
    ontology_types: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""")


class FoodIngredient(Quantity):
    has_quantity_kind: Optional[str] = Field(None, description="""The kind of quantity""")
    type: Literal["FoodIngredient"] = Field("FoodIngredient", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class FoodProcessing(MaterialProcessing):
    follows_procedure: Optional[str] = Field(None)
    uses_physical_device: Optional[str] = Field(None)
    starts_at: Optional[TimePoint] = Field(None)
    ends_at: Optional[TimePoint] = Field(None)
    happens_at: Optional[TimePoint] = Field(None)
    has_interval: Optional[TemporalInterval] = Field(None)
    has_duration: Optional[Duration] = Field(None)
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["FoodProcessing"] = Field("FoodProcessing", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""")
    ontology_types: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""")


class FoodTypeConcept(Concept):
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["FoodTypeConcept"] = Field("FoodTypeConcept", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""")
    ontology_types: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""")


class BasicFoodType(FoodTypeConcept):
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["BasicFoodType"] = Field("BasicFoodType", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""")
    ontology_types: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""")


class CompositeFoodType(FoodTypeConcept):
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["CompositeFoodType"] = Field("CompositeFoodType", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""")
    ontology_types: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""")


# Update forward refs
# see https://pydantic-docs.helpmanual.io/usage/postponed_annotations/
Entity.update_forward_refs()
NamedThing.update_forward_refs()
Concept.update_forward_refs()
InformationEntity.update_forward_refs()
PhysicalDevice.update_forward_refs()
Intangible.update_forward_refs()
Role.update_forward_refs()
Relationship.update_forward_refs()
Location.update_forward_refs()
PointLocation.update_forward_refs()
Observation.update_forward_refs()
Specification.update_forward_refs()
Procedure.update_forward_refs()
MathematicalOperation.update_forward_refs()
Collection.update_forward_refs()
Event.update_forward_refs()
TimePointOrTemporalInterval.update_forward_refs()
TemporalInterval.update_forward_refs()
TimePoint.update_forward_refs()
TemporalRelationship.update_forward_refs()
Agent.update_forward_refs()
Person.update_forward_refs()
Organization.update_forward_refs()
AutomatedAgent.update_forward_refs()
LifeEvent.update_forward_refs()
CreativeWork.update_forward_refs()
Service.update_forward_refs()
QuantityKind.update_forward_refs()
Quantity.update_forward_refs()
Duration.update_forward_refs()
SimpleQuantity.update_forward_refs()
Ratio.update_forward_refs()
QuantityRange.update_forward_refs()
UnitConversionOperation.update_forward_refs()
UnitConcept.update_forward_refs()
Measurement.update_forward_refs()
Variable.update_forward_refs()
PlannedProcess.update_forward_refs()
MaterialCollection.update_forward_refs()
MaterialProcessing.update_forward_refs()
FoodRecipe.update_forward_refs()
FoodIngredient.update_forward_refs()
FoodProcessing.update_forward_refs()
FoodTypeConcept.update_forward_refs()
BasicFoodType.update_forward_refs()
CompositeFoodType.update_forward_refs()

