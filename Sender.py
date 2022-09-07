import random

NUMBER_OF_SENSOR_VALUES = 50
TEMPERATURE_MIN_VALUE = 0
TEMPERATURE_MAX_VALUE = 45
SOC_MIN_VALUE = 0
SOC_MAX_VALUE = 100

#Generate random number
def generate_random_num(num_count,min_num,max_num):
    num_list = []
    for i in range(num_count):
        num_list.append(random.randint(min_num,max_num))
    return num_list
    
#Printing to the console in json format
#Takes sensor data and sensor parameter name as input
def print_in_json(first_sensor_parameter, first_sensor_data, second_sensor_parameter, second_sensor_data):
    for i in range(len(first_sensor_data)):
        print('{{{0}:{1}, {2}:{3}}}\n'.format(first_sensor_parameter, first_sensor_data[i], second_sensor_parameter, second_sensor_data[i]))

#Program starts here
def main_func():
    temperature_list = generate_random_num(NUMBER_OF_SENSOR_VALUES, TEMPERATURE_MIN_VALUE, TEMPERATURE_MAX_VALUE)
    soc_list = generate_random_num(NUMBER_OF_SENSOR_VALUES, SOC_MIN_VALUE, SOC_MAX_VALUE)
    print_in_json("temperature", temperature_list, "soc", soc_list)

if __name__ == '__main__':
    main_func()
    
