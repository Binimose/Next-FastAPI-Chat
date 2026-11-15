# Embedding cache
from functools import lru_cache
@lru_cache(maxsize=1000)
def get_cached_embedding(text: str): return [0.1] * 1536
