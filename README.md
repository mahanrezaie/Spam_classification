# Spam Classifier Project

This project implements a spam classifier in four main steps: cleaning the dataset, exploratory data analysis (EDA), data preprocessing, and model building. Additionally, there is a web application to test the spam classifier.

## Steps

### 1. Cleaning the Dataset

The dataset undergoes a cleaning process to handle missing values, remove duplicates, and ensure the data is in a suitable format for analysis.

### 2. Exploratory Data Analysis (EDA)

Exploratory Data Analysis is performed to gain insights into the dataset. This step involves visualizing and summarizing the data to identify patterns and trends that can inform the subsequent steps.

### 3. Data Preprocessing

Data preprocessing involves transforming the raw data into a format suitable for model training. This step includes text preprocessing for the messages, such as tokenization and vectorization.

### 4. Model Building

The spam classifier model is built using a Multinomial Naive Bayes algorithm. The model is trained on the preprocessed data to distinguish between spam and non-spam messages.

## Web App for Testing

The project includes a web application that allows users to input text messages and test whether they are classified as spam or not. The app utilizes the trained model and vectorizer for real-time predictions.

## How to Use

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/spam-classifier.git
   cd spam-classifier

