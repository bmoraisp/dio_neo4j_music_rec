import os
from typing import Optional

from dotenv import load_dotenv
from neo4j import GraphDatabase, Driver


load_dotenv()


NEO4J_URI: str = os.getenv("NEO4J_URI", "")
NEO4J_USERNAME: str = os.getenv("NEO4J_USERNAME", "")
NEO4J_PASSWORD: str = os.getenv("NEO4J_PASSWORD", "")
NEO4J_DATABASE: Optional[str] = os.getenv("NEO4J_DATABASE") or None


def get_driver() -> Driver:
    """Create and return a Neo4j driver using .env credentials."""
    if not all([NEO4J_URI, NEO4J_USERNAME, NEO4J_PASSWORD]):
        raise RuntimeError("Missing Neo4j credentials in environment variables.")
    return GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD))
