class StatisticsComputer:

    def compute_minimum_value(self, data):
        minimum = min(data)
        return minimum
    
    def compute_maximum_value(self, data):
        maximum = max(data)
        return maximum

    def compute_sma(self, data):
        data = data[-5:]
        sma = sum(data) / len(data)
        return sma