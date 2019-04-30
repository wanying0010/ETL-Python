import csv


class AbstractRecord:
   def __init__(self, name):
       '''
       the abstract class with one instance which is name
       :param name: name
       '''
       self.name = name


class StockStatRecord(AbstractRecord):
    def __init__(self, name, company_name, exchange_country, price, exchange_rate, shares_outstanding, net_income, market_value_usd, pe_ratio):
        '''
        A record class for stockstat that inherits from AbstractRecord
        to initialize the parameters
        :param name:
        :param company_name:
        :param exchange_country:
        :param price:
        :param exchange_rate:
        :param shares_outstanding:
        :param net_income:
        :param market_value_usd:
        :param pe_ratio:
        '''
        super().__init__(name)
        self.company_name = company_name
        self.exchange_country = exchange_country
        self.price = price
        self.exchange_rate = exchange_rate
        self.shares_outstanding = shares_outstanding
        self.net_income = net_income
        self.market_value_usd = market_value_usd
        self.pe_ratio = pe_ratio

    def __str__(self):
        '''
        :return: values and data for stockstat without bad data
        '''
        return 'StockStatRecord({}, {}, {}, {}, {}, {}, {}, {}, {})'.format(self.name, self.company_name, self.exchange_country, self.price, self.exchange_rate, self.shares_outstanding, self.net_income, self.market_value_usd, self.pe_ratio)


class BaseballStatRecord(AbstractRecord):
    def __init__(self, name, salary, G, AVG):
        '''
        a child class for recording baseballstat that inherits from AbstractRecord
        to initialize the parameters
        :param name: name
        :param salary: salary
        :param G: G
        :param AVG: AVG
        '''
        super().__init__(name)
        self.salary = salary
        self.G = G
        self.AVG = AVG

    def __str__(self):
        '''
        :return: values and data for BaseballStat without bad data
        '''
        return 'BaseballStatRecord({}, {}, {}, {})'.format(self.name, self.salary, self.G, self.AVG)


class AbstractCSVReader:

    def __init__(self, path):
        '''
        an abstract class to read CSV file with the parameter
        :param path:
        '''
        self.path = path

    def row_to_record(self, row):
        '''
        a method to record the row from the CSV
        :param row:
        :return: the row from the CSV as a dictionary
        '''
        raise NotImplementedError

    def load(self):
        '''
        the method to open the CSV file and read each row from the file
        :return: a list of records from each row without bad data
        '''
        records = []
        with open(self.path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    record = self.row_to_record(row)
                    records.append(record)
                except:
                    continue
            return records


class BaseballCSVReader(AbstractCSVReader):

    def row_to_record(self, row):
        '''
        a child class that inherits from AbstractCSVReader for reading baseball CSV file
        to raise BadData exception if the validation fails
        :param row: to validate rows that have missing information, empty names, integers, and float
        :return: a lists of validated records as a dictionary
        '''
        try:
            if(row['PLAYER'].strip() ==""):
                raise BadData
            row['SALARY'] = float(row['SALARY'])
            row['G'] = int(row['G'])
            row['AVG'] = float(row['AVG'])
            record = BaseballStatRecord(row['PLAYER'], row['SALARY'], row['G'], row['AVG'])
            return record
        except:
            raise BadData


class StocksCSVReader(AbstractCSVReader):

    def row_to_record(self, row):
        '''
        a child class that inherits from AbstractCSVReader for reading stocks CSV file
        to raise BadData exception if the validation fails
        :param row: to validate rows that have missing information, empty names, integers, and float
        :return: a list of valiated records as a dictionary
        '''
        try:
            if (row['price'].strip() == ""):
                raise BadData
            if (row['exchange_rate'].strip() == ""):
                raise BadData
            if (row['shares_outstanding'].strip() == ""):
                raise BadData
            row['price'] = float(row['price'])
            row['exchange_rate'] = float(row['exchange_rate'])
            row['shares_outstanding'] = float(row['shares_outstanding'])
            row['net_income'] = float(row['net_income'])
            if row['net_income'] == 0:
                raise BadData

            market_value_usd = row['price'] * row['exchange_rate'] * row['shares_outstanding']
            pe_ratio = row['price'] / row['net_income']

            record = StockStatRecord(row['ticker'], row['company_name'], row['exchange_country'], row['price'],
                                     row['exchange_rate'], row['shares_outstanding'], row['net_income'],
                                     market_value_usd, pe_ratio)
            return record
        except:
            raise BadData


class BadData(Exception):
    pass


def main():
    '''
    to load the path of CSV files for both baseball and stockstat
    to print each record for both files
    '''
    baseballrecords = BaseballCSVReader('/Users/wanyingzhao/Desktop/cs 521-Python/CS521_Project_Part1/MLB2008.csv').load()
    for record in baseballrecords:
        print(record)

    stockstatrecords = StocksCSVReader('/Users/wanyingzhao/Desktop/cs 521-Python/CS521_Project_Part1/StockValuations.csv').load()
    for record in stockstatrecords:
        print(record)


if __name__== "__main__":
    main()
