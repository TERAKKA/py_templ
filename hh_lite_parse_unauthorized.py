import requests

def get_vacancies(keyword):
    url = "https://api.hh.ru/vacancies"
    params = {
        "text": keyword,
        "area": 1,  #(1 - Moscow)
        "per_page": 10,  # Number of vacancies per page
    }
    headers = {
        "User-Agent": "HH-User-Agent"
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        vacancies = data.get("items", [])
        for vacancy in vacancies:
            vacancy_id = vacancy.get("id")
            vacancy_title = vacancy.get("name")
            vacancy_url = vacancy.get("alternate_url")
            company_name = vacancy.get("employer", {}).get("name")
            #salary = salary.get("salary")
            print(f"ID: {vacancy_id}\nTitle: {vacancy_title}\nCompany: {company_name}\nURL: {vacancy_url}\n") #Money: {salary}\n
    else:
        print(f"Request failed with status code: {response.status_code}")

get_vacancies("devops")