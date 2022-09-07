import unittest
from unittest.mock import patch 
import Sender
from Sender import generate_random_num, print_in_json, main_func

class TestSender(unittest.TestCase):
    
    #Test print_in_json()
    #Mocking print function
    @patch('builtins.print')
    def test_print_in_json(self,mock_print):
        temperature_list = [25]
        soc_list = [50]
        output_format_json = '{{{0}:{1}, {2}:{3}}}\n'.format("temperature",temperature_list[0],"soc",soc_list[0])
        print_in_json("temperature",temperature_list,"soc",soc_list)
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
        
if __name__ == '__main__':
    unittest.main()
