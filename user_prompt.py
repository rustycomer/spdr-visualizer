from rich.console import Console
from rich.table import Column, Table
import os
import time


# Display Table Set Up
console = Console(color_system='standard')
table = Table(show_header=True, header_style="bold red")
table.add_column("Choice", style="dim")
table.add_column("Sector")

table.add_row('1',  'XLC (Communication Services)')
table.add_row('2',  'XLY (Consumer Discretionary)')
table.add_row('3',  'XLP (Consumer Staples)')
table.add_row('4',  'XLE (Energy)')
table.add_row('5',  'XLF (Financials)')
table.add_row('6',  'XLV (Health Care)')
table.add_row('7',  'XLI (Industrials)')
table.add_row('8',  'XLB (Materials)')
table.add_row('9',  'XLRE (Real Estate)')
table.add_row('10', 'XLK (Technology)')
table.add_row('11', 'XLU (Utilities)')
table.add_row('Q',  'Quit')


def clear_console():
    console.clear()


# Gathering and Handling User Input
def user_input():
    console.print(table)
    user_choice = input('Please enter the number of your choice: ').lower()
    if user_choice == '1':
        return 'https://www.sectorspdr.com/sectorspdr/IDCO.Client.Spdrs.Portfolio/Export/ExportCsv?symbol=xlc'
    elif user_choice == '2':
        return 'https://www.sectorspdr.com/sectorspdr/IDCO.Client.Spdrs.Portfolio/Export/ExportCsv?symbol=xly'
    elif user_choice == '3':
        return 'https://www.sectorspdr.com/sectorspdr/IDCO.Client.Spdrs.Portfolio/Export/ExportCsv?symbol=xlp'
    elif user_choice == '4':
        return 'https://www.sectorspdr.com/sectorspdr/IDCO.Client.Spdrs.Portfolio/Export/ExportCsv?symbol=xle'
    elif user_choice == '5':
        return 'https://www.sectorspdr.com/sectorspdr/IDCO.Client.Spdrs.Portfolio/Export/ExportCsv?symbol=xlf'
    elif user_choice == '6':
        return 'https://www.sectorspdr.com/sectorspdr/IDCO.Client.Spdrs.Portfolio/Export/ExportCsv?symbol=xlv'
    elif user_choice == '7':
        return 'https://www.sectorspdr.com/sectorspdr/IDCO.Client.Spdrs.Portfolio/Export/ExportCsv?symbol=xli'
    elif user_choice == '8':
        return 'https://www.sectorspdr.com/sectorspdr/IDCO.Client.Spdrs.Portfolio/Export/ExportCsv?symbol=xlb'
    elif user_choice == '9':
        return 'https://www.sectorspdr.com/sectorspdr/IDCO.Client.Spdrs.Portfolio/Export/ExportCsv?symbol=xlre'
    elif user_choice == '10':
        return 'https://www.sectorspdr.com/sectorspdr/IDCO.Client.Spdrs.Portfolio/Export/ExportCsv?symbol=xlk'
    elif user_choice == '11':
        return 'https://www.sectorspdr.com/sectorspdr/IDCO.Client.Spdrs.Portfolio/Export/ExportCsv?symbol=xlu'
    elif user_choice == 'q':
        return 'q'
