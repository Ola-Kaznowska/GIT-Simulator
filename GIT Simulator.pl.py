import os
from datetime import datetime
from colorama import Fore, init

# Inicjalizacja kolorów w terminalu
init(autoreset=True)

# Zmienna przechowująca ścieżkę repozytorium
repository_directory = ""
# Zmienna przechowująca historię commitów
commit_history = []

# Funkcja inicjalizująca repozytorium
def initialize_repository(repo_name):
    """Inicjalizuje repozytorium z podaną nazwą."""
    global repository_directory
    
    repository_directory = f".{repo_name}_repo"
    
    # Sprawdzenie, czy repozytorium już istnieje
    if os.path.exists(repository_directory):
        print(f"{Fore.YELLOW}Repozytorium '{repo_name}_repo' jest już zainicjalizowane.")
    else:
        os.makedirs(repository_directory)
        print(f"{Fore.GREEN}Repozytorium '{repo_name}_repo' zostało zainicjalizowane.")

# Funkcja do wykonania commita
def create_commit():
    """Tworzy nowy commit w repozytorium, symulując dodanie nowej wersji."""
    if not os.path.exists(repository_directory):
        print(f"{Fore.RED}Błąd: Repozytorium nie jest zainicjalizowane. Najpierw użyj 'inicjalizuj'.")
        return

    # Tworzenie wpisu w historii commitów
    commit_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    commit_message = f"Commit z dnia {commit_time}"
    commit_history.append(commit_message)
    
    print(f"{Fore.GREEN}Commit zakończony: {commit_message}")

# Funkcja do wyświetlania historii commitów
def display_log():
    """Wyświetla historię commitów w repozytorium."""
    if not os.path.exists(repository_directory):
        print(f"{Fore.RED}Błąd: Repozytorium nie jest zainicjalizowane. Najpierw użyj 'inicjalizuj'.")
        return

    if not commit_history:
        print(f"{Fore.YELLOW}Brak commitów.")
    else:
        print(f"{Fore.CYAN}Historia commitów:")
        for commit_entry in commit_history:
            print(f"{Fore.MAGENTA}{commit_entry}")

# Funkcja do wyświetlania dostępnych commitów w repozytorium
def show_repository():
    """Pokazuje dostępne repozytoria i listę commitów w repozytorium."""
    print(f"{Fore.CYAN}Dostępne repozytoria:")
    if os.path.exists(repository_directory):
        print(f"{Fore.YELLOW}{repository_directory} zawiera:")
        if not commit_history:
            print(f"{Fore.YELLOW}  - Brak commitów.")
        else:
            for commit_entry in commit_history:
                print(f"{Fore.GREEN}  - {commit_entry}")
    else:
        print(f"{Fore.RED}Brak repozytoriów.")

# Funkcja do wyświetlania informacji o programie na początku
def display_program_info():
    """Wyświetla informacje o programie na początku w kolorze niebieskim."""
    print(f"{Fore.BLUE}Witaj w systemie kontroli wersji!")
    print(f"{Fore.BLUE}Jest to program do zarządzania repozytoriami i wersjami commitów.")
    print(f"{Fore.BLUE}Wprowadź odpowiednie polecenia, aby zarządzać repozytoriami i commitami.")
    print(f"{Fore.BLUE}Dostępne polecenia: 'inicjalizuj <repo_name>', 'commit', 'log', 'pokaz', 'wyjdz'.")

# Główna pętla aplikacji
display_program_info()

while True:
    command = input("\nWprowadź polecenie: ").strip().split()

    if not command:
        continue

    cmd = command[0]
    
    # Inicjalizacja repozytorium
    if cmd == "inicjalizuj" and len(command) > 1:
        initialize_repository(command[1])

    # Komenda commit
    elif cmd == "commit":
        create_commit()
    
    # Wyświetlanie logów commitów
    elif cmd == "log":
        display_log()

    # Pokazanie dostępnych commitów w repozytorium
    elif cmd == "pokaz":
        show_repository()

    # Zakończenie programu
    elif cmd == "wyjdz":
        print(f"{Fore.GREEN}Program zakończony.")
        break

    # Obsługa nieznanych komend
    else:
        print(f"{Fore.RED}Błąd: Nieznane polecenie lub niepoprawne użycie.")

