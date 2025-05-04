import argparse
from pdf_scraper import parse_pdf
from url_scraper import parse_url
from exporter import export_to_json, export_to_excel, export_to_txt

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--pdf', help='Path to PDF file')
    parser.add_argument('--url', help='URL to scrape')
    parser.add_argument('--output', default='json', choices=['json', 'excel', 'txt'], help='Output format')
    args = parser.parse_args()

    if args.pdf:
        data = parse_pdf(args.pdf)
    elif args.url:
        data = parse_url(args.url)
    else:
        raise Exception("Please specify either --pdf or --url")

    if args.output == 'json':
        export_to_json(data)
    elif args.output == 'excel':
        export_to_excel(data)
    elif args.output == 'txt':
        export_to_txt(data)

    print(f"✅ Extracted {len(data)} credit card(s). Output saved as {args.output}.")

if __name__ == '__main__':
    main()

