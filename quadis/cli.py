'''the click based CLI'''
from datetime import datetime
from quadis import main
import click

# pas a dictionary to sub-commands
pass_config = click.make_pass_decorator(dict, ensure=True)

def set_date():
    '''prompts user to set the last used date of the card'''
    last_used_month = click.prompt('please enter a month', type=int)
    last_used_day = click.prompt('please enter a day of month', type=int)
    last_used_year = click.prompt('please enter a year', type=int)
    last_used_date = "{0}/{1}/{2}".format(last_used_month,
                                              last_used_day, last_used_year)
    return last_used_date

@click.group()
@click.argument('csv_file')
@click.option('-n', '--card-num',
              help='the card you want to check/add/change')
@pass_config
def cli(config, csv_file, card_num):
    '''CSV_FILE is required, it should be the file used to hold all the
    card information'''
    config['csv_file'] = csv_file

    if card_num is None:  #if card_num is none that means there was no
                          #user input
        config['card_num'] = click.prompt(
            'Please scan card or enter number manually', type=str)
    else:
        config['card_num'] = card_num

@cli.command('check_card')
@pass_config
def check_card(config):
    '''check a card to make sure it is on the csv file and has not been
    used today'''
    card_state = main.check_card(config['csv_file'], config['card_num'],
                                 update_card=click.confirm('update card?'))

    if card_state == 0:
        click.echo(
            'card not found, please add the card using the add_card command')

    elif card_state == 1:
        click.echo('card found and not used today')

    elif card_state == 2:
        click.echo("card used today")

@cli.command()
@click.option('-N', '--name', help='the name of the card holder')
@click.option('--used-today/--not-used-today', default=False,
              help='if the card has been used today')
@pass_config
def add_card(config, name, used_today):
    card_dict = {'card_num':config['card_num'], 'last_used_date':'N/A', 'name':name}

    if name is None:
        card_dict['name'] = click.prompt('please enter a name', type=str)

    if used_today or click.confirm('used today?'):
        card_dict['last_used_date'] = main.date_today.strftime('%m/%d/%Y')

    else:
        if click.confirm('set date?'):
            card_dict['last_used_date'] = set_date()

    for item in main.csv_layout:
        if all([item is not 'last_used_date', item is not 'name', item is not 'card_num']):
            card_dict[item] = click.prompt(
                'to what would you like to set {0} for this card?'
                .format(item), type=str)

    result = main.add_card(config['csv_file'], card_dict)

    card_dict_new = main.card_info(config['csv_file'], config['card_num'])

    if result is 0:
        click.echo('card number {0} successfully added on row {1}'
                   .format(config['card_num'], card_dict_new['row_num']))
    if result is 1:
        click.echo('card number {0} already exists on row {1}'
                   .format(config['card_num'], card_dict_new['row_num']))
    if result is 2:
        click.echo('{0} is not a valid date format'
                   .format(card_dict['last_used_date']))

@cli.command()
@pass_config
def remove_card(config):
    '''remove the specified card'''
    returned_val = main.remove_card(config['csv_file'], config['card_num'])

    if returned_val is 0:
        click.echo('card number {0} removed'.format(config['card_num']))

    elif returned_val is 1:
        click.echo('card number {0} not found'.format(config['card_num']))

@cli.command()
@pass_config
def change_card(config):
    result = None
    card_info = main.card_info(config['csv_file'], config['card_num'])

    if card_info is not 1:
        if click.confirm('change number?'):
            card_info['card_num'] = click.prompt(
                'please enter the new card number', type=str)

        if click.confirm('change name?'):
            card_info['name'] = click.prompt('please enter the new name', type=str)

        if click.confirm('change last used date?'):
            if click.confirm('change to today?'):
                card_info['last_used_date'] = main.date_today.strftime('%m/%d/%Y')
            else:
                card_info['last_used_date'] = set_date()

        for item in main.csv_layout:
            if all([item is not 'last_used_date', item is not 'name', item is not 'card_num',
                    click.confirm('change {0} for this card?'.format(item))]):
                card_info[item] = click.prompt(
                    'to what would you like to set {0} for this card?'
                    .format(item), type=str)

        result = main.change_card(config['csv_file'], config['card_num'],
                                  card_info)

        if result is 0:
            click.echo('card information changed successfully')
        elif result is 1:
            click.echo('card number {0} not found'
                       .format(config['card_num']))
        elif result is 2:
            click.echo('card number {0} already exists'
                       .format(card_info['card_num']))
        elif result is 3:
            click.echo('{0} is an invalid date'
                       .format(card_info['last_used_date']))
    else:
        click.echo('card does not exist')
