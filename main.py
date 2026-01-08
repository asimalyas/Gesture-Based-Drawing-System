# =========================================================
# STEP 1: IMPORT REQUIRED LIBRARIES
# =========================================================
import cv2
import mediapipe as mp
import numpy as np
import math


# =========================================================
# STEP 2: INITIALIZE HAND TRACKING & CAMERA
# =========================================================

# Initialize MediaPipe Hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# Drawing utilities
mp_draw = mp.solutions.drawing_utils

# Open webcam
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# Canvas for drawing
canvas = None

# Default drawing settings
draw_color = (255, 0, 0)      # Blue color
brush_thickness = 10
eraser_thickness = 50
prev_x, prev_y = 0, 0


# =========================================================
# STEP 3: HELPER FUNCTIONS
# =========================================================

def dist(p1, p2):
    """
    Calculate Euclidean distance between two points.
    Used to detect drawing gesture (thumb + index finger).
    """
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])


# =========================================================
# STEP 4: MAIN LOOP (FRAME PROCESSING & UI)
# =========================================================
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip for mirror effect
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    # Create canvas if not initialized or resized
    if canvas is None or canvas.shape[:2] != (h, w):
        canvas = np.zeros((h, w, 3), dtype=np.uint8)

    # Convert frame to RGB for MediaPipe
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    # ---------------- TOP COLOR SELECTION BAR ----------------
    cv2.rectangle(frame, (0, 0), (w, 100), (40, 40, 40), -1)

    # Color buttons (x1, y1, x2, y2) and their colors
    color_boxes = [
        ((50, 20, 140, 80), (255, 0, 0)),     # Blue
        ((160, 20, 250, 80), (0, 255, 0)),    # Green
        ((270, 20, 360, 80), (0, 0, 255)),    # Red
        ((380, 20, 470, 80), (0, 255, 255)),  # Yellow
        ((490, 20, 600, 80), (0, 0, 0))       # Eraser
    ]

    # Draw color buttons
    for box, col in color_boxes:
        cv2.rectangle(frame, (box[0], box[1]), (box[2], box[3]), col, -1)
        if draw_color == col:
            cv2.rectangle(frame, (box[0], box[1]), (box[2], box[3]), (255, 255, 255), 3)

    cv2.putText(frame, "CLEAR", (505, 55),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    # ---------------- RIGHT SIDEBAR STATUS ----------------
    cv2.putText(frame, "Selected:", (1120, 130),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    cv2.rectangle(frame, (1120, 140), (1240, 260), (255, 255, 255), 3)
    cv2.rectangle(frame, (1120, 140), (1240, 260), draw_color, -1)

    if draw_color == (0, 0, 0):
        cv2.putText(frame, "Eraser", (1140, 210),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)


# =========================================================
# STEP 5: HAND GESTURE LOGIC & DRAWING
# =========================================================
    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            lm = hand.landmark

            # Index and Thumb finger tips
            ix, iy = int(lm[8].x * w), int(lm[8].y * h)
            tx, ty = int(lm[4].x * w), int(lm[4].y * h)

            # Color selection when hand is in top bar
            if iy < 100:
                for box, col in color_boxes:
                    if box[0] < ix < box[2]:
                        draw_color = col
                        prev_x, prev_y = 0, 0

            # Drawing when fingers are close
            elif dist((ix, iy), (tx, ty)) < 40:
                if prev_x == 0:
                    prev_x, prev_y = ix, iy

                thickness = eraser_thickness if draw_color == (0, 0, 0) else brush_thickness
                cv2.line(canvas, (prev_x, prev_y), (ix, iy), draw_color, thickness)
                prev_x, prev_y = ix, iy

            else:
                prev_x, prev_y = 0, 0

            mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)


# =========================================================
# STEP 6: MERGE CANVAS & HANDLE CONTROLS
# =========================================================
    gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(gray, 20, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    frame_bg = cv2.bitwise_and(frame, frame, mask=mask_inv)
    canvas_fg = cv2.bitwise_and(canvas, canvas, mask=mask)
    frame = cv2.add(frame_bg, canvas_fg)

    cv2.putText(frame, "Press 'c' to Clear Canvas | 'q' to Quit",
                (10, h - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                (200, 200, 200), 2)

    cv2.imshow("Air Canvas Pro", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    if key == ord('c'):
        canvas = np.zeros((h, w, 3), dtype=np.uint8)


# =========================================================
# CLEANUP
# =========================================================
cap.release()
cv2.destroyAllWindows()
