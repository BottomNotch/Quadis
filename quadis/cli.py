'''this module contains the base functions and the click based CLI'''
import csv
from datetime import datetime
import click

#these are constants for in what collums in the csv file different
#information is located
CARD_NUM_COLUMN = 0
NAME_COLUMN = 1
LAST_USED_COLUMN = 2


# pas a dictionary to sub-commands
pass_config = click.make_pass_decorator(dict, ensure=True)

@click.group()
@click.argument('csv_file')
@click.option('-n', '--card-num', type=click.INT,
              help='the card you want to check/add/change')
@pass_config
def cli(config, csv_file, card_num):
    '''CSV_FILE is required, it should be the file used to hold all the
    card information'''
    config['csv_file'] = csv_file

    if card_num is None:  #if card_num is none that means there was no
                          #user input
        config['card_num'] = click.prompt(
            'Please scan card or enter number manually', type=int)
    else:
        config['card_num'] = card_num

# check if card has been used today with silent mode for non-cli use (not
# fully implemented)
@cli.command()
@pass_config
def check_card(config, silent=False, return_row=False):
    '''check a card to make sure it is on the csv file and has not been
    used today'''
    card_found = False
    row_num = 0  # when and if the card number is found,
                 # the row number it's on will be stored here
    csv_file = open(config['csv_file'])
    csv_list = list(csv.reader(csv_file, delimiter=','))  # To allow edditing
    csv_file.close()  # So the csv file can be opened in write mode
    csv_file = open(config['csv_file'], 'w')
    csv_writer = csv.writer(csv_file, delimiter=',')

    return_val = 0  # if return_row is True this the row of the card will
                    # be returned (or 0 if not found) if False the
                    # following will be returned:
                    # 0 = card not found
                    # 1 = card found and has not been used today
                    # 2 = card used today
    last_used_date = ''
    date_today = datetime.now()

    for row in csv_list:  # scan CSV file for card number
        if row[0] == str(config['card_num']):
            number, name, last_used_date = row
            card_found = True
            row_num = csv_list.index(row)

    if card_found:
        if return_row:
            return_val = row_num

        if last_used_date == date_today.strftime('%m/%d/%Y'):
            if not silent:
                click.echo("card used today")
            return_val = 2

        else:
            csv_list[row_num][LAST_USED_COLUMN] = date_today.strftime('%m/%d/%Y')
            return_val = 1
    else:
        return_val = 0
        if not silent:
            click.echo(
                'card not found, please add the card using the add_card command')
    csv_writer.writerows(csv_list)
    csv_file.close()
    return return_val
