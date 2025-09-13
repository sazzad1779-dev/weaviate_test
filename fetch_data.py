

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

    collections = [
        "MySimpleCollection",
        "MySimpleCollection2",
        "Product_data",
        "MySimpleCollection1"
    ]

    for col_name in collections:
        collection = client.collections.use(col_name)
        response = collection.query.fetch_objects()
        for obj in response.objects:
            print(f"Collection: {col_name}")
            print(obj.properties)  # Prints the properties of each object
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    client.close()