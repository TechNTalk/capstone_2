import pandas as pd
import json
import requests;

class Base:
    """
    Class handles all connection to API object and returns a DataFrame from its initialization

    Class will have these methods:
    * return_url: return the api_url that I am currently working on
    * get_data: scrape data from the API and create a DataFrame from it

    """

    def __init__(self):
       self.api_url = "https://newsapi.org/v2/everything?q=keyword&apiKey=cfed43bddf6146daad4f2b3e6651ba82"
       self.get_data()
       self.clean_data()
    

    def return_url(self): #Activates the url
        return self.api_url
    
    def get_data(self):
        """
        Scraping data from the API and creating a DataFrame from it

        """
        api_url = "https://newsapi.org/v2/everything?q=keyword&apiKey=cfed43bddf6146daad4f2b3e6651ba82"
        response = requests.get(api_url)
        response1 = response.json()['articles']
        self.df = pd.DataFrame.from_dict(response1)

    def clean_data(self):
        columns = ['publishedAt', 'content']
        self.df.drop(columns=columns,axis=1,inplace=True)
        name_change = [{'urlToImage':'url_to_image'}]
        for name in name_change:
            self.df.rename(columns=name,inplace=True)
        self.df.source = [self.df['source'][i]['name'] for i in range(len(self.df))]
        self.df.author = self.df['author'].fillna('No author found')
        self.df.url_to_image = self.df['url_to_image'].fillna('No image found')
        columns = ['url_to_image', 'title', 'description', 'url']
        self.df1 = self.df.drop(columns=columns,axis=1)
        self.df1.to_csv("national_news_broadcast_graph.csv", index=False)




if __name__ == "__main__":
    c = Base()
    c.df.to_csv("src/data/national_news_broadcast.csv", index=False)
