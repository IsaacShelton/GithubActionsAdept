
#include <stdbool.h>
#include <stdlib.h>

#include "AST/ast.h"
#include "AST/ast_constant.h"
#include "AST/ast_expr.h"
#include "AST/ast_type.h"
#include "DRVR/compiler.h"
#include "LEX/token.h"
#include "PARSE/parse_ctx.h"
#include "PARSE/parse_expr.h"
#include "PARSE/parse_global.h"
#include "PARSE/parse_type.h"
#include "TOKEN/token_data.h"
#include "UTIL/ground.h"
#include "UTIL/trait.h"
#include "UTIL/util.h"

errorcode_t parse_global(parse_ctx_t *ctx){
    length_t *i = ctx->i;
    token_t *tokens = ctx->tokenlist->tokens;
    source_t source = ctx->tokenlist->sources[*i];
    ast_t *ast = ctx->ast;
    trait_t traits = TRAIT_NONE;

    if(ctx->composite_association != NULL){
        compiler_panicf(ctx->compiler, source, "Cannot declare global variable within struct domain");
        return FAILURE;
    }

    while(true){
        if(tokens[*i].id == TOKEN_EXTERNAL){
            traits |= AST_GLOBAL_EXTERNAL;
            (*i)++;
            continue;
        }

        if(tokens[*i].id == TOKEN_THREAD_LOCAL){
            traits |= AST_GLOBAL_THREAD_LOCAL;
            (*i)++;
            continue;
        }    

        break;
    }
    
    strong_cstr_t name = parse_take_word(ctx, "INTERNAL ERROR: Expected word");
    if(name == NULL) return FAILURE;

    parse_prepend_namespace(ctx, &name);

    if(tokens[*i].id == TOKEN_EQUALS){
        // Handle old style constant '==' syntax

        if(parse_old_style_constant_global(ctx, name, source)){
            free(name);
            return FAILURE;
        }

        return SUCCESS;
    }

    if(tokens[*i].id == TOKEN_POD){
        traits |= AST_GLOBAL_POD;
        (*i)++;
    }
    
    ast_expr_t *initial_value = NULL;

    ast_type_t type;
    if(parse_type(ctx, &type)) return FAILURE;

    if(tokens[*i].id == TOKEN_ASSIGN){
        (*i)++;
        if(tokens[*i].id == TOKEN_UNDEF){
             // 'undef' does nothing for globals, so pretend like this is a plain definition
            (*i)++;
        } else if(parse_expr(ctx, &initial_value)){
            ast_type_free(&type);
            return FAILURE;
        }
    }

    if(tokens[*i].id != TOKEN_NEWLINE){
        compiler_panicf(ctx->compiler, ctx->tokenlist->sources[*i], "Expected end-of-line after global variable definition");
        if(initial_value) ast_expr_free_fully(initial_value);
        ast_type_free(&type);
        return FAILURE;
    }

    ast_add_global(ast, name, type, initial_value, traits, source);
    return SUCCESS;
}

errorcode_t parse_constant_definition(parse_ctx_t *ctx, ast_constant_t *out_constant){
    // define NAME = value
    //   ^

    // NOTE: Assumes first token is 'define' keyword
    source_t source = ctx->tokenlist->sources[(*ctx->i)++];

    // Get the name of the constant value
    strong_cstr_t name;
    
    if(ctx->compiler->traits & COMPILER_COLON_COLON && ctx->prename){
        name = ctx->prename;
        ctx->prename = NULL;
    } else {
        name = parse_take_word(ctx, "Expected name for constant definition after 'define' keyword");
    }
    if(name == NULL) return FAILURE;

    // Prepend namespace name
    parse_prepend_namespace(ctx, &name);

    // Eat '='
    if(parse_eat(ctx, TOKEN_ASSIGN, "Expected '=' after name of constant")){
        free(name);
        return FAILURE;
    }

    // Parse the expression of the constant
    ast_expr_t *value;
    if(parse_expr(ctx, &value)){
        free(name);
        return FAILURE;
    }

    if(parse_ctx_peek(ctx) != TOKEN_NEWLINE){
        compiler_panicf(ctx->compiler, parse_ctx_peek_source(ctx), "Expected end-of-line after constant definition");
        ast_expr_free_fully(value);
        free(name);
        return FAILURE;
    }

    // Construct the new constant value
    out_constant->name = name;
    out_constant->expression = value;
    out_constant->traits = TRAIT_NONE;
    out_constant->source = source;
    return SUCCESS;
}

errorcode_t parse_global_constant_definition(parse_ctx_t *ctx){
    ast_t *ast = ctx->ast;

    ast_constant_t new_constant;
    if(parse_constant_definition(ctx, &new_constant)) return FAILURE;

    // Make room for another constant
    expand((void**) &ast->constants, sizeof(ast_constant_t), ast->constants_length, &ast->constants_capacity, 1, 8);
    ast->constants[ast->constants_length++] = new_constant;
    return SUCCESS;
}

errorcode_t parse_old_style_constant_global(parse_ctx_t *ctx, strong_cstr_t name, source_t source){
    // SOME_CONSTANT == value
    //               ^

    ast_t *ast = ctx->ast;
    *(ctx->i) += 1;

    ast_expr_t *value;
    if(parse_expr(ctx, &value)) return FAILURE;

    expand((void**) &ast->constants, sizeof(ast_constant_t), ast->constants_length, &ast->constants_capacity, 1, 8);

    // Prepend namespace name
    parse_prepend_namespace(ctx, &name);

    if(parse_ctx_peek(ctx) != TOKEN_NEWLINE){
        compiler_panicf(ctx->compiler, parse_ctx_peek_source(ctx), "Expected end-of-line after constant expression definition");
        ast_expr_free_fully(value);
        free(name);
        return FAILURE;
    }

    ast_constant_t *constant = &ast->constants[ast->constants_length++];
    constant->name = name;
    constant->expression = value;
    constant->traits = TRAIT_NONE;
    constant->source = source;
    return SUCCESS;
}
