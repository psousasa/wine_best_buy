from pandas.io import json
import requests
import pandas as pd
import random
import time
from config import vivino_url, vivino_body, vivino_header


class KelVino:
    def __init__(self, vivino_header: dict, vivino_body: dict, vivino_url: str) -> None:
        self.vivino_body = vivino_body
        self.vivino_url = vivino_url
        self.vivino_header = vivino_header

    def call_vivino_api(self, page: int) -> requests:
        self.vivino_body['page'] = page
        return requests.get(
            self.vivino_url,
            params = self.vivino_body,
            headers= self.vivino_header
        )

    @staticmethod
    def data_transformation(r: requests) -> json:
        
        results = [
        {
            'Winery': t["vintage"]["wine"]["winery"]["name"],
            'Wine': t["vintage"]["wine"]["name"],
            'Year': t["vintage"]["year"],
            'Region': t["vintage"]["wine"]["region"]["name"],
            'Type': t["vintage"]["wine"]["type_id"], # 1: red | 2: white
            'Rating': t["vintage"]["statistics"]["ratings_average"],
            'num_review': t["vintage"]["statistics"]["ratings_count"],
            'price': t["price"]["amount"]
            
        }
        for t in r.json()["explore_vintage"]["matches"]
    ]
        return results

    def get_wine_data(self, page: int) -> pd.DataFrame:
        r = self.call_vivino_api(page)
        results = self.data_transformation(r)
        return pd.DataFrame(results)


if __name__ == '__main__':
    page = 1
    main_df = pd.DataFrame()
    vivino = KelVino(vivino_header, vivino_body, vivino_url)

    while True:
        time.sleep(random.randint(0, 30) / 10)
        try:
            df = vivino.get_wine_data(page)
        except TypeError:
            df = pd.DataFrame()    

        if main_df.empty:
            main_df = df
        else:
            main_df = pd.concat([main_df, df], ignore_index=True)

        if df.empty:
            break

        page += 1

