**# 🎯 Student Skill Gap Analyzer**

> **Know where you stand. Know what to learn next.**

**Student Skill Gap Analyzer** is an interactive Streamlit web application designed to help students understand the gap between their **current skills** and the skills commonly associated with a selected career role.

Instead of simply listing skills, the application turns the comparison into an easy-to-understand **skill match percentage, missing-skill list, learning priorities, and recommended learning path.**

---

## ✨ What Makes It Useful?

Students often know the career they want but are unsure about:

* What skills are relevant to that role?
* Which skills do I already have?
* What am I missing?
* What should I learn first?

This project provides a simple way to answer those questions in one place.

---

## 🚀 Features

### 💼 Role-Based Skill Analysis

Choose a target career role and view the skills associated with it.

### 📊 Skill Match Percentage

The application calculates how many of the selected role's skills match the student's current skills.

### ✅ Skill Coverage

Clearly displays the skills the student already has.

### ❌ Skill Gap Detection

Identifies the skills that are still missing.

### 📚 Learning Priority

Missing skills are presented in a priority sequence to help students decide where to begin.

### 🗺️ Recommended Learning Path

Provides a short learning direction for each missing skill.

### 📈 Visual Progress

A progress bar gives a quick visual representation of the current skill match.

---

## 💼 Supported Career Roles

The current version includes:

| Role             | Example Skills                                    |
| ---------------- | ------------------------------------------------- |
| Data Analyst     | Python, SQL, Excel, Statistics, Power BI          |
| Data Scientist   | Python, SQL, Statistics, Machine Learning, Pandas |
| Python Developer | Python, OOP, Git, SQL, APIs                       |
| Web Developer    | HTML, CSS, JavaScript, Git, APIs                  |

> **Note:** These are simplified project-defined skill sets based on commonly associated skills for the selected roles. They are not intended to represent an official industry-wide requirement.

---

## 🔄 How It Works

```text
       TARGET ROLE
            ↓
   Role Skill Requirements
            ↓
      CURRENT SKILLS
            ↓
      Skill Comparison
            ↓
    ┌───────┴────────┐
    ↓                ↓
 MATCHED           MISSING
 SKILLS             SKILLS
    ↓                ↓
    └───────┬────────┘
            ↓
      MATCH PERCENTAGE
            ↓
    LEARNING PRIORITY
            ↓
    RECOMMENDED PATH
```

---

## 📐 Skill Match Calculation

The project uses a simple matching formula:

**Skill Match % = (Matched Skills ÷ Required Skills) × 100**

### Example

If a Data Analyst role has 5 required skills and a student has 3:

**3 ÷ 5 × 100 = 60%**

The percentage represents **skill coverage within this project's defined skill list**. It is not an employability or job-selection score.

---

## 🛠️ Technology Stack

* **Python** — application logic
* **Streamlit** — interactive web interface
* **Pandas** — data-oriented Python library used in the project environment

---

## ▶️ Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/domahansika/Student_Skill_Gap_Analyzer.git
```

### 2. Open the project folder

```bash
cd Student_Skill_Gap_Analyzer
```

### 3. Install the required libraries

```bash
python -m pip install streamlit pandas
```

### 4. Start the application

```bash
python -m streamlit run app.py
```

The application will open in your browser.

---

## 🎯 Project Objective

The goal of this project is to create a simple, interactive tool that helps students move from:

**"What skills do I have?"**

to

**"What should I learn next?"**

It demonstrates the use of Python programming, interactive UI development, conditional logic, data structures, and basic analytical calculations.

---

## 🔮 Future Improvements

Possible extensions for future versions include:

* Adding more career roles
* Using a larger external skills dataset
* Adding skill proficiency levels
* Tracking learning progress
* Adding skill-wise learning resources
* Storing user assessment history
* Adding visual analytics for skill development

---

## 👩‍💻 Author

**D. HANSIKA REDDY**




⭐ If you find this project useful, feel free to explore the code and try the application.
