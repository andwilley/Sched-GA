from datetime import datetime
from app.models.sniv import Sniv
from app.state.pilots import pilot1

sniv1 = Sniv(datetime(2019, 1, 1, 8, 0), datetime(2019, 1, 1, 12, 0), pilot1.id, 'dental')

snivs = {
    sniv1.id: sniv1
}
