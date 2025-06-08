import os
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders.markdown import UnstructuredMarkdownLoader
from langchain_community.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings

DOCS_DIR = "manim_docs"
INDEX_DIR = "manim_index"

# 1. Load .md files
print("[*] Loading markdown files...")
loader = DirectoryLoader(
    DOCS_DIR,
    glob="**/*.md",
    loader_cls=UnstructuredMarkdownLoader
)
documents = loader.load()

# 2. Split into chunks
print(f"[*] Splitting {len(documents)} documents into chunks...")
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
docs = splitter.split_documents(documents)

# 3. Embedding model
print("[*] Creating embeddings...")
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# 4. Create FAISS index
print("[*] Building FAISS index...")
vectorstore = FAISS.from_documents(docs, embedding_model)

# 5. Save to disk
os.makedirs(INDEX_DIR, exist_ok=True)
vectorstore.save_local(INDEX_DIR)
print(f"[✓] Vector index saved to: {INDEX_DIR}")
