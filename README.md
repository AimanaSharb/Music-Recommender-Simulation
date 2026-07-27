# 🎵 Music Recommender Simulation

## Project Summary

This project builds **VibeMatch 1.0**, a small rule-based music recommender. It
loads a catalog of songs, scores each one against a user's taste profile (favorite
genre, mood, and target energy), and prints a ranked top-K list — each pick paired
with a plain-language reason it was chosen. It runs as a command-line tool and is
also exposed as an object-oriented `Recommender` class covered by unit tests.

---

## How The System Works

Each **`Song`** carries: genre, mood, energy, tempo, valence, danceability, and
acousticness. The scoring currently uses **genre, mood, and energy**.

A **`UserProfile`** stores a favorite genre, a favorite mood, a target energy
level, and whether the user likes acoustic music.

The **`Recommender`** scores every song by adding points for each match:

- **Genre match → +2.0** (strongest taste signal)
- **Mood match → +1.5**
- **Energy closeness → up to +1.0**, scaled by `1 - |song.energy - target|`
- **Acoustic bonus** (OOP version) → `+song.acousticness` if the user likes acoustic

It then **sorts all songs by score, highest first, and returns the top `k`**, each
with an explanation built from the reasons that earned points.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Output of `python -m src.main` for the default `pop / happy / energy=0.8` profile:

```
============================================================
  MUSIC RECOMMENDER
  Profile: genre=pop, mood=happy, energy=0.8
  Loaded 10 songs
============================================================

Top 5 recommendations:

1. Sunrise City - Neon Echo  (score: 4.48)
   Because: matches your pop taste, fits your happy mood, energy (0.82) is close to what you want

2. Gym Hero - Max Pulse  (score: 2.87)
   Because: matches your pop taste, energy (0.93) is close to what you want

3. Rooftop Lights - Indigo Parade  (score: 2.46)
   Because: fits your happy mood, energy (0.76) is close to what you want

4. Night Drive Loop - Neon Echo  (score: 0.95)
   Because: energy (0.75) is close to what you want

5. Storm Runner - Voltline  (score: 0.89)
   Because: energy (0.91) is close to what you want
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

- **Lowering the genre weight (2.0 → 0.5)** for the `pop/happy` profile caused a
  real rank swap at positions 2 and 3:
  - At weight **2.0**: #2 was *Gym Hero* (2.87, pop but *intense* mood), #3 was
    *Rooftop Lights* (2.46, *indie pop* but *happy* mood).
  - At weight **0.5**: *Rooftop Lights* rose to **#2** while *Gym Hero* dropped to
    **#3** (1.37). *Sunrise City* stayed #1 both times because it matches all three.
  - **Takeaway:** when genre counted less, a song matching on *mood + energy* beat
    a song matching only on *genre + energy* — showing the genre weight was the
    single factor deciding the middle of the ranking.
- **Different user types:** a `pop/happy` user gets a clear, confident top pick,
  but a `jazz/relaxed` user has only one real candidate in the catalog, so the
  rest of the list falls back to weak energy-only matches.
- **Energy sensitivity:** because energy contributes at most 1 point, two songs
  with the same genre but very different energy still rank close together —
  suggesting energy could use more weight.

---

## Limitations and Risks

- Works on a **tiny 10-song catalog**, so some genres have only one option.
- **Ignores** tempo, valence, and danceability even though the data has them.
- Does **not understand lyrics or language**, and whole genres (hip-hop, classical,
  country, most non-Western music) are missing.
- **Over-favors genre** because it carries the highest weight, so a genre match can
  win even when the mood is wrong.
- Has **no sense of popularity or novelty** and can't help a user who can't describe
  their taste (the cold-start problem).

See [`model_card.md`](model_card.md) for a deeper discussion.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Building this made it clear that a recommender is really just a **scoring rule
applied consistently** across a catalog. Each song is turned into a number by
adding up points for the things the user cares about, and "predicting" what they'll
like is just sorting by that number. There's no magic — the intelligence lives
entirely in *which* features you choose to weight and *how much*.

The bias question became concrete once I saw how much the genre weight dominated.
If the catalog leans toward one kind of music, or the weights favor one feature,
users with other tastes quietly get worse recommendations even though no one
intended it. Real apps make these same weighting decisions at massive scale, which
is exactly where unfairness can creep in — a system can feel neutral while
systematically under-serving whoever the data and weights don't represent.



