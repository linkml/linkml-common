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


class ModelingAbstraction(ConfiguredBaseModel):
    pass


class GraphElementMixin(ModelingAbstraction):
    pass


class GraphMixin(GraphElementMixin):
    pass


class GraphNodeMixin(GraphElementMixin):
    pass


class GraphEdgeMixin(GraphElementMixin):
    pass


class TreeElementMixin(ModelingAbstraction):
    pass


class TreeMixin(TreeElementMixin):
    pass


class SubTreeMixin(TreeMixin):
    pass


class TreeNodeMixin(TreeElementMixin):
    pass


class DiscreteEntity(ModelingAbstraction):
    pass


class Composite(TreeMixin, ModelingAbstraction):
    """
    A thing that can be composed of other things
    """
    components: Optional[List[Union[AtomicDiscreteEntity, Composite]]] = Field(default_factory=list)


class SimpleComposite(Composite, SubTreeMixin):
    """
    A thing that can be composed of only AtomicDiscreteEntities
    """
    components: Optional[List[AtomicDiscreteEntity]] = Field(default_factory=list)


class AtomicDiscreteEntity(DiscreteEntity, TreeNodeMixin):
    """
    A thing that cannot be decomposed into smaller parts, within a given system of components
    """
    pass


class System(Composite, GraphMixin):
    """
    A system is a composite entity that has connected components
    """
    connections: Optional[List[SystemConnection]] = Field(default_factory=list)
    components: Optional[List[Union[AtomicSystemComponent, SubSystem]]] = Field(default_factory=list)


class SubSystem(System):
    """
    A system that is part of a larger system
    """
    connections: Optional[List[SystemConnection]] = Field(default_factory=list)
    components: Optional[List[Union[AtomicSystemComponent, SubSystem]]] = Field(default_factory=list)


class AtomicSystemComponent(AtomicDiscreteEntity):
    """
    A system component that cannot be decomposed into smaller parts
    """
    pass


class Relationship(GraphEdgeMixin, ModelingAbstraction):
    """
    A relationship between two or more entities
    """
    pass


class BinaryRelationship(Relationship):
    pass


class MultiNAryRelationship(Relationship):
    pass


class BinaryDirectedRelationship(BinaryRelationship):
    subject: Optional[DiscreteEntity] = Field(None, description="""The subject of a relationship""")
    object: Optional[DiscreteEntity] = Field(None, description="""The object of a relationship""")


class SystemConnection(BinaryDirectedRelationship):
    """
    A connection between two system components
    """
    subject: Optional[Union[AtomicSystemComponent, SubSystem]] = Field(None, description="""The subject of a relationship""")
    object: Optional[Union[AtomicSystemComponent, SubSystem]] = Field(None, description="""The object of a relationship""")


class StateTransitionNetworkElement(ModelingAbstraction):
    """
    An element in a state transition network
    """
    pass


class StateTransitionNetwork(StateTransitionNetworkElement, GraphMixin):
    """
    A network of state transitions
    """
    pass


class StateTransition(StateTransitionNetworkElement):
    before: Optional[State] = Field(None, description="""The previous state""")
    after: Optional[State] = Field(None, description="""The next state""")
    conditions: Optional[Any] = Field(None, description="""Conditions under which the transition occurs""")


class State(StateTransitionNetworkElement):
    """
    A state in a state transition network
    """
    pass


# Update forward refs
# see https://pydantic-docs.helpmanual.io/usage/postponed_annotations/
ModelingAbstraction.update_forward_refs()
GraphElementMixin.update_forward_refs()
GraphMixin.update_forward_refs()
GraphNodeMixin.update_forward_refs()
GraphEdgeMixin.update_forward_refs()
TreeElementMixin.update_forward_refs()
TreeMixin.update_forward_refs()
SubTreeMixin.update_forward_refs()
TreeNodeMixin.update_forward_refs()
DiscreteEntity.update_forward_refs()
Composite.update_forward_refs()
SimpleComposite.update_forward_refs()
AtomicDiscreteEntity.update_forward_refs()
System.update_forward_refs()
SubSystem.update_forward_refs()
AtomicSystemComponent.update_forward_refs()
Relationship.update_forward_refs()
BinaryRelationship.update_forward_refs()
MultiNAryRelationship.update_forward_refs()
BinaryDirectedRelationship.update_forward_refs()
SystemConnection.update_forward_refs()
StateTransitionNetworkElement.update_forward_refs()
StateTransitionNetwork.update_forward_refs()
StateTransition.update_forward_refs()
State.update_forward_refs()

