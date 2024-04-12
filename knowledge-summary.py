from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import csv
import sys
import time
import os



def scrape_content(driver, url):
    """Function to scrape content from a webpage"""
    driver.get(url)
    time.sleep(2)  # Wait for the page to load
    
    # Extract the page source
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    
    # Find and extract Introduction, Summary, and LOS elements
    introduction = soup.find(class_='c-article-introduction').get_text(strip=True)
    summary = soup.find(class_='c-article-summary').get_text(strip=True)
    los = soup.find(class_='c-article-los').get_text(strip=True)
    
    # Additional code to extract figures, tables, and formulas if needed
    
    return introduction, summary, los

def main():
    # URLs to scrape
    urls = [
        "https://www.cfainstitute.org/membership/professional-development/refresher-readings/multiple-regression",
        "https://www.cfainstitute.org/membership/professional-development/refresher-readings/time-value-money",
        "https://www.cfainstitute.org/membership/professional-development/refresher-readings/common-probability-distributions",
        "https://www.cfainstitute.org/membership/professional-development/refresher-readings/probability-concepts"
    ]
    
    

    # Specify the path to chromedriver
    chrome_driver_path = "/home/ektabhatia/BigDataDAMG/Assignment05/drivers/chromedriver"

    # Initialize ChromeOptions
    chrome_options = Options()

    # Add arguments to ChromeOptions
    chrome_options.add_argument("--headless")  # Set Chrome to run in headless mode
    chrome_options.binary_location = chrome_driver_path  # Set the path to chromedriver

    # Initialize WebDriver with ChromeOptions
    driver = webdriver.Chrome(options=chrome_options)

    # List to store scraped data
    data = []
    
    try:
        # Scrape content from each URL
        for url in urls:
            introduction, summary, los = scrape_content(driver, url)
            data.append([url, introduction, summary, los])
            
    except Exception as e:
        print("Error:", e)
    finally:
        # Quit WebDriver
        driver.quit()
        
        # Write scraped data to a CSV file
        csv_file = "scraped_data.csv"
        with open(csv_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["URL", "Introduction", "Summary", "LOS"])
            writer.writerows(data)
        
        print("Scraping completed. Data saved to:", csv_file)

if __name__ == "__main__":
    main()