
# SUICIDE RATE ANALYSIS

## INTRODUCTION AND MOTIVATION
----

Suicide rates have become a significant concern in modern society, particularly as they are often linked to depression. Other contributing factors include economic issues, social pressures, and terminal illnesses. To combat this, AI-based chatbots have been developed with an approximate accuracy of 75% to deter individuals from taking their own lives. Moving forward, it's crucial to harness machine learning techniques to more precisely predict suicide attempts. Initial data analysis would explore the number of suicides and examine how various factors correlate and contribute to these incidents. The study would also include visual representations to better understand patterns in suicide attempts. By employing various Python libraries and building multiple models, the research aims to identify the model with the lowest error rate. This study focuses on forecasting suicide rates and understanding the influential factors through machine learning algorithms.

----

## DATASET DESCRIPTION

1. Data Source: **https://www.kaggle.com/datasets/russellyates88/suicide-rates-overview-1985-to-2016**
2. Data Size  : **3MB**
3. Data Shape : **30000 Rows and 12 Columns** 
4. Time Period: **1985 to 2016**
5. Dataset Columns

| No. | Variable               | Type     |
|-----|------------------------|----------|
| 1   | country                | object   |
| 2   | year                   | int64    |
| 3   | sex                    | object   |
| 4   | age                    | object   |
| 5   | suicides_no            | int64    |
| 6   | population             | int64    |
| 7   | suicides/100k pop      | float64  |
| 8   | country-year           | object   |
| 9   | HDI for year           | float64  |
| 10  | gdp_for_year ($)       | object   |
| 11  | gdp_per_capita ($)     | int64    |
| 12  | generation             | object   |
----

## NEED OF CURRENT STUDY

* The World Health Organization reports that annually, about 800,000 people commit suicide, ranking it as the 18th leading cause of death globally. In the United States, it was the tenth leading cause of death in 2018, contributing to a decline in the country's average life expectancy. Suicide impacts individuals across all age groups worldwide. It is estimated that for every adult who dies by suicide, there are over 20 others who attempt it. The majority of suicides, about 79%, occur in low- and middle-income countries.

* Today, many people face severe physical and mental health challenges due to various internal and external factors. Depression commonly affects individuals in their 30s and 40s, but it is also prevalent among children and the elderly, often triggered by academic pressures and social relationships. The stigma associated with mental illness in many societies leads those affected to hide their conditions. Economic instability, along with drug and alcohol abuse, also plays a significant role in self-harm and suicide attempts.

* The initial step in suicide prevention is often seen as a classification challenge, where the goal is to accurately identify individuals at risk of suicide within a specific timeframe to enable timely intervention. However, the most comprehensive meta-analysis, which reviewed 365 studies, indicated that predictions based on individual risk or protective factors have low accuracy and have shown little improvement over time.

----

## Anticipated Outcomes of Current Study

* The current study aims to utilize data analysis to categorize information, providing insights into the causes of suicide within specific regions and timeframes. By examining trends in suicide rates and their underlying causes, the research seeks to inform future preventive measures. Additionally, the study intends to assess whether the incidence of suicide has risen or fallen over time, allowing for comparisons and the development of effective strategies.

* The findings of this investigation can be applied across various approaches to address the issue of suicide prevention. Through a comprehensive review of global suicide data, the study offers organized insights for readers. Early detection of individuals at risk of suicide is crucial for prevention efforts, and machine learning is being explored as a potential tool for this purpose. Our research focuses on developing machine learning models, such as K Nearest Neighbor, Decision Trees, and Random Forest Regression, to predict suicide attempts. The study evaluates the effectiveness of these algorithms in identifying at-risk individuals.
