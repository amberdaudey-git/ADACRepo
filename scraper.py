# scraper.py
"""
Google News Scraper for research on algorithmic hiring systems and fairness
This script fetches news articles based on multiple focused queries and regions,
prints the results, and saves them to separate text files in the outputs/ folder.
"""

import os
from pygooglenews import GoogleNews

# -------------------------------
# Setup
# -------------------------------

# Create outputs folder if it doesn't exist
os.makedirs('outputs', exist_ok=True)

# Focused search queries for your research question
queries = [
    'algorithmic hiring',
    'AI recruitment',
    'hiring fairness',
    'algorithm bias HR',
    'AI job selection'
]

# Regions/languages you want to search (can add more)
regions = [
    {'lang': 'en', 'country': 'US'},  # English, USA
    {'lang': 'en', 'country': 'GB'},  # English, UK
    {'lang': 'nl', 'country': 'NL'}   # Dutch, Netherlands
]

# -------------------------------
# Main scraping loop
# -------------------------------
for region in regions:
    gn = GoogleNews(lang=region['lang'], country=region['country'])
    for query in queries:
        print(f"\nFetching results for '{query}' in {region['country']}...")
        search = gn.search(query)

        # Prepare filename for output
        filename = f"outputs/results_{region['country']}_{query.replace(' ', '_')}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            if 'entries' in search:
                for entry in search['entries']:
                    line = f"{entry['published']} - {entry['title']} - {entry['link']}"
                    print(line)          # Print to terminal
                    f.write(line + "\n") # Save to file
            else:
                print("No entries found!")
                f.write("No entries found!\n")

print("\nScraping complete. Results saved in outputs/ folder.")


