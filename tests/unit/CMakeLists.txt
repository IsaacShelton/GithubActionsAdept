
enable_testing()

add_executable(UnitTestRunner framework/CuTest.c
    src/ast_expr.test.c
    src/lex.test.c
    src/UnitTestRunner.c)

target_include_directories(UnitTestRunner PUBLIC include framework)
target_link_directories(UnitTestRunner PUBLIC ${CURL_LIBRARY_DIRS})
target_link_directories(UnitTestRunner PUBLIC ${LLVM_LIBRARY_DIRS})

message(STATUS "Linking against LLVM statically")
message(STATUS "${LLVM_LIBRARY_DIRS}/../bin/llvm-config")
execute_process(COMMAND ${LLVM_LIBRARY_DIRS}/../bin/llvm-config --link-static --libs OUTPUT_STRIP_TRAILING_WHITESPACE OUTPUT_VARIABLE llvm_static_libs)
message(STATUS ${CURL_LIBRARIES} ${llvm_static_libs} ${EXTRA_REQUIRED_LIBS})
target_link_libraries(UnitTestRunner ${CURL_LIBRARIES} ${llvm_static_libs} ${extra_libs})

set_target_properties(UnitTestRunner adept PROPERTIES LINKER_LANGUAGE CXX)
target_link_libraries(UnitTestRunner libadept)
add_test(UnitTests UnitTestRunner)
