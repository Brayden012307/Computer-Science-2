print("==========================")
print("HOMEWORK 7")
print("==========================")
import pickle
import os

def practice_3_beginner():
    print("\n" + "-" * 50)
    print("EXERCISE 3.1: Pickle & Project Setup")
    print("-" * 50)

    
    shopping_list = ["Apples", "Bananas", "Milk", "Bread"]

   
    with open("shopping.pkl", "wb") as f:
        pickle.dump(shopping_list, f)
    
    print("Shopping list pickled!")

    
    with open("shopping.pkl", "rb") as f:
        loaded_list = pickle.load(f)

    print(f"Loaded list: {loaded_list}")

    
    loaded_list.append("Eggs")
    loaded_list.append("Cheese")

    with open("shopping.pkl", "wb") as f:
        pickle.dump(loaded_list, f)
    
    print("Updated list saved")

    
    project_name = "my_project"
    if not os.path.exists(project_name):
        os.makedirs(project_name)
        print(f"Created directory: {project_name}")

    
    subdirs = ["src", "docs", "tests", "data"]
    for subdir in subdirs:
        path = os.path.join(project_name, subdir)
        if not os.path.exists(path):
            os.makedirs(path)

    
    with open(os.path.join(project_name, "README.md"), "w") as f:
        f.write("# My Project\nInitial documentation.")
    with open(os.path.join(project_name, "src", "main.py"), "w") as f:
        f.write("# Main script")

    
    print("\nProject structure:")
    for root, dirs, files in os.walk(project_name):
        level = root.replace(project_name, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print(f"{subindent}{f}")

practice_3_beginner()

import os
import shutil

def practice_3_intermediate():
    print("\n" + "-" * 50)
    print("EXERCISE 3.2: File Organizer")
    print("-" * 50)

    messy_folder = "messy_files"
    
    
    if not os.path.exists(messy_folder):
        os.makedirs(messy_folder)

    test_files = [
        "document.txt", "image.jpg", "photo.png",
        "report.pdf", "script.py", "data.csv",
        "music.mp3", "video.mp4", "archive.zip"
    ]

    
    for filename in test_files:
        filepath = os.path.join(messy_folder, filename)
        with open(filepath, "w") as f:
            f.write(f"Test file: {filename}")

    
    organized = {
        "documents": [".txt", ".pdf", ".doc"],
        "images": [".jpg", ".png", ".gif"],
        "code": [".py", ".js", ".html"],
        "data": [".csv", ".json", ".xml"],
        "media": [".mp3", ".mp4", ".avi"],
        "archives": [".zip", ".tar", ".rar"]
    }

    
    for category in organized:
        cat_path = os.path.join(messy_folder, category)
        if not os.path.exists(cat_path):
            os.makedirs(cat_path)

    
    for filename in os.listdir(messy_folder):
        filepath = os.path.join(messy_folder, filename)
        
        
        if os.path.isdir(filepath):
            continue
            
        
        _, extension = os.path.splitext(filename)
        
        
        moved = False
        for category, extensions in organized.items():
            if extension.lower() in extensions:
                dest_path = os.path.join(messy_folder, category, filename)
                shutil.move(filepath, dest_path)
                moved = True
                break
        
        if not moved:
            print(f"Skipped {filename}: No category found.")

    
    print("Files organized successfully!")

practice_3_intermediate()

import pickle
import os
import shutil
from datetime import datetime
from pathlib import Path


class GameState:
    def __init__(self):
        self.player_name = ""
        self.level = 1
        self.score = 0
        self.inventory = []
        self.position = (0, 0)

    def __str__(self):
        return f"{self.player_name} - Level {self.level}, Score: {self.score}"


def save_game(game_state, slot_number):
    """Save game to a specific slot"""
    save_dir = "saves"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    filename = f"save_slot_{slot_number}.pkl"
    filepath = os.path.join(save_dir, filename)
    
    with open(filepath, "wb") as f:
        pickle.dump(game_state, f)
    print(f"Game saved to slot {slot_number}")


def create_backup(source_dir, backup_dir="backups"):
    """Create timestamped backup of source directory"""
    if not os.path.exists(source_dir):
        return
    
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
        
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_folder_name = f"backup_{timestamp}"
    dest_path = os.path.join(backup_dir, backup_folder_name)
    
    shutil.copytree(source_dir, dest_path)
    print(f"Backup created at {dest_path}")
    return dest_path


def verify_backup(source, backup):
    """Check all files in source are also in backup"""
    source_files = os.listdir(source)
    backup_files = os.listdir(backup)
    return all(item in backup_files for item in source_files)


def cleanup_old_backups(backup_dir, keep_count=3):
    """Keep only the most recent N backups"""
    backups = [os.path.join(backup_dir, d) for d in os.listdir(backup_dir)]
    backups.sort(key=os.path.getmtime, reverse=True)
    
    for old_backup in backups[keep_count:]:
        shutil.rmtree(old_backup)
        print(f"Deleted old backup: {old_backup}")

def practice_3_advanced():
    print("\n" + "-" * 50)
    print("EXERCISE 3.3: Game Save System")
    print("-" * 50)

    
    game = GameState()
    game.player_name = "Hero"
    game.level = 5
    game.score = 1250
    game.inventory = ["Sword", "Shield", "Potion"]
    game.position = (10, 25)

    
    save_game(game, 1)

    
    save_path = os.path.join("saves", "save_slot_1.pkl")
    with open(save_path, "rb") as f:
        loaded_game = pickle.load(f)
    
    print(f"Loaded: {loaded_game.player_name}, Level: {loaded_game.level}, Score: {loaded_game.score}")
    print(f"Inventory: {loaded_game.inventory}, Position: {loaded_game.position}")

    
    print(f"Available saves: {os.listdir('saves')}")

    
    backup_path = create_backup("saves")
    if verify_backup("saves", backup_path):
        print("Backup verified!")
    
    cleanup_old_backups("backups", keep_count=1)

practice_3_advanced()