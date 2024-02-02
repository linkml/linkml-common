from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "password"))

nodes = [
    {"id": "P1", "label": "Person", "name": "Alice", "age": 30},
    {"id": "P2", "label": "Person", "name": "Bob", "age": 35},
    {"id": "P3", "label": "Person", "name": "Chloe", "age": 35},
    {"id": "Org1", "label": "Organization", "name": "Acme", "age": 35},
    {"id": "Org2", "label": "Organization", "name": "Skynet", "age": 35},
    # ... other nodes
]

edges = [
    {"start": "P1", "end": "P2", "type": "KNOWS", "since": 2020},
    {"start": "P1", "end": "P3", "type": "KNOWS", "since": 2020},
    {"start": "P1", "end": "Org1", "type": "EMPLOYED_BY", "since": 2020},
    {"start": "Org1", "end": "Org2", "type": "SUBSIDIARY_OF", "since": 2020},
    # ... other relationships
]

def add_node(tx, node_label, node_id, **properties):
    # Create a Cypher query for node creation with dynamic label
    props = ', '.join(f"{key}: ${key}" for key in properties.keys())
    query = f"MERGE (n:{node_label} {{id: $node_id, {props}}})"
    tx.run(query, node_id=node_id, **properties)

def add_edge(tx, start_id, end_id, rel_type, **properties):
    # Create a Cypher query for relationship creation
    props = ', '.join(f"{key}: ${key}" for key in properties.keys())
    query = (f"MATCH (a {{id: $start_id}}), (b {{id: $end_id}}) "
             f"MERGE (a)-[r:{rel_type} {{{props}}}]->(b)")
    tx.run(query, start_id=start_id, end_id=end_id, **properties)

def load_data(driver, nodes, edges):
    with driver.session() as session:
        # Add nodes
        for node in nodes:
            session.execute_write(add_node, node['label'], node['id'],
                                  **{k: v for k, v in node.items() if k not in ['id', 'label']})

        # Add edges
        for edge in edges:
            session.execute_write(add_edge, edge['start'], edge['end'], edge['type'],
                                  **{k: v for k, v in edge.items() if k not in ['start', 'end', 'type']})


# Load data into Neo4j
load_data(driver, nodes, edges)