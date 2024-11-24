import threading
import random
import time
from queue import Queue
from math import ceil

# Stałe globalne
K = 5  # Liczba kierunków
STUDENTS_PER_DIRECTION = [random.randint(80, 160) for _ in range(K)]  # Liczba studentów na kierunku
MAX_IN_ROOM = 3  # Maksymalna liczba studentów w jednym pokoju
EXAM_DIRECTION = random.randint(0, K - 1)  # Wylosowany kierunek na egzamin
REPEATERS_PERCENTAGE = 0.05  # Odsetek studentów powtarzających egzamin
PREPARATION_TIME = 3  # Czas przygotowania do odpowiedzi
