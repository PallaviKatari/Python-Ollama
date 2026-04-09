import ollama
import chromadb
from sentence_transformers import SentenceTransformer

# -----------------------------
# STEP 1: LOAD EMBEDDING MODEL
# -----------------------------
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# -----------------------------
# STEP 2: CREATE VECTOR DB
# -----------------------------
chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="docs")

# -----------------------------
# STEP 3: LOAD DATA
# -----------------------------
def load_documents():
    with open("data/sample.txt", "r") as f:
        text = f.read()

    chunks = text.split("\n")

    for i, chunk in enumerate(chunks):
        if chunk.strip() == "":
            continue

        embedding = embedding_model.encode(chunk).tolist()

        collection.add(
            documents=[chunk],
            embeddings=[embedding],
            ids=[str(i)]
        )

# Load once
load_documents()

# -----------------------------
# STEP 4: RETRIEVAL FUNCTION
# -----------------------------
def retrieve(query):
    query_embedding = embedding_model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=2
    )

    return results["documents"][0]


# -----------------------------
# STEP 5: AGENT FUNCTION
# -----------------------------
def run_rag_agent(user_input):

    # Retrieve relevant context
    docs = retrieve(user_input)

    context = "\n".join(docs)

    prompt = f"""
Answer the question using ONLY the context below.

Context:
{context}

Question:
{user_input}
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]


# -----------------------------
# STEP 6: RUN LOOP
# -----------------------------
if __name__ == "__main__":
    print("🤖 RAG Agent (Chat with your data)\nType 'exit' to quit\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        result = run_rag_agent(user_input)
        print("Agent:", result)