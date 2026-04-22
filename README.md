<div align="center">
  <img src="photos/teamlogo%20.jpeg" alt="TechMedics 108+ Logo" width="140" height="auto" />

  <h1>🚑 LifeLine 108+</h1>
  <h3><em>Bridging the Gap: From Panic to Precision</em></h3>

  <p>
    <img src="https://img.shields.io/badge/Google_Solution_Challenge-2026-4285F4?style=for-the-badge&logo=google&logoColor=white" />
    <img src="https://img.shields.io/badge/Theme-Emergency_Response-dc2626?style=for-the-badge" />
    <img src="https://img.shields.io/badge/Status-Live-22c55e?style=for-the-badge" />
  </p>

  <p>
    <a href="https://techmedics-108.onrender.com/">
      <img src="https://img.shields.io/badge/🌐_Live_Demo-techmedics--108.onrender.com-46E3B7?style=for-the-badge&logo=render&logoColor=white" />
    </a>
    &nbsp;
    <a href="https://drive.google.com/file/d/1XYbmHxfMWaXSHama5ysZLa_DLIiKNXnn/view?usp=sharing">
      <img src="https://img.shields.io/badge/▶_Watch_Demo-YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white" />
    </a>
  </p>
</div>

---

## 🌟 What is LifeLine 108+?

**LifeLine 108+** is a real-time emergency response coordination system that intelligently connects **victims → dispatchers → ambulances → hospitals** — even in low-bandwidth or offline scenarios.

> Built for the **Google Solution Challenge 2026** under the theme of **Emergency Response & Healthcare**.

---

## 👥 Team — TechMedics

| # | Name | Role |
|---|------|------|
| 1 | **Vinayaka G C** | Backend & System Architecture |
| 2 | **Inchara P M** | Frontend & UI/UX |
| 3 | **Pragya R K** | Research & Integration |

---

## 🚀 Live Demo

| Interface | URL |
|-----------|-----|
| 📞 Call Center Dashboard | [techmedics-108.onrender.com](https://techmedics-108.onrender.com/) |
| 🚑 Ambulance Driver App | [/api/ambulance/app](https://techmedics-108.onrender.com/api/ambulance/app) |

---

## ✅ Quick Test Guide

### 1️⃣ Real-Time Dispatch (The "Wow" Factor)

```
Step 1 → Open: https://techmedics-108.onrender.com/callcenter
Step 2 → Open (new tab / incognito): https://techmedics-108.onrender.com/api/ambulance/app
         Login ID: DVG-AMB-001
Step 3 → On the dashboard: enter any phone number → click "Initiate Emergency Response"
Step 4 → Click "Assign Nearest Ambulance"
✅ Result → Ambulance app instantly shows EMERGENCY ALERT without any page refresh!
```

### 2️⃣ Live Location Sharing

```
Step 1 → Click "Copy Link" on a call card
Step 2 → Open the link on your phone
Step 3 → Tap "Share My Exact Location"
✅ Result → Dispatcher map updates in real-time with precise GPS coordinates
```

### 3️⃣ AI-Powered Dispatch Assistant

```
Step 1 → Click the "✦ Gemini AI Assistant" button (top-right of dashboard)
Step 2 → Ask anything: "Assess this emergency" or click quick prompts
✅ Result → Gemini AI provides triage assessment & recommended actions
```

### 4️⃣ Nearest Hospital Navigation (New Feature)

```
Step 1 → Driver logs in and receives an emergency assignment
Step 2 → Driver taps "Arrived" at the victim's location
✅ Result → App automatically finds & routes to the nearest hospital (OpenStreetMap)
```

---

## 🏗️ Architecture & Workflow

### Process Flow

<div align="center">
  <img src="photos/flow%20digram.png" alt="Process Flow Diagram" width="700" />
</div>

### System Architecture

<div align="center">
  <img src="photos/architecture.png" alt="System Architecture" width="700" />
</div>

---

## 📸 Screenshots

<div align="center">
  <img src="photos/1.jpeg" alt="Call Center Dashboard" width="45%" />
  &nbsp;
  <img src="photos/2.jpeg" alt="Driver App" width="45%" />
</div>

<br/>

<div align="center">
  <img src="photos/3.jpeg" alt="Location Sharing" width="45%" />
  &nbsp;
  <img src="photos/4.jpeg" alt="Live Tracking" width="45%" />
</div>

<br/>

<div align="center">
  <img src="photos/5.jpeg" alt="System Overview" width="60%" />
</div>

---

## 📺 Demo Video

<div align="center">
  <a href="https://drive.google.com/file/d/1XYbmHxfMWaXSHama5ysZLa_DLIiKNXnn/view?usp=sharing">
    <img src="https://img.shields.io/badge/▶_Watch_Full_Demo-Click_Here-FF0000?style=for-the-badge&logo=youtube&logoColor=white" />
  </a>
</div>

---

## 🛠️ Key Features

| Feature | Description |
|---------|-------------|
| ⚡ **Real-time Dispatch** | Socket.IO powered instant communication between all parties |
| 🗺️ **Smart Assignment** | Auto-assigns nearest available ambulance by GPS distance |
| 📱 **Offline SMS Fallback** | Works even when victim has no internet — SMS-based location protocol |
| 🏥 **Hospital Navigation** | Auto-finds nearest hospital via OpenStreetMap after driver arrives |
| 🤖 **Gemini AI Assistant** | AI-powered triage, incident summary & dispatch recommendations |
| 📍 **Live GPS Tracking** | Real-time ambulance tracking with Leaflet.js maps |
| 📲 **Mobile-First UI** | Fully responsive — works on any device |

---

## 💻 Tech Stack

| Layer | Technology |
|-------|------------|
| **Backend** | Python 3.11, Flask, Flask-SocketIO |
| **Real-time** | Socket.IO (WebSockets) |
| **Database** | SQLite via SQLAlchemy |
| **Maps** | Leaflet.js + OpenStreetMap (free, no API key) |
| **Hospital Search** | OpenStreetMap Overpass API (free) |
| **AI** | Google Gemini 2.0 Flash API |
| **Frontend** | HTML5, CSS3 (Glassmorphism), Vanilla JS |
| **SMS** | Twilio (optional) |
| **Deployment** | Render (free tier) |

---

## 🔧 Local Setup

```bash
# 1. Clone the repo
git clone https://github.com/vinu3783/LifeLine-108-
cd LifeLine-108-

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create your .env file
cp .env.example .env
# Add your GEMINI_API_KEY in .env

# 4. Run the app
python run.py
# Open: http://localhost:5000
```

---

## 🌐 UN Sustainable Development Goals

This project directly addresses:

- **SDG 3** — Good Health and Well-Being
- **SDG 11** — Sustainable Cities and Communities

---

<div align="center">
  <br/>
  <p>
    <img src="https://img.shields.io/badge/Made_with-❤️_in_India-FF9933?style=for-the-badge" />
    &nbsp;
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
    &nbsp;
    <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" />
    &nbsp;
    <img src="https://img.shields.io/badge/Google_Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white" />
  </p>
  <p>© 2026 TechMedics Team · Built for Google Solution Challenge 2026</p>
</div>