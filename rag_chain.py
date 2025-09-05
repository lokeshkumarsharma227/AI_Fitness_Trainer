from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_google_genai import GoogleGenerativeAI
from embeddings import load_embeddings
from dotenv import load_dotenv
import os

load_dotenv()

def build_rag_chain():
    """Build and return the RAG chain for fitness Q&A"""
    
    # Load embeddings
    embeddings = load_embeddings()
    
    # Load the FAISS vectorstore
    try:
        db = FAISS.load_local(
            "vectorstore", 
            embeddings, 
            allow_dangerous_deserialization=True
        )
        print(" Vectorstore loaded successfully")
    except Exception as e:
        raise Exception(f"Failed to load vectorstore: {e}. Make sure to run ingest.py first!")
    
    # Create retriever
    retriever = db.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3}  
    )
    
    # Create prompt template
    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""You are an expert personal fitness trainer and nutritionist specializing in muscle building and strength training.

Use the provided context to answer the question as accurately and helpfully as possible. 
If the context doesn't contain enough information to fully answer the question, say so and provide what information you can.

Context:
{context}

Question: {question}

Answer: Provide a clear, actionable response based on the context above. Include specific recommendations when possible."""
    )
    
    # Initialize the LLM with updated model
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY not found in environment variables. Please set it in your .env file.")
    
    # Try different model names in order of preference
    model_names = ["gemini-1.5-flash", "gemini-1.5-pro", "models/gemini-1.5-flash"]
    
    for model_name in model_names:
        try:
            llm = GoogleGenerativeAI(
                model=model_name,
                google_api_key=api_key,
                temperature=0.3,
                max_output_tokens=1024
            )
            print(f" Using model: {model_name}")
            break
        except Exception as e:
            print(f" Failed to load {model_name}: {e}")
            continue
    else:
        raise Exception("Could not initialize any Gemini model. Please check your API key and model availability.")
    
   
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        chain_type_kwargs={"prompt": prompt},
        return_source_documents=True,
        verbose=True
    )
    
    return qa_chain