import requests
import pandas as pd
import random
import time


def call_vivino(page):
    r = requests.get(
        "https://www.vivino.com/api/explore/explore?wine_type_ids[]=2",
        params={
            "country_code": "PT",
            "country_codes[]": "pt",
            "currency_code": "EUR",
            "min_rating": "3",
            "page": page,
            "grape_filter": "varietal",
            "price_range_max": "25",
            "price_range_min": "2",
            "wine_type_ids[]": "1",
        },
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0"
        }
    )

    results = [
        {
            'Winery': t["vintage"]["wine"]["winery"]["name"],
            'Wine': t["vintage"]["wine"]["name"],
            'Year': t["vintage"]["year"],
            'Region': t["vintage"]["wine"]["region"]["name"],
            'Type': t["vintage"]["wine"]["type_id"],  # 1: red | 2: white
            'Rating': t["vintage"]["statistics"]["ratings_average"],
            'num_review': t["vintage"]["statistics"]["ratings_count"],
            'price': t["price"]["amount"]

        }
        for t in r.json()["explore_vintage"]["matches"]
    ]

    return pd.DataFrame(results)


page = 1
main_df = pd.DataFrame()

while True:
    time.sleep(random.randint(0, 30) / 10)
    df = call_vivino(page)

    if main_df.empty:
        main_df = df
    else:
        main_df = pd.concat([main_df, df], ignore_index=True)

    if df.empty:
        break

    page += 1
