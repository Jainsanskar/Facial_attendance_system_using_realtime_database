# 🎓 Real-Time Face Attendance System

An AI-powered real-time face recognition attendance system using Python, OpenCV, and Firebase. This project captures live webcam feed, detects and recognizes student faces, and updates attendance in the Firebase Realtime Database and Storage.

## 📸 Demo Preview

![Demo Screenshot](Resources/demo_screenshot.png)  
*Sample interface showing recognized student details and real-time UI*

---

## 📌 Features

- Real-time face detection and recognition using webcam
- Attendance logging only after a 2-minute gap to prevent duplicates
- Student images and information stored in Firebase Storage and Realtime Database
- Displays personalized student info (name, major, year, photo, etc.)
- Encodes facial features and stores locally (`EncodeFile.p`)
- Automatic face data upload to Firebase during encoding

---

## 🛠️ Tech Stack

| Technology       | Purpose                         |
|------------------|----------------------------------|
| Python           | Core programming language        |
| OpenCV           | Image capture and processing     |
| face_recognition | Face encoding and matching       |
| Firebase         | Database and cloud storage       |
| cvzone           | Enhanced UI elements in OpenCV   |
| NumPy            | Numerical operations             |
| Pickle           | Data serialization for encodings |

---

## 🧩 Folder Structure

```
.
├── Images/                    # Student face images
├── Resources/                 # UI assets (background, mode screens)
├── EncodeFile.p              # Pickled face encodings with IDs
├── serviceAccountKey.json    # Firebase Admin SDK credentials
├── main.py                   # Real-time face recognition and attendance
├── Encodegenerator.py        # Encode faces and upload to Firebase
├── addDataToDatabase.py      # Add student info to Firebase
└── README.md                 # Project documentation
```

---

## 🚀 Getting Started

### 🔧 Prerequisites

Install required Python packages:

```bash
pip install opencv-python face_recognition firebase-admin numpy cvzone
```

> **Note:** `dlib` is a dependency for `face_recognition`. Install it via wheel if needed on Windows.

### 🔑 Firebase Setup

1. Create a Firebase project.
2. Enable:
   - Realtime Database
   - Cloud Storage
3. Generate and download `serviceAccountKey.json`.
4. Replace `"serviceAccountKey.json"` in the repo with yours.

---

## 🧪 Running the Project

### 1. Add Student Data

- Place student face images in the `Images/` folder.
- Filenames must match student IDs, e.g., `12345.png`.

### 2. Encode Images

```bash
python Encodegenerator.py
```

- Encodes images and saves `EncodeFile.p`
- Uploads face images to Firebase Storage

### 3. Add Student Info

Edit `addDataToDatabase.py` and run:

```bash
python addDataToDatabase.py
```

- Adds metadata (name, major, year, etc.) in Firebase

### 4. Run Face Attendance App

```bash
python main.py
```

- Opens webcam and GUI
- Recognizes students and updates attendance

---

## 🔐 Attendance Logic

- Students are recognized if face match is found
- Attendance is updated only if:
  - Recognized
  - More than 120 seconds have passed since last update
- Attendance count and timestamp are stored in Firebase

---

## 📷 UI Screens

- `background.png` – Base layout for GUI
- `Modes/` – Contains different interface overlays for:
  - Default screen
  - Loading
  - Attendance success
  - Already marked

---

## 📈 Example Student Info Format

Stored under `Students/<id>` in Firebase:

```json
{
  "name": "Dr. Devesh Kumar Lal",
  "major": "Big Data",
  "starting_year": 2020,
  "total_attendance": 31,
  "standing": "G",
  "year": 3,
  "last_attendance_time": "2023-04-01 12:40:00"
}
```

---

## 💡 Future Improvements

- Add multiple images per student for more robust matching
- Admin panel for student management
- Email/SMS notifications
- Web-based dashboard for attendance stats
- Add audio/voice feedback

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Please feel free to fork this repository and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙋‍♂️ Author

**Sanskar Jain**  
[GitHub](https://github.com/yourusername) | [LinkedIn](https://linkedin.com/in/yourprofile)
