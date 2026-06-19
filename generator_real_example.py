tests=["RTC","Eeprom","SPI","UART","USB","I2c"]

def get_tests():
    yield "RTC"
    yield "I2C"
    yield "Eeprom"
    yield "SPI"
    yield "UART"
    yield "USB"

for test in get_tests():
     print("Running",test)
