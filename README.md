# ETL-Python
ETL (Extract, Transform, Load) program in Python

## Motivation
Developed an ETL program in python to extract, transform and load data from CSV files for further analysis.

## Schema
### StockValuations.csv
| Column  | Type |
| ------------- | ------------- |
| ticker | numeric  |
| exchange_country  | string  |
| company_name  | string  |
| price  | numeric  |
| exchange_rate  | numeric  |
| shares_outstanding  | numeric  |
| net_income  | numeric  |

### MLB2008.csv
| Column  | Type |
| ------------- | ------------- |
| PLAYER | string  |
| Record_ID#  | integer  |
| SALARY  | integer  |
| ROOKIE  | integer  |
| POS  | integer  |
| G  | integer  |
| PA  | integer  |
| AB | integer  |
| H  | integer  |
| 1B  | integer  |
| 2B  | integer  |
| 3B  | integer  |
| HR  | integer  |
| TB | integer  |
| BB  | integer  |
| UBB  | integer  |
| IBB  | integer  |
| HBP  | integer  |
| SF  | integer  |
|SH | integer  |
| ROE  | integer  |
| RBI  | integer  |
| LEADOFF_PA | integer  |
| DP  | integer  |
| TP  | integer  |
| WP  | integer  |
| PB | integer  |
| END_GAME  | integer  |
|SO | integer  |
| BK  | integer  |
| RBI  | integer  |
| LEADOFF_PA | integer  |
|SB% | numeric  |
| RUNR  | numeric  |
| D_BPF | numeric  |
| PA% | numeric  |
| D_MLVr  | numeric |
|D_PMLVr  | numeric  |
| D_RPMLVr  | numeric  |
| D_VORPr | numeric  |
| D_MLV  | numeric |

## Scripts
### Part 1
To extract the raw data (row) into a usable format 
* Load the content of the CSV files into usable records
* Use polymorphism to hold data
* Use inheritance to process data

### Part 2
To connect the database and read data
* sqlite3

### Part 3
To perform functions using the extracted records and handle record creation errors

## Installation
[Install python 3.5.3+](https://www.python.org/downloads/)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
