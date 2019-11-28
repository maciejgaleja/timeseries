import unittest
import timeseries.timeseries as timeseries

import datetime

class TestTimeseries(unittest.TestCase):

    def test_constructor_basic(self):
        ts = timeseries.Timeseries()
        self.assertEqual(str(ts), "[][]")

    def test_begin_no_averaging(self):
        ts = timeseries.Timeseries()
        dt = datetime.datetime(2019, 1, 1, 12, 0, 0)
        ts.add(0.0, dt)
        self.assertEqual(ts.begin(), dt)

    def test_begin_averaging(self):
        ts = timeseries.Timeseries()
        delta = datetime.timedelta(minutes=1)
        ts.set_averaging_period(delta)
        dt = datetime.datetime(2019, 1, 1, 12, 43, 42)
        ts.add(0.0, dt)
        dt = datetime.datetime(2019, 1, 1, 12, 43, 0)
        self.assertEqual(ts.begin(), dt)

    def test_averaging(self):
        ts = timeseries.Timeseries()
        ts.set_averaging_period(datetime.timedelta(minutes=1))

        dt = datetime.datetime(2019, 1, 1, 12, 0, 0)
        delta = datetime.timedelta(seconds=15)
        ts.add(0.0, dt)
        dt += delta
        ts.add(1.0, dt)
        dt += delta
        ts.add(2.0, dt)
        dt = datetime.datetime(2019, 1, 1, 12, 1, 5)
        ts.add(1.0, dt)
        self.assertEqual(len(ts.time), 2)

    def test_no_averaging(self):
        ts = timeseries.Timeseries()

        dt = datetime.datetime(2019, 1, 1, 12, 0, 0)
        delta = datetime.timedelta(seconds=15)
        ts.add(0.0, dt)
        dt += delta
        ts.add(1.0, dt)
        dt += delta
        ts.add(2.0, dt)
        dt = datetime.datetime(2019, 1, 1, 12, 1, 0)
        ts.add(1.0, dt)

        self.assertEqual(len(ts.time), 4)
        self.assertEqual(len(ts), 4)


    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
