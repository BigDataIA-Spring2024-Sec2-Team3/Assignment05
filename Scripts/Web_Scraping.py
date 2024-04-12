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
 
 
 
def scrape_content(driver,url) :
    """Function to scrape content using BeautifulSoup"""
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    title_class = soup.find(['h1','h2'], class_='article-title')
   
    # Extract the article title text
    if title_class is not None:
        title = title_class.text.strip()

     # Extract the topic
    topic_span = soup.find('span', class_='content-utility-topics')
    if topic_span is not None:
        topic_text = topic_span.get_text(strip=True)
    else:
        topic_text = "Doesn't Exist"


    year_span = soup.find('span', class_='content-utility-curriculum')
    if year_span is not None:
        year_text = year_span.get_text(strip=True)
    else:
        year_text = "Doesn't Exist"

    # Extract the level text
    level_span = soup.find('span', class_='content-utility-level')
    # Find the span with class "content-utility-topic" within the level_span
    if level_span is not None:
        level_text = level_span.find('span', class_='content-utility-topic').text.strip() # type: ignore
    else:
        level_text = "Doesn't Exist"

 
    # Find the introduction paragraphs
    introduction_section = soup.find('h2', class_='article-section', string=['Introduction', 'Overview'])
 
    # Find all paragraphs within the Introduction section
    if introduction_section is not None:
        intro_paragraphs = introduction_section.find_next_siblings('p')
        # Extract the text from the paragraphs
        paragraphs = ''
        for p in intro_paragraphs:
            # Check if the paragraph is within the Example section
            if p.find_parents('figure', class_='example'):
                break
            # Append text from paragraph
            paragraphs += p.get_text(strip=True) + ' '
        table = introduction_section.find_next_sibling('table')
        if table:
            table_rows = table.find_all('tr') # type: ignore
            table_text = ''
            for row in table_rows:
                columns = row.find_all(['th', 'td'])
                row_text = ''
                for column in columns:
                    row_text += column.get_text(strip=True) + '\t'
                table_text += row_text.strip() + '\n'
            # Append table contents to paragraphs
            paragraphs += '\n\nTable Contents:\n' + table_text
    else:
        paragraphs = "Doesn't Exist"
 
    # LOS
    learning_outcomes_section = soup.find('h2', class_='article-section', string='Learning Outcomes')
    if learning_outcomes_section is not None:
        outcomes_section = learning_outcomes_section.find_next_sibling()
        if outcomes_section is not None:
            bullet_points = [li.get_text(strip=True) for li in outcomes_section.find_all('li')] # type: ignore
            bullet = '\n'.join(bullet_points)
        else:
            outcomes_section = learning_outcomes_section.find_next_sibling('p')
            if outcomes_section is not None:
                bullet_points = [p.get_text(strip=True) for p in outcomes_section.find_all('p') if p.get_text(strip=True)] # type: ignore
                bullet = '\n'.join(bullet_points)
            else:
                bullet = "Doesn't Exist"
    else:
        bullet = "Doesn't Exist"


    # Find the <a> tag for Full PDF link
    link_tag = soup.find('a', class_='locked-content')
    # Extract the link
    if link_tag is not None:
        link = link_tag['href'] # type: ignore
        full_link = "https://www.cfainstitute.org" + link # type: ignore
    else:
        full_link = "Doesn't Exist"

    # Summary section
    summary_section = soup.find('h2', class_='article-section', string='Summary')
    if summary_section is not None:
        summary_div = summary_section.find_next_sibling('div')
        if summary_div is not None:
            bullet_points = [li.get_text(strip=True) for li in summary_div.find_all('li')] # type: ignore
            sbullet = '\n'.join(bullet_points)
        else:
            summary_div = summary_div.find_next_sibling('p') # type: ignore
            if summary_div is not None:
                bullet_points = [p.get_text(strip=True) for p in summary_div.find_all('p') if p.get_text(strip=True)]
                sbullet = '\n'.join(bullet_points)
            else:
                sbullet = "Doesn't Exist"
    else:
        sbullet = "Doesn't Exist"
 
       
    # Store all extracted data in list format
    data = [title, topic_text, year_text, level_text, paragraphs, bullet, full_link, sbullet]
   
    return data
   
 
def main():
    # URLs to scrape
    urls = [
        "https://www.cfainstitute.org/membership/professional-development/refresher-readings/time-value-money",
        "https://www.cfainstitute.org/membership/professional-development/refresher-readings/common-probability-distributions",
        "https://www.cfainstitute.org/membership/professional-development/refresher-readings/multiple-regression",
        "https://www.cfainstitute.org/membership/professional-development/refresher-readings/probability-concepts"
    ]
   
    driver = webdriver.Chrome()
 
    data = []
    headers = []
 
    for url in urls:
        driver.get(url)
        data = scrape_content(driver, url)
       
        # Write scraped data to a CSV file
        csv_file = "data/cfa_data.csv"
        with open(csv_file, "a", newline='', encoding='utf-8') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(data)
                time.sleep(2)

    driver.quit()
 
    print("Scraping completed. Data saved to:", csv_file)
 
if __name__ == "__main__":
    main()