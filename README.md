# 🧠 Smart Todo List with AI Integration

A full-stack intelligent task management app using **Django REST Framework**, **Next.js + Tailwind CSS**, and **LM Studio (Qwen)** for context-aware task suggestions.

> ⚡ Powered by Local LLMs using [LM Studio](https://lmstudio.ai)

---

## 📸 Screenshots


### 🔹 AI-Powered Task Creation
![Create Task Screenshot](./frontend/assets/createtask.png)

### 🔹 Task List Dashboard
![Task List Screenshot](./frontend/assets/tasklist.png)

### 🔹 Dark Mode Toggle
![Dark Mode Screenshot](./frontend/assets/darkmode.png)

---

## 🛠️ Tech Stack

| Layer         | Tech                             |
|---------------|----------------------------------|
| Frontend      | Next.js, Tailwind CSS            |
| Backend       | Django REST Framework (DRF)      |
| Database      | PostgreSQL (local or Supabase)   |
| AI Engine     | LM Studio (Qwen model)           |

---

## ⚙️ Setup Instructions

### 🔧 Backend (Django + PostgreSQL)

```bash
cd backend/
python -m venv env
source env/bin/activate  # Windows: .\env\Scripts\activate
pip install -r requirements.txt

# Update your Supabase/Postgres DB config in settings.py
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
