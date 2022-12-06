import datetime
import json
import os.path
import os

# Ορίζουμε το τρέχον φάκελο ως το φάκελο στον οποίο βρίσκεται αυτό το αρχείο
os.chdir(os.path.dirname(__file__))

LOG_DIR = "logs"

def save_event(event_dict, filepath):
    """
    Αποθηκεύει τα δεδομένα του event_dict σε αρχείο.
    Αν το filepath δεν είναι None, τα δεδομένα αποθήκευονται στο αρχείο
    στη διαδρομή filepath.
    Σε αντίθετη περίπτωση, κατασκευάζουμε ένα νέο όνομα αρχείου σύμφωνα με 
    την τρέχουσα ημερομηνία και ώρα, και το αποθηκεύουμε στο φάκελο LOG_DIR.
    """
    if filepath is None:
        datetime_str = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S_%f")
        filename = f"record_{datetime_str}.json"
        filepath = os.path.join(LOG_DIR, filename)
    
    fp = open(filepath, "w")
    json.dump(event_dict, fp)
    fp.close()