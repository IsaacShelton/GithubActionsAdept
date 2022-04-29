
if (NOT DEFINED ENV{IS_GITHUB_WORKFLOW})
    # Regular Local Testing
    add_test(NAME E2E COMMAND python3 ${CMAKE_CURRENT_SOURCE_DIR}/e2e-runner.py $<TARGET_FILE:HelloWorld> WORKING_DIRECTORY ${EXECUTABLE_OUTPUT_PATH})
else()
    # Github Workflows
    # (we will manually invoke e2e-runner.py)
endif()
