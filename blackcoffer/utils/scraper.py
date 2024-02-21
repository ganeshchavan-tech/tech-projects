import pandas as pd 
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import nltk
from .constant import DATA_FILE_PATH, INPUT_FILE_PATH

nltk.download('stopwords')

def find_article_content(res):
    """
        Extracts article content from the HTML response.

        ### Parameters:
        - res: HTTP response object.

        ### Returns:
        - str: Extracted article content including title and body.
    """
    try:
        # Parsing of web page.
        soup = BeautifulSoup(res.text,'html.parser')

        # Find article title in h1 or title text.
        title = soup.find('h1') or soup.find('title')

        # Find article paragraphs in 'td-post-content tagdiv-type' class.
        body = soup.find('div', class_='td-post-content tagdiv-type')

        # If body is None, then find article paragraphs in 'td_block_wrap tdb_single_content tdi_130 td-pb-border-top td_block_template_1 td-post-content tagdiv-type' class.
        if not body:
            body = soup.find('div', class_='td_block_wrap tdb_single_content tdi_130 td-pb-border-top td_block_template_1 td-post-content tagdiv-type')
        
        # String to write in data files.
        article_text = f"{title.text}\n\n{body.text}"
        return article_text
    
    except Exception as e:
        # Handle exceptions.
        print(f"Error during content extraction: {e}")
        return "Error: Unable to extract article content."


def fetch_data_to_txt(row):
    """
    Fetches data from a given URL and generates a text file with the article content.
    
    ### Parameters:
    - row (pandas.Series): A row from the dataframe containing URL and URL_ID columns.

    ### Returns:
    None
    """
    url = row['URL']
    url_id = row['URL_ID']

    try:
        # Fetch data from url
        res = requests.get(url=url)

        # If status code is 200, generate and write the data in the text file
        if res.status_code == 200:
            text_content = find_article_content(res)
            with open(DATA_FILE_PATH.format(url_id),'w', encoding='utf-8') as f:
                f.write(text_content)
            print(f"File {url_id}.txt generated.")

        else:
            print(f"Failed to fetch URL: {url} -- HTTP status code: {res.status_code}")

    except Exception as e:
        # Handle exceptions
        print(f"Error while fetching data from {url}: {e}")


def concurrent_url_fetcher():
    """
    Function for fetching data from URLs in parallel using multithreading.
    """
    # Read Input file and generate DataFrame
    input_df = pd.read_excel(INPUT_FILE_PATH)

    # Multithreading to reduce file generation time
    with ThreadPoolExecutor() as executor:
        for _, row in input_df.iterrows():
            executor.submit(fetch_data_to_txt, row)
    return input_df



    