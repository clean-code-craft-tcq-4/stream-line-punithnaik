import random

NUMBER_OF_SENSOR_VALUES = 50
FIRST_SENSOR_MIN_VALUE = 0
FIRST_SENSOR_MAX_VALUE = 45
SECOND_SENSOR_MIN_VALUE = 0
SECOND_SENSOR_MAX_VALUE = 100

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
        if first_sensor_data[i] < FIRST_SENSOR_MIN_VALUE or first_sensor_data[i] > FIRST_SENSOR_MAX_VALUE:
            first_sensor_data[i] = "INVALID VALUE";
        if second_sensor_data[i] < SECOND_SENSOR_MIN_VALUE or second_sensor_data[i] > SECOND_SENSOR_MAX_VALUE:
            second_sensor_data[i] = "INVALID VALUE";
        print('{{"{0}":{1}, "{2}":{3}}}\n'.format(first_sensor_parameter, first_sensor_data[i], second_sensor_parameter, second_sensor_data[i]))

#Program starts here
def main_func():
    temperature_list = generate_random_num(NUMBER_OF_SENSOR_VALUES, FIRST_SENSOR_MIN_VALUE, FIRST_SENSOR_MAX_VALUE)
    soc_list = generate_random_num(NUMBER_OF_SENSOR_VALUES, SECOND_SENSOR_MIN_VALUE, SECOND_SENSOR_MAX_VALUE)
    print_in_json("temperature", temperature_list, "soc", soc_list)

if __name__ == '__main__':
    main_func()
