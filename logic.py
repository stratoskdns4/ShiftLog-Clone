import datetime
import json
import os.path
import os

import logging
from db import Event

# Ορίζουμε το τρέχον φάκελο ως το φάκελο στον οποίο βρίσκεται αυτό το αρχείο
os.chdir(os.path.dirname(__file__))

logger = logging.getLogger(__name__)

def list_events()->list:
    """
    Query our events and return the last-n rows
    """
    res = Event.query.select('*').desc().limit(100)
    logger.warning(f'Results from query: {str(res)}')
    
    return res

def save_event(event_dict:dict={}, filepath:str='logs') -> bool:
    """
    Αποθηκεύει τα δεδομένα του event_dict σε αρχείο.
    Αν το filepath δεν είναι None, τα δεδομένα αποθήκευονται στο αρχείο
    στη διαδρομή filepath.
    Σε αντίθετη περίπτωση, κατασκευάζουμε ένα νέο όνομα αρχείου σύμφωνα με 
    την τρέχουσα ημερομηνία και ώρα, και το αποθηκεύουμε στο φάκελο LOG_DIR.
    """
    logger.warning('hi there')
    if not filepath:
        filepath='logs'
    datetime_str = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S_%f")
    filename = f"record_{datetime_str}.json"
    logger.warning(f'saving to {filename}')
    myPath = os.path.join(filepath, filename)
    try:
        with open(myPath, 'w') as fp:
            json.dump(event_dict, fp)
    except FileNotFoundError as e:
        logger.error('Could not find log file')
        return False
    return True



def add_event( ev_dict:dict={})->str:
    # Here we can check the validity of the data before committing
    logger.warning(f'---- adding event ----')
    timestamp = datetime.datetime.now()
    logger.warning(f'timestamp: {timestamp}, {ev_dict}')
    payload = {
            'event_timestamp': timestamp, 
            'employee_name':ev_dict['employee_name'], 
            'event_description':ev_dict['event_description'], 
            'event_result':ev_dict['event_result']
            }
    # Create our record
    res=None
    try:
        res=Event.create(**payload)
    except Exception as e:
        logger.error(f'Error saving out: {e}')
    # Save our changes
    return res

def add_break( ev_dict:dict={})->str:
    # Here we can check the validity of the data before committing
    logger.warning(f'---- adding event ----')
    timestamp = datetime.datetime.now()
    logger.warning(f'timestamp: {timestamp}, {ev_dict}')
    payload = {
            'event_timestamp': ev_dict['event_timestamp'], 
            'employee_name':ev_dict['employee_name'], 
            'event_description': "BREAK EVENT: " + ev_dict['event_description'], 
            'event_result':ev_dict['event_result']
            }
    # Create our record
    res=None
    try:
        res=Event.create(**payload)
    except Exception as e:
        logger.error(f'Error saving out: {e}')
    # Save our changes
    return res

def add_jackpot(jackpot_data):
    description = "{} {} €{:.2f}  {}".format(
        jackpot_data["slot"],
        jackpot_data["time"],
        jackpot_data["amount"],
        jackpot_data["description"]
    ) 
    timestamp = datetime.datetime.now()

    payload = {
            'event_timestamp': timestamp, 
            'employee_name': jackpot_data['name'], 
            'event_description': description, 
            'event_result':'JACKPOT'
            }
    # Create our record
    res=None
    try:
        res=Event.create(**payload)
    except Exception as e:
        logger.error(f'Error saving out: {e}')
    # Save our changes
    return res


def add_cashout(cashout_data):
    description = "{} {} €{:.2f}  {}".format(
        cashout_data["window"],
        cashout_data["time"],
        cashout_data["amount"],
        cashout_data["description"]
    ) 
    timestamp = datetime.datetime.now()

    payload = {
            'event_timestamp': timestamp, 
            'employee_name': cashout_data['name'], 
            'event_description': description, 
            'event_result': 'CASHOUT'
            }
    # Create our record
    res=None
    try:
        res=Event.create(**payload)
    except Exception as e:
        logger.error(f'Error saving out: {e}')
    # Save our changes
    return res
