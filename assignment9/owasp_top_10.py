from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv

# to add options like no windows pop up

options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Enable headless mode
options.add_argument('--disable-gpu')  # Optional, recommended for Windows
options.add_argument('--window-size=1920x1080')  # Optional, set window size

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)


# extract the top 10 security risks

# Task 6: Scraping Structured Data

try:

    # task 6:2 read page
    driver.get("https://owasp.org/www-project-top-ten/")
    
    # task 6:3 Find each of the top 10 vulnerabilities
    top_10_risk = driver.find_element(By.CSS_SELECTOR, 'h2[id="top-10-web-application-security-risks"]')
    if top_10_risk:
        ul_list = top_10_risk.find_element(By.XPATH, "following-sibling::ul")
        if ul_list:
            top_10 = ul_list.find_elements(By.CSS_SELECTOR,'li')
            risks = []
            for risk in top_10:
                link = risk.find_element(By.TAG_NAME, 'a')
                if link:
                    risk_dict = {'Name': link.text, 'Link': link.get_attribute('href')}
                    risks.append(risk_dict)
    
    #  task 6:4 Print out the list and  save data to csv
    print(risks )
            
    with open('./owasp_top_10.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Link"])
        for risk in risks:
            writer.writerow([risk["Name"], risk["Link"]])
    
    
except Exception as e:
    print(f"An error occured: {type(e).__name__} {e}")

finally:
    driver.quit()