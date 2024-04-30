# Suicide Rate Analysis and Prediction
![1_sldzYWPPlz08SGK61VRpqA](https://user-images.githubusercontent.com/94312082/190874958-e7062bd6-c402-48ad-a7d5-e83d995dd169.jpeg)

Link to PPT - 

# INTODUCTION
Suicides have become increasingly concerning in today's society, often linked to depression and various external factors. To prevent suicide attempts, machine learning algorithms can be employed to accurately anticipate them. This study aims to analyze suicide rates and the influencing factors using machine learning. Preliminary data analysis will reveal suicide numbers and the relationship between various factors. Graphical representations will be used to better understand the trends in suicide attempts. Multiple machine learning models will be constructed and compared to determine which has the least error. This research investigates how machine learning algorithms can predict suicide rates and the factors that influence them. 
# IMPORTANCE OF CURRENT STUDY

* Timeline of suicide awareness and statistical reporting. Understanding how awareness and statistics have evolved over the years provides insight into how societies are addressing this critical issue.
Geographical variation in suicide rates
* A global overview:It's fascinating to see how different regions around the world are affected by suicide rates differently, influenced by cultural, economic, and social factors.
* Demographic breakdown: Age, gender, and socioeconomic factors**: Analyzing these categories helps identify the most vulnerable groups and tailor prevention strategies effectively.

# EXPECTATIONS FROM CURRENT STUDY
* Data analysis is conducted to categorize data, allowing the development of preventive actions for future application. This analysis can reveal the underlying causes of suicides in a particular state and year, and track changes in suicide rates linked to specific causes. By analyzing and classifying this data, not only can preventive measures be strategized, but it also facilitates comparisons to assess whether there has been an increase or decrease in suicide rates over time. The insights derived from this research might inform various strategies to address the issue. An extensive examination of worldwide suicide data was undertaken, and the subsequent sections are structured to provide a coherent interpretation to the reader.
* The early detection of individuals at risk of suicide is crucial for effective prevention. Machine learning is increasingly being recognized as a viable approach to this end. Our research focuses on developing a machine learning model that predicts suicide attempts. We utilize models such as K Nearest Neighbor, Decision Trees, and Random Forest Regression, and compare their effectiveness in this context.
# OUTCOMES INTENDED TO ACHIEVE  
* This analysis is aimed at explaining how different machine learning algorithms can be used in predicting suicide rates based on relevant factors collected in the dataset.
* The analysis carried out will also provide knowledge about areas of improvement to the government and other organizations working towards suicide prevention and counselling so that effective steps can be taken.
# METHODS AND TECHNIQUES
## Data Acquisition
The Suicide Rates Overview 1985 to 2016 dataset which is taken from Kaggle consists of 27820 rows and 12 columns. It is compiled from four different datasets (United Nations Development Program (HDI), World Bank, World Health Organization, and Szmali) to identify any attributes that correlated with suicide rates globally. The data is readily available and downloadable in CSV format.
## Cleaning and Normalization
After acquiring the dataset, we will remove null values or redundant rows, drop repeated columns, and perform outlier analysis and treatment. Country, year, sex, age and generation are all non-numerical labeled columns that will be transformed to numerical labels using SkLearn's LabelEncoder. Many machine learning estimators need dataset standardization: if the individual features do not resemble standard normally distributed data, they may perform poorly. SkLearn's RobustScaler is used to normalize the numerical columns population, gdp_for_year, and gdp_per_capita.
## Exploratory Data Analysis
In this stage, many data mining techniques are utilized to uncover hidden trends in the dataset and determine the correlation between variables, as well as plot multiple graphs to uncover trends in suicide rates and identify the many causes that contribute to suicide. Several python libraries such as NumPy, seaborn, matplotlib etc. have been used. Various plots have been shown to better visualize the data. Correlations are shown with the help of heatmaps and scatterplots.
## Machine Learning Models
Now we will train multiple machine learning models on our dataset and utilize validation techniques to check for overall fit. Finally, we will present the best model for suicide prediction. K Nearest Neighbor, Decision Tree Regression, Random Forest Regression, XGBoost Regression and Multilayer Perceptrons are implemented and evaluated based on accuracies and RMSE scores.
# IMPLEMENTATION
## Dataset
The dataset has been taken from Kaggle. It has 27,820 rows with 12 columns. Some of the columns are numerical types which include GDP per capita, HDI for year, suicides_no, while others like country, age, sex, generation etc. are categorical. It includes data from over 100 countries from 1985 to 2016.
## Evaluation Metrics
The Evaluation Metrics used are accuracy and RMSE scores. Accuracy is a common evaluation metric for classification problems. It is the number of correct predictions made as a ratio of all predictions made. RMSE is one of the most widely used measures for assessing the precision of continuous data. Because RMSE gives large errors a higher weight than MAE, it should be more useful when large errors are undesirable.
Since XGBoost Regression has the highest accuracy and lowest RMSE, it can be considered the best model.
## Model Training and Evaluation 
Our Machine Learning algorithms are K Nearest Neighbor, Decision Tree, Random Forest, XGBoost, and Multilayer Perceptrons (Deep Learning). Below are the accuracies and RMSE's of each model.

K Nearest Neighbor Regression : Accuracy - 0.771, RMSE- 0.279

Decision Tree Regression : Accuracy - 0.967, RMSE- 0.105

Random Forest Regression - Accuracy - 0.988, RMSE- 0.063

XG Boost Regression - Accuracy - 0.997, RMSE- 0.029


# RESULTS DISCUSSION

Data analysis helped us understand several underlying trends in suicide attempts over the years 1985 and 2016. Coming to the performance of the four machine learning models - Among all the trained models, XGBoost has the highest accuracy and lowest RMSE. This is because XGBoost is very good in execution Speed & model performance. Random forest had an accuracy of 98.9%, followed by Decision Tree, Multilayer Perceptrons and K-Nearest Neighbors with 96.7, 88.7 and 77.1 % respectively.

# CONCLUSION 

This analysis was aimed at explaining how different machine learning algorithms can be used in predicting suicide rates based on relevant factors collected in the dataset. Although there have been several successful high precision models, there is still potential for development. Preliminary data analysis showed some surprising findings which includes teen men are more likely to commit suicide. Machine learning algorithms like XGBoost and Random Forest Regression consistently outperformed other algorithms and had the highest accuracy and precision. The analysis carried out will also provide knowledge about areas of improvement to the government and other organizations working towards suicide prevention and counselling so that effective steps can be taken.

# FUTURE WORK

* This project can be further improvised by combining multiple data sets related to suicides and performing in-depth analysis.
* Some statistical tests- hypothesis testing can be performed which can extract valuable insights.
* Sentiment Analysis can be used to figure out in which social media people feel more free to talk about their mental health.

# REFERENCES

Boudreaux, E. D., Rundensteiner, E., Liu, F., Wang, B., Larkin, C., Agu, E., Ghosh, S., Semeter, J., Simon, G., & Davis-Martin, R. E. (2021). Applying Machine Learning Approaches to Suicide Prediction Using Healthcare Data: Overview and Future Directions. Frontiers in psychiatry, 12, 707916. https://doi.org/10.3389/fpsyt.2021.707916

Gen-Min Lin, Masanori Nagamine, Szu-Nian Yang, Yueh-Ming Tai, Chin Lin, Hiroshi Sato, “Machine Learning Based Suicide Ideation Prediction for Military Personnel”, IEEE Journal of Biomedical and Health Informatics, vol. 24, issue: 7, July 2020

Hasmitha Bhutham, “Suicide rates analysis and prediction” , December 2020.

Mrs. B. Ida Seraphim , Subroto Das , Apoorv Ranjan, 2021, A Machine Learning Approach to Analyze and Predict Suicide Attempts, INTERNATIONAL JOURNAL OF ENGINEERING RESEARCH & TECHNOLOGY (IJERT) Volume 10, Issue 04 (April 2021).
