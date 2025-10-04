# Career Path Recommendation System

A machine learning-based web application built in **Google Colab** that predicts the most suitable career paths for students based on their skills.

---

## Features
- Predicts careers such as **Data Scientist**, **AI Engineer**, **Software Developer**, **HR**, and more
- Interactive interface using **Streamlit** in Colab
- Quick career recommendations based on skill inputs

---

## How It Works
1. Users input their skill levels in **Math**, **Coding**, and **Communication** using sliders.
2. A **Decision Tree Classifier** trained in Colab predicts the most suitable career path.
3. A **Label Encoder** converts numerical predictions into readable career names.
4. Streamlit displays the predicted career instantly in the browser.

---

## Tech Stack
- **Python 3.x**
- **Google Colab** (development and execution environment)
- **Streamlit** (interactive web interface)
- **Scikit-learn** (machine learning)
- **Joblib** (model and label serialization)

---

## How to Run in Colab
1. Open the Colab notebook containing the project.
2. Make sure all dependencies are installed:
```python
!pip install streamlit pyngrok scikit-learn joblib

3.Run the notebook cells sequentially:
  Train the model (or load pre-trained model files)
  Create the Streamlit app (app.py)
  Start the app using ngrok to get a public URL
4.Open the public URL provided by ngrok to access the app.

Author
Vaishnavi S
