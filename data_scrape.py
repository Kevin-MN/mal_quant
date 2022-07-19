import requests as re
import bs4 as bs
import numpy as np
from datetime import datetime
import pandas as pd



def main():
    #make get request to mal
    mal_seasonal = re.get('https://myanimelist.net/anime/season')

    #turn into Beautiful soup object for parsing
    mal_seasonal_html = bs.BeautifulSoup(mal_seasonal.text)

    #create sequential data arrays
    html_seasonal_titles = mal_seasonal_html.find_all('a', {'class':'link-title'})
    html_seasonal_scores = mal_seasonal_html.find_all('div', {'class':'score'})
    html_seasonal_members = mal_seasonal_html.find_all('div', {'class':'member'})


    #create empty array to store extracted data
    seasonal_titles = np.array([])
    seasonal_scores = np.array([])
    seasonal_members = np.array([])

    #store total number of data points fo use throughout program
    seasonal_anime_count = len(html_seasonal_titles)

    for i in np.arange(seasonal_anime_count):
        seasonal_titles = np.append(seasonal_titles, html_seasonal_titles[i].text)
        seasonal_scores = np.append(seasonal_scores, html_seasonal_scores[i].text)
        seasonal_members = np.append(seasonal_members, html_seasonal_members[i].text)

    recorded_datetime = np.repeat(datetime.now(), seasonal_anime_count)
    
    mal_dict = {'anime':pd.Series(seasonal_titles), 'scores':pd.Series(seasonal_scores), 'members':pd.Series(seasonal_members),'datetime':pd.Series(recorded_datetime)}

    seasonal_data = pd.DataFrame(mal_dict)

    reprod = pd.read_csv('seasonal_mal_data2.csv')

    concat_table= pd.concat([seasonal_data, reprod])

    concat_table.to_csv('seasonal_mal_data2.csv', index = False)

main()
print('Scraping has completed with no errors.')


