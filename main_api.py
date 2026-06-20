from fastapi import FastAPI
from pydantic import BaseModel, field_validator
from fastapi.middleware.cors import CORSMiddleware
from datetime import date
from database import get_connection

app = FastAPI()


@app.get("/")
def home():
    return {
        "status": "success",
        "message": "Placement Tracker API Running",
        "docs": "/docs"
    }


@app.get("/health")
def health_check():
    try:
        conn = get_connection()
        conn.close()

        return {
            "status": "healthy",
            "database": "connected"
        }

    except Exception as e:
        return {
            "status": "unhealthy",
            "database": str(e)
        }




@app.get("/problems")
def get_problems():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM problems"
    )

    rows = cursor.fetchall()

    conn.close()

    problems = []

    for row in rows:

        problems.append({
            "id": row[0],
            "name": row[1],
            "topic": row[2],
            "difficulty": row[3],
            "solved_date": str(row[4])
        })

    return problems




@app.get("/problems/search")
def search_problems(
    topic: str | None = None,
    difficulty: str | None = None
):

    conn = get_connection()
    cursor = conn.cursor()

    values = []

    query = """
    SELECT * FROM problems
    WHERE 1=1
    """

    if topic:
        query += " AND topic=%s"
        values.append(topic)

    if difficulty:
        query += " AND difficulty=%s"
        values.append(difficulty)

    cursor.execute(query, values)

    rows = cursor.fetchall()

    conn.close()

    problems = []

    for row in rows:

        problems.append({
            "id": row[0],
            "name": row[1],
            "topic": row[2],
            "difficulty": row[3],
            "solved_date": str(row[4])
        })

    return problems




@app.get("/problems/{problem_id}")
def get_problem(problem_id: int):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM problems WHERE id=%s",
        (problem_id,)
    )

    row = cursor.fetchone()

    conn.close()

    if row is None:
        return {
            "error": "Problem not found"
        }

    return {
        "id": row[0],
        "name": row[1],
        "topic": row[2],
        "difficulty": row[3],
        "solved_date": str(row[4])
    }




@app.post("/problems")
def add_problem(problem: Problem):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO problems
    (name, topic, difficulty, solved_date)
    VALUES (%s,%s,%s,CURDATE())
    """

    cursor.execute(
        query,
        (
            problem.name,
            problem.topic,
            problem.difficulty
        )
    )

    conn.commit()

    conn.close()

    return {
        "message": "Problem Added Successfully"
    }




@app.put("/problems/{problem_id}")
def update_problem(
    problem_id: int,
    problem: UpdateProblem
):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    UPDATE problems
    SET topic=%s,
        difficulty=%s
    WHERE id=%s
    """

    cursor.execute(
        query,
        (
            problem.topic,
            problem.difficulty,
            problem_id
        )
    )

    conn.commit()

    if cursor.rowcount == 0:

        conn.close()

        return {
            "error": "Problem not found"
        }

    conn.close()

    return {
        "message": "Updated Successfully"
    }



@app.delete("/problems/{problem_id}")
def delete_problem(problem_id: int):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    DELETE FROM problems
    WHERE id=%s
    """

    cursor.execute(
        query,
        (problem_id,)
    )

    conn.commit()

    if cursor.rowcount == 0:

        conn.close()

        return {
            "error": "Problem not found"
        }

    conn.close()

    return {
        "message": "Deleted Successfully"
    }
