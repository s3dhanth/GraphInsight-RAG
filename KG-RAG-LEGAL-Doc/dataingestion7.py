from bs4 import BeautifulSoup
import requests

def fetch_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print("Failed to retrieve content. Status code:", response.status_code)
        return None

def parse_charter_html(html_content):
    soup = BeautifulSoup(html_content, "html.parser")

    results = []
    current_title = None
    current_article = None
    next_is_title_heading = False  # Flag to capture title heading after TITLE

    for p in soup.find_all("p"):
        text = p.get_text(strip=True)

        if text.startswith("TITLE"):
            # Save previous article
            if current_article:
                current_title["Articles"].append(current_article)
                current_article = None

            # Save previous title
            if current_title:
                results.append(current_title)

            # Prepare new title
            current_title = {
                "TitleID": text,  # e.g., TITLE I
                "TitleName": "",  # to be filled in next paragraph
                "Articles": []
            }
            next_is_title_heading = True

        elif next_is_title_heading and current_title:
            current_title["TitleName"] = text  # Grab the heading
            next_is_title_heading = False

        elif text.startswith("Article"):
            # Save previous article
            if current_article:
                current_title["Articles"].append(current_article)

            current_article = {
                "Article Number": text,
                "Article Title": "",
                "Article Text": ""
            }

        elif current_article and not current_article["Article Title"]:
            current_article["Article Title"] = text

        elif current_article:
            current_article["Article Text"] += text + "\n"

    # Save last article and title
    if current_article:
        current_title["Articles"].append(current_article)
    if current_title:
        results.append(current_title)

    return results

# Example usage
url = 'https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:12012P/TXT'
html = fetch_html(url)
if html:
    parsed = parse_charter_html(html)
    print(parsed[0])  # sanity check

import pandas as pd

# Assuming `parsed` contains the parsed data
titles_data = []
articles_data = []

for title in parsed[7:]:
    titles_data.append({
        "TitleID": title["TitleID"],
        "TitleName": title["TitleName"]
    })
    for article in title["Articles"]:
        articles_data.append({
            "TitleID": title["TitleID"],
            "Article Number": article["Article Number"],
            "Article Title": article["Article Title"],
            "Article Text": article["Article Text"].strip()
        })

# Convert to DataFrames
df_titles = pd.DataFrame(titles_data)
df_articles = pd.DataFrame(articles_data)

# Save to CSV
df_titles.to_csv("titles.csv", index=False)
df_articles.to_csv("articles.csv", index=False)