import os
import weaviate
import requests
import json
from dotenv import load_dotenv

load_dotenv()
weaviate_api = os.getenv('WEAVIATE_API')
huggingface_api = os.getenv('HUGGINGFACE_API')


client = weaviate.Client(
    url = "https://corprep-vdb-bk49tyjx.weaviate.network",  
    auth_client_secret=weaviate.AuthApiKey(api_key=weaviate_api),
    additional_headers = {
        "X-HuggingFace-Api-Key": huggingface_api
    }
)

class_obj = {
  "class": "Newscatcher",
  "vectorizer": "text2vec-huggingface",
  "moduleConfig": {
    "text2vec-huggingface": {
      "model": "sentence-transformers/all-MiniLM-L6-v2", 
      "options": {
        "waitForModel": true
      }
    }
  }
}

client.schema.create_class(class_obj)











# url = 'https://raw.githubusercontent.com/weaviate-tutorials/quickstart/main/data/jeopardy_tiny.json'
# resp = requests.get(url)
# data = json.loads(resp.text)

# # Configure a batch process
# with client.batch(
#     batch_size=100
# ) as batch:
#     # Batch import all Questions
#     for i, d in enumerate(data):
#         print(f"importing question: {i+1}")

#         properties = {
#             "answer": d["Answer"],
#             "question": d["Question"],
#             "category": d["Category"],
#         }

#         client.batch.add_data_object(
#             properties,
#             "Question",
#         )