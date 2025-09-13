import os
import weaviate
from dotenv import load_dotenv
from weaviate.auth import AuthApiKey
from weaviate.classes import config as wc

load_dotenv(override=True)

# -------------------------------------------------
# Environment
# -------------------------------------------------
HTTP_HOST = os.getenv("WEAVIATE_URL")          # e.g. 54.199.97.121
HTTP_PORT = 8080
GRPC_HOST = os.getenv("WEAVIATE_URL")
GRPC_PORT = 50051

print(f"Connecting to Weaviate at {HTTP_HOST}:{HTTP_PORT} (HTTP) "
      f"and {GRPC_HOST}:{GRPC_PORT} (gRPC)")

headers = {"X-OpenAI-Api-Key": os.getenv("OPENAI_API_KEY")}
client = None

try:
    # -------------------------------------------------
    # Connection
    # -------------------------------------------------
    client = weaviate.connect_to_custom(
        headers=headers,
        http_host=HTTP_HOST,
        http_port=HTTP_PORT,
        http_secure=False,
        grpc_host=GRPC_HOST,
        grpc_port=GRPC_PORT,
        grpc_secure=False,
        auth_credentials=AuthApiKey(api_key=os.getenv("WEAVIATE_API_KEY")),
        skip_init_checks=True,
    )

    coll_name = "MySimpleCollection1"

    # -------------------------------------------------
    # Create collection if it doesn't already exist
    # -------------------------------------------------
    
    print(f"Existing collections: {client.collections.list_all()}")
    existing = [c for c in client.collections.list_all()]
    if coll_name not in existing:
        print(f"Creating collection {coll_name}")
        client.collections.create(
            name=coll_name,
            properties=[
                wc.Property(name="title", data_type=wc.DataType.TEXT),
                wc.Property(name="description", data_type=wc.DataType.TEXT),
                wc.Property(name="number_field", data_type=wc.DataType.NUMBER),
            ],
            vectorizer_config=wc.Configure.Vectorizer.text2vec_openai(),
        )
    else:
        print(f"Collection {coll_name} already exists, reusing it")

    my_collection = client.collections.get(coll_name)

    # -------------------------------------------------
    # Insert a couple of documents (auto-vectorized)
    # -------------------------------------------------
    description = (
        "This is a long description to test EFS storage growth. "
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "This is a long description to test EFS storage growth. "
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "This is a long description to test EFS storage growth. "
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "This is a long description to test EFS storage growth. "
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "This is a long description to test EFS storage growth. "
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "This is a long description to test EFS storage growth. "
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "This is a long description to test EFS storage growth. "
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "This is a long description to test EFS storage growth. "
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "This is a long description to test EFS storage growth. "
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "This is a long description to test EFS storage growth. "
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "This is a long description to test EFS storage growth. "
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "This is a long description to test EFS storage growth. "
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "This is a long description to test EFS storage growth. "
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "This is a long description to test EFS storage growth. "
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "This is a long description to test EFS storage growth. "
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "This is a long description to test EFS storage growth. "
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "This is a long description to test EFS storage growth. "
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "This is a long description to test EFS storage growth. "
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "This is a long description to test EFS storage growth. "
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "This is a long description to test EFS storage growth. "
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "This is a long description to test EFS storage growth. "
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "This is a long description to test EFS storage growth. "
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "This is a long description to test EFS storage growth. "
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "This is a long description to test EFS storage growth. "
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "This is a long description to test EFS storage growth. "
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "This is a long description to test EFS storage growth. "
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "This is a long description to test EFS storage growth. "
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "This is a long description to test EFS storage growth. "
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
        "The Weaviate vectorizer (OpenAI) will embed this automatically."
    )


    for i in range(30):  # Insert multiple times to increase storage usage
        my_collection.data.insert(
            properties={
                "title": "Introduction to Weaviate",
                "description": description,
                "number_field": i,
            }
        )
    

    print("Insertion complete. Check your EFS metrics for storage changes.")

finally:
    if client:
        client.close()
        print("Connection closed.")
