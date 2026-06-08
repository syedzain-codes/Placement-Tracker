import mysql.connector
from datetime import date
def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="MASHALLAH",
        database="placement_tracker"
    )

    return conn





def add_problem():

    name = input("Problem Name: ")
    topic = input("Topic: ")
    difficulty = input("Difficulty: ")

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO problems
    (name, topic, difficulty, solved_date)
    VALUES (%s,%s,%s,%s)
    """

    values = (
        name,
        topic,
        difficulty,
        date.today()
    )

    cursor.execute(query, values)

    conn.commit()

    conn.close()

    print("Problem Added Successfully")

def view_problems():

   

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM problems"
    )

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()

def del_problem(index):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    DELETE FROM problems
    WHERE id = %s
    """

    cursor.execute(query, (index,))

    if cursor.rowcount == 0:
        print("Invalid ID")
    else:
        conn.commit()
        print("Problem Deleted Successfully")

    conn.close()
    


    

def statistics():
  

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM problems")

    rows = cursor.fetchall()

    easy = 0
    medium = 0
    hard = 0

    for row in rows:

        if row[3].lower() == "easy":
            easy += 1

        elif row[3].lower() == "medium":
            medium += 1

        elif row[3].lower() == "hard":
            hard += 1

    print(f"Easy   : {easy}")
    print(f"Medium : {medium}")
    print(f"Hard   : {hard}")
    print(f"Total  : {len(rows)}")

    conn.close()
def search_by_topic(topic_name):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT *
    FROM problems
    WHERE LOWER(topic) = LOWER(%s)
    """

    cursor.execute(query, (topic_name,))

    rows = cursor.fetchall()

    if len(rows) == 0:
        print("Topic Not Yet Solved")

    else:
        for row in rows:

            print("-" * 30)
            print(f"ID           : {row[0]}")
            print(f"Problem Name : {row[1]}")
            print(f"Topic        : {row[2]}")
            print(f"Difficulty   : {row[3]}")
            print(f"Date Solved  : {row[4]}")
            print("-" * 30)

    conn.close()





    
def update(problem_id):

    conn = get_connection()
    cursor = conn.cursor()

    print("1. Update Topic")
    print("2. Update Difficulty")

    choice = int(input("Enter Choice: "))

    if choice == 1:

        new_topic = input("Enter New Topic: ")

        query = """
        UPDATE problems
        SET topic = %s
        WHERE id = %s
        """

        cursor.execute(query, (new_topic, problem_id))

    elif choice == 2:

        new_difficulty = input("Enter New Difficulty: ")

        query = """
        UPDATE problems
        SET difficulty = %s
        WHERE id = %s
        """

        cursor.execute(query, (new_difficulty, problem_id))

    else:
        print("Invalid Choice")
        conn.close()
        return

    if cursor.rowcount == 0:
        print("Invalid ID")
    else:
        conn.commit()
        print("Updated Successfully")

    conn.close()

def recent_problems():

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT *
    FROM problems
    ORDER BY solved_date DESC
    LIMIT 5
    """

    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        if len(rows) == 0:
            print("No Problems Found")
            conn.close()
            return
       

        print("-" * 30)
        print(f"ID           : {row[0]}")
        print(f"Problem Name : {row[1]}")
        print(f"Topic        : {row[2]}")
        print(f"Difficulty   : {row[3]}")
        print(f"Date Solved  : {row[4]}")
        print("-" * 30)

    conn.close()
def topic_breakdown():

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT topic, COUNT(*)
    FROM problems
    GROUP BY topic
    """

    cursor.execute(query)

    rows = cursor.fetchall()

    print("\nTopic Breakdown")

    for topic, count in rows:
        print(f"{topic} : {count}")

    conn.close()
    

    
      



   
       





while True:

    print("\n=== Placement Tracker ===")
    print("1. Add Problem")
    print("2. View Problems")
    print("3. delete")
    print("4,.statistics")
    print("5.search by name")
    print("6:update")
    print("7.Recent Problems")
    print("8.Topic wise breakdown")
    print("9.exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        add_problem()

    elif choice == 2:
        view_problems()

    elif choice==3:
        y=int(input("Enter index of problem to delete"))
        del_problem(y)    
    elif choice==4:
        statistics()  
    elif choice==5 :
        s=input("enter topic name")
        search_by_topic(s) 
    elif choice==6: 
        s=int(input("Enter index of problem to update"))
        update(s)   

    elif choice ==7:
        recent_problems()
        

    elif choice==8:
        topic_breakdown()
        
    elif choice==9:
        print("program exit")
        break   
    else:
        print("enter correct choice")


   





   