# 🤖 JARVIS Face Detector

Real-time face detection system with a JARVIS-inspired HUD overlay built using Python and OpenCV.

## 📸 Demo
<!-- Add screenshot here after taking one -->
![Demo](assets/screenshot.png)

## ✨ Features
- Real-time face detection using Haar Cascade classifier
- Animated HUD corner brackets around detected faces
- Scanning line animation over detected face
- Concentric circle scanner overlay
- FPS counter display
- Automatic video recording to output folder

## 🛠️ Tech Stack
- Python 3.x
- OpenCV
- NumPy

## ⚙️ Setup & Run

```bash
pip install -r requirements.txt
python jarvis.py
```

Press `Q` to quit. Output saved to `output/jarvis_demo.mp4`.

## 📁 Project Structure
```
jarvis-face-detector/
├── jarvis.ipynb       # Jupyter notebook (development)
├── jarvis.py          # Main Python script
├── requirements.txt   # Dependencies
├── assets/            # Screenshots and demo GIFs
└── output/            # Recorded video output (gitignored)
```
