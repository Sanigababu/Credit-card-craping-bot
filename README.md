# Credit-card-craping-bot

A Python bot that extracts credit card information from either a URL or a PDF brochure and outputs structured data in JSON and Excel formats.

## Features
- URL scraping using BeautifulSoup
- PDF parsing using PyMuPDF
- Output to Excel and JSON
- Fully local and free to use

## Setup
```bash
python -m venv .venv
.venv\Scripts\Activate.ps1  # Use this in PowerShell
```

## Usage
```bash
python main.py --url "https://example.com/cards"
python main.py --pdf sample_inputs/brochure.pdf
```

## Output
Results will be saved:
- `credit_cards.json`

---

## Folder Structure
```
Credit card scraping bot/
│
├── main.py              # Entry point for scraping
├── url_scraper.py       # Scraper logic for web URLs using Selenium
├── pdf_scraper.py       # Extracts and parses text from PDF files
├── exporter.py          # Exports data to Excel
├── requirements.txt     # Required Python packages
└── README.md            # Project documentation

```

---

---

## ⚙️ Features

- ✅ Scrape credit card names and descriptions from the **SBICard website** or a **PDF file**
- ✅ Export results to an **Excel file**
- ✅ CLI-based interaction
- 🚧 (Optional) Extendable to other banks or formats

---

## 🖥️ Requirements

- Python 3.7+
- Google Chrome
- ChromeDriver (same version as your browser)

**Install dependencies:** 

```bash
pip install -r requirements.txt
```
