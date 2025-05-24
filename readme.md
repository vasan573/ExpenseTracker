# 💰 Expense Management System

This project is an **Expense Management System** built with a **FastAPI backend** and a **Streamlit frontend**. It allows users to log and analyze expenses efficiently, with a clear interface and real-time analytics.

---

## 🗂 Project Structure


---

## 🧰 Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Backend**: [FastAPI](https://fastapi.tiangolo.com/)
- **Testing**: `pytest`
- **HTTP Requests**: `requests`
- **Data Handling**: `pandas`, `matplotlib`

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/vasan573/ExpenseTracker.git
cd expense-management-system.
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3.Run the FastAPI server
```bash
uvicorn server.server:app --reload
```
### 4. Run the streamlit app
```bash
streamlit run frontend/app.py
```