───────────────────────────────────────────────
⟬📼 RETRO BOOK LIBRARY 📖⟭
───────────────────────────────────────────────
❝ Bringing nostalgia to the cloud ☁️ with Google Books magic ❞
───────────────────────────────────────────────

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ 🧠 Purpose
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
・Create a fully functional media outcome (NCEA Level 3)
・Retro-themed book manager 📚
・Integrates Google Books API 🔍
・Includes student user roles & admin dashboard 💻

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ 👥 Users
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
★ Students
┗▶ Can register, log in, search books, add/remove them from personal library
★ Admin
┗▶ Can view all users and their library collections

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ 🧰 Tech Stack
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
‣ Python 3 🐍
‣ Django Framework 🌐
‣ SQLite Database 🗃️
‣ HTML/CSS/JavaScript 🎨
‣ Google Books API ☁️
‣ Retro-styled frontend (fonts, colors, layout) 🎮

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ 💡 Key Features
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
✦ User Registration & Login System
✦ Google Book Search Integration
✦ Prevents duplicate book entries using Google ID
✦ Each user has a personal library
✦ Admin Dashboard to view all users and their books
✦ Fully retro aesthetic (CSS styling + vibe)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ 🧪 Test Table (Frontend Media Outcome)
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

Component	Tested ✅	Result
User Registration	✅	Success
Login / Logout	✅	Works as expected
Book Search	✅	Google API Integration
Add to Library	✅	Prevents duplicates
Delete Book	✅	Cleans up properly
Admin View	✅	Sees users + libraries

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ 📘 ERD (Entity Relationship Diagram)
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

↳ Book
┣━ title
┣━ authors
┣━ description
┣━ thumbnail
┗━ google_id (unique)

↳ LibraryEntry
┣━ user (FK)
┣━ book (FK)
┗━ date_added

👾 1 Book → Many Users
👾 1 User → Many Books

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ 🚀 Run Locally
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
📝 Prerequisites: Python 3, Django, pip

❶ Clone repo
❷ Run the migrations

nginx
Copy
Edit
python3 manage.py makemigrations  
python3 manage.py migrate  
❸ Run the server

nginx
Copy
Edit
python3 manage.py runserver  
❹ Access it at: http://localhost:8000

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ 🔮 Future Add-Ons
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
✧ Add a star rating & review system ⭐
✧ Export book list to PDF/CSV 📤
✧ Animate covers like VHS-style scrolling
✧ Theme selector (CRT green, amber, etc.)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ 🕶️ Aesthetic
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
Retro 80s–90s design vibes:
✷ Terminal fonts (monospace)
✷ Neon glow accents
✷ Pixel art & CRT glitch effects (optional CSS)
✷ 🧃 Vaporwave mode: pending...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💾 Made with vintage vibes by [Your Name]
🗓️ 2025 | 📼 Retro Book Library™
