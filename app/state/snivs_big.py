from datetime import datetime
from app.models.sniv import Sniv
from app.state.pilots_big import _pilot_list

# 9 snivs (1 unavail, 4 half day)
_sniv_list = [
    Sniv(datetime(2019, 1, 1, 8, 0), datetime(2019, 1, 1, 12, 0), _pilot_list[0].id, 'dental'),
    Sniv(datetime(2019, 1, 1, 19, 0), datetime(2019, 1, 1, 23, 0), _pilot_list[4].id, 'school'),
    Sniv(datetime(2019, 1, 1, 13, 0), datetime(2019, 1, 1, 23, 0), _pilot_list[6].id, 'OFP'),
    Sniv(datetime(2019, 1, 1, 16, 30), datetime(2019, 1, 1, 23, 0), _pilot_list[9].id, 'OFP'),
    Sniv(datetime(2019, 1, 1, 0, 30), datetime(2019, 1, 1, 23, 0), _pilot_list[15].id, 'OFP'),
    Sniv(datetime(2019, 1, 1, 5, 0), datetime(2019, 1, 1, 9, 0), _pilot_list[20].id, 'massage'),
    Sniv(datetime(2019, 1, 1, 5, 0), datetime(2019, 1, 1, 9, 0), _pilot_list[28].id, 'massage'),
    Sniv(datetime(2019, 1, 1, 15, 0), datetime(2019, 1, 1, 23, 0), _pilot_list[30].id, 'massage'),
    Sniv(datetime(2019, 1, 1, 13, 45), datetime(2019, 1, 1, 23, 0), _pilot_list[34].id, 'kids'),
]

snivs = {sniv.id: sniv for sniv in _sniv_list}
