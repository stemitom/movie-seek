from flask import Flask, render_template, request
from elasticsearch import Elasticsearch, ElasticsearchException, RequestsHttpConnection
from elasticsearch import helpers
import logging

logger = logging.getLogger(__name__)
app = Flask(__name__)

# es = Elasticsearch(
#     hosts=[
#         {
#             "host": "host.docker.internal", 
#             "port": 9200
#         }
#     ], 
#     connection_class=RequestsHttpConnection, 
#     max_retries=30,
#     retry_on_timeout=True, 
#     request_timeout=30
# )

es = Elasticsearch(

)

@app.route("/index")
def index():
    documents = list()
    with open("data/moviedata.json") as f:
        for f in f.readlines: documents.append(f)
    data = helpers.bulk(
        es, documents, index="movies"
    )
    return data


