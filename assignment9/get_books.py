# TASK 2:3 Find the HTML element for a single entry in the search results list. 

# li cp-search-result-item 

# TASK 2:4 Within that element, find the element that stores the title

# span title-content 

# TASK 2:5 Within the search results li element, find the element that stores the author.  
# Hint: This is a link.  Note the class value and save it.  
# Some books do have multiple authors, so you'll have to handle that case.

# a author-link

# TASK 2:6 Within the search results li element, find the element that stores the format of the book and the year it was published. 
# Note the class value and save it.  Now in this case, the class might not be enough to find the part of the li element you want. 
# So look at the div element that contains the format and year. 
# You want to note that class value too.

# span display-info-primary
# div cp-format-info


# TASK 3: Write a Program to Extract this Data


# task 3:1 
# Initialize selenium and the appropriate driver


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import json
import time
# to add options like no windows pop up

options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Enable headless mode
options.add_argument('--disable-gpu')  # Optional, recommended for Windows
options.add_argument('--window-size=1920x1080')  # Optional, set window size

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)

# Task 3:4 Within your program, create an empty list called results.  
# You are going to add dict values to this list, one for each search result.

results = []

# Task 3:2
#  fetch a web page

try:

    driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")

# Task 3:3 Find all the li elements in that page for the search list results
# li cp-search-result-item 


    

    while True:
        
        time.sleep(2)  # pause between pages
        search_list_results = driver.find_elements(By.CSS_SELECTOR, 'li.cp-search-result-item')
        print(len(search_list_results))
    
   

    
# Task 3:5 Main loop: You iterate through the list of li entries. 
# For each, you find the entry that contains title of the book, and get the text for that entry. 
# Then you find the entries that contain the authors of the book, and get the text for each. 
# If you find more than one author, you want to join the author names with a semicolon ; between each.  
# Then you find the div that contains the format and the year, 
# and then you find the span entry within it that contains this information.  You get that text too.  
# You now have three pieces of text.  Create a dict that stores these values, with the keys being Title, Author, and Format-Year.  
# Then append that dict to your results list.
        
        
        for result in search_list_results:
            
            book_dict = {}

        # title
        
            try:
                book_title = result.find_element(By.CSS_SELECTOR,'span.title-content')
                if book_title:
                    book_dict['Title'] = book_title.text.strip()
                else:
                    book_dict['Title'] = 'no title'
        
        # author
          
                book_authors = result.find_elements(By.CSS_SELECTOR,'a.author-link')
                if book_authors:
                    book_dict['Author'] = '; '.join([author.text.strip() for author in book_authors])
                else:
                    book_dict['Author'] = 'no author'
            
            
        # Format-Year
            
                book_format_year_div = result.find_element(By.CSS_SELECTOR,'div.cp-format-info')
                book_format_year = book_format_year_div.find_element(By.CSS_SELECTOR,'span.display-info-primary ')
                if book_format_year:
                    book_dict['Format-Year'] = book_format_year.text.strip()
                else:
                    book_dict['Format-Year'] = 'no format/year'
                    
            except Exception as e:
                print(f"An error occured: {type(e).__name__} {e}")
    
            results.append(book_dict)
            
        # Try clicking the "Next" button
        try:
            next_button = driver.find_element(By.CSS_SELECTOR, 'li.pagination__next-chevron a')
            next_button.click()
        except Exception:
            break  # "Next" button not found, assume last page
            
            
        
    # TASK 3:6 Create a DataFrame from this list of dicts.  Print the DataFrame.
    # print(results)
    df = pd.DataFrame(results)
    print(df)
    
    
# TASK 4: Write out the Data

# TASK 4:1 Write the DataFrame to a file called get_books.csv within the assignment9 folder

    df.to_csv("./get_books.csv")
    

# TASK 4:2 Write the results list out to a file called get_books.json, also within the assignment9 folder.  
# You should write it out in JSON format.

    with open("./get_books.json", "w") as json_file:
        json.dump(results, json_file, indent=4)


except Exception as e:
    print(f"An error occured: {type(e).__name__} {e}")

finally:
    driver.quit()