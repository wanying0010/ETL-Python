import sqlite3
import Zhao_Wanying_Project_Part1
from collections import deque

class AbstractDAO:
    def __init__(self, db_name):
        '''
        create a base class called AbstractDAO with the parameter db_name
        :param db_name: db_name = db_name
        '''
        self.db_name = db_name

    def insert_records(self, records):
        '''
        the raise notimplementederror makes the child classes to implement their own methods
        :param records:
        '''
        raise NotImplementedError

    def select_all(self):
        '''
        the raise notimplementederror makes the child classes to implement their own methods
        '''
        raise NotImplementedError

    def connect(self):
        '''
        this method allows the file to connect to the db_name database and return the connection
        '''
        conn = sqlite3.connect(self.db_name)
        return conn


class BaseballStatsDAO(AbstractDAO):
    def insert_records(self, records):
        '''
        A child class that inherits from the base class
        :param records: BaseballStatsRecords
        :return: a list of records and execute the table to insert rows and records
        '''
        conn = self.connect()
        cursor = conn.cursor()
        for record in records:
            cursor.execute("INSERT INTO baseball_stats VALUES (?, ?, ?, ?)", (record.name, record.G, record.AVG, record.salary))
        conn.commit()
        conn.close()

    def select_all(self):
        '''
        invoke the connection
        :return: all the rows from the table
        '''
        conn = self.connect()
        cursor = conn.cursor()
        baseball_deque = deque()
        rows = cursor.execute("SELECT * FROM baseball_stats")
        for row in rows:
            record = Zhao_Wanying_Project_Part1.BaseballStatRecord(row[0],row[3], row[1], row[2])
            baseball_deque.append(record)
        conn.close()
        return baseball_deque

class StockStatsDAO(AbstractDAO):
    def insert_records(self, records):
        '''
        a child class inherits from AbstractDAO
        :param records: StockStatRecords
        :return: a list of records and execute the table to insert rows and records
        '''
        conn = self.connect()
        cursor = conn.cursor()
        for record in records:
            cursor.execute("INSERT INTO stock_stats VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                           (record.company_name, record.name, record.exchange_country,
                            record.price, record.exchange_rate, record.shares_outstanding,
                            record.net_income, record.market_value_usd, record.pe_ratio
                            ))
        conn.commit()
        conn.close()

    def select_all(self):
        '''
        invoke the connection
        :return: all the rows from the table
        '''
        conn = self.connect()
        cursor = conn.cursor()
        stock_deque = deque()
        rows = cursor.execute("SELECT * FROM stock_stats")
        for row in rows:
            record = Zhao_Wanying_Project_Part1.StockStatRecord(row[1], row[0], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
            stock_deque.append(record)
        conn.close()
        return stock_deque

def main():
    # read baseball data from CSV
    baseballrecords = Zhao_Wanying_Project_Part1.BaseballCSVReader(
        '/Users/wanyingzhao/Desktop/cs 521-Python/CS521_Project_Part1/MLB2008.csv').load()

    # create connection and insert baseball data to the database
    bb_dao = BaseballStatsDAO('baseball.db')
    bb_dao.insert_records(baseballrecords)

    # get all records from database
    bb_stats_records = bb_dao.select_all()

    # initiate variables
    baseball_total_salary = {}
    baseball_average_salary = {}

    # gather data
    for record in bb_stats_records:
        average = round(record.AVG, 3)
        if(average in baseball_total_salary):
            baseball_total_salary[average].append(record.salary)
        else:
            baseball_total_salary[average] = [record.salary]

    # calculate the average
    for key, salary in baseball_total_salary.items():
        baseball_average_salary[key] = sum(salary) / len(salary);

    # print the average
    for avg, salary in baseball_average_salary.items():
        print("{0:.3f}".format(avg), "{0:,.2f}".format(salary))

    # get records from CSV file
    stock_records = Zhao_Wanying_Project_Part1.StocksCSVReader("/Users/wanyingzhao/Desktop/cs 521-Python/CS521_Project_Part1/StockValuations.csv").load()
    stock_stats_dao = StockStatsDAO('stocks.db')

    # insert records
    stock_stats_dao.insert_records(stock_records)
    stock_stats_records = stock_stats_dao.select_all()
    countries = {}

    # count the countries and print the country and the count
    for record in stock_stats_records:
        if record.exchange_country in countries:
            countries[record.exchange_country] += 1
        else:
            countries[record.exchange_country] = 1
    for country, count in countries.items():
        print(country, count)
if __name__ == "__main__" :
    main()

