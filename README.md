# X-twitter-bookmarkscrapper

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

Install dependencies with:

```bash
pip install -r requirements.txt
```

> ✅ The script uses [`webdriver-manager`](https://github.com/SergeyPirogov/webdriver_manager) to auto-manage the correct ChromeDriver version for your system.

---

## 🛠️ Setup & Usage

1. **Run the script:**

   ```bash
   python x_bookmarks_scrapper.py
   ```

2. **Manual Login:**

   * A Chrome browser window will open and navigate to [https://twitter.com/i/bookmarks](https://twitter.com/i/bookmarks)
   * Log into your X account manually
   * Once bookmarks are loaded, **return to the terminal and press ENTER**

3. **Extraction Process:**

   * The script scrolls to load additional bookmarks
   * Bookmark details are extracted and saved

4. **Output:**

   * Results are saved to `bookmarks.json` in the project directory

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

You can customize the following settings in `x_bookmarks_scrapper.py`:

### 🔁 Scroll Settings

Adjust number of scrolls and delay between scrolls in the `scroll_to_load()` function:

```python
scroll_to_load(driver, scrolls=7, delay=2)
```

### 🧠 Persistent Login (Optional)

To avoid logging in every time:

1. Uncomment this line in `setup_browser()`:

```python
# options.add_argument("--user-data-dir=selenium")
```

2. This creates a user profile that keeps your login session cached.

---

## 📁 Project Structure

```text
├── x_bookmarks_scrapper.py   # Main script
├── requirements.txt          # Python dependencies
├── bookmarks.json            # Output file (auto-generated)
└── .gitignore                # Python and Selenium-related exclusions
```

---

## 🛠️ Troubleshooting

* **Chrome not found?** Make sure it’s installed and accessible from your system’s PATH.
* **Driver mismatch?** `webdriver-manager` should auto-resolve it, but try updating manually if needed.
* **X login fails?** Be sure you're using the correct URL and allow time for bookmarks to load before pressing ENTER.

---

## 📄 License

This project is for **personal, non-commercial use** only. Please respect [X's Terms of Service](https://twitter.com/en/tos).

---

## 👤 Author

**PRICEWES*
Feel free to fork, modify, or contribute with proper credit!

---


