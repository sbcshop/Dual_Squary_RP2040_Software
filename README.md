# Dual_Squary_RP2040_Software

<img src= "" />

Dual Squary RP2040 features two 1.54" square displays, powered by the RP2040 chip, and an onboard 6D MEMS IMU, offering the perfect platform for your creative projects. This powerful combination ensures precise control and dynamic visualization, making it ideal for a wide range of innovative applications.

This github provides getting started guide for Dual Squary RP2040.

### Features:
- Powered by Raspberry Pi RP2040 microcontroller 
- Dual 1.54” Square display arrangement for creative visual interactions
- Board features an array of four WS2812B RGB Led with true 16M color support
- Onboard QMI8658C 6D MEMS inertial measurement unit, incorporates a 3-axis gyroscope and a 3- axis accelerometer
- Power and Charging LED for status indication
- Battery hookup and charging facilities for portability
- Onboard microSD card support for data logging purposes
- Multipurpose GPIOs breakout for additional peripheral interfacing
- Type C interface for power and programming purpose
- Boot Button for programming and 3 User Programmable Buttons to add additional controls to project 


### Specifications:
- **Microcontroller**: RP2040 Dual ARM Cortex-M0+
- **Memory**: 264kB on-chip SRAM, 2MB on-board QSPI flash
- **Supply Voltage**: 5V
- **Operating pin voltage**: 3.3V
- **Display**: 
	- **Display Size**: 1.54” 
	- **Display Type**: IPS TFT Square
	- **Display Resolution**:  240 x 240 pixels
	- **Display colors**: 65K RGB
	- **Display interface**: SPI
	- **Display Driver**: ST7789V
- **Battery Support**: 3.7V Lithium Ion 
- **Battery Charge Management**: MCP73831 
- **RGB LED**: WS2812B  
- **6D IMU Sensor**: QMI8658C
- **Operating Temperature Range**: -20°C ~ +70°C 

## Getting Started with Daul Squary RP2040
### Pinout
<img src= "" />
  
### Interfacing Details
 - **_Dual Display interfacing with RP2040_**
	
   | RP2040 | Main Display | Function |
   |---|---|---|
   | GPIO18 | LCD1_CLK | Clock pin of SPI interface for Display|
   | GPIO19 | LCD1_DIN | MOSI (Master OUT Slave IN) pin of SPI interface|
   | GPIO17  | LCD1_CS | Chip Select pin of SPI interface|
   | GPIO6 | LCD1_DC| Data/Command (MISO) pin of SPI interface|
   | GPIO7 | LCD1_BL | Backlight of display|
   | GPIO16 | LCD1_RST | Reset of display|
	
   | RP2040 | Common Display | Function |
   |---|---|---|
   | GPIO10 | LCD2_CLK | Clock pin of SPI interface for Display|
   | GPIO11 | LCD2_DIN | MOSI (Master OUT Slave IN) pin of SPI interface|
   | GPIO13 | LCD2_CS | Chip Select pin of SPI interface|
   | GPIO14  | LCD2_DC| Data/Command (MISO) pin of SPI interface|
   | GPIO15 | LCD2_BL | Backlight of display|
   | GPIO12 | LCD2_RST | Reset of display|

   ```
    #Code Snippets: Display interfacing
    spi0 = SPI(0, baudrate=40000000, sck=Pin(18), mosi=Pin(19)) # Main (RP2040) board Display SPI pins
    spi1 = SPI(1, baudrate=40000000, sck=Pin(10), mosi=Pin(11))	# Common base board display SPI pins
    
    # Define TFT displays with different CS pins
    tft0 = st7789.ST7789(spi0, 240, 240, reset=Pin(16, Pin.OUT), cs=Pin(17, Pin.OUT), dc=Pin(6, Pin.OUT), backlight=Pin(7, Pin.OUT), rotation=0)
    tft1 = st7789.ST7789(spi1, 240, 240, reset=Pin(12, Pin.OUT), cs=Pin(13, Pin.OUT), dc=Pin(14, Pin.OUT), backlight=Pin(15, Pin.OUT), rotation=0)
    
    tft0.init() 
    tft1.init()
   ```

 - **_SDcard Interface_**
   | RP2040 | SDCard | Function |
   |---|---|---|
   | GPIO2 | CARD_CLK | Clock pin of SPI interface for Display|
   | GPIO3  | CARD_MOSI | MOSI (Master OUT Slave IN) pin of SPI interface|
   | GPIO4 | CARD_MISO  | MISO (Master IN Slave OUT) pin of SPI interface|
   | GPIO5  | CARD_CS  | Chip Select pin of SPI interface|
   ```
   #Code Snippets: SD interfacing
   spi=SPI(0,sck=Pin(2),mosi=Pin(3),miso=Pin(4)) #define and configure sdcard SPI interfacing
   sd=SDCard(spi,Pin(5)) # SDCard(arg1, arg2) => arg1 : SPI, arg2 : CS
   ```
   
- **_QMI8658C IMU Interfacing_**
  | RP2040 | IMU | Function |
  |---|---|---|
  |GPIO21 | I2C_SCL | I2C Serial Clock |
  |GPIO20 | I2C_SDA | I2C Data pin |
  
- **_Buttons Interfacing_**
  | RP2040 | Hardware | Function |
  |---|---|---|
  |GPIO22| BT1 | Programmable Button |
  |GPIO9 | BT2 | Programmable Button |
  |GPIO8 | BT3 | Programmable Button |
  
- _**GPIOs Breakout**_
  | RP2040 | Function |
  |---|---|
  | 3V3 | Supply 3.3V  |
  | GP0 | Multipurpose GPIO |
  | GP1 | Multipurpose GPIO |
  | GND | Supply Ground |
  
### 1. How to Install Boot Firmware 

- Every board will be pre-installed with suitable MicroPython firmware with the inbuilt display driver module, so you can skip this step and jump to [**Step 2**](https://github.com/sbcshop/2x2_Display_PicoW_Software/tree/main#2-running-first-program) for trying Demo Codes.
- In any case, you want to add again **MicroPython firmware**. First, you need to *Press and Hold* the boot button onboard, and then, without releasing the button, connect it to PC/laptop using Type C USB interface. Check below image for reference,
  
  <img src="https://github.com/sbcshop/ArdiPi_Software/blob/main/images/pico_bootmode.gif" width="340" height="228">

- Now your device is in boot mode, and you will see a new mass storage device named "RPI-RP2" as shown in the below figure.

  <img src= "https://github.com/sbcshop/PiCoder-Software/blob/main/images/RPI_folder.jpg" width="720" height="360"/>

- Download the relevant MicroPython firmware file provided in this repo above, ["**_firmware_dual_squary_RP2040.uf2_**"](https://github.com/sbcshop/Dual_Squary_RP2040_Software/blob/main/firmware_dual_squary_RP2040.uf2)
    
  Drag and drop Firmware file onto the RPI-RP2 volume.

  <img src= "https://github.com/sbcshop/2x2_Display_PicoW_Software/blob/main/images/firmware_install.png" width="740" height="463">

<!--
### 2. Running First Program
   - Download **Thonny IDE** from [Download link](https://thonny.org/) as per your OS and install it.
   - Download this github which contains various examples and open anyone of example in Thonny.

     <img src= "https://github.com/sbcshop/2x2_Display_PicoW_Software/blob/main/images/github_download.png" width="767" height="386" />
   - Now we have **Thonny IDE application** and github example codes, Connect hardware to laptop/PC. Open any example code in Thonny IDE. Then select micropython device at the bottom right with a suitable COM port, as shown in the below figure. You might get a different COM port.

     <img src="https://github.com/sbcshop/2x2_Display_PicoW_Software/blob/main/images/select_device.png" width="448" height="196">
  
   - Make sure to save [_**lib**_](https://github.com/sbcshop/2x2_Display_PicoW_Software/tree/main/examples/2x2_Display_PicoW_Round1_28/lib) folder which contains dependent library file to device to avoid any execution error.

      <img src= "https://github.com/sbcshop/2x2_Display_PicoW_Software/blob/main/images/lib_save.png" />

   - Once everything all set, with any demo code open click on green play button to test program.

     <img src= "https://github.com/sbcshop/2x2_Display_PicoW_Software/blob/main/images/run_script.png" />

   - For standalone execution save script into Pico as main.py,

     <img src= "https://github.com/sbcshop/2x2_Display_PicoW_Software/blob/main/images/main_save.png" />

     Try out below provided reference example demo codes and modify to build your own application codes.
     

### Example Codes
   Try reference demo codes to test onboard components, also make sure to save lib folder into Pico W of board which contains library files.
   - [Display Demo Code](https://github.com/sbcshop/2x2_Display_PicoW_Software/blob/main/examples/2x2_Display_PicoW_Square1_54/Demo_4Display.py) : Visualize onboard display working with sample code
   - [BME280 Sensor](https://github.com/sbcshop/2x2_Display_PicoW_Software/blob/main/examples/2x2_Display_PicoW_Square1_54/Demo_BME280.py) : BME280 sensor to read Temperature, humidity and pressure demo
   - [More...](https://github.com/sbcshop/2x2_Display_PicoW_Software/tree/main/examples/2x2_Display_PicoW_Square1_54)

   Using this sample code as a guide, you can modify, build, and share codes!!

   -->
## Resources
  * [Schematic]()
  * [Hardware Files]()
  * [Step File]()
  * [MicroPython getting started for RPi Pico/Pico W](https://docs.micropython.org/en/latest/rp2/quickref.html)
  * [Raspberry Pico Datasheet](https://github.com/sbcshop/2x2_Display_PicoW_Software/blob/main/Documents/pico-w-datasheet.pdf)
  * [QMI8658C Datasheet](https://github.com/sbcshop/2x2_Display_PicoW_Software/blob/main/Documents/ds3231.pdf)
  * [Datasheet](https://github.com/sbcshop/2x2_Display_PicoW_Software/blob/main/Documents/BME280-Datasheet.pdf)


## Related Products  
  * [2x2 Display with ESP32 S3 (Round)](https://shop.sb-components.co.uk/products/2x2-quad-display-board?variant=41538301493331)

    ![2x2 Display with ESP32 S3 (Round)](https://shop.sb-components.co.uk/cdn/shop/files/mainroundesp32.png?v=1720527042&width=300)
    
  * [2x2 Display with ESP32 S3 (Square)](https://shop.sb-components.co.uk/products/2x2-quad-display-board?variant=41538301526099)

    ![2x2 Display with ESP32 S3 (Square)](https://shop.sb-components.co.uk/cdn/shop/files/mainsquareesp32.png?v=1720527077&width=300)
    
  * [Touchsy - 3.2" Touch LCD Display Based on Pico W](https://shop.sb-components.co.uk/products/touchsy-3-2-touch-lcd-display-based-on-pico-w?variant=40828148744275)

    ![Touchsy - 3.2" Touch LCD Display Based on Pico W](https://shop.sb-components.co.uk/cdn/shop/files/touchsypicowresitive.jpg?v=1686903806&width=300)
  
  * [Rotary Encoder - LED Array & Touch LCD Powered by Pico W](https://shop.sb-components.co.uk/products/rotary-encoder-led-array-touch-lcd-for-esp32-pico-hat?variant=41002601676883)

    ![Rotary Encoder - LED Array & Touch LCD Powered by Pico W](https://shop.sb-components.co.uk/cdn/shop/files/RotaryEncoder-LEDArray_TouchLCDforESP32PicoHAT_7.png?v=1710413189&width=300)


## Product License

This is ***open source*** product. Kindly check LICENSE.md file for more information.

Please contact support@sb-components.co.uk for technical support.
<p align="center">
  <img width="360" height="100" src="https://cdn.shopify.com/s/files/1/1217/2104/files/Logo_sb_component_3.png?v=1666086771&width=300">
</p>
