from datetime import datetime
from app.models.sniv import Sniv
from app.state.pilots import pilot1, pilot8

sniv1 = Sniv(datetime(2019, 1, 1, 8, 0), datetime(2019, 1, 1, 12, 0), pilot1.id, 'dental')
sniv2 = Sniv(datetime(2019, 1, 1, 20, 0), datetime(2019, 1, 1, 23, 0), pilot8.id, 'dental')

snivs = {
    sniv1.id: sniv1,
    sniv2.id: sniv2,
}
