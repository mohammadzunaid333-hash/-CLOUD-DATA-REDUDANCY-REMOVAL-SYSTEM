from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from database import conn

app = FastAPI()

# -------------------- CORS --------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------- Model --------------------

class Record(BaseModel):
    name: str
    email: str

# -------------------- Home --------------------

@app.get("/")
def home():
    return {
        "message": "Cloud Data Redundancy Removal System API Running"
    }

# -------------------- Get Records --------------------

@app.get("/records")
def get_records():

    cursor = conn.cursor()

    cursor.execute("""
        SELECT name,email
        FROM records
        WHERE name!='' AND email!=''
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    cursor.close()

    return [
        {
            "name": row[0],
            "email": row[1]
        }
        for row in rows
    ]

# -------------------- Add Record --------------------

@app.post("/add-record")
def add_record(record: Record):

    cursor = conn.cursor()

    name = record.name.strip()
    email = record.email.strip()

    if name == "" or email == "":
        cursor.close()
        return {
            "status": "error",
            "message": "Name and Email are required!"
        }

    cursor.execute(
        "SELECT * FROM records WHERE email=?",
        (email,)
    )

    if cursor.fetchone():
        cursor.close()
        return {
            "status": "error",
            "message": "Duplicate Email! Record already exists."
        }

    cursor.execute(
        "INSERT INTO records(name,email) VALUES(?,?)",
        (name, email)
    )

    conn.commit()
    cursor.close()

    return {
        "status": "success",
        "message": "Record Added Successfully!"
    }

# -------------------- Delete Record --------------------

@app.delete("/delete-record/{email}")
def delete_record(email: str):

    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM records WHERE email=?",
        (email,)
    )

    conn.commit()
    cursor.close()

    return {
        "status": "success",
        "message": "Record Deleted Successfully!"
    }

# -------------------- Database Status --------------------

@app.get("/status")
def status():

    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM records")

    total = cursor.fetchone()[0]

    cursor.close()

    return {
        "database": "Connected",
        "total_records": total
    }