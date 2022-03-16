# ml-demo2

This repo contains the code for the Kasna/Eliiza Google ML Specialisation, demo 2.

## Overview

Black Friday is a colloquial term for the Friday following Thanksgiving in the United States and can be seen as the start of the Christmas shopping season. Retail stores aggressively promote sales at discounted prices. This season is crucial for the economy and retails as many consumers hold out for these sales due to the large discounts and great offers. 

For retailers, this is an opportunity to move overstocked items at the lowest possible process and move season items off the shelf. On Black Friday 2021, US consumers spent $8.92 billion at online sales for goods after Thanksgiving. This only just falls short of the previous years record-setting $9.03 billion according to Adobe.

Due to the growing popularity of Black Friday Sales, Retailers spent a significant amount of the year and resources planning their sales to maximise profits.

This demo builds a recommender model to address these business goals. A recommender model seeks to predict the rating or preference of a given item. They can be used accross music plateforms, social media newsfeeds, streaming services etc.


## Get User Inference
To get an inference from the model a query needs to be made to the cloud function with the packet structure: 

```
{
  "User_ID: <Valid User_ID>
}
```

The cloud function will then gather the top 10 Product_IDs the user is most_likely to buy, the User's profile, and Product Information before returning a summation of the Users expected spenditure for the month on these products.
