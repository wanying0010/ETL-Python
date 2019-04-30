from csv import DictReader
import queue
import threading
import Project_Part1

stocks_rows = queue.Queue()
stocks_records = queue.Queue()

class Runnable():
    def __call__(self, *args, **kwargs):
        '''
        A callable class named Runnable with the method __call__ which will never end the loop if the condition is true
        Get rows from the stocks_rows queue
        :param args:
        :param kwargs: the timeout parameter to 1 second
        :return: print "working hard!!" to the console and return the stocks records to the new StockStatRecord object
        '''
        print("{} working hard!!!".format(id(self)))
        while(True):
            try:
                row = stocks_rows.get(timeout=1)
            # to end the loop without printing an error when there is an exception of "Empty"
            except queue.Empty:
                break
            try:
                if (row['price'].strip() == ""):
                    raise Zhao_Wanying_Project_Part1.BadData
                if (row['exchange_rate'].strip() == ""):
                    raise Zhao_Wanying_Project_Part1.BadData
                if (row['shares_outstanding'].strip() == ""):
                    raise Zhao_Wanying_Project_Part1.BadData
                row['price'] = float(row['price'])
                row['exchange_rate'] = float(row['exchange_rate'])
                row['shares_outstanding'] = float(row['shares_outstanding'])
                row['net_income'] = float(row['net_income'])
                if row['net_income'] == 0:
                    raise Zhao_Wanying_Project_Part1.BadData

                market_value_usd = row['price'] * row['exchange_rate'] * row['shares_outstanding']
                pe_ratio = row['price'] / row['net_income']

                record = Zhao_Wanying_Project_Part1.StockStatRecord(row['ticker'], row['company_name'], row['exchange_country'], row['price'],
                                         row['exchange_rate'], row['shares_outstanding'], row['net_income'],
                                         market_value_usd, pe_ratio)
            except:
                continue

            stocks_records.put(record)

class FastStocksCSVReader:
    def __init__(self, path_to_csv):
        '''
        An __init__ method which will take the path to the file to be read
        :param path_to_csv: path_to_csv
        '''
        self.path_to_csv = path_to_csv
    def load(self):
        '''
        to open the CSV and read each row from the file
        :return: put each row in the stocks_rows queue
        '''
        with open(self.path_to_csv) as csv_file:
            reader = DictReader(csv_file)
            for row in reader:
                stocks_rows.put(row)
        # create 4 threads, also start and add each new_thread to the thread list
        threads = []
        for i in range(0,4):
            new_thread = threading.Thread(target=Runnable())
            new_thread.start()
            threads.append(new_thread)
        # invoke the join for each new_thread in the list of threads
        for item in threads:
            item.join()
        record_list = []
        # add each record fo stocks_records to a new list and return the list when they are loaded
        while(True):
            try:
                record = stocks_records.get(timeout=1)
            except queue.Empty:
                break;
            record_list.append(record)
        return record_list;

def main():
    '''
    load the CSV file
    :return: print each record with "str.format"
    '''
    records = FastStocksCSVReader("/Users/wanyingzhao/Desktop/cs 521-Python/CS521_Project_Part1/StockValuations.csv").load()
    for item in records:
        print(item)

if __name__=='__main__':
    main()
