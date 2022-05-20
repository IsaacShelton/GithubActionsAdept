#!/usr/bin/python3

import sys
from os.path import join, dirname, abspath
from framework import test, e2e_framework_run

e2e_root_dir = dirname(abspath(__file__))
src_dir = join(e2e_root_dir, "src")

def run_all_tests():
    executable = sys.argv[1]
    always = lambda _: True
    
    test("Adept",
        [executable],
        lambda output: b"     /\xe2\xe2\\\n    /    \\    \n   /      \\    \n  /   /\\   \\        The Adept Compiler v2.7 - (c) 2016-2022 Isaac Shelton\n /   /\\__   \\\n/___/    \\___\\\n\nUsage: adept [options] [filename]\n\nOptions:\n    -h, --help        Display this message\n    -e                Execute resulting executable\n    -w                Disable compiler warnings\n    -o FILENAME       Output to FILENAME (relative to working directory)\n    -n FILENAME       Output to FILENAME (relative to file)\n    -c                Emit object file\n    -O0,-O1,-O2,-O3   Set optimization level\n    --windowed        Don't open console with executable (only applies to Windows)\n    -std=2.x          Set standard library version\n    --version         Display compiler version\n    --root            Display root folder\n    --help-advanced   Show lesser used compiler flags\n" in output
    )
    test("address", [executable, join(src_dir, "address/main.adept")], always)
    test("aliases", [executable, join(src_dir, "aliases/main.adept")], always)
    test("alignof", [executable, join(src_dir, "alignof/main.adept")], always)
    test("andor", [executable, join(src_dir, "andor/main.adept")], always)
    test("andor_circuit", [executable, join(src_dir, "andor_circuit/main.adept")], always)
    test("anonymous_composites", [executable, join(src_dir, "anonymous_composites/main.adept")], always)
    test("anonymous_fields", [executable, join(src_dir, "anonymous_fields/main.adept")], always)
    test("any_fixed_array", [executable, join(src_dir, "any_fixed_array/main.adept")], always)
    test("any_function_pointer", [executable, join(src_dir, "any_function_pointer/main.adept")], always)
    test("any_type_as", [executable, join(src_dir, "any_type_as/main.adept")], always)
    test("any_type_info", [executable, join(src_dir, "any_type_info/main.adept")], always)
    test("any_type_inventory", [executable, join(src_dir, "any_type_inventory/main.adept")], always)
    test("any_type_kind", [executable, join(src_dir, "any_type_kind/main.adept")], always)
    test("any_type_list", [executable, join(src_dir, "any_type_list/main.adept")], always)
    test("any_type_offsets", [executable, join(src_dir, "any_type_offsets/main.adept")], always)
    test("any_type_sizes", [executable, join(src_dir, "any_type_sizes/main.adept")], always)
    test("array_access", [executable, join(src_dir, "array_access/main.adept")], always)
    test("as", [executable, join(src_dir, "as/main.adept")], always)
    test("assign_func", [executable, join(src_dir, "assign_func/main.adept")], always)
    test("assign_func_autogen", [executable, join(src_dir, "assign_func_autogen/main.adept")], always)
    test("assignment", [executable, join(src_dir, "assignment/main.adept")], always)
    test("at", [executable, join(src_dir, "at/main.adept")], always)
    test("bitwise", [executable, join(src_dir, "bitwise/main.adept")], always)
    test("bitwise_assign", [executable, join(src_dir, "bitwise_assign/main.adept")], always)
    test("break", [executable, join(src_dir, "break/main.adept")], always)
    test("break_to", [executable, join(src_dir, "break_to/main.adept")], always)
    test("cast", [executable, join(src_dir, "cast/main.adept")], always)
    test("character_literals", [executable, join(src_dir, "character_literals/main.adept")], always)
    test("circular_pointers", [executable, join(src_dir, "circular_pointers/main.adept")], always)
    test("colons_alternative_syntax", [executable, join(src_dir, "colons_alternative_syntax/main.adept")], always)
    test("complement", [executable, join(src_dir, "complement/main.adept")], always)
    test("complex_composite_rtti", [executable, join(src_dir, "complex_composite_rtti/main.adept")], always)
    test("conditionless_block", [executable, join(src_dir, "conditionless_block/main.adept")], always)
    test("conditionless_break_label", [executable, join(src_dir, "conditionless_break_label/main.adept")], always)
    test("const_variables", [executable, join(src_dir, "const_variables/main.adept")], always)
    test("constants", [executable, join(src_dir, "constants/main.adept")], always)
    test("constants_old_style", [executable, join(src_dir, "constants_old_style/main.adept")], always)
    test("constants_scoped", [executable, join(src_dir, "constants_scoped/main.adept")], always)
    test("constructor", [executable, join(src_dir, "constructor/main.adept")], always)
    test("continue", [executable, join(src_dir, "continue/main.adept")], always)
    test("continue_to", [executable, join(src_dir, "continue_to/main.adept")], always)
    test("default_args", [executable, join(src_dir, "default_args/main.adept")], always)
    test("defer", [executable, join(src_dir, "defer/main.adept")], always)
    test("defer_auto_noop", [executable, join(src_dir, "defer_auto_noop/main.adept")], always)
    test("defer_global", [executable, join(src_dir, "defer_global/main.adept")], always)
    test("deprecated", [executable, join(src_dir, "deprecated/main.adept")], always)
    test("disallow",
        [executable, join(src_dir, "disallow/main.adept")],
        lambda output: b"main.adept:20:11: error: Cannot use disallowed 'func print(this *Thing, value int) void = delete'\n  20|     thing.print(1234)\n                ^^^^^\n" in output,
        expected_exitcode=1
    )
    test("disallow_assignment",
        [executable, join(src_dir, "disallow_assignment/main.adept")],
        lambda output: b"main.adept:11:5: error: Assignment for type 'Thing' is not allowed\n  11|     a = b\n          ^\n" in output,
        expected_exitcode=1
    )
    test("disallow_assignment_container",
        [executable, join(src_dir, "disallow_assignment_container/main.adept")],
        lambda output: b"main.adept:13:5: error: Assignment for type 'ThingContainer' is not allowed\n  13|     a = b\n          ^\n" in output,
        expected_exitcode=1
    )
    test("disallow_funcaddr",
        [executable, join(src_dir, "disallow_funcaddr/main.adept")],
        lambda output: b"main.adept:6:38: error: Cannot use disallowed 'func disallowedFunction(value int) int = delete'\n  6|     function_pointer func(int) int = func &disallowedFunction\n                                          ^^^^\n" in output,
        expected_exitcode=1
    )
    test("disallow_poly",
        [executable, join(src_dir, "disallow_poly/main.adept")],
        lambda output: b"main.adept:6:5: error: Cannot call disallowed 'func testWithoutBody(value $T) void = delete'\n  6|     testWithoutBody(10)\n         ^^^^^^^^^^^^^^^" in output,
        expected_exitcode=1
    )
    test("dropped_values", [executable, join(src_dir, "dropped_values/main.adept")], always)
    test("each_in", [executable, join(src_dir, "each_in/main.adept")], always)
    test("each_in_fixed", [executable, join(src_dir, "each_in_fixed/main.adept")], always)
    test("each_in_list", [executable, join(src_dir, "each_in_list/main.adept")], always)
    test("each_in_static", [executable, join(src_dir, "each_in_static/main.adept")], always)
    test("either_way_multiply", [executable, join(src_dir, "either_way_multiply/main.adept")], always)
    test("elif", [executable, join(src_dir, "elif/main.adept")], always)
    test("embed", [executable, join(src_dir, "embed/main.adept")], always)
    test("entry_point", [executable, join(src_dir, "entry_point/main.adept")], always)
    test("enums", [executable, join(src_dir, "enums/main.adept")], always)
    test("equals_func", [executable, join(src_dir, "equals_func/main.adept")], always)
    test("external", [executable, join(src_dir, "external/main.adept")], always)
    test("fallthrough", [executable, join(src_dir, "fallthrough/main.adept")], always)
    test("fixed_array", [executable, join(src_dir, "fixed_array/main.adept")], always)
    test("fixed_array_alternative_syntax", [executable, join(src_dir, "fixed_array_alternative_syntax/main.adept")], always)
    test("fixed_array_assign", [executable, join(src_dir, "fixed_array_assign/main.adept")], always)
    test("fixed_array_deference", [executable, join(src_dir, "fixed_array_deference/main.adept")], always)
    test("fixed_array_pass", [executable, join(src_dir, "fixed_array_pass/main.adept")], always)
    test("fixed_array_var_size", [executable, join(src_dir, "fixed_array_var_size/main.adept")], always)
    test("fixed_array_var_size_field", [executable, join(src_dir, "fixed_array_var_size_field/main.adept")], always)
    test("for", [executable, join(src_dir, "for/main.adept")], always)
    test("foreign_func_optional_names", [executable, join(src_dir, "foreign_func_optional_names/main.adept")], always)
    test("foreign_in_namespace", [executable, join(src_dir, "foreign_in_namespace/main.adept")], always)
    test("func_aliases", [executable, join(src_dir, "func_aliases/main.adept")], always)
    test("func_aliases_va", [executable, join(src_dir, "func_aliases_va/main.adept")], always)
    test("funcaddr", [executable, join(src_dir, "funcaddr/main.adept")], always)
    test("funcaddr_autogen", [executable, join(src_dir, "funcaddr_autogen/main.adept")], always)
    test("funcaddr_autogen_noop_defer", [executable, join(src_dir, "funcaddr_autogen_noop_defer/main.adept")], always)
    test("funcaddrnull", [executable, join(src_dir, "funcaddrnull/main.adept")], always)
    test("funcptr", [executable, join(src_dir, "funcptr/main.adept")], always)
    test("functions", [executable, join(src_dir, "functions/main.adept")], always)
    test("globals", [executable, join(src_dir, "globals/main.adept")], always)
    test("hello_world", [executable, join(src_dir, "hello_world/main.adept")], always)
    test("hexadecimal", [executable, join(src_dir, "hexadecimal/main.adept")], always)
    test("idx_manipulation", [executable, join(src_dir, "idx_manipulation/main.adept")], always)
    test("if", [executable, join(src_dir, "if/main.adept")], always)
    test("ifelse", [executable, join(src_dir, "ifelse/main.adept")], always)
    test("import", [executable, join(src_dir, "import/main.adept")], always)
    test("import_std", [executable, join(src_dir, "import_std/main.adept")], always)
    test("import_std_c_like", [executable, join(src_dir, "import_std_c_like/main.adept")], always)
    test("increment", [executable, join(src_dir, "increment/main.adept")], always)
    test("increment_stmt", [executable, join(src_dir, "increment_stmt/main.adept")], always)
    test("initializer_list", [executable, join(src_dir, "initializer_list/main.adept")], always)
    test("initializer_list_abstract", [executable, join(src_dir, "initializer_list_abstract/main.adept")], always)
    test("inline_declaration", [executable, join(src_dir, "inline_declaration/main.adept")], always)
    test("inner_struct", [executable, join(src_dir, "inner_struct/main.adept")], always)
    test("int_ptr_cast", [executable, join(src_dir, "int_ptr_cast/main.adept")], always)
    test("internal_deference", [executable, join(src_dir, "internal_deference/main.adept")], always)
    test("internal_deference_generic", [executable, join(src_dir, "internal_deference_generic/main.adept")], always)
    test("list_map", [executable, join(src_dir, "list_map/main.adept")], always)
    test("llvm_asm", [executable, join(src_dir, "llvm_asm/main.adept")], always)
    test("loose_struct_syntax", [executable, join(src_dir, "loose_struct_syntax/main.adept")], always)
    test("major_minor_release", [executable, join(src_dir, "major_minor_release/main.adept")], always)
    test("management_access", [executable, join(src_dir, "management_access/main.adept")], always)
    test("management_as", [executable, join(src_dir, "management_as/main.adept")], always)
    test("management_assign", [executable, join(src_dir, "management_assign/main.adept")], always)
    test("management_defer", [executable, join(src_dir, "management_defer/main.adept")], always)
    test("management_math", [executable, join(src_dir, "management_math/main.adept")], always)
    test("management_pass", [executable, join(src_dir, "management_pass/main.adept")], always)
    test("mathassign", [executable, join(src_dir, "mathassign/main.adept")], always)
    test("member", [executable, join(src_dir, "member/main.adept")], always)
    test("meta_dynamic", [executable, join(src_dir, "meta_dynamic/main.adept")], always)
    test("meta_get", [executable, join(src_dir, "meta_get/main.adept")], always)
    test("methods", [executable, join(src_dir, "methods/main.adept")], always)
    test("multiple_declaration", [executable, join(src_dir, "multiple_declaration/main.adept")], always)
    test("namespace_alternative_syntax", [executable, join(src_dir, "namespace_alternative_syntax/main.adept")], always)
    test("namespaces", [executable, join(src_dir, "namespaces/main.adept")], always)
    test("negate", [executable, join(src_dir, "negate/main.adept")], always)
    test("new_cstring", [executable, join(src_dir, "new_cstring/main.adept")], always)
    test("new_delete", [executable, join(src_dir, "new_delete/main.adept")], always)
    test("new_dynamic", [executable, join(src_dir, "new_dynamic/main.adept")], always)
    test("new_undef", [executable, join(src_dir, "new_undef/main.adept")], always)
    test("newline_tolerance", [executable, join(src_dir, "newline_tolerance/main.adept")], always)

e2e_framework_run(run_all_tests)
