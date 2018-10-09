import pandas as pd

def inven_count(line):
    val = raw_input('Do you want to start inventory?: ')
    if val == 'no':
        print 'Ok'
        quit()
    tag = raw_input('Start scanning stuf: ')
    num = []
    tags = []
    dict = {'No':num}
    count = 1

    while tag != 'exit':
        val = raw_input('Scan new item: ')

        if val == 'exit':
            tags.append(tag)
            num.append(1)
            data = pd.DataFrame(dict,index=tags)
            data.to_csv('inventory_count.csv')
            upload_line_inventory(line)
            print "File uploaded"
            quit()

        if val != tag:
            tags.append(tag)
            num.append(count)
            data = pd.DataFrame(dict,index=tags)
            data.to_csv('inventory.csv')
            count = 0
            tag = val

        while tag == val:
            val1 = raw_input('Scan new item: ')

            count += 1
            tag = val1

        tags.append(val)
        num.append(count)
        data = pd.DataFrame(dict,index=tags)
        data.to_csv(line+'inventory_count.csv')
        count = 1

    return None
if __name__ == "__main__":
    from file_upload import upload_line_inventory
    line_number = raw_input('What line are you?: ')
    inven_count(line_number)
