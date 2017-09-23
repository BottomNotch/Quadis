'''this module contains the base functions that will be used by the GUI and CLI'''
import csv
from datetime import datetime

#these are constants for in what collums in the csv file different
#information is located
CARD_NUM_COLUMN = 0
NAME_COLUMN = 1
LAST_USED_COLUMN = 2

date_today = datetime.now()

def check_date(date_str):
    '''used to make sure the given string is in the correct format'''
    try:
        datetime.strptime(date_str, '%m/%d/%Y')
    except ValueError:
        return_val = 1
    else:
        return_val = 0
    return return_val


def card_info(csv_file, card_num):
    csv_file = open(csv_file)
    csv_reader = csv.reader(csv_file, delimiter=',')
    return_val = None

    for row in csv_reader:
        if row[CARD_NUM_COLUMN] == str(card_num):
            return_val = row
            continue
        else:
            return_val = 1

    return return_val

def check_card(csv_data, card_num, return_row=False, update_card=True):
    '''check a card to make sure it is on the csv file and has not been
    used today (also has statements and return_row which makes this
    return the row number of the card'''
    card_found = False
    row_num = 0  # when and if the card number is found,
                 # the row number it's on will be stored here
    csv_file = open(csv_data)
    csv_list = list(csv.reader(csv_file, delimiter=','))  # To allow editing
    csv_file.close()  # So the csv file can be opened in write mode
    csv_file = open(csv_data, 'w')
    csv_writer = csv.writer(csv_file, delimiter=',')

    return_val = None  # if return_row is True this the row of the card will
                       # be returned (or 0 if not found) if False the
                       # following will be returned:
                       # 0 = card not found
                       # 1 = card found and has not been used today
                       # 2 = card used today
    last_used_date = ''

    for row in csv_list:  # scan CSV file for card number
        if row[0] == str(card_num):
            last_used_date = row[LAST_USED_COLUMN]
            card_found = True
            row_num = csv_list.index(row)

    if card_found:
        if return_row:
            return_val = row_num

        elif last_used_date == date_today.strftime('%m/%d/%Y'):
            return_val = 2  #card used today

        else:
            if update_card:
                csv_list[row_num][LAST_USED_COLUMN] = date_today.strftime('%m/%d/%Y')
            return_val = 1  #card found and not used today
    else:
        return_val = 0  #card not found

    csv_writer.writerows(csv_list)
    csv_file.close()
    return return_val

def add_card(csv_file, card_num, name, last_used_date, row_num):
    '''adds a new card to the CSV file'''
    row_num = check_card(csv_file, card_num, return_row=True)
    csv_file = open(csv_file, 'a')
    csv_writer = csv.writer(csv_file, delimiter=',')
    row_list = [0, 0, 0]
    return_val = None  #0: success
                       #1: card exists
                       #2: invalid date format

    if row_num is not 0:  #don't modify the CSV file if the card exists
        csv_file.close()
        return_val = 1

    else:
        row_list[CARD_NUM_COLUMN] = card_num
        row_list[NAME_COLUMN] = name
        row_list[LAST_USED_COLUMN] = last_used_date

        if last_used_date is 'N/A' or check_date(last_used_date) is 0:
            csv_writer.writerow(row_list)
            return_val = 0
        else:
            return_val = 2
    csv_file.close()
    return return_val

def remove_card(csv_data, card_num):
    '''deletes the card with the given number from the CSV file'''
    csv_file = open(csv_data)
    csv_list = list(csv.reader(csv_file, delimiter=','))
    csv_file.close()  # So the csv file can be opened in write mode
    csv_file = open(csv_data, 'w')
    csv_writer = csv.writer(csv_file, delimiter=',')
    return_val = 1

    #write all rows except the one that needs to be deleted
    for row in csv_list:
        if str(card_num) not in row:
            csv_writer.writerow(row)

        else:
            return_val = 0  #return 0 if the row was found
    csv_file.close()
    return return_val

def change_card(csv_data, card_num, new_card_num, name, last_used_date):
    '''change the information connected a given card number (including the card number)'''
    csv_file = open(csv_data)
    csv_list = list(csv.reader(csv_file, delimiter=','))
    csv_file.close()  # So the csv file can be opened in write mode
    csv_file = open(csv_data, 'w')
    csv_writer = csv.writer(csv_file, delimiter=',')
    return_val = None  # 0: success
                       # 1: card not found
                       # 2: the new card number already exists
                       # 3: invalid date

    if all([new_card_num is not card_num,
            check_card(csv_data, new_card_num) is not 0]):
        return_val = 2

    elif check_date(last_used_date) is 1:
        return_val = 3

    else:
        for row in csv_list:
            print(row[0])
            if str(card_num) == row[CARD_NUM_COLUMN]:
                index = csv_list.index(row)
                csv_list[index][CARD_NUM_COLUMN] = new_card_num
                csv_list[index][NAME_COLUMN] = name
                csv_list[index][LAST_USED_COLUMN] = last_used_date
                return_val = 0
                continue

            else:
                return_val = 1

    csv_writer.writerows(csv_list)
    csv_file.close()
    return return_val
