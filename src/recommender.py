from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

import csv
@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def _score(self, user: UserProfile, song: Song) -> float:
        """Return a match score for one song against the user's profile."""
        score = 0.0
        if song.genre == user.favorite_genre:
            score += 2.0
        if song.mood == user.favorite_mood:
            score += 1.5
        score += 1.0 - abs(song.energy - user.target_energy)   # energy closeness
        if user.likes_acoustic:
            score += song.acousticness                          # bonus for acoustic lovers
        return score

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        ranked = sorted(self.songs, key=lambda song: self._score(user, song), reverse=True)
        return ranked[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        reasons = []
        if song.genre == user.favorite_genre:
            reasons.append(f"it's {song.genre}, your favorite genre")
        if song.mood == user.favorite_mood:
            reasons.append(f"it has a {song.mood} mood you like")
        if not reasons:
            reasons.append("it's a fresh pick to broaden your taste")
        return "Recommended because " + ", and ".join(reasons)

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    # TODO: Implement CSV loading logic

    songs = []
    with open(csv_path, newline = "", encoding = "utf-8") as f:
        reader = csv.DictReader(f) 
        for row in reader:
            row["id"] = int(row["id"])
            for col in ['energy', 'tempo_bpm', 'valence', 'danceability', 'acousticness']:
                row[col] = float(row[col])
            songs.append(row)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    score = 0.0
    reasons: List[str] = []

   
    if song["genre"] == user_prefs.get("genre"):
        score += 2.0
        reasons.append(f"matches your {user_prefs['genre']} taste")

    
    if song["mood"] == user_prefs.get("mood"):
        score += 1.5
        reasons.append(f"fits your {user_prefs['mood']} mood")

    
    if "energy" in user_prefs:
        energy_gap = abs(song["energy"] - user_prefs["energy"])
        closeness = 1.0 - energy_gap          # ~1 when close, ~0 when far apart
        score += closeness
        if energy_gap <= 0.15:
            reasons.append(f"energy ({song['energy']}) is close to what you want")

    if not reasons:
        reasons.append("a fresh pick outside your usual preferences")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    scored = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)
        scored.append((song, score, explanation))

    scored.sort(key=lambda item: item[1], reverse=True)

    return scored[:k]
