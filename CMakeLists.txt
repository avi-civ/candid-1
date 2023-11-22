cmake_minimum_required(VERSION 3.10)
project(candid)

set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED True)

include_directories(include)
file(GLOB SOURCES "src/*.c" )

add_executable(candid ${SOURCES})
