import asyncio
import multiprocessing
import os

from azure.identity.aio import DefaultAzureCredential

async def create_index_maybe():
    """Create the index and upload documents if the index does not exist."""
    from api.rag_helper import RAGHelper
    async with DefaultAzureCredential() as creds:
        endpoint = os.environ.get('AZURE_AI_SEARCH_ENDPOINT')
        if endpoint:
            rag = RAGHelper(
                endpoint=endpoint,
                credential=creds,
                index_name=os.getenv('AZURE_AI_SEARCH_INDEX_NAME'),
                dimensions=None,
                model=os.getenv('AZURE_AI_EMBED_DEPLOYMENT_NAME'),
                embeddings_client=None
            )
            # If another application instance already have created the index,
            # do not upload the documents.
            if await rag.create_index_or_false(
              vector_index_dimensions=int(
                  os.getenv('AZURE_AI_EMBED_DIMENSIONS'))):
                embeddings_path = os.path.join(os.path.dirname(__file__), 'api', 'data', 'embeddings.csv')
                assert embeddings_path, f'File {embeddings_path} not found.'
                await rag.upload_documents(embeddings_path)


def on_starting(server):
    """This code runs once before the workers will start."""
    asyncio.get_event_loop().run_until_complete(create_index_maybe())


max_requests = 1000
max_requests_jitter = 50
log_file = "-"
bind = "0.0.0.0:50505"

if not os.getenv("RUNNING_IN_PRODUCTION"):
    reload = True

preload_app = True
num_cpus = multiprocessing.cpu_count()
workers = (num_cpus * 2) + 1
worker_class = "uvicorn.workers.UvicornWorker"

timeout = 120
