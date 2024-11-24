class Commission(threading.Thread):
    def __init__(self, name, queue, results, dean, is_practical=True):
        super().__init__()
        self.name = name
        self.queue = queue
        self.results = results
        self.dean = dean
        self.is_practical = is_practical

    def run(self):
        while not self.queue.empty():
            if self.dean.evacuate_signal.is_set():
                print(f"{self.name} opuszcza budynek z powodu ewakuacji.")
                break

            current_batch = []
            for _ in range(min(MAX_IN_ROOM, self.queue.qsize())):
                student = self.queue.get()
                current_batch.append(student)

            for student in current_batch:
                print(f"{student['id']} przystępuje do {self.name}.")
                time.sleep(random.uniform(1, 2))  # Czas zadawania pytań
                scores = [random.choice([2.0, 3.0, 3.5, 4.0, 4.5, 5.0]) for _ in range(3)]
                self.results[student["id"]] = scores

                # Ocena końcowa
                if 2.0 in scores and self.is_practical and not student["is_repeater"]:
                    print(f"{student['id']} nie zdał praktycznej.")
                elif self.is_practical or student["is_repeater"]:
                    theoretical_queue.put(student)

                if self.dean.evacuate_signal.is_set():
                    print(f"{student['id']} przerywa egzamin.")
                    break
