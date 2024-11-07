# Movie Reviews Analysis

**In this challenge the New York times and the TMDB Apis' are accessed to retrieve information about movies, the information is 
then processed and transfered to thier respective dataframes after further modifications the dataframes are merged into one and 
saved to a csv file.**

# <font color='blue'>Part 1: Accessing the New York Times API<font>
**In Part one the New York times API is accessed to obtain the reviews of movies from January 1st 2023 and May 31st 2023.
After retrieving the API key form the .env file the query is built and executed, the data is later loaded into the reviews_df.
from which the movie titles are extracted. The movie titles are acquired from the headline.main column, to perform this task we 
used regex patterns by implementing the get_title function. It is worth noting that only 3 entries did not have a discernable 
title and after careful examination only one did not have a title and the two that did were entered manually.**

# <font color='blue'>Part 2: Accessing The Movie Database API<font>
**In Part two the titles obtained from the New York times API are used to get the details from the movie:**

**1-  title                  2-  original title    3-  runtime
4-  production countries   5-  revenue           6-  budget
7-  spoken languages       8-  genres            9-  release date
10- original language      11- homepage          13- vote count
14- vote average           15- overview** 

**To perform this task is a three step process:**

**1- we get the api key from the .env file build and execute the query using the titles obtained from the reviews_df dataframe in json 
   format.**
**2- From the data returned we get the movied id which is then used to build a second query to get the movie details json file.**

**3- Each details file is then processed impletmenting the get_movie_details & the get_nested_info function to retrieve the data points 
   listed above which is then added to list to then create a dataframe.**

# <font color='blue'>Part 3: Merging and Cleaning the Data for Export<font>
**For part three both processed data frames NY Times and the TMDB respectively are merged. The following titles in the  reviews['Title']_df
column were not found while accessing the TMDB api.**
**Missing titles:**
**1- Aulcie                2- Tea With the Dames       3- Rogers Park,
4- If You Love Godard      5- Keep the Change          6- Forever My Girl'
7- Love Beats Rhymes**

**Due to the missing titles the tmdb data frame has less entries thant the reviews data frame, for this reason the merge was executed as a 
'left-merge' with the tmdb_df on the left.**
**The following columns were unpacked utilizing a regex pattern to eliminate the unwanted characters:**
**1- spoken_languages
2- production_countries
3- genres**

**In the final step the merged data frame merged_df was saved without indices to a csv file.**










