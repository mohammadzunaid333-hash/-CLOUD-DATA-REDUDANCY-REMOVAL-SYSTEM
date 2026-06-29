
# ☁️ Cloud Data Redundancy Removal System

A modern web application built using **FastAPI, SQLite, HTML, CSS, and JavaScript** to efficiently store unique records while preventing duplicate data. The system helps maintain clean and organized data by automatically detecting redundant entries.

---

## 📌 Project Overview

The **Cloud Data Redundancy Removal System** is designed to eliminate duplicate records before storing them in the database. It provides an easy-to-use interface where users can add, search, delete, and export records.

This project demonstrates CRUD operations, database integration, REST APIs, and frontend-backend communication.

---

## ✨ Features

- ✅ Add New Records
- ✅ Duplicate Email Detection
- ✅ View Stored Records
- ✅ Delete Records
- ✅ Live Search (Name & Email)
- ✅ Export Records to CSV
- ✅ Total Record Counter
- ✅ Database Status Indicator
- ✅ Responsive & Modern UI
- ✅ FastAPI REST API

---

## 🛠️ Technologies Used

### Frontend
- HTML5
- CSS3
- JavaScript (ES6)

### Backend
- FastAPI
- Python

### Database
- SQLite

---

## 📂 Project Structure

```
CloudDataRedundancyRemovalSystem/
│
├── app.py
├── database.py
├── data.db
├── index.html
├── style.css
├── script.js
├── README.md
└── screenshots/
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/Cloud-Data-Redundancy-Removal-System.git
```

### 2. Open Project

```bash
cd Cloud-Data-Redundancy-Removal-System
```

### 3. Install Dependencies

```bash
pip install fastapi uvicorn
```

### 4. Run Backend

```bash
uvicorn app:app --reload
```

Backend runs on:

```
http://127.0.0.1:8000
```

API Documentation:

```
http://127.0.0.1:8000/docs
```

### 5. Run Frontend

Open `index.html` using **Live Server** in Visual Studio Code.

```
http://127.0.0.1:5500
```

---

## 📷 Application Preview

### Dashboard

- Total Records Counter
- Database Status
- Add New Record
- Search Records
- Delete Records
- Export CSV

---



## 🔗 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | API Status |
| GET | `/records` | Fetch All Records |
| POST | `/add-record` | Add New Record |
| DELETE | `/delete-record/{email}` | Delete Record |
| GET | `/status` | Database Status |

---

## 💡 How It Works

1. User enters Name and Email.
2. System checks if the email already exists.
3. Duplicate entries are rejected.
4. Unique records are stored in SQLite.
5. Records are displayed instantly.
6. Users can search, delete, or export data.

---

## 🚀 Future Enhancements

- Edit/Update Records
- User Authentication
- Cloud Database Integration
- File Upload Support
- Record History
- Dashboard Analytics
- Dark Mode
- Email Validation
- Pagination

---

## 🎯 Learning Outcomes

This project helped in understanding:

- REST API Development
- CRUD Operations
- SQLite Database
- FastAPI Framework
- JavaScript Fetch API
- Frontend & Backend Integration
- Responsive Web Design

---

## 👨‍💻 Author

**Mohammed Zunaid**

B.Tech CSE (Artificial Intelligence & Data Science)

Mohan Babu University, Tirupati


LinkedIn:www.linkedin.com/in/
pinjari-mohammed-zunaid-14076527a



---

## 📄 License

This project is developed for educational and internship purposes.

---

⭐ If you like this project, don't forget to give it a star on GitHub!



