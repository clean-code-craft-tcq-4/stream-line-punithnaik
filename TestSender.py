import unittest
from unittest.mock import patch 
import Sender
from Sender import generate_random_num, print_in_json, main_func, check_invalid_value

class TestSender(unittest.TestCase):
    
    #Test print_in_json()
    #Mocking print function
    @patch('builtins.print')
    def test_print_in_json_valid_value(self,mock_print):
        temperature_list = [25]
        soc_list = [50]
        output_format_json = '{{"{0}":{1}, "{2}":{3}}}\n'.format("temperature",temperature_list[0],"soc",soc_list[0])
        print_in_json({"temperature":temperature_list,"soc":soc_list})
        mock_print.assert_called_with(output_format_json)

    #Test print_in_json() for temperature less than min
    @patch('builtins.print')
    def test_temperature_less_than_min(self,mock_print):
        temperature_list = [-1]
        soc_list = [0]
        output_format_json = '{{"{0}":{1}, "{2}":{3}}}\n'.format("temperature","INVALID VALUE","soc",soc_list[0])
        print_in_json({"temperature":temperature_list,"soc":soc_list})
        mock_print.assert_called_with(output_format_json)

    #Test print_in_json() for temperature greater than max
    @patch('builtins.print')
    def test_temperature_greater_than_max(self,mock_print):
        temperature_list = [46]
        soc_list = [100]
        output_format_json = '{{"{0}":{1}, "{2}":{3}}}\n'.format("temperature","INVALID VALUE","soc",soc_list[0])
        print_in_json({"temperature":temperature_list,"soc":soc_list})
        mock_print.assert_called_with(output_format_json)

    #Test print_in_json() for soc less than min
    @patch('builtins.print')
    def test_soc_less_than_min(self,mock_print):
        temperature_list = [0]
        soc_list = [-1]
        output_format_json = '{{"{0}":{1}, "{2}":{3}}}\n'.format("temperature",temperature_list[0],"soc","INVALID VALUE")
        print_in_json({"temperature":temperature_list,"soc":soc_list})
        mock_print.assert_called_with(output_format_json)

    #Test print_in_json() for soc greater than max
    @patch('builtins.print')
    def test_soc_greater_than_max(self,mock_print):
        temperature_list = [45]
        soc_list = [101]
        output_format_json = '{{"{0}":{1}, "{2}":{3}}}\n'.format("temperature",temperature_list[0],"soc","INVALID VALUE")
        print_in_json({"temperature":temperature_list,"soc":soc_list})
        mock_print.assert_called_with(output_format_json)

    #Test print_in_json() for both temperature and soc less than min
    @patch('builtins.print')
    def test_temperature_soc_less_than_min(self,mock_print):
        temperature_list = [-1]
        soc_list = [-1]
        output_format_json = '{{"{0}":{1}, "{2}":{3}}}\n'.format("temperature","INVALID VALUE","soc","INVALID VALUE")
        print_in_json({"temperature":temperature_list,"soc":soc_list})
        mock_print.assert_called_with(output_format_json)

    #Test print_in_json() for both temperature and soc greater than max
    @patch('builtins.print')
    def test_temperature_soc_greater_than_max(self,mock_print):
        temperature_list = [46]
        soc_list = [101]
        output_format_json = '{{"{0}":{1}, "{2}":{3}}}\n'.format("temperature","INVALID VALUE","soc","INVALID VALUE")
        print_in_json({"temperature":temperature_list,"soc":soc_list})
        mock_print.assert_called_with(output_format_json)

    #Test generate_random_num() if number of values is 0
    def test_generate_random_num_zero_count(self):
        self.assertTrue(generate_random_num(0,1,10) == [])

    #Test generate_random_num() if number of values is 50
    def test_generate_random_num_fifty_count(self):
        return_value = generate_random_num(50,0,100)
        self.assertTrue(len(return_value) == 50)

    #Test main_func()
    #Mocking generate_random_num
    #Mocking print_in_json
    @patch('Sender.generate_random_num')
    @patch('Sender.print_in_json')
    def test_main_func(self,mock_print_in_json,mock_generate_random_num):
        main_func()
        self.assertEqual(mock_generate_random_num.call_count,2)
        self.assertEqual(mock_print_in_json.call_count,1)

    #Test check_invalid_value
    def test_check_invalid_value(self):
        self.assertFalse(check_invalid_value(20,0,45))
        self.assertTrue(check_invalid_value(-1,0,45))
        self.assertTrue(check_invalid_value(46,0,45))
        self.assertFalse(check_invalid_value(20,0,100))
        self.assertTrue(check_invalid_value(-1,0,100))
        self.assertTrue(check_invalid_value(101,0,100))
      
if __name__ == '__main__':
    unittest.main()
