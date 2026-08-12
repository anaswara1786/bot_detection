# A Multimodal AI Systems for Web Bot, Botnet, and Automated Interaction Detection

A machine learning system that detects bots by analyzing user behavior, browsing patterns, and network activity - eliminating the need for CAPTCHAs.

## ✨ What It Does

Instead of asking users to solve puzzles, our system silently monitors three layers of behavior:

Network Layer - Analyzes traffic patterns
Browser Layer - Examines HTTP request behavior
Behavioral Layer - Tracks mouse movement patterns

Each layer classifies traffic as Human or Bot using machine learning models (Random Forest + SVM).

## 📊 Results

### Layer	Model	Accuracy
Network	Random Forest              :98.57%
Browser	RF + SVM Ensemble	         :86.76%
Behavioral	RF + SVM Ensemble      :96.37%
🚀 Quick Start
Install Dependencies
bash
pip install -r requirements.txt
Run the Demo
bash
python demo_backend_production.py
# Open http://localhost:5000/demo.html
Interactive Demo Features
Real-time mouse tracking
Live detection results (Human/Bot)
Bot simulator for testing
Visual statistics
🛠️ Technology Stack
Python - Core language
scikit-learn - ML models (Random Forest, SVM)
Flask - Backend API
JavaScript - Frontend tracking
Selenium - Bot simulation
📁 Project Structure
bot-detection/
├── backend/
│   ├── demo_backend_production.py    # Main API server
│   └── models/                        # Pre-trained ML models
├── frontend/
│   ├── demo.html                      # Interactive demo
│   └── weblog_demo.html               # Browser behavior scenarios
├── simulators/
│   ├── bot_simulator_with_results.py # Mouse bot tester
│   └── weblog_simulator.py            # HTTP request simulator
├── datasets/
│   └── mouse_dataset_full.csv        # Training data
└── models/
    ├── network_model.pkl              # 98.57% accuracy
    ├── bot_detection_corrected.pkl   # 86.76% accuracy
    └── mouse_model_balanced.pkl      # 96.37% accuracy
🎯 How It Works
Data Collection
Collect mouse movements, HTTP requests, network flows
Extract features (velocity, pauses, request patterns, etc.)
Feature Analysis
Network: 7 features (packet counts, flow duration, etc.)
Browser: 11 features (request types, error rates, etc.)
Behavioral: 33 features (velocity, acceleration, pauses, etc.)
Classification
Random Forest and SVM models analyze features
Each layer votes: Human or Bot
Router combines results for final decision
Result
Probability Score (0-1): How likely is a bot?
Prediction: HUMAN or BOT
Confidence: HIGH, MEDIUM, or LOW
💡 Key Innovation

SMOTE Data Augmentation:

Original mouse dataset was imbalanced (502 humans vs 2,528 bots)
Applied SMOTE to create synthetic human samples
Result: Improved human detection from 75% to 95.4%
🎮 Try the Demo
bash
# Start server
python demo_backend_production.py

# The demo includes:
# 1. Mouse Tracking Interface
#    - Move your mouse naturally
#    - System detects if you're human or bot
#
# 2. Bot Simulator
#    - Shows how bots move (linear, fast, no pauses)
#    - System correctly identifies as bot
#
# 3. Browser Behavior Scenarios
#    - Normal browsing vs aggressive scraping
#    - System distinguishes patterns
📈 Performance
Average Latency: 47ms (invisible to users)
Throughput: 500-1000 requests/second
False Positive Rate: 8% (at optimized threshold)
Defense in Depth: Bot must fool all 3 layers
🔧 API Usage
python
import requests

# Mouse detection
data = {
    "avg_speed": 150,
    "max_speed": 300,
    "distance": 2000,
    "pauses": 8,
    "duration": 12.5,
    "clicks": 5
}

response = requests.post('http://localhost:5000/detect_mouse', json=data)
result = response.json()

print(result['prediction'])        # 'HUMAN' or 'BOT'
print(result['bot_probability'])   # 0.00-1.00
print(result['confidence'])        # 'HIGH', 'MEDIUM', 'LOW'
📚 Models Included

Pre-trained models are ready to use:

network_model.pkl - Network layer (254K training samples)
bot_detection_corrected.pkl - Browser layer (12K training samples)
mouse_model_balanced.pkl - Behavioral layer (5K balanced samples)

No training required - just run the demo!

✅ Features
✅ Three-layer detection system
✅ Real-time mouse tracking
✅ Interactive demo with visualization
✅ Bot simulator for testing
✅ Sub-50ms response time
✅ Production-ready code
✅ Pre-trained models included
🐛 Troubleshooting

Server won't start?

bash
# Make sure port 5000 is free
lsof -i :5000

# Or change port in code

Models not loading?

bash
# Verify models exist
ls -la models/

# Re-install dependencies
pip install --upgrade scikit-learn

Demo page not loading?

bash
# Check server is running
curl http://localhost:5000/health
📖 Learn More
See detailed documentation in /docs folder
Check VIVA_QUESTIONS_ANSWERS.md for deep dive
Read PROJECT_COMPLETE_SUMMARY.md for full project walkthrough
📄 License

MIT License - feel free to use and modify

👤 Author

Your Name | GitHub | Email

Made to eliminate CAPTCHAs and improve user experience ✨
