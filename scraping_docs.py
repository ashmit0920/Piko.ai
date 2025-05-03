import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from markdownify import markdownify as md
import time

BASE_URL = "https://docs.manim.community/en/stable/"
START_URL = urljoin(BASE_URL, "reference.html")
OUTPUT_DIR = "manim_docs"

visited = set()
delay_between_requests = 1  # seconds


def is_valid_doc_url(url):
    """Filter URLs to only include relevant Manim documentation pages."""
    parsed = urlparse(url)
    return (
        parsed.netloc == "docs.manim.community"
        and "/reference/manim" in parsed.path
        and url.endswith(".html")
    )


def save_markdown_from_url(url):
    print(f"[+] Scraping: {url}")
    try:
        res = requests.get(url)
        if res.status_code != 200:
            print(f"[!] Failed to fetch: {url}")
            return

        soup = BeautifulSoup(res.text, "html.parser")
        main = soup.find("div", class_="article-container")
        if not main:
            print(f"[!] Main content not found in: {url}")
            return

        text_md = md(str(main))

        parsed = urlparse(url)
        filename = parsed.path.replace("/", "_").replace(".html", ".md")
        filepath = os.path.join(OUTPUT_DIR, filename)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"# Source: {url}\n\n")
            f.write(text_md)

    except Exception as e:
        print(f"[!] Error scraping {url}: {e}")


def crawl_and_scrape(start_url):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    to_visit = {start_url}

    while to_visit:
        url = to_visit.pop()
        if url in visited:
            continue
        visited.add(url)

        try:
            res = requests.get(url)
            if res.status_code != 200:
                continue

            soup = BeautifulSoup(res.text, "html.parser")
            for link in soup.find_all("a", href=True):
                href = link["href"]
                full_url = urljoin(url, href)

                if is_valid_doc_url(full_url) and full_url not in visited:
                    to_visit.add(full_url)

            # If this is a valid documentation page, save it
            if is_valid_doc_url(url):
                save_markdown_from_url(url)

            time.sleep(delay_between_requests)

        except Exception as e:
            print(f"[!] Error visiting {url}: {e}")


if __name__ == "__main__":
    print("[*] Starting Manim documentation scrape...")
    crawl_and_scrape(START_URL)
    print("[✓] Scraping complete. Saved in 'manim_docs/'")
