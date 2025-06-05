# Python Embedding Service – RepoSense.AI

This Python microservice provides text/code embeddings using a transformer model served via a minimal FastAPI application. It is used by the Node.js backend for semantic embedding and search functionality.

---

## ✅ Setup Instructions

### 1. Install Python (version 3.8 or above)

Download Python from the official site:  
[https://www.python.org/downloads](https://www.python.org/downloads)

During installation, make sure to:

- ✅ Check **"Add Python to PATH"**
- ✅ Ensure **pip** is installed

Verify installation:

```bash
python --version
pip --version
```
After cloning the repository - 

1. Create and Activate a Virtual Environment

# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

2. Install Dependencies

pip install -r requirements.txt

3. Run the Python Server

uvicorn app.main:app --host 0.0.0.0 --port 5005
