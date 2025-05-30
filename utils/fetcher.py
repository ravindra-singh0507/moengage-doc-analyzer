from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import json
import sys
import os
import traceback

def extract_article_text(url):
    try:
        options = Options()
        options.add_argument("--headless")  # use legacy headless mode
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920x1080")

        # Optional: Explicitly set Chrome binary path
        options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

        driver.get(url)
        wait = WebDriverWait(driver, 15)

        # Wait for article content; fallback to entire body
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "article, .article-body, body")))

        soup = BeautifulSoup(driver.page_source, "html.parser")
        driver.quit()

        # Flexible selectors for title and body
        title_tag = soup.select_one(".article-title, h1")
        body_tag = soup.select_one(".article-body, article, main")

        content_parts = []

        if title_tag:
            content_parts.append(title_tag.get_text(strip=True))

        if body_tag:
            for tag in body_tag.find_all(["h1", "h2", "h3", "p", "li"]):
                text = tag.get_text(strip=True)
                if text:
                    content_parts.append(text)

        content = "\n".join(content_parts).strip()

        return { "content": content } if content else { "error": "No content found in the body" }

    except Exception as e:
        return {
            "error": "Exception occurred",
            "details": traceback.format_exc()
        }

# Optional CLI use
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python fetcher.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    result = extract_article_text(url)

    os.makedirs("outputs", exist_ok=True)
    with open("outputs/sample_output.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print("Extraction complete. Output saved to outputs/sample_output.json")
