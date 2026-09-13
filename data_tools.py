import random
import os
from datetime import datetime


os.makedirs("data", exist_ok=True)


def generate_data_file():
    names = [
        " lisa ",
        "JOHN",
        " aisha",
        "Peter ",
        "sarah",
        " DAVID ",
        "michael",
        " Thandi "
    ]

    with open("data/students.txt", "w") as file:
        for name in names:
            score = random.randint(0, 100)
            file.write(f"{name},{score}\n")

    return "Student data file generated successfully."


def load_students():
    students = []

    with open("data/students.txt", "r") as file:
        for line in file:
            clean_line = line.strip()

            if clean_line:
                name, score = clean_line.split(",")

                clean_name = name.strip().title()
                clean_score = int(score.strip())

                students.append((clean_name, clean_score))

    return students


def export_report(text):
    with open("data/report.txt", "w") as file:
        file.write(text)

    return "Report exported successfully."


def log_event(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("data/activity.log", "a") as file:
        file.write(f"[{timestamp}] {message}\n")
