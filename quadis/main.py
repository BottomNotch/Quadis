'''this module contains the base functions that will be used by the GUI and CLI'''
import csv
from datetime import datetime

csv_layout = ['card_num', 'name','under_13', 'under_18', 'under_60',
              'over_59', 'zip', 'last_used_date']

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


def card_info(csv_data, card_num):
    csv_file = open(csv_data)
    csv_reader = csv.reader(csv_file, delimiter=',')
    card_dict = dict()
    return_val = None
    index = 0
    for row in csv_reader:
        index += 1
        if row[csv_layout.index('card_num')] == str(card_num):
            for item in csv_layout:
                card_dict[item] = row[csv_layout.index(item)]
            card_dict['row_num'] = index
            return_val = card_dict
            break
        else:
            return_val = 1

    return return_val

def check_card(csv_data, card_num, update_card=True):
    '''check a card to make sure it is on the csv file and has not been
    used today (also has statements and return_row which makes this
    return the row number of the card'''
    csv_file = open(csv_data)
    csv_list = list(csv.reader(csv_file, delimiter=','))  # To allow editing
    csv_file.close()  # So the csv file can be opened in write mode
    csv_file = open(csv_data, 'w')
    csv_writer = csv.writer(csv_file, delimiter=',')

    return_val = None  # 0 = card not found
                       # 1 = card found and has not been used today
                       # 2 = card used today
    card_dict = card_info(csv_data, card_num)

    if card_dict is not 1:
        if card_dict['last_used_date'] == date_today.strftime('%m/%d/%Y'):
            return_val = 2  #card used today

        else:
            if update_card:
                csv_list[card_dict['row_num']]\
                [csv_layout.index('last_used_date')] =\
                date_today.strftime('%m/%d/%Y')
            return_val = 1  #card found and not used today
    else:
        return_val = 0  #card not found

    csv_writer.writerows(csv_list)
    csv_file.close()
    return return_val

def add_card(csv_data, card_dict):
    '''adds a new card to the CSV file'''
    csv_file = open(csv_data, 'a')
    csv_writer = csv.writer(csv_file, delimiter=',')
    row_list = list()
    return_val = None  #0: success
                       #1: card exists
                       #2: invalid date format

    if card_info(csv_data, card_dict['card_num']) != 1:  #if card exists
        csv_file.close()
        return_val = 1

    else:
        for item in csv_layout:
            row_list.append(card_dict[item])

        if card_dict['last_used_date'] is 'N/A' or check_date(card_dict['last_used_date']) is 0:
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

def change_card(csv_data, card_num, card_dict):
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

    if all([card_dict['card_num'] is not card_num,
            check_card(csv_data, card_dict['card_num']) is not 0]):
        return_val = 2

    elif check_date(card_dict['last_used_date']) is 1:
        return_val = 3

    else:
        for row in csv_list:
            if str(card_num) == row[csv_layout.index(card_num)]:
                for item in csv_layout:
                    row[csv_layout.index(item)] = card_dict[item]
                return_val = 0
                break

            else:
                return_val = 1

    csv_writer.writerows(csv_list)
    csv_file.close()
    return return_val
