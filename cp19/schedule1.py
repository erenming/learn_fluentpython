"""
#schedule1.py: traversing OSCON schedule data
# BEGIN SCHEDULE1_DEMO
>>> import shelve
>>> db = shelve.open(DB_NAME)  # <1>
>>> if CONFERENCE not in db:  # <2>
...     load_db(db)  # <3>
...
>>> speaker = db['speaker.3471']  # <4>
>>> type(speaker)  # <5>
<class 'schedule1.Record'>
>>> speaker.name, speaker.twitter  # <6>
('Anna Martelli Ravenscroft', 'annaraven')
>>> db.close()  # <7>
"""

import warnings

import osconfeed


DB_NAME = 'data/schedule1_db'
CONFERENCE = 'conference.115'


class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


def load_db(db):
    raw_data = osconfeed.load()
    warnings.warn('loading' + DB_NAME)
    for collection, rec_list in raw_data['Schedule'].items():
        record_type = collection[:-1]
        for record in rec_list:
            key = '{}.{}'.format(record_type, record['serial'])
            record['serial'] = key
            db[key] = Record(**record)

if __name__ == '__main__':
    import doctest
    doctest.testmod()