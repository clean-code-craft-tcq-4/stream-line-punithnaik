from Constants import MAXIMUM, MINIMUM, SIMPLE_MOVING_AVERAGE, TEMPERATURE, SOC


SENSOR_READINGS = "SensorReadings"
FORMATTED_READINGS = "FormattedReadings"
STATISTICS = "Statistics"
CONSOLIDATED_STATISTICS = "ConsolidatedStatistics"

SENSOR_INPUT_1 = [20, 30, -10, 0, 10]
SENSOR_INPUT_2 = [100, 50, 17, 43, 9]
STATISTICS_OUTPUT_1 = {'Min': -10, 'Max': 30, 'SMA': 10.0}
STATISTICS_OUTPUT_2 = {'Min': 9, 'Max': 100, 'SMA': 43.8}

VALIDATE_MINIMUM_VALUE = [{
    SENSOR_READINGS : SENSOR_INPUT_1,
    MINIMUM : -10
},
{
    SENSOR_READINGS : SENSOR_INPUT_2,
    MINIMUM : 9
}]

VALIDATE_MAXIMUM_VALUE = [{
    SENSOR_READINGS : SENSOR_INPUT_1,
    MAXIMUM : 30
},
{
    SENSOR_READINGS : SENSOR_INPUT_2,
    MAXIMUM : 100
}]

VALIDATE_SMA_VALUE = [{
    SENSOR_READINGS : SENSOR_INPUT_1,
    SIMPLE_MOVING_AVERAGE : 10.0
},
{
    SENSOR_READINGS : SENSOR_INPUT_2,
    SIMPLE_MOVING_AVERAGE : 43.8
}]

VALIDATE_FORMAT_DATA = [
    {
        SENSOR_READINGS : [
                    {TEMPERATURE: 50, SOC: 20},
                    {TEMPERATURE: 51, SOC: 60},
                    {TEMPERATURE: 21, SOC: 90}
                ],
        FORMATTED_READINGS: {TEMPERATURE: [50, 51, 21], SOC: [20, 60, 90]}
    },
    {
        SENSOR_READINGS : [
                    {TEMPERATURE: -10, SOC: 23},
                    {TEMPERATURE: 31, SOC: 68},
                    {TEMPERATURE: 91, SOC: 99}
                ],
        FORMATTED_READINGS: {TEMPERATURE: [-10, 31, 91], SOC: [23, 68, 99]}
    }
]

VALIDATE_STATISTICS_COMPUTATION = [{
    SENSOR_READINGS : SENSOR_INPUT_1,
    STATISTICS : STATISTICS_OUTPUT_1
},
{
    SENSOR_READINGS : SENSOR_INPUT_2,
    STATISTICS : STATISTICS_OUTPUT_2
}]

VALIDATE_CONSOLIDATION = [
    {
        SENSOR_READINGS: {TEMPERATURE: [50, 51, 21, 10, 100], SOC: [20, 60, 90, 30, 75]},
        CONSOLIDATED_STATISTICS : {
            SOC: 
            {SIMPLE_MOVING_AVERAGE: 55.0, MAXIMUM: 90, MINIMUM: 20},
            TEMPERATURE: 
            {SIMPLE_MOVING_AVERAGE: 46.4, MAXIMUM: 100, MINIMUM: 10}}
    },
    {
        SENSOR_READINGS: {TEMPERATURE: [-10, 13, 26, 87, 73], SOC: [100, 82, 64, 39, 55]},
        CONSOLIDATED_STATISTICS : {
            SOC: 
            {SIMPLE_MOVING_AVERAGE: 68.0, MAXIMUM: 100, MINIMUM: 39},
            TEMPERATURE: 
            {SIMPLE_MOVING_AVERAGE: 37.8, MAXIMUM: 87, MINIMUM: -10}}
    }
]