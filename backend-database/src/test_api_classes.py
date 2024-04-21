from api_classes import DataObserver, ApiAdapter, ApiFacade

dat = DataObserver()
api = ApiAdapter()

# Data observer test:
class TestDataObserver:
# Probably trivial since it is a hashing function, however i wasn't sure if these should be left out
    def test_hashing_same_data(self):
        assert dat.prepare_hash('(this is some sample data)') == dat.prepare_hash('(this is some sample data)')

    def test_hashing_diff_data(self):
        assert dat.prepare_hash('(These two examples)') != dat.prepare_hash('(Now shouldn"t match because they are different)')

# Checking if internal state changes as expected

    def test_initial_data_in(self):
        assert dat.check_for_change("This is new data, since the observer hasn't had any data yet") == True

    def test_another_change(self):
        assert dat.check_for_change("Now, this is another set of new data") == True

    def test_no_change(self):
        assert dat.check_for_change("Now, this is another set of new data") == False

# Now, the tedious part, because the api interface is really convoluted and thus the adapter is complex as well...
# Api adapter test:
class TestApiAdapter:
    def test_parse_api_stops(self):
        assert api.parse_api_stops({"result": [{"values": [{"value": "1001", "key": "zespol"},{"value": '01', "key": "slupek"},{"value": "Testowy przystanek", "key": "nazwa_zespolu"},{"value": "1001", "key": "id_ulicy"},{"value": "50.0000", "key": "szer_geo"}, {"value": "20.0000", "key": "dlug_geo"}, {"value": "testowo", "key": "kierunek"}, {"value": "1969-01-01 00:00:00.0", "key": "obowiązuje od"}]}]}) == [(100101,  "Testowy przystanek", 50.0000, 20.0000, "testowo", "1969-01-01 00:00:00.0")]

    def test_parse_api_lines(self):
        assert api.parse_api_lines({"result": [{"values":[{"value":"143", "key":"linia"}]}, {"values":[{"value":"187", "key":"linia"}]}]}) == ["143", "187"]

    def test_parse_api_timetables(self):
        assert api.parse_api_timetables({"result":[{"values":[{"value":"nieważne", "key":"symbol_2"},{"value":"nieważne", "key":"symbol_1"},{"value":"101", "key":"brygada"},{"value":"testowo", "key":"kierunek"},{"value":"TP-TOP", "key":"trasa"},{"value":"6:47:00", "key":"czas"}]}]}) == [("101", "testowo", "TP-TOP", "06:47:00")]

    def test_fix_time_no_leading_zero(self):
        assert api.fix_time("3:30:00") == "03:30:00"

    def test_fix_time_past_midnight(self):
        assert api.fix_time("25:30:00") == "01:30:00"

    def test_fix_time_no_changes_needed(self):
        assert api.fix_time("13:30:00") == "13:30:00"