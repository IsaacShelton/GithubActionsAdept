
#include "CuTest.h"

void TestHelloWorld(CuTest *test){
    CuAssertIntEquals(test, 100, 100);
}

CuSuite *HelloWorldSuite(){
    CuSuite* suite = CuSuiteNew();
    SUITE_ADD_TEST(suite, TestHelloWorld);
    return suite;
}
