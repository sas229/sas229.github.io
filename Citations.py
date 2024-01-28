from bs4 import BeautifulSoup as bs
import requests 
import numpy as np
import matplotlib.pyplot as plt

url = "https://scholar.google.com/citations?user=CFA0lFsAAAAJ&hl=en"
html = requests.get(url).text
soup = bs(html, 'html.parser')

cites_html = soup.findAll("span", class_="gsc_g_al")
years_html = soup.findAll("span", class_="gsc_g_t")

citations = np.empty(len(cites_html))
years = np.empty(len(cites_html))
for i in range(len(cites_html)):
    cite_i = cites_html[i]
    year_i = years_html[i]
    citation=int(cite_i.text.strip())
    year=int(year_i.text.strip())
    citations[i] = citation
    years[i] = year
    
plt.bar(years, citations)
plt.bar(years, np.cumsum(citations))
plt.show()
        
