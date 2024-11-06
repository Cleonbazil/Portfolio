# SpooderApp™ Guide

## *Introduction*

**SpooderApp™** began as a dream. A simple dream. Or... More accurately it began as a not-so-simple school project with such a broad scope that it needed to be narrowed down to a more attainable dream. One of utilizing existing customer feedback to help small and large businesses, alike, gain deeper insight towards avenues of improvement. Sure, a business owner could spend hours scrolling through their **Google Reviews**, but what if there was a faster way? A *simpler* way?

Enter **SpooderApp™**! Powered by our `roberto` Transformer, and our `davidlingo` OpenAI LangChain, **SpooderApp™** utilizes Selenium and BeautifulSoup to scrape available reviews on your behalf. Leverage the power of Machine Learning (ML) and Natural Language Processing (NLP) to take the guesswork and time commitment *out* of comprehending your customers' feedback!

## *How to Use*

1. Select a business from the dropdown menu at the top left of the interface.
2. View the rating statistics (including average ratings and total available reviews) and an interactive map of business locations.
3. Explore the reviews, their sentiment, and dynamic feedback provided by **SpooderApp™**.

## *Features*

- **Interactive Map:**
    - View the all the available locations for a selected business in one, easy to understand map.
- **Sentiment Analysis:**
    - Get a general feel for how customers and consumers feel about a selected business.
- **Feedback:**
    - Receive feedback tailored to the available reviews for a selected business.

#### *Under the Hood*

So how does it work? Simple! *(At least in theory...)*

By fine-tuning a pre-trained `distilbert-base-uncased` Transformer, we built our sentiment analysis model, `roberto`, to gauge the individual mood of each review for a selected business -  as well as provides the model's confidence in that gauging. The overall general sentiment is then classified through simple logic *(read: comparing the sum totals among the sentiment labels of "positive", "neutral", and "negative")*, and an average *(read: mean)* confidence score in that sentiment is provided in line.

Detailed web scraping then provided the sample set of businesses used for this demonstration. The reviews parsed through that process were then prepared and fed into `davidlingo`, our OpenAI LangChain powered by `gpt-3.5-turbo`, to provide customized feedback based on each individual business' needs.

#### *Limitations*

As noted, this demonstration provides a curated selection of businesses to illustrate the power of leveraging ML and NLP for improvements. Due to the time frame in which **SpooderApp™** had for development, no further data is available at this time.  Additionally, only up to fifty (50) reviews were scraped per business, which - admittedly - affects the available data to be fed into `davidlingo`. And while `roberto` provides a mean accuracy of around eighty percent (~80%) in labeling reviews as "positive", "neutral", or "negative", the sample size it was trained on may affect its confidence in "neutral" and "negative" classifications.

#### *Future Considerations*

If given more time to develop its features further, **SpooderApp™** was envisioned to meet the following milestones;
- Allow for ad hoc searches of businesses and real-time web scraping
- Retrieve a complete list of available reviews in lieu of the sampled up-to-fifty (=< 50)
- Train `roberto` on a larger dataset than the six thousand (6,000) reviews provided
- Brand and logo development (because a cute little spooder logo would be too adorable for words)

## *Contact*

For any questions, support, or interest in further development, please contact the development team through the project manager at [odelepax@gmail.com](mailto:odelepax@gmail.com?subject=SpooderApp%20Inquiry).