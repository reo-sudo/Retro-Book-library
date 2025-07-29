# 🌌 RETRO BOOK LIBRARY 📚

<div align="center">


[![Python](https://img.shields.io/badge/Python-3.8+-FF6B6B?style=for-the-badge&logo=python&logoColor=white)]()
[![Django](https://img.shields.io/badge/Django-4.0+-4ECDC4?style=for-the-badge&logo=django&logoColor=white)]()
[![SQLite](https://img.shields.io/badge/SQLite-Database-45B7D1?style=for-the-badge&logo=sqlite&logoColor=white)]()
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)]()
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)]()
</div>

A simple Django app made for a school project. It allows you to manage books in a retro-style interface.

---

## Contents

- [Overview](#overview)  
- [Features](#features)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Project Structure](#project-structure)  
- [Licence](#licence)

---

## Overview

Built during Year 13 Digital Tech, this web app simulates a small library system. Users can register, add books, borrow and return them. Styled with neon vibes and Google Books integration to enhance experience.

---

## Features

- **User System**: Registration, login, Student/Admin roles  
- **Book Operations**: Add book, borrow, return, list view  
- **Search**: External (Google Books) + local  
- **Basic Retro Style**: Neon palette CSS + responsive layout  
- **Feedback**: Error messages and flash notifications

---

## Installation

```bash
git clone https://github.com/reo-sudo/Retro-Book-library.git
cd Retro-Book-library
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser  # optional
python manage.py runserver
