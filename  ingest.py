import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from embeddings import load_embeddings

def ingest_documents():
    """Load PDFs, split into chunks, and create FAISS vectorstore"""
    
    # Check if data directory exists
    data_dir = "data"
    if not os.path.exists(data_dir):
        raise FileNotFoundError(f"Data directory '{data_dir}' not found!")
    
    # Load documents
    documents = []
    pdf_files = [f for f in os.listdir(data_dir) if f.endswith('.pdf')]
    
    if not pdf_files:
        raise FileNotFoundError("No PDF files found in the data directory!")
    
    print(f"Found {len(pdf_files)} PDF files to process...")
    
    for pdf_file in pdf_files:
        pdf_path = os.path.join(data_dir, pdf_file)
        print(f"Loading: {pdf_file}")
        
        loader = PyPDFLoader(pdf_path)
        docs = loader.load()
        documents.extend(docs)
        print(f"  - Loaded {len(docs)} pages")
    
    print(f"\nTotal documents loaded: {len(documents)}")
    
    # Split documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separators=["\n\n", "\n", " ", ""]
    )
    
    splits = text_splitter.split_documents(documents)
    print(f"Split into {len(splits)} chunks")
    
    # Load embeddings
    print("Loading embeddings model...")
    embeddings = load_embeddings()
    
    # Create FAISS vectorstore
    print("Creating FAISS vectorstore...")
    vectorstore = FAISS.from_documents(splits, embeddings)
    
    # Save the vectorstore
    vectorstore_path = "vectorstore"
    vectorstore.save_local(vectorstore_path)
    print(f" Vectorstore saved to '{vectorstore_path}'")
    
    # Verify the files were created
    expected_files = ["index.faiss", "index.pkl"]
    for file in expected_files:
        file_path = os.path.join(vectorstore_path, file)
        if os.path.exists(file_path):
            print(f" {file} created successfully")
        else:
            print(f"Warning: {file} not found!")

if __name__ == "__main__":
    try:
        # Check if .env file exists
        if not os.path.exists('.env'):
            print(".env file not found!")
            print("Please create a .env file with your GOOGLE_API_KEY")
            print("Example: GOOGLE_API_KEY=your_api_key_here")
            exit(1)
            
        ingest_documents()
        print("\n Ingestion completed successfully!")
        print("You can now run: streamlit run app.py")
    except Exception as e:
        print(f" Error during ingestion: {e}")
        print("\nTroubleshooting steps:")
        print("1. Make sure PDF files are in the 'data/' directory")
        print("2. Install required packages: pip install -r requirements.txt")
        print("3. Create .env file with GOOGLE_API_KEY")