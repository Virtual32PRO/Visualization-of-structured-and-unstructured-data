from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient, models

from io import BytesIO
from pypdf import PdfReader
import uuid
import re
from typing import Iterable

CTRL = re.compile(r"[\x00-\x1f]+")

EMB = SentenceTransformer(
    "Snowflake/snowflake-arctic-embed-l",
    trust_remote_code=True,
)

client = QdrantClient(host="localhost", port=6333)
COLLECTION = "docs"


def _to_string(x: Iterable | bytes | str) -> str:
    if isinstance(x, bytes):
        try:
            x = x.decode("utf‑8")
        except UnicodeDecodeError:
            x = x.decode("latin1", errors="ignore")
    elif isinstance(x, (list, tuple)):
        x = " ".join(map(str, x))
    else:
        x = str(x)
    return CTRL.sub(" ", x).strip()



def _read_pdf(file: BytesIO) -> list[str]:
    pages_clean: list[str] = []
    reader = PdfReader(file)
    for idx, page in enumerate(reader.pages, 1):
        raw = page.extract_text()
        if not raw:                     
            continue
        txt = _to_string(raw)
        if txt:
            pages_clean.append(txt)
    return pages_clean




def add_pdf(file: BytesIO, filename: str) -> None:
    pages = _read_pdf(file)
    if not pages:
        return
    vecs = EMB.encode(pages, batch_size=8, normalize_embeddings=True).tolist()

    points = [
        models.PointStruct(
            id=str(uuid.uuid4()),               
            vector=v,
            payload={
                "text": pg,
                "source": filename,
                "page": i + 1,
            },
        )
        for i, (pg, v) in enumerate(zip(pages, vecs))
    ]
    client.upsert(collection_name=COLLECTION, points=points)





def init_collection() -> None:
    if COLLECTION not in [c.name for c in client.get_collections().collections]:
        client.recreate_collection(
            collection_name=COLLECTION,                          
            vectors_config=models.VectorParams(
                size=EMB.get_sentence_embedding_dimension(),
                distance=models.Distance.COSINE,
            ),
        )


def add_docs(texts: list[str]) -> None:
    vecs     = EMB.encode(texts, normalize_embeddings=True).tolist()
    payloads = [{"text": t} for t in texts]


    points = [
        models.PointStruct(id=i, vector=v, payload=p)
        for i, (v, p) in enumerate(zip(vecs, payloads))
    ]

    client.upsert(
        collection_name=COLLECTION,
        points=points,
    )


def retrieve(query: str, top_k: int = 4):
    vec = EMB.encode(query, normalize_embeddings=True).tolist()
    hits = client.search(
        collection_name=COLLECTION,                       
        query_vector=vec,
        limit=top_k,
    )
    return [h.payload["text"] for h in hits], hits
