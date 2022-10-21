from Constants import INVALID_VALUE, TEMPERATURE, SOC, SENSOR_DATA_FORMAT, SENSOR_INVALID_DATA_FORMAT
class MockSender():
    def format_and_send_data(self, sensor_data):
        formatted_sensor_data = [str(datum) for datum in sensor_data]
        print(formatted_sensor_data)
        return formatted_sensor_data

    def send_valid_data(self):
        sensor_data = [SENSOR_DATA_FORMAT.format(TEMPERATURE, 30, SOC, 50)]*50
        formatted_sensor_data = self.format_and_send_data(sensor_data)
        return formatted_sensor_data

    def send_invalid_data(self):
        sensor_data = [SENSOR_INVALID_DATA_FORMAT.format(TEMPERATURE, INVALID_VALUE, SOC, 50)]*50
        formatted_sensor_data = self.format_and_send_data(sensor_data)
        return formatted_sensor_data 
    