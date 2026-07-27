# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

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

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



