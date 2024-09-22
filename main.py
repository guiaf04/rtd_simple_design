import machine
import time
import os

# Function to read voltage sensor
def read_voltage():
    adc = machine.ADC(0)  # Use ADC pin GP4
    conversion_factor = 3.3 / (65535)  # ADC conversion factor
    sensor_value = adc.read_u16() * conversion_factor
    return sensor_value
                                                                                                                                                                                                                                                                               
# Function to log voltage data to CSV file
def log_voltage():
    file_name = "voltage_log_pcb_tarde.csv"
    timestamp = time.localtime()
    voltage = read_voltage()
#     print(voltage)
    resistance = 0.003299194 * voltage
    print("Voltage: {:.10f}, Resistance: {:.10f}\n".format(voltage, resistance))
    timestamp_str = format_timestamp(timestamp)
    # Check if CSV file exists, if not create it with header
    if not file_name in os.listdir():
        with open(file_name, 'w') as file:
            file.write('Timestamp,voltage, Resistance\n')
    
    # Append voltage data to CSV file
    with open(file_name, 'a') as file:
        file.write('{},{:.12f},{:.12f}\n'.format(timestamp_str, voltage, resistance))

def format_timestamp(timestamp):
    year, month, day, hour, minute, second, *_ = timestamp
    timestamp_str = "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(year, month, day, hour, minute, second)
    return timestamp_str

# Function to read voltage data from CSV file
def read_voltage_log():
    file_name = "voltage_log_pcb_tarde.csv"
    voltage_data = []
    # Check if CSV file exists
    if file_name in os.listdir():
        with open(file_name, 'r') as file:
            # Skip header line
            next(file)
            # Read each line and parse data
            for line in file:
                parts = line.strip().split(',')
                if len(parts) >= 2:
                    timestamp = parts[0].strip('(')  # Remove any extra characters from the timestamp
                    voltage = float(parts[1])
                    voltage_data.append((timestamp, voltage))
                else:
                    print("Invalid line:", line)
    
    return voltage_data

# Example usage: Log voltage every 5 seconds
while True:    
    log_voltage()
    time.sleep(1)
