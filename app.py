import os
import streamlit as st
from rag_chain import build_rag_chain
import fitz  # PyMuPDF for PDF handling

# Set page configuration with a custom background color and font
st.set_page_config(page_title="AI Fitness Trainer", layout="wide")
st.markdown(
    """
    <style>
    body {
        background-color: #e8f5e9; /* Light green background */
        font-family: 'Arial', sans-serif; /* Custom font */
    }
    .sidebar .sidebar-content {
        background-color: #ffffff; /* White sidebar background */
    }
    h1, h2, h3, h4, h5, h6 {
        color: #2e7d32; /* Dark green for headings */
    }
    .st-expander {
        background-color: #f1f8e9; /* Light green for expanders */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Ask Your Muscle Trainer Bot")

# Initialize session state for messages
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Initialize the RAG chain
@st.cache_resource
def get_qa_chain():
    return build_rag_chain()

# Function to display PDF files
def display_pdfs(data_folder):
    pdf_files = [f for f in os.listdir(data_folder) if f.endswith('.pdf')]
    if not pdf_files:
        st.write("No PDF files found in the data folder.")
        return None

    selected_pdf = st.selectbox("Select a PDF to view:", pdf_files)
    if selected_pdf:
        pdf_path = os.path.join(data_folder, selected_pdf)
        with fitz.open(pdf_path) as pdf:
            st.write(f"### {selected_pdf}")
            for page_num, page in enumerate(pdf, start=1):
                st.write(f"#### Page {page_num}")
                st.text(page.get_text("text"))

# Main app logic
try:
    qa_chain = get_qa_chain()

    # Layout: Central query bar, collapsible chat history and PDF viewer on the right
    col1, col2 = st.columns([2, 1])

    with col1:
        st.header("Ask Your Question")
        query = st.text_input("Ask a question about building muscle, fitness, or nutrition:", key="query_input")

        if query:
            with st.spinner("Thinking..."):
                try:
                    result = qa_chain.invoke(query)

                    # Handle different return types
                    if isinstance(result, dict):
                        answer = result.get('result', result.get('answer', str(result)))
                    else:
                        answer = str(result)

                    # Store the query and answer in session state
                    st.session_state.messages.append({"role": "user", "content": query})
                    st.session_state.messages.append({"role": "bot", "content": answer})

                    # Display the answer
                    st.success(f" Answer: {answer}")
                except Exception as e:
                    st.error(f"Error processing query: {str(e)}")

    with col2:
        st.header("Options")
        view_option = st.selectbox("What do you want to view?", ["Chat History", "PDF Viewer"])

        if view_option == "Chat History":
            with st.expander("Chat History", expanded=True):
                for message in st.session_state.messages:
                    role = " " if message['role'] == "bot" else " "
                    st.markdown(f"**{role}:** {message['content']}")

        elif view_option == "PDF Viewer":
            with st.expander("PDF Viewer", expanded=True):
                display_pdfs(data_folder="./data")

except Exception as e:
    st.error(f"Failed to initialize the AI trainer: {str(e)}")
    st.write("Please make sure:")
    st.write("1. Your GOOGLE_API_KEY is set in the .env file")
    st.write("2. The vectorstore has been created (run ingest.py first)")
    st.write("3. All required packages are installed")