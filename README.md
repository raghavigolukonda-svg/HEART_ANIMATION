# ❤️ Python Turtle Heart Curve Animation

This project draws a **heart shape using Python Turtle graphics** and a bit of **mathematics**.  
It is more than just a drawing — it combines programming, math, and creativity to show:  
**"When a programmer falls in love ❤"**

---

## 🔍 How It Works (Deeper Explanation)

1. **Mathematical Heart Equation**  
   The heart shape is generated using a famous set of parametric equations:
   - **x(t) = 16 * (sin(t))³**
   - **y(t) = 13cos(t) – 5cos(2t) – 2cos(3t) – cos(4t)**  

   These equations define the geometry of a heart.  
   By scaling (`× 10`) and plotting each `(x, y)` point, Turtle traces the entire curve.

2. **Turtle Graphics Setup**  
   - The canvas is set to **600×600** pixels with a black background.  
   - A red pen (`pensize=2`) is used to draw and fill the heart.  
   - Turtle goes point by point, following the parametric curve.

3. **Text Message**  
   After drawing, Turtle writes a message at the center:  
   *“When a programmer falls in love ❤”* in white text.

4. **Loop Execution**  
   - The program iterates `t` from `0` to `2π` in small steps (`0.01`).  
   - Each step calculates `(x, y)` and moves the Turtle to that point.  
   - Filling begins and ends, producing a **solid red heart**.

---

## 🚀 Features
- Uses **pure Python**, no external dependencies.  
- Combines **math + graphics** to generate a smooth heart curve.  
- Adds a **custom romantic message** at the center.  
- Clean black background for contrast.

---

## 🛠️ Tech Stack
- **Language**: Python 3.x  
- **Libraries**:  
  - `turtle` (for graphics, built-in in Python)  
  - `math` (for sine & cosine functions)

---

