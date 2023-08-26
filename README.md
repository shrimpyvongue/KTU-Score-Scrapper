# Web Scraper for KTU Grade Card

This is a web scraper written in Python using the Playwright and BeautifulSoup libraries. The scraper is designed to log into the KTU (APJ Abdul Kalam Technological University) student portal, navigate to the semester grade card listing page, and extract the data from the grade card table.

## Prerequisites

- Python 3.x
- Playwright library (`pip install playwright`)
- BeautifulSoup library (`pip install beautifulsoup4`)

## Usage

1. Install the required dependencies:
    `pip install playwright beautifulsoup4`
2. Run the scraper:
    `python scraper.py`

## Configuration

- Modify the `username` and `password` fields in `scraper.py` to match your KTU student portal login credentials.
- Adjust the selectors in the script to match the HTML structure of the website if needed.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- This scraper was developed for educational purposes and to demonstrate web scraping techniques.
- The Playwright and BeautifulSoup libraries were used to interact with the web page and parse the HTML, respectively.

Feel free to modify and extend the scraper to suit your needs.
