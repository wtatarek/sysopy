students = []
practical_queue = Queue()
theoretical_queue = Queue()
practical_results = {}
theoretical_results = {}

# Tworzenie studentów
for direction_id in range(K):
    for student_id in range(STUDENTS_PER_DIRECTION[direction_id]):
        student = {
            "id": f"K{direction_id + 1}_S{student_id + 1}",
            "direction": direction_id,
            "is_repeater": random.random() < REPEATERS_PERCENTAGE,
        }
        students.append(student)

# Studenci przychodzą do kolejki
random.shuffle(students)
for student in students:
    if student["direction"] == EXAM_DIRECTION or student["is_repeater"]:
        practical_queue.put(student)

print(f"Liczba studentów przystępujących do egzaminu: {practical_queue.qsize()}")
