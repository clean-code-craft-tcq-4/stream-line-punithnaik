from StatisticsComputer import StatisticsComputer

class StatisticsFactory:
    def __init__(self) -> None:
        self.statistics_computer = StatisticsComputer()

    def get_statistical_func_by_name(self, name):
        statistical_functions = {
            "Min": self.statistics_computer.compute_minimum_value,
            "Max": self.statistics_computer.compute_maximum_value,
            "SMA": self.statistics_computer.compute_sma
        }

        return statistical_functions.get(name, None)
