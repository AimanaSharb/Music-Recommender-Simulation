"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

try:
    from recommender import load_songs, recommend_songs  # run as: python src/main.py
except ModuleNotFoundError:
    from src.recommender import load_songs, recommend_songs  # run as: python -m src.main


def main() -> None:
    songs = load_songs("data/songs.csv")

    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("=" * 60)
    print("  MUSIC RECOMMENDER")
    print(f"  Profile: genre={user_prefs['genre']}, "
          f"mood={user_prefs['mood']}, energy={user_prefs['energy']}")
    print(f"  Loaded {len(songs)} songs")
    print("=" * 60)
    print(f"\nTop {len(recommendations)} recommendations:\n")

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"{rank}. {song['title']} - {song['artist']}  (score: {score:.2f})")
        print(f"   Because: {explanation}")
        print()


if __name__ == "__main__":
    main()
