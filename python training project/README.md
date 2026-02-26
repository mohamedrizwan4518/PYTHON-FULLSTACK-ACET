# 🐍 PyQuest AI – Gamified Python Learning Platform

PyQuest AI is a production-ready, full-stack learning platform designed to teach Python through a futuristic, gamified experience. It features an **AI Mentor** and **Real-time Code Evaluation** powered by **Ollama (Llama 3)**, along with a robust XP and leveling system.

![PyQuest AI Banner](https://raw.githubusercontent.com/your-username/pyquest-ai/main/static/img/banner.png) *(Note: Replace with your actual hosted image path)*

## 🚀 Key Features

- **AI-Powered Mentorship**: Real-time chat with a Llama 3 mentor that provides hints and explains concepts.
- **Intelligent Code Evaluation**: Automated scoring (1-10) and feedback for Python challenges based on logic, efficiency, and readability.
- **Gamification Engine**:
  - **XP & Leveling**: Gain experience points and level up (Dynamic Formula: `100 * (level ^ 1.5)`).
  - **Streaks**: Track daily consistency with bonus XP.
  - **Badges**: Unlock unique badges like *Syntax Survivor*, *Function Forger*, and *Architect*.
  - **Leaderboard**: Compete with other learners globally.
- **Futuristic UI**: A premium dark-themed interface with neon accents, dynamic gradients, and responsive glassmorphism components.
- **Local AI Resilience**: Runs entirely on **Ollama**, ensuring zero API costs and high availability.

## 🛠️ Tech Stack

- **Backend**: Python (Flask)
- **Database**: SQLAlchemy (SQLite for local, PostgreSQL ready)
- **AI Engine**: Ollama (Llama 3)
- **Frontend**: Vanilla HTML5, CSS3 (Modern Flex/Grid), JavaScript (AJAX)
- **Authentication**: Flask-Login

## 📦 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/pyquest-ai.git
cd pyquest-ai
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Setup Ollama (Llama 3)
Ensure you have [Ollama](https://ollama.com/) installed and running:
```bash
ollama serve
ollama pull llama3
```

### 4. Environment Variables
Create a `.env` file in the root directory:
```text
SECRET_KEY=your_secure_secret_key
DATABASE_URL=sqlite:///pyquest.db
```

### 5. Seed the Database
Populate the platform with the real-world curriculum:
```bash
python seed.py
```

## 🏃 Launching the Platform

Start the Flask development server:
```bash
python app.py
```
Visit `http://127.0.0.1:5000` in your browser to start your quest! 🎮

## 📁 Project Structure

```text
├── app.py              # Application Entry Point
├── extensions.py       # Decoupled Flask Extensions (DB, Login)
├── seed.py             # Database Seeding Script
├── models/             # SQLAlchemy Models
├── routes/             # Flask Blueprints (Auth, Lessons, AI)
├── services/           # Business Logic (AI, XP, Badges)
├── static/             # CSS, JS, and Images
└── templates/          # Jinja2 HTML Templates
```

## 📜 Curriculum Source
Built based on the **Python Learning Path (Basic -> Advanced)** concept map, featuring World-based progression and Boss Challenges.

---
*Created with ❤️ by Antigravity AI for future Pythonistas.*
