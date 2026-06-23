import cv2
import time

def draw_hud(frame, x, y, w, h):
    color = (255, 255, 0)
    thickness = 2
    line = 30
    cv2.line(frame, (x, y), (x+line, y), color, thickness)
    cv2.line(frame, (x, y), (x, y+line), color, thickness)
    cv2.line(frame, (x+w, y), (x+w-line, y), color, thickness)
    cv2.line(frame, (x+w, y), (x+w, y+line), color, thickness)
    cv2.line(frame, (x, y+h), (x+line, y+h), color, thickness)
    cv2.line(frame, (x, y+h), (x, y+h-line), color, thickness)
    cv2.line(frame, (x+w, y+h), (x+w-line, y+h), color, thickness)
    cv2.line(frame, (x+w, y+h), (x+w, y+h-line), color, thickness)

def draw_scanner(frame, x, y, w, h):
    cx, cy = x + w // 2, y + h // 2
    cv2.circle(frame, (cx, cy), int(w/3), (255, 255, 0), 2)
    cv2.circle(frame, (cx, cy), int(w/5), (255, 255, 0), 1)
    cv2.circle(frame, (cx, cy), 4, (0, 255, 255), -1)
    cv2.line(frame, (cx-20, cy), (cx+20, cy), (0, 255, 255), 1)
    cv2.line(frame, (cx, cy-20), (cx, cy+20), (0, 255, 255), 1)

def draw_text(frame, x, y, w, h):
    cv2.putText(frame, "CONFIDENCE : 99%", (x-20, y-60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,0), 2)
    cv2.putText(frame, "TARGET LOCKED", (x-20, y-30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)
    cv2.putText(frame, "WELCOME BACK ANKIT", (50, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,255), 2)
    cv2.putText(frame, "STATUS : ONLINE", (x+w+20, y+20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,0), 1)
    cv2.putText(frame, "TRACKING : ACTIVE", (x+w+20, y+45), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,0), 1)
    cv2.putText(frame, "THREAT : LOW", (x+w+20, y+70), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,0), 1)

def main():
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )
    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('output/jarvis_demo.mp4', fourcc, 20, (640, 480))
    scan_offset = 0
    prev_time = time.time()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Camera Error")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        cv2.putText(frame, "JARVIS ONLINE", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,0), 2)

        for (x, y, w, h) in faces:
            draw_hud(frame, x, y, w, h)
            draw_text(frame, x, y, w, h)
            draw_scanner(frame, x, y, w, h)
            scan_offset = (scan_offset + 5) % h
            cv2.line(frame, (x, y+scan_offset), (x+w, y+scan_offset), (0,255,255), 2)

        current_time = time.time()
        fps = int(1 / (current_time - prev_time + 1e-9))
        prev_time = current_time
        cv2.putText(frame, f"FPS : {fps}", (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)

        out.write(frame)
        cv2.imshow("JARVIS FACE DETECTOR", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()