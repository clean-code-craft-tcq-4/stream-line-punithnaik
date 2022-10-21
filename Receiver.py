import sys
import json

from Constants import UNSUPPORTED_STATISTICS_TYPE, INVALID_VALUE, MINIMUM, MAXIMUM, SIMPLE_MOVING_AVERAGE
from StatisticsFactory import StatisticsFactory

class Receiver:
    def __init__(self) -> None:
        self.statistics_computer = ()
        self.statistical_figures = []
        self.statistical_factory = StatisticsFactory()
    
    def ignore_invalid_data(self, processed_readings):
        return [datum for datum in processed_readings if INVALID_VALUE not in datum.values()]

    def receive_data_from_sender(self):
        lines = filter(None, (line.rstrip() for line in sys.stdin))
        processed_readings = [json.loads(line) for line in lines]
        cleaned_data = self.ignore_invalid_data(processed_readings)
        return cleaned_data

    def format_received_data(self, received_sensor_data):
        return {sensor: [sensor_data[sensor] for sensor_data in received_sensor_data] for sensor in received_sensor_data[0]}

    def configure_statistics(self, statistical_figures):
        [self.statistical_figures.append(statistics) for statistics in statistical_figures]

    def compute_statistics(self, data):
        statistics = {}
        for stat_name in self.statistical_figures:
            stat_computer = self.statistical_factory.get_statistical_func_by_name(stat_name)
            if stat_computer is not None:
                statistics.update({stat_name: stat_computer(data)})
            else:
                raise ValueError(UNSUPPORTED_STATISTICS_TYPE)
        return statistics

    def consolidate_statistical_data(self, sensor_data):
        final_statistics = {}
        for sensor, data in sensor_data.items():
            statistics = self.compute_statistics(data)
            final_statistics.update({sensor: statistics})
        return final_statistics

    def receive_and_analyze(self):
        received_data = self.receive_data_from_sender()
        formatted_data = self.format_received_data(received_data)
        computed_statistics = self.consolidate_statistical_data(formatted_data)
        print(computed_statistics)


if __name__ == '__main__':
    receiver = Receiver() # pragma: no cover
    receiver.configure_statistics([MINIMUM, MAXIMUM, SIMPLE_MOVING_AVERAGE]) # pragma: no cover
    receiver.receive_and_analyze() # pragma: no cover