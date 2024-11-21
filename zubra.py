import requests
from bs4 import BeautifulSoup as BS
import pandas  as pd
url = "https://www.zaubacorp.com/company-by-address/Hyderabad"
response = requests.get(url)
if response.status_code!= 200:
    print("failed to fetch page ")
else:
    soup = BS(response.contxt,'html:parser')
    company_table = soup.find('table',{'class':'table'})
    if company_table:
        rows = company_table.find_all('tr')
        company_data=[]
        for row in rows[1:]:
            columns = row.find_all('td')
            if len(columns)>=4:
                company_name=columns[0].text.strip()
                email = columns[1].text.strip()
                address = columns[2].text.strip()
                founder_name = columns[3].text.strip() if len(columns) > 3 else ''
                
                
                company_data.append({'Company name':'company_name','Email':'email','Address':'address','Founder name':'founder_name'})
        df=pd.Dataframe(company_data)
        df.to_excel('Hyderabad_companies.xlsx',index = False , engine = 'openpyxl')

        print("Data saved to Hyderabad_companies.xlsx")
    else: 
        print("Failed to find the company table on the page ")
