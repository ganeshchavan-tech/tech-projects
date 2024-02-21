from utils.scraper import concurrent_url_fetcher
import pandas as pd
from utils.sentiment_analysis_utils import data_analyser
from utils.constant import OUTPUT_DATA_STRUCTURE_FILE_PATH

def main():
    """
    This function is the main workflow of the program, including concurrent URL fetching,
    sentiment analysis, data conversion, and the generation of a final CSV output file.

    Workflow Steps:
    1. Concurrently fetch data from URLs and store it in the ArticleFiles folder.
    2. Perform sentiment analysis on the fetched data.
    3. Convert the list of dictionaries into a DataFrame.
    4. Generate the final output in a CSV file.

    The function does not take any parameters.

    Output:
    The final output is a CSV file containing the analyzed data, and it is saved at the specified path.
    """

    # Fetch the data from URLs concurrently and store in the ArticleFiles folder.
    print("Article data fetching started...")
    df = concurrent_url_fetcher()
    print("Successfully generated the data text files.")

    # Perform sentiment analysis on the fetched data.
    print("Performing Sentiment Analysis and Analysis of Readability...")
    all_article_score = data_analyser(df)
    print("Analysis Completed.")

    # Convert the list of dictionaries into a DataFrame.
    main_data = pd.DataFrame(all_article_score)

    # Generation of final output in CSV file.
    main_data.to_csv(OUTPUT_DATA_STRUCTURE_FILE_PATH,index=False)

    print(f"Successfully generated the {OUTPUT_DATA_STRUCTURE_FILE_PATH} file.")


if __name__ == "__main__":
    main()