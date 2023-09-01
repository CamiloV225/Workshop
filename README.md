# Workshop

## Summary

This repository contains the development and analysis performed on the `candidates.csv` dataset. The dataset contains valuable information about interviewees, encompassing their skill sets and interview details for various job applications. This workshop evaluates your data management skills and your ability to create meaningful visualizations.

This is a small overview of the columns and their data type:
- first_name: varchar
- last_name: varchar
- email: varchar
- application_date: date default current_date
- country: varchar
- yoe: integer
- seniority: varchar
- technology: varchar
- code_challenge_score: integer
- technical_interview_score: integer


## Tools Used

- **Database:** PostgreSQL
- **Data Analysis Language:** SQL
- **Data Visualization:** Python, Matplotlib

## How to Use This Repository

To use this repository, first you will need to have the following software installed:

- PostgreSQL
- Python 3.10
- Jupyter Notebook

Then you will need to download the repository and install the libraries needed to run the code:

1. You can clone the repository with this command: `https://github.com/CamiloV225/Workshop`
2. After that, you can install the following libraries that we will need to run the code:
   - Psycopg2: is the library that allows us to connect our code with Postgres, here you need to use the credentials in order to access the database.
   - Pandas: it will be useful to create a dataframe for easy management.
   - Matplotlib: A useful library to do the graphical analysis.

Once you have the necessary software installed, you can clone the repository to your local machine. Then, open the Jupyter Notebook in the `data-analysis` directory. The notebook contains all of the SQL queries and visualizations for the workshop.

I hope this is what you are looking for. Let me know if you have any other questions.
