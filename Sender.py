import random

NUMBER_OF_SENSOR_VALUES = 50

#Add sensors here
sensor = ["temperature","soc"]

#Set min and max values for sensors
min_max_values = {sensor[0]:[0,45],sensor[1]:[0,100]}

#Generate random number
def generate_random_num(num_count,min_num,max_num):
    num_list = []
    for i in range(num_count):
        num_list.append(random.randint(min_num,max_num))
    return num_list

#To check any invalid value
def check_invalid_value(value,min_value,max_value):
    if value < min_value or value > max_value:
        return True
    else:
        return False

def get_data_length(data):
    if isinstance(data,dict):
        return [len(value) for key,value in data.items()][0]
    else:
        return 0
    
#Printing to the console in json format
#Takes sensor data and sensor parameter name as input
def print_in_json(data):
    data_length = get_data_length(data)
    for data_index in range(data_length):
        printing_format = '{{'
        for sensor in data:
            if check_invalid_value(data[sensor][data_index],min_max_values[sensor][0],min_max_values[sensor][1]):
                data[sensor][data_index] = "INVALID VALUE";
            printing_format = printing_format + '"{0}":{1}'.format(sensor, data[sensor][data_index]) + ', '
        printing_format = printing_format[:len(printing_format)-2] + '}}\n'
        print(printing_format.format())

#Program starts here
def main_func():
    temperature_list = generate_random_num(NUMBER_OF_SENSOR_VALUES, min_max_values[sensor[0]][0], min_max_values[sensor[0]][1])
    soc_list = generate_random_num(NUMBER_OF_SENSOR_VALUES, min_max_values[sensor[1]][0], min_max_values[sensor[1]][1])
    print_in_json({sensor[0]:temperature_list,sensor[1]:soc_list})

if __name__ == '__main__':
    main_func()

