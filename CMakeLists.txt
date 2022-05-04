cmake_minimum_required(VERSION 3.10)

project(adept)

add_executable(adept src/main.c)
target_include_directories(adept PUBLIC include)

enable_testing()
add_subdirectory(tests)
