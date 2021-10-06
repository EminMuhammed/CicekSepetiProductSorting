import dataprocessing
import model_func
import CicekSepetiScrape

import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 500)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.float_format', lambda x: '%.2f' % x)


def make_all(baseurl, page):
    # scraping
    home_url_list = CicekSepetiScrape.create_home_url(baseurl, page)
    all_product_url_list = CicekSepetiScrape.scrape_all_product_url(home_url_list)
    icerikler = CicekSepetiScrape.get_product(all_product_url_list)
    df = CicekSepetiScrape.convert(icerikler)

    # PROCESSING
    df = dataprocessing.processing(df)
    df = dataprocessing.rating(df)

    model_func.bayes_apply(df)
    model_func.weigthed_apply(df)

    return df

