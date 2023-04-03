 





import pandas as pd

class CountryCodes:
    
    @staticmethod
    def create_country_codes_map():
        cc = pd.read_html("https://www.iban.com/country-codes")[0]
        cc["Country"] = cc["Country"].str.lower()
        cc.to_csv("./data/country_codes.csv", encoding='utf-8', index=False)
    
    
    @staticmethod
    def to_alpha3(df, columnn):
        country_codes = pd.read_csv("./data/country_codes.csv")
        df[columnn] = df[columnn].str.lower()
        df[columnn] = df[columnn].map(country_codes.set_index('country')['alpha3'])
