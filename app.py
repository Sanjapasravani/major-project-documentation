import json

from src.knowledge_graph import MedicalKnowledgeGraph
from src.rag_engine import MediGraphRAG


def main():

    print("=" * 50)
    print("       MEDIGRAPH AI")
    print(" GraphRAG Medical Decision Support")
    print("=" * 50)

    kg = MedicalKnowledgeGraph(
        "data/medical_knowledge.json"
    )

    engine = MediGraphRAG(kg)

    print("\nKnowledge Graph Statistics:")

    print(kg.get_graph_statistics())

    while True:

        query = input(
            "\nEnter medical research query "
            "(or type exit): "
        )

        if query.lower() == "exit":
            break

        response = engine.generate_response(query)

        print("\n--- MediGraph AI Response ---")

        print(json.dumps(
            response,
            indent=4
        ))


if __name__ == "__main__":
    main()