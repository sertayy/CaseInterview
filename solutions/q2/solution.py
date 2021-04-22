import pandas as pd
from argparse import ArgumentParser
from collections import Counter
from typing import Dict, List
import logging

TOP = None


def top_products_stores(product_store_df: pd.DataFrame, quantity_dict: Dict[str, int]) -> pd.DataFrame:
    """
    Calculates top seller products or top seller stores according to the given parameters.
    :param product_store_df: dataframe of product.csv or store.csv files
    :param quantity_dict: quantity dictionary of products or stores
    :return: top seller products or top seller stores
    """
    max_pairs: Dict[str, int] = on_equality_func(quantity_dict)
    product_names: List[str] = []
    for pair in max_pairs:
        product_names.append(product_store_df.loc[product_store_df['id'] == pair, 'name'].iloc[0])
    return pd.DataFrame(list(zip(product_names, max_pairs.values())), columns=['name', 'quantity'])


def on_equality_func(quantity_dict) -> Dict[str, int]:
    """
    Adds the equal values to the data frame. In that case the number of rows are more than the top value.
    :param quantity_dict: quantity dictionary
    :return: a dictionary consisting of maximum values
    """
    max_pairs: Dict[str, int] = dict(Counter(quantity_dict).most_common(TOP))
    min_value = min(max_pairs, key=max_pairs.get)
    for product in quantity_dict:
        if product not in max_pairs and quantity_dict[product] == quantity_dict[min_value]:  # on equality case
            max_pairs[product] = quantity_dict[product]
    return max_pairs


def top_brands_cities(quantity_dict: Dict[str, int], product_store_df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """
    Calculates top seller brands or top seller cities according to the given parameters.
    :param quantity_dict: quantity dictionary of products or stores
    :param product_store_df: dataframe of product.csv or store.csv files
    :param column_name: brand or store
    :return: top seller brands or top seller cities
    """
    best_sellers: Dict[str, int] = {}  # can be brand or city
    for key in quantity_dict:  # can be store or product
        brand = product_store_df.loc[product_store_df['id'] == key, column_name].iloc[0]  # can be city
        if brand in best_sellers:
            best_sellers[brand] += quantity_dict[key]
        else:
            best_sellers[brand] = quantity_dict[key]
    max_pairs: Dict[str, int] = on_equality_func(best_sellers)
    return pd.DataFrame(max_pairs.items(), columns=[column_name, 'quantity'])


def calc_quantity(sales_between_dates: pd.DataFrame, key: str) -> Dict[str, int]:
    """
    Calculates the quantity of each product and store.
    :param sales_between_dates: represents the sales in the given date interval
    :param key: product or store
    :return: returns the quantity dictionary of products or stores => {product/store: quantity}
    """
    key_list = list(sales_between_dates[key])
    quantities = list(sales_between_dates["quantity"])
    quantity_dict: Dict[str, int] = {}
    for i in range(len(key_list)):
        if key_list[i] in quantity_dict:
            quantity_dict[key_list[i]] += quantities[i]
        else:
            quantity_dict[key_list[i]] = quantities[i]
    return quantity_dict


def top_sellers(min_date: str, max_date: str):
    """
    Main simulation function.
    :param min_date: lower bound of date
    :param max_date: upper bound of date
    """
    product_df = pd.read_csv("input/product.csv")
    sales_df = pd.read_csv("input/sales.csv")
    store_df = pd.read_csv("input/store.csv")
    date_interval: bool = (sales_df['date'] >= min_date) & (sales_df['date'] <= max_date)
    product_quantity = calc_quantity(sales_df.loc[date_interval], "product")
    store_quantity = calc_quantity(sales_df.loc[date_interval], "store")

    top_seller_product = top_products_stores(product_df, product_quantity)
    print("-- top seller product --")
    print(top_seller_product)

    top_seller_stores = top_products_stores(store_df, store_quantity)
    print("-- top seller store --")
    print(top_seller_stores)

    top_seller_brand = top_brands_cities(product_quantity, product_df, "brand")
    print("-- top seller brand --")
    print(top_seller_brand)

    top_seller_cities = top_brands_cities(store_quantity, store_df, "city")
    print("-- top seller city --")
    print(top_seller_cities)


if __name__ == '__main__':
    try:
        arg_parser = ArgumentParser()
        arg_parser.add_argument("--min-date", type=str, nargs='?', default="2020-01-01",  const="2020-01-01")
        arg_parser.add_argument("--max-date", type=str, nargs='?', default="2020-06-30",  const="2020-06-30")
        arg_parser.add_argument("--top", type=int, nargs='?', default=3,  const=3)
        args = arg_parser.parse_args()
        TOP = args.top
        top_sellers(args.min_date, args.max_date)
    except Exception as ex:
        logging.error("An error occured ==> {0}".format(ex))
        raise ex
