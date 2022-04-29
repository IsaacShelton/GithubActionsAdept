
enable_testing()
add_executable(UnitTestRunner framework/CuTest.c src/HelloWorld.c src/UnitTestRunner.c)
target_include_directories(UnitTestRunner PUBLIC include framework)
add_test(UnitTests UnitTestRunner)
