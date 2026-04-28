import json
import os


SETTINGS_FILE = "settings.json"
LEADERBOARD_FILE = "leaderboard.json"


def load_settings():
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "r") as f:
            return json.load(f)
  
    return {"sound": True, "car_color": "red", "difficulty": "Medium"}

def save_settings(settings_dict):
    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings_dict, f, indent=4)

def load_leaderboard():
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, "r") as f:
            return json.load(f)
    return []


def add_score(name, score):
    scores = load_leaderboard()
    scores.append({"name": name, "score": score})
    scores = sorted(scores, key=lambda x: x['score'], reverse=True)[:10]
    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(scores, f, indent=4)

