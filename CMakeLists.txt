cmake_minimum_required(VERSION 3.10)

project(HelloWorld)

add_executable(HelloWorld src/main.c)
target_include_directories(HelloWorld PUBLIC include)

enable_testing()
add_subdirectory(tests)
