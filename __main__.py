from bitdeli.widgets import Title, Description, set_theme
from bitdeli.chain import Profiles
from collections import Counter

set_theme('playground')
          
text = {}

def volume(it):
    hours = Counter()
    for profile in it:
        for tstamp, group, ip, event in profile['events']:
            hour = group.split(':')[-1] + ':00:00'
            hours[hour] += 1
            
    latest = max(hours)
    text['latest-hour'] = latest.replace('T', ' ')
    text['latest-num'] = hours[latest]
    text['first-hour'] = min(hours).replace('T', ' ')
    text['total'] = sum(hours.itervalues())
    
    yield {'type': 'line',
           'label': 'Number of events by hour',
           'size': (12, 3),
           'data': list(sorted(hours.iteritems()))}
    yield {'type': 'text',
           'size': (5, 2),
           'label': 'Number of events in the latest batch',
           'head': hours[latest]}
    yield {'type': 'text',
           'size': (5, 2),
           'label': 'Total number of events',
           'color': 2,
           'head': text['total']}
    
Profiles().map(volume).show()

Title('{latest-num} events received', text)

Description("""
The latest batch of events was processed at {latest-hour}.
It contains {latest-num} events.

In total, {total} has been received since {first-hour}.""", text)