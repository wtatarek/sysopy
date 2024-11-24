5.1. Założenia projektowe kodu
Projekt symuluje egzamin dla studentów na drugim roku studiów z zachowaniem zasad i zdarzeń opisanych w treści zadania. Założenia projektowe obejmują:

Studenci losowo reprezentują różne kierunki, a każdy kierunek ma określoną liczbę studentów (80-160).
Studenci z wybranego kierunku przystępują do egzaminu, inni wracają do domu.
Egzamin składa się z części praktycznej (Komisja A) i teoretycznej (Komisja B).
Wyniki każdej części są oceniane przez komisję, a wynik końcowy ustala dziekan.
Symulacja uwzględnia przerwanie egzaminu przez sygnał ewakuacji, po którym komisje i studenci opuszczają budynek.
Synchronizacja procesów i wątków odpowiada rzeczywistemu przebiegowi egzaminu.



Raport do projektu: Symulacja egzaminu na wydziale X
5.1. Założenia projektowe kodu
Projekt symuluje egzamin dla studentów na drugim roku studiów z zachowaniem zasad i zdarzeń opisanych w treści zadania. Założenia projektowe obejmują:

Studenci losowo reprezentują różne kierunki, a każdy kierunek ma określoną liczbę studentów (80-160).
Studenci z wybranego kierunku przystępują do egzaminu, inni wracają do domu.
Egzamin składa się z części praktycznej (Komisja A) i teoretycznej (Komisja B).
Wyniki każdej części są oceniane przez komisję, a wynik końcowy ustala dziekan.
Symulacja uwzględnia przerwanie egzaminu przez sygnał ewakuacji, po którym komisje i studenci opuszczają budynek.
Synchronizacja procesów i wątków odpowiada rzeczywistemu przebiegowi egzaminu.
Ogólny opis kodu
Kod został podzielony na moduły, w których każdy odzwierciedla inny aspekt symulacji:

Dean: Zarządza sygnałami i publikuje wyniki.
Commission: Obsługuje studentów, przypisując oceny dla części praktycznej i teoretycznej egzaminu.
Student: Reprezentuje studenta w systemie; trafia do kolejek na podstawie kierunku lub statusu powtarzającego.
Synchronizacja została zrealizowana przy użyciu bibliotek Python (threading, queue).


Co udało się zrobić
Symulacja zdarzeń egzaminu:

Losowanie studentów i przydział do odpowiednich kolejek.
Obsługa kolejki do komisji A (praktycznej) i komisji B (teoretycznej).
Generowanie ocen na podstawie losowych wyników i średnich zaokrąglonych zgodnie z zasadami.
Dziekan publikuje wyniki po zakończeniu egzaminu.
Obsługa wątków:

Komisje działają jako oddzielne wątki, które obsługują kolejki studentów.
Obsługa sygnałów ewakuacji i zatrzymanie działania komisji.
Dodane elementy specjalne:

Możliwość wprowadzenia powtarzających się studentów (ok. 5% wszystkich).
Losowa liczba studentów i czas obsługi egzaminu w komisjach.
Synchronizacja wątków, uwzględniając równoczesną obsługę wielu studentów.


Z czym były problemy
Synchronizacja wątków:
Zarządzanie dostępem studentów do komisji wymagało precyzyjnego użycia blokad i warunków, aby uniknąć przeciążeń lub zablokowania wątku.
Ewakuacja:
Obsługa przerwania egzaminu w środku działania komisji wymagała uważnego sprawdzania sygnałów w każdej pętli pracy komisji.
Zaokrąglanie ocen:
W implementacji algorytmu zaokrąglania musiało zostać uwzględnione precyzyjne przypisywanie ocen zgodnie z opisanymi zasadami.



Raport do projektu: Symulacja egzaminu na wydziale X
5.1. Założenia projektowe kodu
Projekt symuluje egzamin dla studentów na drugim roku studiów z zachowaniem zasad i zdarzeń opisanych w treści zadania. Założenia projektowe obejmują:

Studenci losowo reprezentują różne kierunki, a każdy kierunek ma określoną liczbę studentów (80-160).
Studenci z wybranego kierunku przystępują do egzaminu, inni wracają do domu.
Egzamin składa się z części praktycznej (Komisja A) i teoretycznej (Komisja B).
Wyniki każdej części są oceniane przez komisję, a wynik końcowy ustala dziekan.
Symulacja uwzględnia przerwanie egzaminu przez sygnał ewakuacji, po którym komisje i studenci opuszczają budynek.
Synchronizacja procesów i wątków odpowiada rzeczywistemu przebiegowi egzaminu.
Ogólny opis kodu
Kod został podzielony na moduły, w których każdy odzwierciedla inny aspekt symulacji:

Dean: Zarządza sygnałami i publikuje wyniki.
Commission: Obsługuje studentów, przypisując oceny dla części praktycznej i teoretycznej egzaminu.
Student: Reprezentuje studenta w systemie; trafia do kolejek na podstawie kierunku lub statusu powtarzającego.
Synchronizacja została zrealizowana przy użyciu bibliotek Python (threading, queue).
Co udało się zrobić
Symulacja zdarzeń egzaminu:

Losowanie studentów i przydział do odpowiednich kolejek.
Obsługa kolejki do komisji A (praktycznej) i komisji B (teoretycznej).
Generowanie ocen na podstawie losowych wyników i średnich zaokrąglonych zgodnie z zasadami.
Dziekan publikuje wyniki po zakończeniu egzaminu.
Obsługa wątków:

Komisje działają jako oddzielne wątki, które obsługują kolejki studentów.
Obsługa sygnałów ewakuacji i zatrzymanie działania komisji.
Dodane elementy specjalne:

Możliwość wprowadzenia powtarzających się studentów (ok. 5% wszystkich).
Losowa liczba studentów i czas obsługi egzaminu w komisjach.
Synchronizacja wątków, uwzględniając równoczesną obsługę wielu studentów.
Z czym były problemy
Synchronizacja wątków:
Zarządzanie dostępem studentów do komisji wymagało precyzyjnego użycia blokad i warunków, aby uniknąć przeciążeń lub zablokowania wątku.
Ewakuacja:
Obsługa przerwania egzaminu w środku działania komisji wymagała uważnego sprawdzania sygnałów w każdej pętli pracy komisji.
Zaokrąglanie ocen:
W implementacji algorytmu zaokrąglania musiało zostać uwzględnione precyzyjne przypisywanie ocen zgodnie z opisanymi zasadami.
Zauważone problemy z testami
Wielowątkowość:
Testowanie wyników w środowisku wielowątkowym wymagało ustalenia kolejności działań, aby wyniki były spójne.
Losowość:
Ze względu na losowość wyników testowanie wymagało ustalenia stałych nasion (random.seed()), aby odtwarzać wyniki testów.


Linki do istotnych fragmentów kodu
Poniżej przedstawiono przykładowe linki do fragmentów kodu, które ilustrują wykorzystanie odpowiednich konstrukcji systemowych. Fragmenty te należy umieścić w repozytorium GitHub, a linki należy dostosować.

Tworzenie i obsługa wątków:

pthread_create i pthread_join: Fragment kodu obsługujący komisje jako wątki:
Link do fragmentu kodu komisji
Obsługa sygnałów:

signal i kill: Dziekan wysyła sygnał ewakuacji:
Link do fragmentu kodu dziekana
Synchronizacja procesów i wątków:

pthread_mutex_lock i pthread_cond_wait: Synchronizacja dostępu studentów do komisji:
Link do fragmentu kodu synchronizacji
Kolejki komunikatów:

queue.Queue: Obsługa kolejek studentów:
Link do fragmentu kodu kolejek
Obsługa plików (opcjonalnie):

Wyniki egzaminu mogą być zapisane w pliku: Link do fragmentu zapisu wyników
