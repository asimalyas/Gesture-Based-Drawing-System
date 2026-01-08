# 🎨 Gesture-Based Drawing System 

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue.svg">
  <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-green">
  <img src="https://img.shields.io/badge/MediaPipe-Hand%20Tracking-orange">
  <img src="https://img.shields.io/badge/Status-Active-success">
</p>

<p align="center">
  ✋ Draw in the air • 🎨 Change colors • 🧽 Erase with gestures  
</p>

---

## ✨ Overview

**Gesture-Based Drawing System** is a real-time computer vision application that allows users to draw on the screen using **hand gestures only**, without touching a mouse, keyboard, or screen.

The system uses a webcam to track hand movements and converts finger gestures into smooth digital drawings using **OpenCV** and **MediaPipe**.

> 🚀 No touch. No mouse. Just Computer Vision.

---

## 🚀 Features

✔️ Real-time hand tracking via webcam  
✔️ Gesture-based drawing using index finger  
✔️ Virtual color palette (UI bar)  
✔️ Eraser mode using hand gestures  
✔️ Adjustable brush & eraser thickness  
✔️ Live color preview sidebar  
✔️ Smooth and responsive drawing experience  

---

## 🧠 How It Works

1. Webcam captures live video frames  
2. MediaPipe detects hand landmarks  
3. Distance between thumb & index finger is calculated  
4. Finger movement is mapped to drawing strokes  
5. Virtual canvas is merged with live video feed  

---

## 🛠️ Tech Stack

| Technology | Description |
|----------|------------|
| Python | Core programming language |
| OpenCV | Image processing & rendering |
| MediaPipe | Hand landmark detection |
| NumPy | Matrix & array operations |
| Math | Distance calculations |

---

## 📂 Project Structure

Gesture-Based-Drawing-System/
│
├── main.py # Main application logic
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── .gitattributes



### 🎮 How to Use
🖐️ Wait for the webcam to initialize
✍️ Use index finger to draw in the air
🎨 Move finger to the top bar to change colors
🧽 Select black color to erase
⌨️ Press C to clear the canvas
❌ Press Q to quit the application

### 📸 Demo
🎥 You can add a demo GIF or video here for better visualization
(Recommended for higher GitHub engagement)

### 🔮 Future Enhancements
Undo / Redo gesture support

Save drawings as image files

Multi-hand drawing support

Shape & symbol recognition

AI-based handwriting detection

### 👨‍💻 Author
Muhammad Asim Ilyas
🎓 Software Engineering Student
💻 Python | Computer Vision | AI
📍 Pakistan

🔗 GitHub: https://github.com/asimalyas
📸 Instagram: @code_with_asim
