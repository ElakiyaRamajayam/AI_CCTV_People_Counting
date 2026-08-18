\# 🚀 AI CCTV People Counting \& Detection System



> An AI-powered CCTV surveillance and people-counting system built with \*\*YOLOv8\*\* and \*\*Python\*\*, designed for real-time detection, counting, and visual monitoring through image, video, and webcam inputs.



\## 📌 Overview



\*\*AI CCTV People Counting\*\* is an intelligent computer vision application that uses the YOLOv8 object detection model to identify and count people from different video sources.



The project provides a user-friendly interface for analyzing images, uploaded videos, and live webcam feeds, making it suitable for applications such as smart surveillance, crowd monitoring, occupancy analysis, and security systems.



\## ✨ Features



\* 🎯 Real-time person detection using YOLOv8

\* 👥 Automatic people counting

\* 🖼️ Image-based detection

\* 🎥 Video-based detection

\* 📹 Live webcam detection

\* 📊 Detection and monitoring dashboard

\* 🎨 Custom user interface

\* ⚙️ Configurable application settings

\* 📈 Detection results and reports

\* 🧩 Modular project architecture



\## 🛠️ Technologies Used



| Technology    | Purpose                               |

| ------------- | ------------------------------------- |

| \*\*Python\*\*    | Core programming language             |

| \*\*YOLOv8\*\*    | Object detection and people counting  |

| \*\*OpenCV\*\*    | Image and video processing            |

| \*\*Streamlit\*\* | Interactive web application interface |

| \*\*NumPy\*\*     | Numerical and array operations        |

| \*\*Pandas\*\*    | Data processing and analysis          |

| \*\*Pillow\*\*    | Image processing                      |



\## 🧠 How It Works



```text

Input Source

&#x20;    │

&#x20;    ├── Image

&#x20;    ├── Video

&#x20;    └── Webcam

&#x20;         │

&#x20;         ▼

&#x20;    YOLOv8 Model

&#x20;         │

&#x20;         ▼

&#x20;  Person Detection

&#x20;         │

&#x20;         ▼

&#x20;   People Counting

&#x20;         │

&#x20;         ▼

&#x20;Visualization \& Reports

```



\## 📂 Project Structure



```text

AI\_CCTV\_People\_Counting/

│

├── assets/                 # Images and application assets

├── components/             # Reusable UI components

├── models/                 # YOLO model-related code

├── styles/                 # Application styling and themes

├── utils/                  # Utility and video-processing functions

├── views/                  # Application pages and detection modules

│

├── app.py                  # Main application entry point

├── requirements.txt        # Python dependencies

├── yolov8n.pt              # YOLOv8 detection model

├── .gitignore              # Git ignored files

└── README.md               # Project documentation

```



\## ⚙️ Installation



\### 1. Clone the repository



```bash

git clone https://github.com/ElakiyaRamajayam/AI\_CCTV\_People\_Counting.git

cd AI\_CCTV\_People\_Counting

```



\### 2. Create a virtual environment



```bash

python -m venv venv

```



\### 3. Activate the virtual environment



\*\*Windows:\*\*



```bash

venv\\Scripts\\activate

```



\*\*Linux / macOS:\*\*



```bash

source venv/bin/activate

```



\### 4. Install dependencies



```bash

pip install -r requirements.txt

```



\## ▶️ Run the Application



Start the application with:



```bash

streamlit run app.py

```



Then open the local URL provided by Streamlit in your browser.



\## 📸 Application



The application provides different detection modes for analyzing:



\* 🖼️ Images

\* 🎥 Video files

\* 📹 Live webcam streams



You can add screenshots of the application here to showcase the interface and detection results.



\## 🤖 YOLOv8



This project uses \*\*YOLOv8\*\* for object detection and people counting.



The lightweight `yolov8n.pt` model is included in the repository for convenience.



The larger `yolov8x.pt` model is not included because of GitHub's file-size limitations.



\## 🎯 Use Cases



This system can be adapted for:



\* 🏢 Office occupancy monitoring

\* 🛍️ Retail store analytics

\* 🚪 Entry and exit monitoring

\* 🏫 Crowd monitoring

\* 🏭 Workplace safety monitoring

\* 🎥 Smart CCTV systems

\* 📊 People-flow analysis



\## 🔮 Future Improvements



Potential improvements include:



\* \[ ] Multi-camera CCTV support

\* \[ ] Real-time alerts and notifications

\* \[ ] Advanced crowd-density analysis

\* \[ ] Person tracking across frames

\* \[ ] Database integration

\* \[ ] Historical analytics

\* \[ ] Cloud deployment

\* \[ ] Automated report generation

\* \[ ] Improved model accuracy



\## 📋 Requirements



\* Python 3.x

\* Webcam (for live detection)

\* Windows / Linux / macOS

\* Internet connection for installing dependencies



\## 👩‍💻 Author



\*\*Elakiya Ramajayam\*\*



Developed as an AI/computer-vision project focused on intelligent CCTV monitoring, object detection, and people counting.



\---



⭐ \*\*If you find this project useful, consider giving it a star on GitHub!\*\*



