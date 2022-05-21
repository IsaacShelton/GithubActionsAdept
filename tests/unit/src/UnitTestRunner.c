
#include <stdio.h>
#include <stdlib.h>
#include "CuTest.h"

CuSuite *CuSuite_for_ast_expr();
CuSuite *CuSuite_for_lex();

int RunAllTests(){
    CuString *output = CuStringNew();
    CuSuite* suite = CuSuiteNew();

    CuSuiteAddSuite(suite, CuSuite_for_lex());

    printf("Running...\n");
    CuSuiteRun(suite);
    printf("Done Running...\n");
    CuSuiteSummary(suite, output);
    CuSuiteDetails(suite, output);
    printf("%s\n", output->buffer);
    return suite->failCount;
}

int main(){
    return RunAllTests();
}
