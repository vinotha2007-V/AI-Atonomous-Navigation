import cv2
from perception import detect_obstacles
from planning import plan_path
from control import control_robot

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    obstacles = detect_obstacles(frame)
    
    direction = plan_path(obstacles, frame.shape[1])
    
    control_robot(direction)
    
    # Draw obstacles
    for (x, y, w, h) in obstacles:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2)
    
    cv2.putText(frame, direction, (20,50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
    
    cv2.imshow("Autonomous Navigation", frame)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
