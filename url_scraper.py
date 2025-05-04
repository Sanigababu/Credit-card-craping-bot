import requests
from bs4 import BeautifulSoup
import re

def extract_credit_cards_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    cards = []
    blocks = soup.find_all(["div", "section", "article", "li", "p"])

    for block in blocks:
        text = block.get_text(separator=" ").strip()
        if re.search(r'credit card', text, re.IGNORECASE):
            card = {}
            name = re.search(r'(?i)^([\w\s]+credit card)', text)
            if name:
                card['name'] = name.group(1).strip()

            apr = re.search(r'(?i)APR[^:]*:\s*(.+)', text)
            if apr:
                card['APR'] = apr.group(1).strip()

            fee = re.search(r'(?i)Annual Fee[^:]*:\s*(.+)', text)
            if fee:
                card['Annual Fee'] = fee.group(1).strip()

            rewards = re.search(r'(?i)Rewards[^:]*:\s*(.+)', text)
            if rewards:
                card['Rewards'] = rewards.group(1).strip()

            bonus = re.search(r'(?i)Sign[-\s]?up Bonus[^:]*:\s*(.+)', text)
            if bonus:
                card['Sign-up Bonus'] = bonus.group(1).strip()

            if card:
                cards.append(card)

    return cards

def parse_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return extract_credit_cards_from_html(response.text)
    else:
        raise Exception(f"Failed to fetch {url}, status code {response.status_code}")
