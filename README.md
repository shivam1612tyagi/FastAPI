# FastAPI – The Complete Course 🚀

A hands-on, project-based repository covering **FastAPI** from the fundamentals to advanced, production-ready concepts — RESTful API design, database integration with SQLAlchemy, authentication & authorization with JWT, and deployment strategies.

> 📚 Companion code for the *"FastAPI - The Complete Course (Beginner + Advanced)"* journey — built while learning to design, build, and deploy high-performance APIs with Python.

---

## 📌 About This Repository

This repo is organized into incremental **Projects**, each one building on the last — starting from a simple `GET /books` endpoint and progressing to a full-stack **Todo Application** with user authentication, role-based access, and a real database backend.

Whether you're learning FastAPI for the first time or revisiting core concepts, the code here is meant to be read top-to-bottom, project by project.

---

## 🗂️ Project Structure

```
FastAPI/
│
├── PythonRefresher/        # Python fundamentals refresher (OOP, classes, etc.)
├── Project_1/               # Intro to FastAPI - first endpoints
├── Project_2/                # Books API - CRUD, validation, status codes
├── Project 3/                  # Database integration with SQLAlchemy
├── Project 3.5/                 # TodoApp - authentication foundations
│    └── TodoApp/
│         └── routers/
│              └── auth.py     # JWT-based auth logic
├── Project 4/
│    └── TodoApp/               # Authorization & JWT tokens
├── Project 5/                   # Advanced features / deployment-ready app
├── TodoAPP/                      # Rough Todo application
├── 1_TodoAPP/                     # Rough Todo app iteration
│
├── FastAPI_Slides.pdf            # Course reference slides
├── command_history.txt           # Useful CLI commands used during the course
├── create_virtual_env.txt        # venv setup notes
├── create_virtual_env_using_uv.txt  # uv-based venv setup notes
├── main.py
├── pyproject.toml
├── requirements.txt
└── README.md
```

> 💡 Folder names may vary slightly across course updates — check the repo root for the latest structure.

---

## ✨ What You'll Find Here

- **FastAPI Fundamentals** – routing, path/query parameters, request bodies
- **Pydantic Models** – request & response validation with field-level rules
- **RESTful API Design** – proper use of HTTP methods & status codes
- **Database Integration** – SQLAlchemy ORM with SQLite/PostgreSQL
- **Authentication & Authorization** – JWT tokens, password hashing, role-based access
- **Full-Stack Todo App** – a complete app tying everything together
- **Testing** – unit tests for API endpoints
- **Deployment** – notes on shipping a FastAPI app to production

---

## 🛠️ Tech Stack

| Tool                            | Purpose                               |
| -------------------------------- | -------------------------------------- |
| **FastAPI**                      | Web framework for building APIs        |
| **Uvicorn**                       | ASGI server                            |
| **SQLAlchemy**                    | ORM for database interaction           |
| **Pydantic**                      | Data validation & settings management  |
| **JWT (python-jose / passlib)**   | Authentication & password hashing      |
| **SQLite / PostgreSQL**           | Database                               |
| **Pytest**                        | Testing framework                      |

---

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/shivam1612tyagi/FastAPI.git
cd FastAPI
```

### 2. Create & activate a virtual environment

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac / Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

> Prefer `uv`? See `create_virtual_env_using_uv.txt` for the faster, uv-based setup.

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Navigate into a project folder

```bash
cd "Project 5/TodoApp"
```

### 5. Run the application

```bash
uvicorn main:app --reload
```

### 6. Open the interactive API docs

```
http://127.0.0.1:8000/docs
```

---

## 📖 How to Use This Repo

1. Start with `PythonRefresher/` if you need a quick Python OOP refresher.
2. Move through `Project_1` → `Project 5` in order — each folder is self-contained and builds on concepts from the previous one.
3. Read the code alongside the endpoint docs at `/docs` (Swagger UI) to see requests/responses in action.
4. Experiment — break things, add new endpoints, and test them via Swagger UI or `pytest`.
5. Refer to `FastAPI_Slides.pdf` for conceptual explanations alongside the code.

---

## 🤝 Contributing

This is primarily a learning repository, but suggestions, fixes, and improvements are welcome:

1. Fork the repo
2. Create a new branch (`git checkout -b feature/improvement`)
3. Commit your changes
4. Open a Pull Request

---

## 📄 License

This project is intended for educational purposes. Please check the repository for specific license details.

---

## 🙌 Credits

**Repository maintained by:** [Shivam Tyagi](https://github.com/shivam1612tyagi)

---

⭐ If this repo helped you learn FastAPI, consider giving it a star!
