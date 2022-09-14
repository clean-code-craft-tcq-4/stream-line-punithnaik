class MockSender():
    def send_data(self):
        sensor_data = ['{{"{0}":{1}, "{2}":{3}}}\n'.format("temperature", 30, "soc", 50)]*50
        formatted_sensor_data = [str(datum) for datum in sensor_data]
        print(formatted_sensor_data)
        return formatted_sensor_data

    def send_invalid_data(self):
        sensor_data = ['{{"{0}":"{1}", "{2}":{3}}}\n'.format("temperature", "INVALID VALUE", "soc", 50)]*50
        formatted_sensor_data = [str(datum) for datum in sensor_data]
        print(formatted_sensor_data)
        return formatted_sensor_data 
    