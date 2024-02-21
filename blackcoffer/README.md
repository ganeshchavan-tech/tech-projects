# Blackcoffer: Data Extraction and NLP

## Introduction
The script extracts textual data from given URLs, conducting a comprehensive text analysis to compute variable scores.

**Approach:**

1. Utilize the pandas library to read the Excel file, generating a DataFrame containing URL and URL ID information.

2. Leverage the BeautifulSoup library for parsing HTML output.

3. Employ multithreading with the concurrent fetching of data from URLs, storing the results in the 'ArticleFiles' folder. Utilize a multithreading pool executor to optimize execution time.

4. Generate a list of custom stopwords by reading a dedicated stopwords file.

5. Iterate over each URL ID to perform an in-depth analysis of each article.

6. Develop distinct functions for calculating various variables, ensuring modularity and maintainability.

7. Perform sentiment analysis and readability analysis on the fetched data, incorporating custom stopwords for enhanced accuracy.

8. Convert the resulting list of dictionaries into a structured DataFrame for further analysis and presentation.

9. Generate the final output in the form of a CSV file, providing a comprehensive record of the computed variable scores.

This approach combines the efficiency of concurrent data fetching, the power of external libraries for HTML parsing, and a structured analysis process to yield meaningful insights from the extracted textual data. The modular design facilitates easy maintenance and scalability, while the final output in CSV format ensures accessibility and compatibility with various data analysis tools.

## Instructions

Before running the script, ensure you have the following set up:

1. **Python:** Installed on your machine (version 3.12.1 recommended).
2. **ArticlesFile Folder:** To store data txt files.
3. **`input.xlsx` File:** Excel file containing columns 'URL_ID' and 'URL' with associated data.
4. **MasterDictionary Folder:** Contains a txt file of positive and negative words.
5. **StopWords Folder:** Contains a txt file of stopwords.
6. **Constant Variables:** Setup the constant variables in `./utils/constant.py` file

## Dependencies:
- `pandas`
- `openpyxl`
- `requests`
- `bs4`
- `nltk`

## Installation

1. Download the Repository as a zip file.
2. Extract the zip file.
3. Open a terminal and navigate to the 'blackcoffer' directory.
4. Install Dependencies:
    ```
    pip install -r requirements.txt
    ```
5. Run the script by executing the following command:
    ```
    python3 main.py
    ```

# Result:
- It will generate raw article text files in the 'ArticleFiles' folder.
- It will generate an 'Output Data Structure' file containing text analysis scores.

# Contributors
**Ganesh Chavan:** chavanganesh229@gmail.com
