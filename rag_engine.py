from src.retriever import MedicalRetriever


class MediGraphRAG:

    def __init__(self, knowledge_graph):

        self.kg = knowledge_graph

        self.retriever = MedicalRetriever(
            knowledge_graph
        )

    def generate_response(self, query):

        documents = self.retriever.retrieve(query)

        graph_context = self.retriever.graph_retrieval(
            query
        )

        if not documents:

            return {
                "status": "insufficient_evidence",
                "answer": (
                    "Insufficient evidence in the "
                    "available knowledge base."
                ),
                "sources": [],
                "graph_context": graph_context
            }

        evidence = []

        for doc in documents:

            evidence.append({
                "document_id": doc["id"],
                "title": doc["title"],
                "evidence": doc["text"],
                "source": doc["source"]
            })

        answer = (
            "Retrieved evidence is available. "
            "Review the supporting documents below. "
            "This prototype does not independently "
            "establish a medical diagnosis or treatment."
        )

        return {
            "status": "evidence_retrieved",
            "answer": answer,
            "sources": evidence,
            "graph_context": graph_context
        }