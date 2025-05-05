from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import ollama

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up templates
templates = Jinja2Templates(directory="templates")

# Sample Q&A data
qna_data = [
    {"question": "What is Python?", "answer": "Python is a high-level, interpreted programming language known for its readability and versatility."},
    {"question": "What is FastAPI?", "answer": "FastAPI is a modern, high-performance web framework for building APIs with Python."},
    {"question": "What is an LLM?", "answer": "An LLM (Large Language Model) is an AI model trained on vast text data to understand and generate human-like text."},
]

@app.get("/", response_class=HTMLResponse)
async def get_qna(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "qna_data": qna_data})

@app.post("/submit")
async def submit_question(question: str = Form(...)):
    # Combine Q&As into a context string
    context = "\n".join([f"Q: {qa['question']}\nA: {qa['answer']}" for qa in qna_data])
    
    # Create prompt for LLM
    prompt = f"""You are a helpful assistant. Below is a list of Q&As:\n\n{context}\n\nUser question: {question}\n\nIf the user's question matches or is similar to a question in the Q&As, return the corresponding answer. If not, generate a concise, accurate answer based on your knowledge. Answer in plain text."""
    
    # Query the LLM
    response = ollama.chat(
        model="phi3",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return {"answer": response["message"]["content"]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)