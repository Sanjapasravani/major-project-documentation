import json
import networkx as nx


class MedicalKnowledgeGraph:

    def __init__(self, data_path):
        self.graph = nx.Graph()
        self.documents = []

        self.load_data(data_path)

    def load_data(self, data_path):

        with open(data_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        self.documents = data["documents"]

        for doc in self.documents:

            entities = doc["entities"]

            for entity in entities:
                self.graph.add_node(
                    entity,
                    document_id=doc["id"]
                )

            for i in range(len(entities)):
                for j in range(i + 1, len(entities)):

                    self.graph.add_edge(
                        entities[i],
                        entities[j],
                        relation="co_occurs_in_document",
                        document_id=doc["id"]
                    )

    def get_related_entities(self, entity):

        if entity not in self.graph:
            return []

        return list(self.graph.neighbors(entity))

    def get_graph_statistics(self):

        return {
            "nodes": self.graph.number_of_nodes(),
            "edges": self.graph.number_of_edges()
        }