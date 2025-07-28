# 🔼 Higher or Lower – Python Game

A terminal-based **"Higher or Lower"** game built with Python. In this game, the player is shown two famous people, each with a short description and a hidden popularity score (simulated by follower count). The player must guess which person is **more popular**. The game continues until the player makes a wrong choice or all comparisons are exhausted.

---

## 🧠 How It Works

- A dictionary stores:
  - Name of the person  
  - A short description  
  - Simulated "follower count" (popularity score)
  
- On each turn, two different people are randomly chosen for comparison.
- The player picks the more popular one by entering `1` or `2`.
- If correct, the score increases and the less popular person is removed from future rounds.
- If incorrect, the game ends and the final score is displayed.

---


