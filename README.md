# 🌷 Grade 1 Study App — Thai Curriculum

A mobile-first Grade 1 study and revision app designed around the Thai primary school curriculum.

The app combines **subject-based lessons, long-form reading, read-aloud learning, practice exercises, review tests, and mistake revision** in a child-friendly pastel interface.

Built with **Python + Streamlit**.

---

## ✨ Current Demo

The first subject implemented is:

### 🔬 Science — Grade 1

Current Science content includes:

1. **ตัวเรา พืช และสัตว์**  
   Our Body, Plants and Animals

2. **พืชและสัตว์ในท้องถิ่น**  
   Plants and Animals in the Local Environment

3. **วัสดุรอบตัวเรา**  
   Materials Around Us

4. **หินและท้องฟ้าของเรา**  
   Rocks and Our Sky

Other subjects are prepared as placeholders and will be added gradually.

---

## 🎯 App Concept

The learning flow is designed to be simple for young children:

**Home → Choose Subject → Choose Chapter → Read / Listen → Practice → Review Test → Review Mistakes**

The goal is to make revision easier without requiring children to constantly press "Next" while studying.

Lessons therefore use **long-form scrollable reading content**, similar to a reading app.

---

## 🌈 Main Features

### 📚 Subject-Based Learning

The home screen is organized by subject.

Current subject menu includes:

- 🔬 Science
- 🧮 Maths
- 🔤 English
- 📖 ภาษาไทย
- 🏮 Chinese
- 🌍 Social Studies
- 🔡 Phonics
- 💻 Coding

Science is currently active for the first prototype.

---

### 📖 Long-Form Lesson Reading

Lessons are displayed as continuous reading content rather than short flashcards.

This allows children to:

- read at their own pace
- listen while following the text
- scroll naturally through the lesson
- review the entire chapter without repeatedly pressing Next

---

### 🔊 Read-Aloud Learning

Each lesson includes a read-aloud toolbar.

Features include:

- ▶ Play
- ⏸ Pause / Resume
- ↶ Rewind
- ↷ Forward
- draggable reading progress bar
- reading progress percentage

The read-aloud toolbar stays together with the chapter navigation while reading.

---

### 📌 Fixed Chapter Navigation

Chapter navigation remains visible while the child scrolls through long lesson content.

Example:

`บท 1` | `บท 2` | `บท 3` | `บท 4`

The audio controls stay directly below the chapter navigation.

This creates a reading-app style experience and makes switching chapters easier.

---

### ✏️ Practice Exercises

Each chapter includes short practice questions.

Practice mode provides:

- multiple-choice questions
- immediate feedback
- explanations after answering
- automatic tracking of incorrect answers

---

### 📝 Review Tests

The app supports several revision modes:

#### Review by Chapter
Practice questions from the current chapter.

#### Review the Whole Book
Questions mixed from multiple chapters.

#### Before Exam
A larger mixed test designed for exam preparation.

Unlike practice mode, review tests do not immediately reveal the answer after every question.

---

### ⭐ Mistake Revision

Incorrect answers are automatically collected into:

**ข้อที่เคยผิด — Questions I Got Wrong**

Children can return later and practice only the questions they previously answered incorrectly.

The learning loop becomes:

**Wrong → Save → Review → Try Again → Master**

This helps focus revision on weaker areas instead of repeatedly practicing material the child already understands.

---

## 🎨 Design

The UI is designed specifically for young learners.

Design principles include:

- mobile-first layout
- large touch-friendly buttons
- soft pastel rainbow colors
- rounded cards
- minimal visual clutter
- simple navigation
- large readable Thai text
- child-friendly icons
- long-form reading experience

The interface is optimized for both desktop testing and mobile use.

---

## 🛠 Tech Stack

- **Python**
- **Streamlit**
- HTML / CSS
- JavaScript
- Browser Web Speech API for read-aloud controls

---

## 📂 Project Structure

```text
grade1-study-app-thai-curriculum/
│
├── app.py
├── requirements.txt
├── README.md
└── assets/
