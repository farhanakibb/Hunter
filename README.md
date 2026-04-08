# 🎯 DUCK HUNT — Pygame

> A classic Duck Hunt-style shooting game built with Python and Pygame.
> Move your scope, aim, and shoot birds flying across the screen!

---

## 🎮 About

A fun shooting game inspired by the classic Duck Hunt (Nintendo, 1984), recreated in Python using the Pygame library. 3 birds fly across the field with different movement patterns — catch them all!

---

## 🚀 Getting Started

### Prerequisites

```bash
pip install pygame
```

### Folder Structure

```
duck-hunt/
│
├── main.py
└── pic/
    ├── field5.jpg
    ├── scope.webp
    ├── bird-removebg-preview.png
    ├── bird2-removebg-preview.png
    ├── bird3-removebg-preview.png
    └── blood-removebg-preview.png
```

### Run the Game

```bash
python main.py
```

---

## 🕹️ Controls

| Action | Input        |
|--------|-------------|
| Aim    | Move Mouse  |
| Shoot  | Left Click  |
| Quit   | Close Window |

---

## ✨ Features

- ✅ 3 birds with unique movement patterns
- ✅ Animated scope that reacts to clicking
- ✅ Blood splat effect on successful hit
- ✅ Kill counter tracking
- ✅ Scrolling background field
- ✅ 60 FPS smooth gameplay

---

## 🔧 Known Issues / Future Plans

- [ ] Add kill count display on screen
- [ ] Fix bird respawn after being shot
- [ ] Add gunshot & bird sound effects
- [ ] Add a timer / round system
- [ ] Improve hitbox accuracy with `pygame.Rect`
- [ ] Refactor birds into a class / list

---

## 🛠️ Built With

| Tech     | Purpose               |
|----------|-----------------------|
| Python 3 | Core language         |
| Pygame   | Game engine & rendering |

---

## 📄 License

Open source and free to use for learning purposes.

---

## 🙌 Acknowledgements

Inspired by the classic **Duck Hunt** game originally developed by Nintendo (1984).

---

*Made with ❤️ using Python & Pygame · Have fun & keep hunting! 🦆🎯*
