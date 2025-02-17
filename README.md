# RoadSafe 🚗

RoadSafe is a computer vision model that can detect vehicular accidents in real-time using CCTV footage and automatically alerts authorities to reduce emergency response times.

## 🎯 Features

- Real-time accident detection with 89% accuracy
- Automatic emergency services notification via Twilio API
- Web-based accident logging interface
- Confidence threshold management to minimize false positives
- Visual monitoring interface with detection status

## 🛠️ Technology Stack

- **Computer Vision**: OpenCV
- **Machine Learning**: TensorFlow, Keras
- **API Integration**: Twilio
- **Frontend**: HTML, CSS
- **Backend**: Python
- **Data Processing**: NumPy

## 📋 Prerequisites

- Python 3.7+
- TensorFlow 2.x
- OpenCV
- Twilio Account
- Required Python packages (see Installation)
- Jupyter Notebook (for model training)

## ⚙️ Installation & Setup

1. Clone the repository:
```
git clone https://github.com/sidtum/RoadSafe.git
cd RoadSafe
```

2. Install required packages:
```
pip install tensorflow opencv-python twilio numpy jupyter
```

3. Download the dataset:
   - Access the dataset from [Kaggle - Accident Detection from CCTV Footage](https://www.kaggle.com/datasets/ckay16/accident-detection-from-cctv-footage/code)
   - Place the dataset in the project directory

4. Generate the model files:
   - Run the `road-accident-detection.ipynb` Jupyter notebook
   - This will create two required files:
     - `model.json`
     - `model_weights.h5`

5. Prepare video footage:
   - Obtain an MP4 file containing car crash footage
   - Update the video path in `crashDetector.py`:
     ```python
     video = cv2.VideoCapture("path/to/your/video.mp4")
     ```

6. Configure Twilio credentials in crashDetector.py:
```
account_sid = "your_account_sid"
auth_token = "your_auth_token"
```

## 🚀 Usage

1. Run the main detection script:
```
python crashDetector.py
```

2. The system will:
- Process CCTV footage in real-time
- Display detection status with confidence levels
- Call authorities when accidents are detected with high confidence (>94%)
- Log all incidents to a web interface

## 💡 How It Works

The system operates in several key steps:

1. **Video Processing**: Continuously processes frames from CCTV footage using OpenCV
2. **Accident Detection**: Analyzes frames using a trained TensorFlow model
3. **Alert System**: 
   - Triggers when detection confidence exceeds 86.5%
   - Alerts authorities when confidence exceeds 94%
4. **Incident Logging**: Records all detected accidents with timestamps in a web interface

## 📊 Performance Metrics

- Detection Accuracy: 89%
- Emergency Response Time Improvement: 18%
- False Positive Rate: <5%

## 🌐 Web Interface

The system includes a web-based dashboard that:
- Displays a log of all detected accidents
- Shows timestamp information
- Provides a clean, responsive interface
- Maintains a historical record of incidents
