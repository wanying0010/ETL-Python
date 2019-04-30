import sqlite3

def main():
    '''
    connect the file to the database, and create two tables named baseball_stats and stock_stats
    :return: Baseball_stats shows and returns the columns include player_name, games_played, average, and salary
             Stock_stats shows and returns the columns include company_name, ticker, exchange_country, price, exchange_rate, share_outstanding, net_income, market_value_usd, and pe_ratio
    '''

    conn = sqlite3.connect('baseball.db')

    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS baseball_stats
                 (player_name text, games_played int, average real, salary real)''')

    conn.close()

    conn = sqlite3.connect('stocks.db')

    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS stock_stats
                     (company_name text, ticker text, exchange_country text, price real, exchange_rate real, shares_outstanding real, net_income real, market_value_usd real, pe_ratio real)''')

    conn.close()




if __name__== "__main__":
    main()
