class Dean:
    def __init__(self):
        self.evacuate_signal = threading.Event()  # Sygnał do ewakuacji
        self.results = []  # Wyniki egzaminu

    def send_evacuate_signal(self):
        print("Dziekan ogłasza ewakuację!")
        self.evacuate_signal.set()

    def publish_results(self):
        print("\n=== Wyniki egzaminu ===")
        for result in self.results:
            print(result)
