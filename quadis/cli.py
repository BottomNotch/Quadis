import click
import csv

#a helper class to pass arguments/options from the top level command to sub-commands
class Config(object):
    #this will be the csv file with the all the card information
    csv_file = 0

    def __init__(self):
        pass

#create a decorator to pass the a Config object to sub-commands
pass_config = click.make_pass_decorator(Config, ensure=True)

@click.group()
@click.argument('csv_file')
@pass_config
def cli(config, csv_file):
    '''CSV_FILE is required, it should be the file used to hold all the card information'''
    config.csv_file = csv_file    

#check if card has been used today with silent mode for non-cli use (not fully implemented)
@cli.command()
@click.option('--card-num', type=click.INT, default=0, help='the card you want to check') 
@pass_config
def check_card(config, card_num, silent=False):
    card_found = False
    row_num_counter = 0    #used count row numbers to find the row the card number is on
    row_num = 0    #when and if the card number is found, the row number it's on will be stored here
    csv_file = open(config.csv_file)
    csv_reader = csv.reader(csv_file, delimiter=',')
    return_val = 0    #0 = card found and has not been used today 1 = card not found 2 = card used today
    if card_num == 0:    #if no card number was given prompt user input
        card_num_int = click.prompt('Please scan card or enter number manually', type=int)
    else:
        card_num_int = card_num

    for row in csv_reader:    #scan CSV file for card number
        number, name, last_used_date = row
        if number == str(card_num_int):
            card_found = True
            row_num = row_num_counter
    
        row_num_counter += 1

    if card_found:
        pass    #to be implemented
    
    else:
        return_val = 1
        if silent == False:      
             click.echo('card {0} not found, please add the card using the add_card command'.format(card_num))
    
    return return_val
