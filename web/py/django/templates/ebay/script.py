import datetime
from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection
from ebaysdk.shopping import Connection as Shopping
from ebaysdk.trading import Connection as Trading
# API Call Reference for Finding API
# findCompletedItems
# findItemsAdvanced
# findItemsByCategory
# findItemsByKeywords
# findItemsByProduct
# findItemsIneBayStores
# getHistograms
# getSearchKeywordsRecommendation
# getVersion

# BRAINSTORMING
# I want to get a list of endingsoonest items
# and then I want to sort them by price and number of bidders

# Extract each listing object and convert it to a django model

# Get list of unpaid purchases
# Uses Trading


def getUnpaid():
    api = Trading(config_file="config.yaml")
    response = api.execute('GetUser', {})
    print(response.dict())
    for i in response.dict():
        print(i)

    # print(response.reply)


def quickStartDemo():
    api = Connection(config_file="config.yaml")
    response = api.execute('findItemsAdvanced', {'keywords': 'legos'})
    item = response.reply.searchResult.item[0]

    print(item)


# Corrects the query: poklemon -> pokemon
def correctQuery(query):
    api = Connection(config_file="config.yaml")
    response = api.execute('getSearchKeywordsRecommendation', {
                           'keywords': query})
    items = response.reply
    print(items.keywords)
    return items.keywords


def ebayAuth():
    api = Connection(config_file="config.yaml")
    return api


# user-input query
def inputQuery():
    x = input("Search Query:")
    return correctQuery(x)


if __name__ == "__main__":
    print("hello")
    getUnpaid()
