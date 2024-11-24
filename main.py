# Inicjalizacja dziekana
dean = Dean()

# Uruchomienie komisji A (praktyczna)
commission_a = Commission("Komisja A (praktyczna)", practical_queue, practical_results, dean, is_practical=True)
commission_a.start()
commission_a.join()

# Uruchomienie komisji B (teoretyczna)
commission_b = Commission("Komisja B (teoretyczna)", theoretical_queue, theoretical_results, dean, is_practical=False)
commission_b.start()

# Symulacja ewakuacji po losowym czasie
evacuation_time = random.uniform(5, 10)
time.sleep(evacuation_time)
dean.send_evacuate_signal()

commission_b.join()

# Publikacja wyników
dean.results.extend(practical_results.items())
dean.results.extend(theoretical_results.items())
dean.publish_results()
