class MedicalRetriever:

    def __init__(self, knowledge_graph):
        self.kg = knowledge_graph

    def retrieve(self, query, top_k=3):

        query_words = set(query.lower().split())

        results = []

        for doc in self.kg.documents:

            text = (
                doc["title"] + " " + doc["text"] + " " +
                " ".join(doc["entities"])
            ).lower()

            score = sum(
                1 for word in query_words
                if word in text
            )

            if score > 0:
                results.append((score, doc))

        results.sort(
            key=lambda item: item[0],
            reverse=True
        )

        return [
            doc for score, doc in results[:top_k]
        ]

    def graph_retrieval(self, query):

        matched_entities = []

        for entity in self.kg.graph.nodes:

            if entity.lower() in query.lower():
                matched_entities.append(entity)

        related_entities = set()

        for entity in matched_entities:

            related_entities.update(
                self.kg.get_related_entities(entity)
            )

        return {
            "matched_entities": matched_entities,
            "related_entities": list(related_entities)
        }