from fastapi import APIRouter

from database import get_connection

from schemas import Problem, UpdateProblem, ProblemResponse

router = APIRouter()


@router.get("/problems")
def get_problems():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM problems")

    rows = cursor.fetchall()

    problems = []

    for row in rows:

        problems.append({
            "id": row[0],
            "name": row[1],
            "topic": row[2],
            "difficulty": row[3],
            "solved_date": str(row[4])
        })

    conn.close()

    return problems


@router.get(
    "/problems/{problem_id}",
    response_model=ProblemResponse
)

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


@router.post("/problems")
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


@router.put("/problems/{problem_id}")
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


@router.delete("/problems/{problem_id}")
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
@router.get("/problems/search")
def search_problems(topic: str):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM problems
        WHERE topic = %s
        """,
        (topic,)
    )

    rows = cursor.fetchall()

    conn.close()

    return rows