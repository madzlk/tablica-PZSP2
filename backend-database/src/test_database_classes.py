from database_classes import DatabaseAdapter
from datetime import datetime

dat = DatabaseAdapter()

# Testing Database Adapter
class TestDatabaseAdapter:
    # Simply remove the data from tuples
    def test_parse_database_stop_ids(self):
        assert dat.parse_database_stop_ids([(100101,), (100102,), (100103,)]) == [100101, 100102, 100103]

    # makes it longer by turning a dict into a list - but also easier to query
    def test_turn_timetables_into_query(self):
        assert [x[:-1] for x in dat.turn_timetables_into_query({100101: {"143": [("101", "testowo", "TP-TOP", "06:47:00")], "187": [("404", "testowo", "TP-TBP", "08:03:00")]}})] == [(100101, "143", "testowo", "06:47:00", "101", "TP-TOP"),(100101, "187", "testowo", "08:03:00", "404", "TP-TBP")]

    # checkes if it correctly reorders the times.
    def test_parse_times(self):
        now = datetime.now()
        assert dat.parse_times([('temp', 'temp', "00:00:00"), ('temp', 'temp', str(now)), ('temp', 'temp', "24:00:00")]) == [('temp', 'temp', str(now)), ('temp', 'temp', "24:00:00"), ('temp', 'temp', "00:00:00")]