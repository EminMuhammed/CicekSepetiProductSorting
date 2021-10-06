import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 500)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.float_format', lambda x: '%.2f' % x)


def processing(dataframe):
    # drop nan
    dataframe.dropna(inplace=True)

    # edit comments
    dataframe["comment_number"] = [int(i.replace("Yorum", "").replace("(", "").replace(")", "")) for i in
                                   dataframe["comment_number"]]

    # edit price
    dataframe["price"] = [i.replace("\n", "").replace("TL", "") for i in dataframe["price"]]

    # edit rating column
    dataframe["rating"] = [float(i.split("üzerinden")[1].replace("yıldız", "").replace(",", ".")) for i in
                           dataframe["rating"]]

    return dataframe


def rating(dataframe):
    # edit rating stars
    dataframe["5_points"] = [
        int(int(i.split(":")[1].replace("%", "").replace(";", "")) * dataframe.iloc[index, :]["comment_number"] / 100)
        for index, i in enumerate(dataframe["5_points"])]
    dataframe["4_points"] = [
        int(int(i.split(":")[1].replace("%", "").replace(";", "")) * dataframe.iloc[index, :]["comment_number"] / 100)
        for index, i in enumerate(dataframe["4_points"])]
    dataframe["3_points"] = [
        int(int(i.split(":")[1].replace("%", "").replace(";", "")) * dataframe.iloc[index, :]["comment_number"] / 100)
        for index, i in enumerate(dataframe["3_points"])]
    dataframe["2_points"] = [
        int(int(i.split(":")[1].replace("%", "").replace(";", "")) * dataframe.iloc[index, :]["comment_number"] / 100)
        for index, i in enumerate(dataframe["2_points"])]
    dataframe["1_points"] = [
        int(int(i.split(":")[1].replace("%", "").replace(";", "")) * dataframe.iloc[index, :]["comment_number"] / 100)
        for index, i in enumerate(dataframe["1_points"])]

    dataframe["vote_count"] = dataframe["5_points"] + dataframe["4_points"] + dataframe["3_points"] + dataframe[
        "2_points"] + dataframe["1_points"]

    return dataframe
