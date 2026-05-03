from flask import Flask, render_template, request, jsonify
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import os

app = Flask(__name__)

print("Loading Superior AI Brain (FAISS Search Only)...")

# 1. Load the Vector Database (No API Keys, No Groq for Lab 12)
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vector_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

# 2. Setup the Retriever (Fetches top 3 chunks)
retriever = vector_db.as_retriever(search_kwargs={"k": 3})

print("Semantic Search Engine Ready!")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"answer": "Please ask a question.", "sources": []})
    
    try:
        # 3. Perform Similarity Search directly on FAISS (No LLM generation)
        docs = retriever.invoke(user_input)
        
        # 4. Format the raw database chunks to show Lab 12 proof
        raw_answer = "Here are the top semantic matches from the FAISS Database:\n\n"
        for i, doc in enumerate(docs):
            raw_answer += f"**Match {i+1}:** {doc.page_content}\n\n"
            
        # Extract unique sources
        sources = list(set([doc.metadata.get('source', 'Official Superior Document') for doc in docs]))
        
        return jsonify({
            "answer": raw_answer,
            "sources": sources
        })
    except Exception as e:
        print(f"Server Error: {e}") 
        return jsonify({
            "answer": f"Database Error: {str(e)}", 
            "sources": []
        })

if __name__ == "__main__":
    app.run(debug=True, port=5000)