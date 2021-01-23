import elasticsearch
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("msmarco-distilroberta-base-v2")

es = elasticsearch.Elasticsearch(
    "https://admin:admin@localhost:9200",
    verify_certs=False,
    ssl_show_warn=False,
)

if __name__ == "__main__":
    search_query = "leader in the war of 5 kings"
    query_emb = model.encode(search_query).tolist()
    res = es.search(
        body={
            "size": 5,
            "query": {"knn": {"sentence_emb": {"vector": query_emb, "k": 5}}},
            "_source": ["sentence_text", "document_name"],
        },
        index="got",
    )
    print(res)
