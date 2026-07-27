# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

**VibeMatch 1.0** — a small, rule-based music recommender.

---

## 2. Intended Use

VibeMatch recommends songs from a fixed catalog that best match a user's stated
taste. Given a profile (favorite genre, favorite mood, target energy level),
it ranks the catalog and returns the top few songs, each with a short
plain-language explanation of *why* it was chosen.

- **Recommendations:** an ordered top-K list of songs with a match score and reasons.
- **Assumptions:** the user can describe their taste as a genre, a mood, and an
  energy preference, and that those three signals are a reasonable proxy for what
  they want to hear right now.
- **Audience:** this is a **classroom / learning project**, not a production system.
  It exists to show how data + a scoring rule turn into ranked recommendations.

---

## 3. How the Model Works

Imagine giving each song a report card. For every thing you care about, the song
earns points:

- If the song's **genre** is your favorite, it gets **2 points** — genre is the
  strongest signal of taste, so it's weighted highest.
- If the song's **mood** matches yours, it gets **1.5 points**.
- For **energy**, the song earns up to **1 point** depending on how close its
  energy is to your target. A perfect match earns the full point; the further
  apart they are, the less it earns.
- (In the object-oriented version) if you say you **like acoustic** music, songs
  also get a bonus equal to how acoustic they are.

Every song is scored this way, then sorted from highest to lowest, and the top
few are shown. Alongside each pick, the system lists the reasons it earned points
("matches your pop taste, fits your happy mood…") so the recommendation is never
a black box.

**Changes from the starter logic:** the starter simply returned the first few
songs unsorted. I added the weighted scoring rule, real CSV loading, human-readable
explanations, and a fallback message for songs that match nothing ("a fresh pick
outside your usual preferences").

---

## 4. Data

The catalog is a small CSV, `data/songs.csv`, with **10 songs**.

- **Columns:** id, title, artist, genre, mood, energy, tempo_bpm, valence,
  danceability, acousticness.
- **Genres represented:** pop, indie pop, lofi, rock, ambient, jazz, synthwave.
- **Moods represented:** happy, chill, intense, relaxed, moody, focused.
- I did not add or remove songs — the dataset is the one provided.
- **Missing from the data:** language/lyrics, release year, artist popularity,
  and cultural context. Whole families of music (hip-hop, classical, country,
  most non-Western genres) are absent, so the catalog is narrow.

---

## 5. Strengths

- Works well for users whose taste lines up with a **well-represented genre**,
  like pop or lofi, where there are several candidates to rank.
- The scoring captures the intuitive idea that an **exact genre + mood + energy**
  match should clearly beat a partial one — the `pop/happy/0.8` profile puts
  *Sunrise City* (a pop, happy, 0.82-energy track) on top by a wide margin.
- Every recommendation comes with a **reason**, which makes the results easy to
  sanity-check and matches my intuition when I read them.

---

## 6. Limitations and Bias

- **Ignores most features:** tempo, valence, and danceability are in the data but
  don't affect the score. Two very different songs can tie.
- **Underrepresented tastes:** a user who loves a genre with only one song (e.g.
  jazz, rock) gets almost no real choice, and genres missing from the catalog
  can never be recommended at all.
- **Overfits to genre:** because genre is worth the most points, a strong genre
  match can dominate even when the mood is completely wrong.
- **Popularity blind spot:** the system has no notion of what's popular or new,
  so it can't surface trending music the way real apps do.
- **Cold start:** it assumes the user already knows their genre/mood/energy; it
  can't help someone who can't describe their taste.

---

## 7. Evaluation

- **Profiles tested:** the default `pop / happy / energy=0.8`, plus mental checks
  for `lofi / chill / low-energy` type users.
- **What I looked for:** does the most obvious match land at #1, do the scores
  fall off in a sensible order, and do the printed reasons actually explain the
  ranking.
- **Automated tests:** the OOP version is checked by `tests/test_recommender.py`
  (2/2 passing) — one test confirms the pop/happy song ranks first, the other
  confirms explanations are non-empty strings.
- **What surprised me:** how much the genre weight (2.0) dominates. Songs that
  matched only on energy scored under 1.0, so a single big-weight feature can
  effectively decide the whole ranking.

---

## 8. Future Work

- Use more of the data — factor in tempo, valence, and danceability.
- Add a **popularity / trending boost** so fresh hits can surface, like real apps.
- Add a small **exploration factor** so the top-K isn't always the same safe picks,
  improving diversity.
- Support **multiple favorite genres** and softer matching (e.g. "pop" is close to
  "indie pop") instead of exact-match only.
- Richer explanations that mention *how strong* each reason was.

---

## 9. Personal Reflection

I learned that a recommender is really just a scoring rule applied consistently
across a catalog — the "intelligence" lives in which features you weight and by
how much. The most interesting discovery was how a single heavily-weighted feature
(genre) can quietly dominate every result, which is exactly where bias sneaks in:
if the catalog or the weights favor one kind of music, users with other tastes get
worse recommendations without anyone intending it. It made me realize the polished
apps I use are making these same weighting choices on a massive scale.
