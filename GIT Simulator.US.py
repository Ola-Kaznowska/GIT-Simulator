import os
from datetime import datetime
from colorama import Fore, init
from alive_progress import alive_bar
from time import sleep

init(autoreset=True)

REPO_DIR = ""
commit_history = []

def initialize(repo_name):
    global REPO_DIR
    
    REPO_DIR = f".{repo_name}_repo"
    
    if os.path.exists(REPO_DIR):
        print(f"{Fore.YELLOW}Repository '{repo_name}_repo' is already initialized.")
    else:
        os.makedirs(REPO_DIR)
        print(f"{Fore.GREEN}Repository '{repo_name}_repo' has been initialized.")

def commit():
    if not os.path.exists(REPO_DIR):
        print(f"{Fore.RED}Error 00X001: Repository is not initialized. Use 'initialize' first.")
        return

    commit_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    commit_message = f"Commit on {commit_time}"
    commit_history.append(commit_message)
    
    print(f"{Fore.GREEN}Committing...")
    
    # Loading animation during commit
    with alive_bar(100) as bar:
        for i in range(100):
            sleep(0.01)
            bar()
    
    print(f"{Fore.GREEN}Commit completed: {commit_message}")

def log():
    if not os.path.exists(REPO_DIR):
        print(f"{Fore.RED}Error 00X001: Repository is not initialized. Use 'initialize' first.")
        return

    if not commit_history:
        print(f"{Fore.YELLOW}No commits.")
    else:
        print(f"{Fore.CYAN}Commit history:")
        for commit_entry in commit_history:
            print(f"{Fore.MAGENTA}{commit_entry}")

def show():
    print(f"{Fore.CYAN}Available repositories:")
    if os.path.exists(REPO_DIR):
        print(f"{Fore.YELLOW}{REPO_DIR} contains:")
        if not commit_history:
            print(f"{Fore.YELLOW}  - No commits.")
        else:
            for commit_entry in commit_history:
                print(f"{Fore.GREEN}  - {commit_entry}")
    else:
        print(f"{Fore.RED}Error 00X002: No repositories.")

def display_info():
    print(f"{Fore.BLUE}Welcome to the version control system GIT!")
    print(f"{Fore.BLUE}This program is for managing repositories and commit versions.")
    print(f"{Fore.BLUE}Use the appropriate commands to manage repositories and commits.")
    print(f"{Fore.BLUE}Available commands: 'initialize <repo_name>', 'commit', 'log', 'show', 'exit'.")

display_info()

while True:
    command = input("\nEnter command: ").strip().split()

    if not command:
        continue

    cmd = command[0]
    
    if cmd == "initialize" and len(command) > 1:
        initialize(command[1])

    elif cmd == "commit":
        commit()
    
    elif cmd == "log":
        log()

    elif cmd == "show":
        show()

    elif cmd == "exit":
        print(f"{Fore.GREEN}Program terminated.")
        break

    else:
        print(f"{Fore.RED}Error 00X003: Unknown command or incorrect usage.")

