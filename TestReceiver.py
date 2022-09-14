import unittest
from unittest.mock import patch
from io import StringIO
import sys
import io
import ReceiverTestData
from Receiver import Receiver
from MockSender import MockSender
from StatisticsComputer import StatisticsComputer
from StatisticsFactory import StatisticsFactory

STD_OUT = 'sys.stdout'
STD_IN = 'sys.stdin'

class TestStatisticsComputer(unittest.TestCase):
    def __init__(self, method_name: str = ...) -> None:
        super().__init__(method_name)
        self.statistics_computer = StatisticsComputer()

    def test_compute_minimum_value(self):
        self.assertEqual(self.statistics_computer.compute_minimum_value([20, 30, -10, 0, 10]), -10)

    def test_compute_maximum_value(self):
        self.assertEqual(self.statistics_computer.compute_maximum_value([20, 30, -10, 0, 10]), 30)
    
    def test_compute_sma(self):
        self.assertEqual(self.statistics_computer.compute_sma([30, -10, 0, 10, 11]), 8.2)

class TestStatisticsFactory(unittest.TestCase):
    def __init__(self, method_name: str = ...) -> None:
        super().__init__(method_name)
        self.statistical_factory = StatisticsFactory()

    def test_get_statistical_func_by_name(self):
        self.assertEqual(self.statistical_factory.get_statistical_func_by_name("Min").__name__, StatisticsComputer().compute_minimum_value.__name__)
        self.assertEqual(self.statistical_factory.get_statistical_func_by_name("Median"), None)

class TestReceiver(unittest.TestCase):
    def __init__(self, method_name: str = ...) -> None:
        super().__init__(method_name)
        self.receiver = Receiver()
        self.receiver.configure_statistics(["Min", "Max", "SMA"])

    @patch(STD_IN, io.StringIO(''.join(MockSender().send_data())))
    def test_receive_data(self):
        self.assertEqual(len(self.receiver.receive_data_from_sender()), 50)
    
    @patch(STD_IN, io.StringIO(''.join(MockSender().send_invalid_data())))
    def test_receive_data(self):
        self.assertEqual(len(self.receiver.receive_data_from_sender()), 0)
    
    def test_data_formatter(self):
        self.assertEqual(self.receiver.format_received_data(
            [
                {"temperature": 50, "soc": 20},
                {"temperature": 51, "soc": 60},
                {"temperature": 21, "soc": 90}
            ]), {"temperature": [50, 51, 21], "soc": [20, 60, 90]})
    
    def test_configure_statistics(self):
        self.receiver.configure_statistics(["Min","Max"])
        result = all(stat in self.receiver.statistical_figures for stat in ["Min","Max"])
        self.assertEqual(result, True)
    
    def test_compute_statistics(self):
        self.assertEqual(self.receiver.compute_statistics([50, 52, -21, 10, 100]), \
            {'SMA': 38.2, 'Max': 100, 'Min': -21})
        receiver = Receiver()
        receiver.configure_statistics(["Median"])
        with self.assertRaises(ValueError) as context:
            receiver.compute_statistics([10, 10, 23, 20, 11])

        self.assertEquals(str(context.exception), 'Unsupported Statistics Type')

    def test_consolidate_statistical_data(self):
        self.assertEqual(self.receiver.consolidate_statistical_data({"temperature": [50, 51, 21, 10, 100], "soc": [20, 60, 90, 30, 75]}),
        {'soc': {'SMA': 55.0, 'Max': 90, 'Min': 20},
        'temperature': {'SMA': 46.4, 'Max': 100, 'Min': 10}})
        receiver = Receiver()
        receiver.configure_statistics(["Median"])
        with self.assertRaises(ValueError) as context:
            receiver.consolidate_statistical_data({"temperature": [50, 51, 21, 10, 100], "soc": [20, 60, 90, 30, 75]})

        self.assertEquals(str(context.exception), 'Unsupported Statistics Type')
    
    @patch(STD_IN, io.StringIO(''.join(MockSender().send_data())))
    def test_receiver(self):
        with patch(STD_OUT, new = StringIO()) as fake_out:
            self.receiver.receive_and_analyze()
            self.assertEqual(fake_out.getvalue().strip(), 
            """{'temperature': {'Min': 30, 'Max': 30, 'SMA': 30.0}, 'soc': {'Min': 50, 'Max': 50, 'SMA': 50.0}}""")



if __name__ == '__main__':
  sys.exit(unittest.main()) # pragma: no cover
