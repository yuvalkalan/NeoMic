# Generated Cmake Pico project file

cmake_minimum_required(VERSION 3.13)

set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# Initialise pico_sdk from installed location
# (note this can come from environment, CMake cache etc)

# == DO NEVER EDIT THE NEXT LINES for Raspberry Pi Pico VS Code Extension to work ==
if(WIN32)
    set(USERHOME $ENV{USERPROFILE})
else()
    set(USERHOME $ENV{HOME})
endif()
set(sdkVersion 2.0.0)
set(toolchainVersion 13_2_Rel1)
set(picotoolVersion 2.0.0)
set(picoVscode ${USERHOME}/.pico-sdk/cmake/pico-vscode.cmake)
if(EXISTS ${picoVscode})
    include(${picoVscode})
endif()
# ====================================================================================
set(PICO_BOARD pico CACHE STRING "Board type")

# Pull in Raspberry Pi Pico SDK (must be before project)
include(pico_sdk_import.cmake)

project(NeoMic C CXX ASM)
# Initialise the Raspberry Pi Pico SDK
pico_sdk_init()

# Add executable. Default name is the project name, version 0.1

add_executable(${PROJECT_NAME} src/main.cpp)

target_sources(${PROJECT_NAME} PRIVATE
    src/main.cpp
    src/BlinkLed/BlinkLed.cpp
    src/Clock/Clock.cpp
    src/LedControl/LedControl.cpp
    src/LedControl/NeoPixelLed/NeoPixelLed.cpp
    src/LedControl/NeoPixelLed/NeoPio/NeoPio.cpp
    src/LedControl/Settings/Settings.cpp
    src/AnalogRead/AnalogRead.cpp
    src/Rotary/Button/Button.cpp
    src/Rotary/Rotary.cpp
    src/LedControl/NeoPixelLed/Color/Color.cpp
    src/SerialIn/SerialIn.cpp
)

# Add any user requested libraries
target_link_libraries(${PROJECT_NAME}
    pico_stdlib
    hardware_pio
    hardware_dma
    hardware_flash
    hardware_adc
    pico_multicore
)

# Modify the below lines to enable/disable output over UART/USB
pico_enable_stdio_uart(${PROJECT_NAME} 0)
pico_enable_stdio_usb(${PROJECT_NAME} 1)

# Create pio header files
pico_generate_pio_header(${PROJECT_NAME}
    ${CMAKE_CURRENT_LIST_DIR}/src/LedControl/NeoPixelLed/NeoPio/NeoPio.pio)

# Create map/bin/hex/uf2 files
pico_add_extra_outputs(${PROJECT_NAME})
