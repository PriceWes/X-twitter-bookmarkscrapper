import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def setup_browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # Uncomment the next line to use a persistent Chrome profile (optional)
    # options.add_argument("--user-data-dir=selenium")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def scroll_to_load(driver, scrolls=5, delay=3):
    for i in range(scrolls):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(delay)

def extract_bookmarks(driver):
    posts = driver.find_elements(By.XPATH, "//article[@role='article']")
    bookmarks = []

    for post in posts:
        try:
            content = post.text.split("\n")
            tweet_url_element = post.find_element(By.XPATH, ".//a[contains(@href, '/status/')]")
            tweet_url = tweet_url_element.get_attribute("href")

            author = content[0] if content else ""
            tweet_text = " ".join(content[1:])

            bookmarks.append({
                "author": author,
                "url": tweet_url,
                "text": tweet_text
            })

        except NoSuchElementException:
            continue

    return bookmarks

def save_to_json(data, filename="bookmarks.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"✅ Bookmarks saved to {filename}")

def main():
    driver = setup_browser()
    driver.get("https://twitter.com/i/bookmarks")

    input("📌 Log into your Twitter account, then press ENTER when bookmarks are visible...")

    scroll_to_load(driver, scrolls=7, delay=2)

    print("🔍 Extracting bookmarks...")
    bookmarks = extract_bookmarks(driver)

    save_to_json(bookmarks)

    driver.quit()

if __name__ == "__main__":
    main()
