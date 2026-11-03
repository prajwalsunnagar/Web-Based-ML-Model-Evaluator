# Sprint 1 Demonstration Recording Guide & Narration Script

**Project Title:** Web-Based ML Model Evaluator  
**Milestone:** Sprint 1 Review  
**Target Duration:** 60 Seconds (1 Minute)  
**Target Output File:** `docs/demo_videos/sprint1_demo.mp4`  
**Recording Status:** **PENDING MANUAL RECORDING** (Use this guide for screencast capture)  
**Team Members:** Prajwal Sunnagar, Shreyank S, Skanda, Sujal

---

## 1. Recording Setup & Technical Requirements

- **Resolution:** 1080p ($1920 \times 1080$) at 30 fps.
- **Audio:** Clear voiceover with noise suppression; no background music.
- **Format:** MP4 (H.264 video codec, AAC audio).
- **Target File Size:** $< 15\text{ MB}$.
- **Local Application Command:**
  ```bash
  streamlit run app.py
  ```
- **Prepared Datasets:**
  - `sample_data/classification_sample.csv` (15 rows, 4 classes)
  - `sample_data/regression_sample.csv` (10 rows, numeric values)

---

## 2. Timed Scene-by-Scene Script

| Timestamp | Visual Screen Action | Voiceover Narration Script | Focus Feature |
|---|---|---|---|
| **0:00 – 0:10** | Open browser to `http://localhost:8501`. Display clean landing page and title header. | *"Welcome to the Sprint 1 demonstration of the Web-Based ML Model Evaluator. Our web application provides an intuitive, browser-based environment for uploading model predictions and calculating standardized performance metrics."* | Introduction & UI overview |
| **0:10 – 0:25** | Drag and drop `sample_data/classification_sample.csv` into the file uploader. Show instant file size badge and 10-row dataset preview table. | *"We begin by uploading `classification_sample.csv`. The system validates file format and size limits under 10 MB, immediately presenting the first ten rows alongside dataset dimensions: 15 rows, 4 columns, and zero missing values."* | CSV Upload, Size Validation, Dataset Preview |
| **0:25 – 0:38** | Select Task: `Classification`. Map actual column to `terrain_actual`, predicted column to `terrain_predicted`. Check all metrics (`Accuracy`, `Precision`, `Recall`, `F1-score`). | *"Under Evaluation Configuration, we select Classification as the task type, set our ground truth column to `terrain_actual`, and model predictions to `terrain_predicted`, enabling Accuracy, Precision, Recall, and F1-score with weighted averaging."* | Configuration & Metric Selection |
| **0:38 – 0:50** | Click **Calculate evaluation metrics**. Display KPI cards (Accuracy: 0.8667) and 4x4 confusion matrix. | *"Clicking calculate executes the evaluation engine deterministically. KPI cards showcase our overall accuracy of 86.67%, while the confusion matrix displays true versus predicted distributions across all four terrain classes."* | Execution & Visual Results Presentation |
| **0:50 – 1:00** | Select identical columns (`terrain_actual` for both) to show the immediate validation warning banner. Wrap up. | *"To demonstrate validation safety, mapping identical columns immediately triggers a clear warning banner. With all core unit and integration tests passing, this concludes our Sprint 1 demonstration. Thank you!"* | Validation Safety & Conclusion |

---

## 3. Post-Recording Encoding Command

After recording the screen capture, compress the video using ffmpeg:
```bash
ffmpeg -i raw_sprint1_recording.mov -vcodec libx264 -crf 28 -pix_fmt yuv420p docs/demo_videos/sprint1_demo.mp4
```
