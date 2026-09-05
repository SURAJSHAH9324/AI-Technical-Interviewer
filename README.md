# 🎤 AI Technical Interviewer

An AI-powered technical interview practice system that simulates a real technical interview.

The project is being built step by step to learn:

- LLMs
- AI Agents
- Multi-Agent Systems
- State Management
- LangGraph
- Adaptive AI Workflows
- Voice AI
- Backend Development
- Databases
- Testing
- Docker
- Git/GitHub

---

## 🚧 Current Status

**Phase 1 — Environment & Local LLM Setup**

- [x] Python environment created
- [x] Virtual environment created
- [x] Virtual environment activated
- [x] pip upgraded
- [x] Python dependencies installed
- [x] `.gitignore` created
- [x] `.env` created
- [x] Ollama installed
- [x] Ollama version verified
- [x] Ollama server started
- [x] Ollama model list checked
- [x] System RAM checked
- [x] Local model selected
- [ ] Download Qwen3 8B
- [ ] Run Qwen3 8B
- [ ] Connect Python to Ollama

---

## 💻 Environment Setup

### 1. Check Python

Open PowerShell:

```powershell
python --version
```

Python 3.11+ is recommended.

Example:

```
Python 3.11.x
```

### 2. Check pip

```powershell
pip --version
```

If pip is available, continue.

### 3. Create the Project

Go to Desktop:

```powershell
cd Desktop
```

Create the project:

```powershell
mkdir AI-Interviewer
```

Enter the project:

```powershell
cd AI-Interviewer
```

### 4. Create Virtual Environment

Create a Python virtual environment:

```powershell
python -m venv venv
```

This creates:

```
AI-Interviewer/
└── venv/
```

The virtual environment keeps project dependencies isolated from other Python projects.

### 5. Activate Virtual Environment

On Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

After activation, the terminal should show:

```
(venv) PS C:\Users\<username>\Desktop\AI-Interviewer>
```

The `(venv)` confirms that the virtual environment is active.

### 6. Upgrade pip

Run:

```powershell
python -m pip install --upgrade pip
```

---

## 📦 Python Dependencies

At the beginning, we are installing only the packages currently required.

Install:

```powershell
pip install python-dotenv
```

Check installed packages:

```powershell
pip list
```

We are using Ollama for local LLM inference, so an OpenAI API key is not required for the current setup.

---

## 📄 requirements.txt

Create a file:

```
requirements.txt
```

Current contents:

```
python-dotenv
```

More dependencies will be added later when required.

---

## 📄 .gitignore

Create:

```
.gitignore
```

Add:

```
venv/
.venv/
.env
__pycache__/
*.pyc
.pytest_cache/
```

This prevents:

- Virtual environment files
- Environment variables/secrets
- Python cache files
- Test cache

from being committed to GitHub.

---

## 🔐 .env

Create:

```
.env
```

Currently, no API key is required because we are using Ollama locally.

Example for future environment variables:

```
OPENAI_API_KEY=your_api_key_here
```

Never commit `.env` to GitHub.

The `.env` file is already included in `.gitignore`.

---

## 🦙 Ollama Setup

### Why are we using Ollama?

Ollama allows us to run an LLM locally on our computer.

Instead of:

```
Python
   ↓
Internet
   ↓
Cloud LLM API
```

we can use:

```
Python
   ↓
Ollama
   ↓
Local LLM
```

Benefits:

- No API cost for local inference
- Good for learning
- Runs locally
- Helps us understand how applications communicate with LLMs
- Useful for learning local LLM deployment

### 1. Install Ollama

Download Ollama for Windows:

https://ollama.com/download/windows

Install Ollama normally.

After installation, open a new PowerShell or Command Prompt.

### 2. Verify Ollama Installation

Run:

```powershell
ollama --version
```

Current environment returned:

```
client version is 0.30.10
```

Initially, the following warning appeared:

```
Warning: could not connect to a running Ollama instance
Warning: client version is 0.30.10
```

This does not mean Ollama failed to install.

It means:

- Ollama client = installed
- Ollama server = not running

### 3. Start Ollama Server

Run:

```powershell
ollama serve
```

Keep this terminal open.

Ollama runs its local server on:

```
http://127.0.0.1:11434
```

### 4. Open Another Terminal

Do not close the terminal running:

```
ollama serve
```

Open another PowerShell window.

Go to the project:

```powershell
cd Desktop\AI-Interviewer
```

Activate the virtual environment:

```powershell
venv\Scripts\Activate.ps1
```

### 5. Check Installed Ollama Models

Run:

```powershell
ollama list
```

Initially, the output was:

```
NAME    ID    SIZE    MODIFIED
```

with no model underneath.

This means:

- Ollama installed ✅
- Ollama server running ✅
- LLM model installed ❌

This is expected because we have not downloaded a model yet.

---

## 💾 Check Computer RAM

Before downloading a local LLM, check the available RAM.

Run:

```powershell
systeminfo | findstr /C:"Total Physical Memory"
```

Current result:

```
Total Physical Memory: 15,902 MB
```

Approximately:

```
16 GB RAM
```

---

## 🧠 Selected Local Model

Based on the available system RAM, we selected:

**Qwen3 8B**

Ollama model name:

```
qwen3:8b
```

---

## ⬇️ Next Step: Download Qwen3 8B

Run:

```powershell
ollama pull qwen3:8b
```

Wait for the download to finish.

Then check:

```powershell
ollama list
```

The model should appear in the list.

Expected result will look similar to:

```
NAME        ID        SIZE        MODIFIED
qwen3:8b    ...       ...         ...
```

---

## 🧪 Run the Model

After the model has finished downloading:

```powershell
ollama run qwen3:8b
```

Then test it with a simple question:

```
What is Python?
```

If the model responds, the local LLM setup is working.

---

## 🧠 What We Are Learning

At this stage, the basic LLM flow is:

```
User Prompt
     ↓
Ollama
     ↓
Qwen3 8B
     ↓
Generated Response
```

Ollama is the local runtime.

Qwen3 8B is the LLM model.

---

## 🐍 Next Development Step

Once Qwen3 is running successfully, we will connect Python to Ollama.

The architecture will become:

```
Python Application
       ↓
Ollama
       ↓
Qwen3 8B
       ↓
Response
       ↓
Python Application
```

This will be our first real AI application step.

---

## 🎤 Basic AI Interviewer

After Python → Ollama is working, we will build a simple interviewer first.

The first version will NOT contain multiple agents.

Initial flow:

```
User
 ↓
Python
 ↓
LLM
 ↓
Interview Question
 ↓
User Answer
 ↓
LLM
 ↓
Evaluation
```

Once this works, we will introduce interview state.

---

## 🧠 Interview State

Eventually we will maintain information such as:

```python
state = {
    "role": "Python Developer",
    "difficulty": "medium",
    "question": "...",
    "answer": "...",
    "score": 8,
    "feedback": "...",
    "question_number": 3
}
```

Think of state as a shared notebook containing the current interview information.

---

## 🤖 Multi-Agent System

After the basic interviewer works, we will split responsibilities into specialized agents.

### Question Agent

Generates interview questions.

```
Role
Skills
Difficulty
Previous questions
        ↓
Question Agent
        ↓
Question
```

### Evaluator Agent

Evaluates the candidate's answer.

```
Question
+
Answer
   ↓
Evaluator Agent
   ↓
Score + Evaluation
```

### Feedback Agent

Provides useful feedback.

```
Evaluation
   ↓
Feedback Agent
   ↓
Strengths + Improvements
```

---

## 🔀 Orchestration

Eventually the interview workflow will become:

```
Question Agent
      ↓
Candidate Answer
      ↓
Evaluator Agent
      ↓
Feedback Agent
      ↓
Adaptive Router
      ↓
Next Question
```

This workflow will later be implemented using LangGraph.

---

## 🕸️ Why LangGraph Comes Later

We will not start with LangGraph immediately.

First we will:

```
Understand workflow manually
        ↓
Understand state
        ↓
Understand agents
        ↓
Build multi-agent flow
        ↓
Use LangGraph
```

This makes it easier to understand what LangGraph is actually solving.

---

## 📈 Adaptive Difficulty

The interviewer should eventually adapt to the candidate's performance.

Example:

```
Score < 5
    ↓
Easier question

Score 5–7
    ↓
Similar difficulty

Score >= 8
    ↓
Harder question
```

---

## 🖥️ Streamlit UI

*(To be added once the backend interview logic is working.)*
