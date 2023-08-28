import psycopg2
import matplotlib.pyplot as plt
import pandas as pd

def connect_postgres():
    connection = psycopg2.connect(
        database="Taller",
        user="postgres",
        password="Ronny1212",
        host="localhost",
        port=5432
    )
    return connection
    print("Database connection ok")

def create_table():
    connection = connect_postgres()
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE candidates (
        first_name varchar(255),
        last_name varchar(255),
        email varchar(255),
        application_date DATE DEFAULT CURRENT_DATE,
        country varchar(255),
        yoe integer,
        seniority varchar(255),
        technology varchar(255),
        code_challenge_score integer, 
        technical_interview_score integer
    )""")

    connection.commit()
    cursor.close()
    connection.close()


def insert_to_table():
    connection = connect_postgres()
    cursor = connection.cursor()
    with open("C:/Users/camil/OneDrive/Escritorio/ETL/candidates.csv", "r") as f: 
        next(f)
        cursor.copy_from(f, "candidates", sep=";")
    connection.commit()
    cursor.close()
    connection.close()

def Query1():
    connection = connect_postgres()
    cursor = connection.cursor()
    cursor.execute("SELECT technology, COUNT(*) AS resultado_tech FROM candidates WHERE code_challenge_score >= 7 AND technical_interview_score >=7 GROUP BY technology")
    results = cursor.fetchall()
    tecnologies = []
    for row in results:
        tecnologies.append(row)

    departments = [tupla[0] for tupla in tecnologies]
    employees = [tupla[1] for tupla in tecnologies]

    plt.pie(employees, labels=departments)
    plt.title("Employee Count by Department")
    plt.show()


def Query2():
    connection = connect_postgres()
    cursor = connection.cursor()
    cursor.execute("SELECT EXTRACT(year FROM application_date) AS year, COUNT(application_date) AS conteo FROM candidates WHERE code_challenge_score >= 7 AND technical_interview_score >=7 GROUP BY year")
    results = cursor.fetchall()
    year = []
    for row in results:
        year.append(row)


    years = [tupla[0] for tupla in year]
    employees = [tupla[1] for tupla in year]
    colors = ["#09607d", "#2b3266", "#1d7d72","#1d7d72","#3f1d7d"]
    plt.barh(years,employees, color = colors)
    plt.title("Employee Count by year")
    plt.show()

def Query3():
    connection = connect_postgres()
    cursor = connection.cursor()
    cursor.execute("SELECT seniority, COUNT(seniority) AS resultado_seniority FROM candidates WHERE code_challenge_score >= 7 AND technical_interview_score >=7 GROUP BY seniority")
    results = cursor.fetchall()
    seniorits = []
    for row in results:
        seniorits.append(row)

    seniorit = [tupla[0] for tupla in seniorits]
    employees = [tupla[1] for tupla in seniorits]
    colors = ["#09607d", "#2b3266", "#1d7d72","#1d7d72","#3f1d7d"]
    plt.bar(seniorit,employees, color=colors)
    plt.title("Employee Count by Seniority")
    plt.show()

def Query4():
    countries_list = ['United States of America', 'Brazil', 'Colombia', 'Ecuador']
    colors = ["#09607d", "#2b3266", "#1d7d72","#1d7d72","#3f1d7d"]
    connection = connect_postgres()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT country, COUNT(country) as co, CAST(EXTRACT(year FROM application_date)AS INT) AS year
        FROM candidates
        WHERE country IN ('United States of America', 'Brazil', 'Colombia', 'Ecuador')
        AND code_challenge_score >= 7
        AND technical_interview_score >=7
        GROUP BY country, year
        ORDER BY year
    """)
    results = cursor.fetchall()
    countries =[]
    for row in results:
        countries.append(row)
    df = pd.DataFrame(countries)
    df.columns = ['country','employes','year']
    print(df)
    plt.figure(figsize=(10, 6))
    #
    for country in countries_list:
        by_country = df[df['country'] == country]
        plt.plot(by_country['year'], by_country['employes'], marker='o', label=country)
        
    plt.xlabel('Year')
    plt.ylabel('Hires_count')
    plt.title('Hires by country over years')
    plt.legend(df['country'].unique())
    plt.xticks(df['year'].unique())
    plt.show()

if __name__ == "__main__":
    connection = connect_postgres()

    Query4()

