import random
import sqlite3

connection = sqlite3.connect("portfolio.db")
cursor = connection.cursor()


def clear_database():
    cursor.execute("DELETE FROM post")
    cursor.execute("DELETE FROM question")

    connection.commit()


def generate_post_table():
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS post (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            content TEXT NOT NULL
        )
    """
    )

    for i in range(0, 25):
        random_num = random.randrange(1, 1000)
        content = """Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                    Sed euismod libero sit amet sapien scelerisque tempus."""

        cursor.execute(
            """
            INSERT INTO post (title, content)
            VALUES (?, ?)
        """,
            (random_num, content),
        )

    connection.commit()


def generate_question_table():
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS question (
            id INTEGER PRIMARY KEY,
            content TEXT NOT NULL,
            answer TEXT NOT NULL
        )
    """
    )

    questions = [
        "What is the capital of France?",
        "Who is the author of 'Romeo and Juliet'?",
        "What is the largest planet in our solar system?",
        "What year was the first iPhone released?",
        "What is the chemical symbol for water?",
        "Who painted the Mona Lisa?",
        "What is the tallest mountain in the world?",
        "What is the currency of Japan?",
        "Which programming language is known as the 'language of the web'?",
        "What is the boiling point of water in Celsius?",
    ]
    answers = [
        "Paris",
        "William Shakespeare",
        "Jupiter",
        "2007",
        "H2O",
        "Leonardo da Vinci",
        "Mount Everest",
        "Japanese yen",
        "JavaScript",
        "100 degrees",
    ]

    for i in range(len(questions)):
        cursor.execute(
            """
            INSERT INTO question (content, answer)
            VALUES (?, ?)
        """,
            (questions[i], answers[i]),
        )

    connection.commit()


if __name__ == "__main__":
    clear_database()
    generate_post_table()
    generate_question_table()
    connection.close()
