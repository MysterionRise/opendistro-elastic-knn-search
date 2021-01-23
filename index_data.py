from datetime import time
from pathlib import Path

import elasticsearch
import nltk.data
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("msmarco-distilroberta-base-v2")

sent_detector = nltk.data.load("tokenizers/punkt/english.pickle")

es = elasticsearch.Elasticsearch(
    "https://admin:admin@localhost:9200",
    verify_certs=False,
    ssl_show_warn=False,
)


def read_sentences(text: str, doc_name: str):
    text = text.replace("\n", "")
    text = text.replace("=", "")
    text = text.replace("'", "'")
    sentences = sent_detector.tokenize(text.strip())
    encoded_sents = [
        {
            "document_name": doc_name,
            "sentence_emb": model.encode(s),
            "sentence_text": s,
        }
        for s in sentences
    ]
    return encoded_sents


def read_data(data_path: str):
    file_paths = [p for p in Path(data_path).glob("**/*")]
    docs = []
    for path in file_paths:
        if path.suffix.lower() == ".txt":
            with open(path) as doc:
                text = doc.read()
                sentences = read_sentences(text, path.name)

            for sent in sentences:
                docs.append({"index": {}})
                docs.append(sent)
                if len(docs) >= 10000:
                    es.bulk(docs, index="got")
                    time.sleep(1)
                    docs = []
            print(len(sentences))
        else:
            raise Exception(
                f"Indexing of {path.suffix} files is not supported."
            )


if __name__ == "__main__":
    docs = read_data("data/article_txt_got")
