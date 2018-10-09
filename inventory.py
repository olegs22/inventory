import numpy as np
import pandas as pd

def inventory():
    val = raw_input('Do you want to start inventory?: ')
    if val == 'no':
        print 'Ok'
        quit()

    num = []
    tags = []
    dict = {'No':num}
    while val != 'exit':
        val = raw_input('Scan an item: ')
        if val == 'exit':
            quit()
        item_quan = input('How many pieces are?: ')
        tags.append(val)
        num.append(item_quan)
        data = pd.DataFrame(dict,index=tags)
        data.to_csv('inventory.csv')
    return None

inventory()
