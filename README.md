# Flashcard Quiz App

A colorful, interactive flashcard quiz application built with pure HTML, CSS, and JavaScript — no frameworks, no build tools. Just open `index.html` in any browser and start studying.

---

## Live Preview

> Open `index.html` directly in your browser. No server or installation required.

---

## Features

### Core Quiz Features
- **3D Card Flip** — Click the card or the "Show Answer" button to reveal the answer with a smooth flip animation
- **Navigation** — Move between cards using Previous / Next buttons or clickable dot indicators
- **Keyboard Shortcuts** — `←` / `→` to navigate, `Space` or `Enter` to flip
- **Auto-advance** — After marking a card, the app automatically moves to the next one

### Score & Result Tracking
- **Got it / Missed buttons** — Appear after flipping each card so you can self-assess
- **Live stats** — Streak, Correct count, and Missed count update in real time in the header
- **Result Summary Modal** — Appears automatically once all cards are judged, showing:
  - Animated score ring (conic-gradient circle) with your percentage
  - Trophy emoji and motivational message based on your score
  - Tally chips for Correct, Missed, and Skipped
  - Full card review list (missed cards first, then correct)
- **Restart All Cards** — Resets the full 20-card deck to start fresh
- **Retry Missed Cards** — Loads only the cards you got wrong for a focused second attempt
- **Perfect Score Confetti** — Extra confetti burst when you hit 100%

### Card Management (CRUD)
- **Add Cards** — Inline form to create new flashcards with a question and answer
- **Edit Cards** — Click the pencil icon on any card in the list to pre-fill and update it
- **Delete Cards** — Click the trash icon with a confirmation prompt before removing
- **Persistent Storage** — All cards are saved to `localStorage` and survive page refresh

### Visual & UX Design
- **Animated pastel background** — Lavender → violet → sky → mint gradient that slowly loops
- **Floating blur blobs** — Three soft-colored blobs float in the background for depth
- **Rainbow stripe** — Animated full-spectrum stripe runs across the top of the card panel
- **Per-card gradient** — Each flashcard gets its own color gradient (purple, pink, teal, gold…)
- **Card emoji** — A rotating emoji appears on each question face (🤔 💭 🧠 🎯…)
- **Confetti burst** — 80 pastel confetti pieces explode every time an answer is revealed
- **Dot indicators** — Color-coded per card: 🟣 Current · 🟢 Correct · 🔴 Missed · ⚪ Unseen
- **Streak counter** — Tracks consecutive correct answers
- **Wiggle hover effect** — Card subtly wiggles on hover before flipping
- **Toast notifications** — Brief feedback messages on add, update, delete, and marking

---

## Default Flashcards (20 Cards)

The app ships with 20 pre-loaded questions across 5 categories:

| # | Category | Question |
|---|---|---|
| 1 | General Knowledge | What is the capital of France? |
| 2 | General Knowledge | Which planet is known as the Red Planet? |
| 3 | General Knowledge | How many continents are there on Earth? |
| 4 | General Knowledge | What is the largest ocean in the world? |
| 5 | General Knowledge | Who painted the Mona Lisa? |
| 6 | Mathematics | What is 7 × 8? |
| 7 | Mathematics | What is the value of π to 2 decimal places? |
| 8 | Mathematics | What is the square root of 144? |
| 9 | Mathematics | How many sides does a hexagon have? |
| 10 | Mathematics | What is 15% of 200? |
| 11 | Science | What does HTML stand for? |
| 12 | Science | What is the powerhouse of the cell? |
| 13 | Science | What gas do plants absorb from the atmosphere? |
| 14 | Science | What is the chemical symbol for Gold? |
| 15 | Science | How many bones are in the adult human body? |
| 16 | Literature & History | Who wrote "Romeo and Juliet"? |
| 17 | Literature & History | In which year did World War II end? |
| 18 | Literature & History | Who was the first person to walk on the Moon? |
| 19 | Technology | What does CPU stand for? |
| 20 | Technology | What programming language is known as the language of the web? |

---

## How to Use

### Studying
1. Open `index.html` in your browser
2. Read the question on the card
3. Click the card or press **Space** to flip and see the answer
4. Click **Got it!** if you knew it, or **Missed** if you didn't
5. The app auto-advances to the next card
6. After all 20 cards, the **Result Summary** modal appears

### Result Summary
- View your score percentage, correct count, missed count, and skipped count
- Read through the review list to revisit what you missed
- Click **Restart All Cards** to go again from the beginning
- Click **Retry Missed Cards** to focus only on the ones you got wrong

### Managing Cards
1. Scroll down to the **Manage Cards** panel
2. Click **+ Add Card** to open the form
3. Fill in the Question and Answer fields, then click **Save**
4. Use the ✏️ button to edit any existing card
5. Use the 🗑️ button to delete a card (with confirmation)

### Keyboard Shortcuts
| Key | Action |
|---|---|
| `←` Arrow | Previous card |
| `→` Arrow | Next card |
| `Space` | Flip card |
| `Enter` | Flip card |

---

## Score Grading

| Score | Trophy | Message |
|---|---|---|
| 100% | 🏆 | Perfect Score! Outstanding! |
| 80–99% | 🥇 | Excellent! Almost there! |
| 60–79% | 🥈 | Good Effort! Keep practising! |
| 40–59% | 🥉 | Keep Going! You're making progress! |
| 0–39% | 📚 | Need More Study! Review and try again! |

---

## Tech Stack

| Technology | Usage |
|---|---|
| HTML5 | Page structure and semantic markup |
| CSS3 | Animations, gradients, glassmorphism, responsive layout |
| Vanilla JavaScript | App logic, state management, DOM manipulation |
| localStorage | Persistent card storage across sessions |
| Canvas API | Confetti animation |

No external libraries, frameworks, or build tools are used.

---

## Project Structure

```
CodeALpha_Flashcard_Quiz_App/
├── index.html      # Complete app (HTML + CSS + JS in one file)
└── README.md       # Project documentation
```

---

## Getting Started

```bash
# Clone the repository
git clone https://github.com/RubaiyaKamal/CodeALpha_Flashcard_Quiz_App.git

# Navigate into the folder
cd CodeALpha_Flashcard_Quiz_App

# Open in browser (Windows)
start index.html

# Open in browser (Mac)
open index.html

# Open in browser (Linux)
xdg-open index.html
```

Or simply double-click `index.html` in your file explorer.

---

## Screenshots

> The app features a colorful animated pastel background, bubbly pill-shaped buttons, per-card gradient flashcards, dot progress indicators, and a full result summary modal with a score ring.

---

## Author

**Rubaiya Kamal**
Internship Project — CodeAlpha (Month 2)

---

## License

This project is open source and available under the [MIT License](LICENSE).
