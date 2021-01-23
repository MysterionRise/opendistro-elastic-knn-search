curl -X PUT "localhost:9200/got?pretty" -H 'Content-Type: application/json' -d'
{
  "settings": {
    "index.knn": true
  },
  "mappings": {
    "properties": {
      "sentence_emb": {
        "type": "knn_vector",
        "dimension": 768
      },
      "sentence_text": {
        "type": "text",
        "fields": {
          "keyword": {
            "type": "keyword",
            "ignore_above": 256
          }
        }
      },
      "document_name": {
        "type": "text",
        "fields": {
          "keyword": {
            "type": "keyword",
            "ignore_above": 256
          }
        }
      }
    }
  }
}
'
