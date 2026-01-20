def initialize():

    global global_QnA, student, students, num_of_pass, num_of_distinction, total_score
    global_QnA = []

    student = {
        "studentID": None,
        "studentScore": None
    }
    students = []
    num_of_pass = 0
    num_of_distinction = 0
    total_score = 0

    students = [{"studentID": 1, "studentScore": 10}, {"studentID": 2, "studentScore": 15},
                {"studentID": 3, "studentScore": 5}, {"studentID": 4, "studentScore": 3},
                {"studentID": 5, "studentScore": 6}]
    global_QnA = [
        {
            "question": "8^0",
            "answer": 1,
            "options": ["1", "0", "8", "0.5"]
        },
        {
            "question": "42 / 7",
            "answer": 6,
            "options": ["5", "6", "7", "8"]
        },
        {
            "question": "190 + (-30)",
            "answer": 160,
            "options": ["220", "60", "160", "70"]
        },
        {
            "question": "6^2",
            "answer": 36,
            "options": ["22", "12", "16", "36"]
        },
        {
            "question": "7 * 7",
            "answer": 49,
            "options": ["49", "47", "46", "42"]
        },
        {
            "question": "121^(1/2)",
            "answer": 11,
            "options": ["10", "11", "12", "13"]
        },
        {
            "question": "21 / 3",
            "answer": 7,
            "options": ["7", "8", "9", "6"]
        },
        {
            "question": "10^3",
            "answer": 1000,
            "options": ["10", "10000", "1000", "100"]
        },
        {
            "question": "11 * 11",
            "answer": 121,
            "options": ["111", "121", "130", "120"]
        },
        {
            "question": "12^2",
            "answer": 144,
            "options": ["141", "144", "151", "120"]
        },
        {
            "question": "15 * 5",
            "answer": 75,
            "options": ["65", "80", "75", "70"]
        },
        {
            "question": "72 / 8",
            "answer": 9,
            "options": ["8", "6", "7", "9"]
        },
        {
            "question": "16 * 3",
            "answer": 48,
            "options": ["46", "44", "48", "42"]
        },
        {
            "question": "17 - 19",
            "answer": -2,
            "options": ["2", "-2", "0", "1"]
        },
        {
            "question": "9^2",
            "answer": 81,
            "options": ["17", "11", "18", "81"]
        }
    ]


def get_int_in_range(max_val):
    value = -1

    while not 0 <= value <= max_val:
        try:
            value = int(input(f"Please enter a value between 0 and {max_val}:\n"))
        except:
            print(f"Invalid input. Please enter a number between 0 and {max_val}.\nTRY AGAIN!\n")

    return value
