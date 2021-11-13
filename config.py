vivino_url = "https://www.vivino.com/api/explore/explore?wine_type_ids[]=2"
vivino_body = {
            "country_code": "PT",
            "country_codes[]":"pt",
            "currency_code":"EUR",
            "min_rating":"3",
            "page": None,
            "grape_filter":"varietal",
            "price_range_max":"25",
            "price_range_min":"2",
            "wine_type_ids[]":"1",            
        }
vivino_header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0"}