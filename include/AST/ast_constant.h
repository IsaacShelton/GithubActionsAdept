
#ifndef _ISAAC_AST_CONSTANT_H
#define _ISAAC_AST_CONSTANT_H

/*
    ============================= ast_constant.h ==============================
    Module for abstract syntax tree named constant expressions
    ---------------------------------------------------------------------------
*/

#ifdef __cplusplus
extern "C" {
#endif

#include "UTIL/ground.h"
#include "UTIL/trait.h"
#include "AST/ast_expr_lean.h"

// ---------------- ast_constant_t ----------------
// A named constant expression
typedef struct {
    strong_cstr_t name;
    ast_expr_t *expression;
    trait_t traits;
    source_t source;
} ast_constant_t;

// ---------------- ast_constant_clone ----------------
// Creates a clone of a named AST constant
ast_constant_t ast_constant_clone(ast_constant_t *original);

// ---------------- ast_constant_make_empty ----------------
// Makes an AST constant empty, so that it looses ownership
// of its members
void ast_constant_make_empty(ast_constant_t *out_constant);

#ifdef __cplusplus
}
#endif

#endif // _ISAAC_AST_CONSTANT_H
