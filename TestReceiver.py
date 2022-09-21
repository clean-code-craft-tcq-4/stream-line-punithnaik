import unittest
from unittest.mock import patch
from io import StringIO
import sys
import io
import ReceiverTestData
from Constants import SIMPLE_MOVING_AVERAGE, UNSUPPORTED_STATISTICS_TYPE, MINIMUM, MAXIMUM, MEDIAN, MODE
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
        for data in ReceiverTestData.VALIDATE_MINIMUM_VALUE:
            self.assertEqual(
                self.statistics_computer.compute_minimum_value(
                    data.get(ReceiverTestData.SENSOR_READINGS)), 
                    data.get(MINIMUM))

    def test_compute_maximum_value(self):
        for data in ReceiverTestData.VALIDATE_MAXIMUM_VALUE:
            self.assertEqual(
                self.statistics_computer.compute_maximum_value(
                    data.get(ReceiverTestData.SENSOR_READINGS)), 
                    data.get(MAXIMUM))
    
    def test_compute_sma(self):
        for data in ReceiverTestData.VALIDATE_SMA_VALUE:
            self.assertEqual(
                self.statistics_computer.compute_sma(
                    data.get(ReceiverTestData.SENSOR_READINGS)), 
                    data.get(SIMPLE_MOVING_AVERAGE))
class TestStatisticsFactory(unittest.TestCase):
    def __init__(self, method_name: str = ...) -> None:
        super().__init__(method_name)
        self.statistical_factory = StatisticsFactory()

    def test_get_statistical_func_by_name(self):
        self.assertEqual(self.statistical_factory.get_statistical_func_by_name(MINIMUM).__name__, StatisticsComputer().compute_minimum_value.__name__)
        self.assertEqual(self.statistical_factory.get_statistical_func_by_name(MEDIAN), None)

class TestReceiver(unittest.TestCase):
    def __init__(self, method_name: str = ...) -> None:
        super().__init__(method_name)
        self.receiver = Receiver()
        self.receiver.configure_statistics([MINIMUM, MAXIMUM, SIMPLE_MOVING_AVERAGE])

    @patch(STD_IN, io.StringIO(''.join(MockSender().send_valid_data())))
    def test_receive_data(self):
        self.assertEqual(len(self.receiver.receive_data_from_sender()), 50)
    
    @patch(STD_IN, io.StringIO(''.join(MockSender().send_invalid_data())))
    def test_receive_invalid_data(self):
        self.assertEqual(len(self.receiver.receive_data_from_sender()), 0)
    
    def test_data_formatter(self):
        for data in ReceiverTestData.VALIDATE_FORMAT_DATA:
            self.assertEqual(
                self.receiver.format_received_data(
                    data.get(ReceiverTestData.SENSOR_READINGS)), 
                    data.get(ReceiverTestData.FORMATTED_READINGS))
    
    def test_configure_statistics(self):
        self.receiver.configure_statistics([MINIMUM, MAXIMUM])
        result = all(stat in self.receiver.statistical_figures for stat in [MINIMUM, MAXIMUM])
        self.assertEqual(result, True)
    
    def test_compute_statistics(self):
        for data in ReceiverTestData.VALIDATE_STATISTICS_COMPUTATION:
            self.assertEqual(
                self.receiver.compute_statistics(
                    data.get(ReceiverTestData.SENSOR_READINGS)), \
            data.get(ReceiverTestData.STATISTICS))
        
            receiver = Receiver()
            receiver.configure_statistics([MODE])
            with self.assertRaises(ValueError) as context:
                receiver.compute_statistics(data.get(ReceiverTestData.SENSOR_READINGS))

            self.assertEqual(str(context.exception), UNSUPPORTED_STATISTICS_TYPE)

    def test_consolidate_statistical_data(self):
        for data in ReceiverTestData.VALIDATE_CONSOLIDATION:
            self.assertEqual(
                self.receiver.consolidate_statistical_data(
                    data.get(ReceiverTestData.SENSOR_READINGS)),
                    data.get(ReceiverTestData.CONSOLIDATED_STATISTICS))
            receiver = Receiver()
            receiver.configure_statistics([MEDIAN])
            with self.assertRaises(ValueError) as context:
                receiver.consolidate_statistical_data(data.get(ReceiverTestData.SENSOR_READINGS))

            self.assertEqual(str(context.exception), UNSUPPORTED_STATISTICS_TYPE)
    
    @patch(STD_IN, io.StringIO(''.join(MockSender().send_valid_data())))
    def test_receiver(self):
        with patch(STD_OUT, new = StringIO()) as fake_out:
            self.receiver.receive_and_analyze()
            self.assertEqual(fake_out.getvalue().strip(), 
            """{'temperature': {'Min': 30, 'Max': 30, 'SMA': 30.0}, 'soc': {'Min': 50, 'Max': 50, 'SMA': 50.0}}""")



if __name__ == '__main__':
  sys.exit(unittest.main()) # pragma: no cover
