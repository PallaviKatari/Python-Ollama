# 🤖 AI Agents Learning Project (Level 1 → Level 4)

This project demonstrates the step-by-step evolution of building AI agents using Python and local LLMs (Ollama).

---

# 📌 Overview

You will learn how to build:

| Level   | Description                         |
| ------- | ----------------------------------- |
| Level 1 | Basic Agent (Manual Tool Usage)     |
| Level 2 | AI decides which tool to use        |
| Level 3 | Memory + Tool-based Agent           |
| Level 4 | RAG Agent (Chat with your own data) |

---

# 🧰 Tech Stack

* Python 3.9+
* Ollama (Local LLM)
* ChromaDB (Vector Database)
* Sentence Transformers (Embeddings)

---

# 📦 Installation

## 1. Install Python packages

```bash
pip install ollama chromadb sentence-transformers
```

---

## 2. Install Ollama

Download and install from:
https://ollama.com

Run a model:

```bash
ollama run llama3
```

---

# 🧠 Level 1: Basic Agent

## 🔹 Features

* Uses simple `if/else`
* Calls tools manually
* No AI decision-making

## 🔹 Tools

* Calculator
* Weather (mock)

## 🔹 Key Concept

> Rule-based automation

---

# 🧠 Level 2: AI Tool Selection Agent

## 🔹 Features

* AI decides which tool to use
* No hardcoded logic
* Uses JSON output

## 🔹 Key Concept

> LLM as a decision-maker

## 🔹 Example Flow

1. User input → LLM
2. LLM returns JSON:

```json
{
  "tool": "calculate",
  "input": "10+5"
}
```

3. Tool executed dynamically

---

# 🧠 Level 3: Memory Agent

## 🔹 Features

* Maintains conversation history
* Context-aware responses
* Still uses tools

## 🔹 Key Improvements

* Stores last N messages
* Handles follow-up questions

## 🔹 Example

```
User: What is 10+5  
Agent: 15  
User: add 20  
Agent: 35
```

## 🔹 Key Concept

> Stateful AI (context awareness)

---

# 🧠 Level 4: RAG Agent (Retrieval-Augmented Generation)

## 🔹 Features

* Reads your documents
* Stores embeddings in vector DB
* Retrieves relevant context
* Answers based on your data

---

## 🔹 Architecture

```
User Query
    ↓
Embedding Model
    ↓
Vector Database (ChromaDB)
    ↓
Relevant Documents
    ↓
LLM (Ollama)
    ↓
Final Answer
```

---

## 🔹 Key Components

### 1. Embeddings

Convert text into vectors:

```python
embedding_model.encode(text)
```

---

### 2. Vector Database

Store and retrieve:

```python
collection.add(...)
collection.query(...)
```

---

### 3. Retrieval

Find relevant chunks:

```python
retrieve(query)
```

---

### 4. LLM Response

Use context:

```python
context + question → answer
```

---

# 📁 Project Structure

```
project/
│
├── agent_level1.py
├── agent_level2.py
├── agent_level3.py
├── rag_agent.py
│
├── data/
│   └── sample.txt
│
└── README.md
```

---

# 🧪 Example Queries

## Level 1–3

```
10+5
weather in Chennai
Tell me a joke
```

## Level 4 (RAG)

```
What is Python?
What is RAG?
What does Ollama do?
```

---

# ⚠️ Common Issues

## ❌ Ollama Error

```
Make sure Ollama is running:
ollama run llama3
```

---

## ❌ JSON Parsing Error

* LLM may not follow format strictly
* Use regex extraction

---

## ❌ Type Errors

* Always convert to string:

```python
str(value)
```

---

# 🚀 Future Improvements

## 🔥 Combine Everything

* Agent + Memory + RAG + Tools

## 🔥 Add PDF Support

* Read PDFs instead of text files

## 🔥 Build UI

* Streamlit / React frontend

## 🔥 Multi-Agent Systems

* Multiple agents collaborating

---

# 🎯 Learning Outcome

By completing this project, you now understand:

* ✅ How AI agents work
* ✅ Tool usage with LLMs
* ✅ Memory in AI systems
* ✅ Retrieval-Augmented Generation (RAG)
* ✅ Local LLM usage (no API cost)

---

# 🏁 Conclusion

You have built a **complete AI agent system from scratch**:

* Level 1 → Rules
* Level 2 → AI Decisions
* Level 3 → Memory
* Level 4 → Knowledge Retrieval


