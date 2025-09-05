from langchain_huggingface import HuggingFaceEmbeddings
import warnings

def load_embeddings():
    """Load HuggingFace embeddings with error handling"""
    try:
        # Suppress tokenizer warnings
        warnings.filterwarnings("ignore", category=FutureWarning)
        
        return HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={"device": "cpu"},  # Force CPU to avoid GPU issues
            encode_kwargs={"normalize_embeddings": True}  # Normalize for better similarity
        )
    except Exception as e:
        print(f"Error loading embeddings: {e}")
        raise