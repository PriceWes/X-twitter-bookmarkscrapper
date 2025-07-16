#  X-twitter-bookmarkscrapper

A Python automation script that extracts your bookmarked posts from **X (formerly Twitter)** and saves them in a clean, structured `JSON` file.

---

## 🚀 Features

* Automates Chrome browser using Selenium
* Scrolls through your X bookmarks page to load all content
* Extracts:

  * 🧑 Author name
  * 🔗 Post URL
  * 📝 Post text
* Saves bookmarks in a readable JSON format (`bookmarks.json`)

---

## 🧰 Requirements

Make sure you have the following:

* **Python 3.6+**
* **Google Chrome** (installed on your system)

---

## 🛠️ Setup & Usage (with Virtual Environment)

### 1. 📦 Clone the repository

```bash
git clone https://github.com/yourusername/x-twitter-bookmarkscrapper.git
cd x-twitter-bookmarkscrapper
```

### 2. 🧪 Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate      # On Linux/macOS
# OR
venv\Scripts\activate         # On Windows
```

### 3. 📚 Install dependencies

```bash
pip install -r requirements.txt
```

> ✅ The script uses [`webdriver-manager`](https://github.com/SergeyPirogov/webdriver_manager) to auto-manage the correct ChromeDriver version for your system.

---

## ▶️ Running the Script

```bash
python x_bookmarks_scrapper.py
```

---

## 🔐 Manual Login

* A Chrome browser window will open and navigate to [https://twitter.com/i/bookmarks](https://twitter.com/i/bookmarks)
* Log into your X account manually
* Once bookmarks are loaded, **return to the terminal and press ENTER**

---

## 🔍 Extraction Process

* The script scrolls to load more bookmarks
* Extracted details are saved in `bookmarks.json` inside the project folder

---

## 🗃️ Output Format

Each bookmark is stored as a JSON object like this:

```json
{
  "author": "Author Name",
  "url": "https://x.com/username/status/1234567890",
  "text": "Post content and metadata"
}
```

---

## ⚙️ Configuration Options

### 🔁 Scroll Settings

You can adjust the number of scrolls and delay time:

```python
scroll_to_load(driver, scrolls=7, delay=2)
```

### 🧠 Persistent Login (Optional)

Uncomment the following line in `setup_browser()` to keep your login session saved:

```python
# options.add_argument("--user-data-dir=selenium")
```

---

## 📁 Project Structure

```text
├── x_bookmarks_scrapper.py   # Main script
├── requirements.txt          # Python dependencies
├── bookmarks.json            # Output file (auto-generated)
├── .gitignore                # Git ignored files
└── venv/                     # Virtual environment (ignored by Git)
```

---

## 🛠️ Troubleshooting

* **Chrome not found?** Ensure it's installed and added to your system PATH
* **ChromeDriver version mismatch?** `webdriver-manager` handles it automatically
* **Login fails?** Ensure you're on the correct page and fully logged in before pressing ENTER

---

## 📄 License

This project is for **personal, non-commercial use** only. Please respect [X's Terms of Service](https://twitter.com/en/tos).

---

## 👤 Author

**PRICEWES**
Feel free to fork, modify, or contribute with proper credit!

---
