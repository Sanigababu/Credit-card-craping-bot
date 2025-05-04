import pdfplumber
import re

def extract_text_from_pdf(path):
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def clean_line(line):
    return re.sub(r'\s+', ' ', line).strip()

def extract_credit_cards_from_text(text):
    cards = []
    
    # Split into chunks based on card name patterns or double newlines
    blocks = re.split(r'\n\s*\n+', text)

    for block in blocks:
        block = block.strip()
        if not block or len(block) < 40:
            continue

        # Heuristics: must mention "credit card" or known card keywords
        if not re.search(r'credit card|SBI|SimplySAVE|IRCTC|PRIME|Air India|Cashback', block, re.IGNORECASE):
            continue

        lines = block.split("\n")
        lines = [clean_line(line) for line in lines if line.strip()]

        card = {}

        # 1. Name
        name_match = re.search(r'(?i)([A-Z][A-Za-z &\-]{3,} (credit card|card))', block)
        if name_match:
            card["name"] = name_match.group(1).strip()
        else:
            card["name"] = lines[0] if lines else "Unnamed Card"

        # 2. Annual Fee
        fee_match = re.search(r'(?i)(Annual Fee|Joining Fee)[^\d]*(INR|Rs\.?|₹)?\s*[\d,]+', block)
        if fee_match:
            card["Annual Fee"] = fee_match.group(0).strip()

        # 3. Rewards
        rewards_match = re.search(r'(?i)(Reward Points|Rewards|Cashback)[^\n:]*[:\-]?\s*(.*)', block)
        if rewards_match:
            card["Rewards"] = rewards_match.group(2).strip()

        # 4. APR
        apr_match = re.search(r'(?i)(APR|Interest Rate)[^\n:]*[:\-]?\s*(.*)', block)
        if apr_match:
            card["APR"] = apr_match.group(2).strip()

        # 5. Sign-up Bonus
        bonus_match = re.search(r'(?i)(Sign[-\s]?up Bonus|Welcome Offer)[^\n:]*[:\-]?\s*(.*)', block)
        if bonus_match:
            card["Sign-up Bonus"] = bonus_match.group(2).strip()

        cards.append(card)

    return cards

def parse_pdf(path):
    raw_text = extract_text_from_pdf(path)

    # Optional: Save raw text for debugging
    with open("raw_text.txt", "w", encoding="utf-8") as f:
        f.write(raw_text)

    return extract_credit_cards_from_text(raw_text)

