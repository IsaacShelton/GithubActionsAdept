
#ifdef __EMSCRIPTEN__
#include <emscripten.h>
#endif

#ifdef _WIN32
#define WIN32_LEAN_AND_MEAN
#include <windows.h>
#else
#define _GNU_SOURCE
#include <stdlib.h>
#endif

#ifdef __linux__
#include <linux/limits.h>
#endif

#include <stdbool.h>
#include <stdio.h>
#include <string.h>

#include "DRVR/compiler.h"
#include "UTIL/color.h"
#include "UTIL/filename.h"
#include "UTIL/ground.h"
#include "UTIL/string.h"

strong_cstr_t filename_name(const char *filename){
    length_t i;
    strong_cstr_t stub;
    length_t filename_length = strlen(filename);

    if(filename_length == 0){
        stub = malloc(filename_length + 1);
        memcpy(stub, filename, filename_length + 1);
        return stub;
    }

    for(i = filename_length - 1; i != 0; i--){
        if(filename[i] == '/' || filename[i] == '\\'){
            length_t stub_size = filename_length - i; // Includes null character
            stub = malloc(stub_size);
            memcpy(stub, &filename[i+1], stub_size);
            return stub;
        }
    }

    stub = malloc(filename_length + 1);
    memcpy(stub, filename, filename_length + 1);
    return stub;
}

weak_cstr_t filename_name_const(weak_cstr_t filename){
    length_t i;
    length_t filename_length = strlen(filename);

    if(filename_length == 0) return "";

    for(i = filename_length - 1 ; i != 0; i--){
        if(filename[i] == '/' || filename[i] == '\\'){
            return &filename[i+1];
        }
    }

    return filename;
}

strong_cstr_t filename_path(const char *filename){
    length_t i;
    length_t filename_length = strlen(filename);
    strong_cstr_t path;

    if(filename_length == 0){
        path = malloc(1);
        path[0] = '\0';
        return path;
    }

    for(i = filename_length - 1 ; i != 0; i--){
        if(filename[i] == '/' || filename[i] == '\\'){
            path = malloc(i + 2);
            memcpy(path, filename, i + 1);
            path[i + 1] = '\0';
            return path;
        }
    }

    path = malloc(1);
    path[0] = '\0';
    return path;
}

strong_cstr_t filename_local(const char *current_filename, const char *local_filename){
    // NOTE: Returns string that must be freed by caller
    // NOTE: Appends 'local_filename' to the path of 'current_filename' and returns result

    if(current_filename == NULL || current_filename[0] == '\0'){
        return strclone("");
    }

    length_t current_filename_cutoff;
    bool found = false;
    strong_cstr_t result;

    for(current_filename_cutoff = strlen(current_filename) - 1; current_filename_cutoff != 0; current_filename_cutoff--){
        if(current_filename[current_filename_cutoff] == '/' || current_filename[current_filename_cutoff] == '\\'){
            found = true;
            break;
        }
    }

    if(found){
        result = malloc(current_filename_cutoff + strlen(local_filename) + 2);
        memcpy(result, current_filename, current_filename_cutoff);
        result[current_filename_cutoff] = '/';
        memcpy(&result[current_filename_cutoff + 1], local_filename, strlen(local_filename) + 1);
        return result;
    } else {
        result = malloc(strlen(local_filename) + 1);
        strcpy(result, local_filename);
        return result;
    }

    return NULL; // Should never be reached
}

strong_cstr_t filename_adept_import(const char *root, const char *filename){
    // NOTE: Returns string that must be freed by caller

    length_t root_len = strlen(root);

    length_t filename_len = strlen(filename);
    char *result = malloc(root_len + filename_len + 8);
    sprintf(result, "%simport/%s", root, filename);
    return result;
}

strong_cstr_t filename_ext(const char *filename, const char *ext_without_dot){
    // NOTE: Returns a newly allocated string with replaced file extension

    length_t i;
    length_t filename_length = strlen(filename);
    maybe_null_strong_cstr_t without_ext = NULL;
    length_t without_ext_length;
    length_t ext_length = strlen(ext_without_dot);

    for(i = filename_length - 1 ; i != 0; i--){
        if(filename[i] == '.'){
            without_ext = malloc(i);
            memcpy(without_ext, filename, i);
            without_ext_length = i;
            break;
        } else if(filename[i] == '/' || filename[i] == '\\'){
            without_ext = strclone(filename);
            without_ext_length = filename_length;
            break;
        }
    }

    if(without_ext == NULL){
        without_ext = strclone(filename);
        without_ext_length = filename_length;
    }

    strong_cstr_t with_ext = malloc(without_ext_length + ext_length + 2);
    memcpy(with_ext, without_ext, without_ext_length);
    memcpy(&with_ext[without_ext_length], ".", 1);
    memcpy(&with_ext[without_ext_length + 1], ext_without_dot, ext_length + 1);
    free(without_ext);
    return with_ext;
}

#ifdef __EMSCRIPTEN__
EM_JS(strong_cstr_t, node_path_resolve, (const char *filename), {
	var path = require('path');
    var contents;

    try {
	    contents = path.resolve(UTF8ToString(filename));
    } catch(error){
        return null;
    }

	bytes = lengthBytesUTF8(contents);
	ptr = _malloc(bytes + 1);
	stringToUTF8(contents, ptr, bytes + 1);
	return ptr;
});
#endif

strong_cstr_t filename_absolute(const char *filename){
    #if defined(__EMSCRIPTEN__)
    return node_path_resolve(filename);
    #elif defined(_WIN32) || defined(_WIN64)

    char *buffer = malloc(512);
    if(GetFullPathName(filename, 512, buffer, NULL) == 0){
        free(buffer);
        return NULL;
    }
    return buffer;

    #else

    char *buffer = realpath(filename, NULL);

    if(buffer == NULL){
        die("filename_absolute() - Could not determine absolute path for '%s'\n", filename);
    }

    #ifdef TRACK_MEMORY_USAGE
    if(buffer)
        memory_track_external_allocation(buffer, strlen(buffer) + 1, __FILE__, __LINE__);
    #endif
    
    return buffer;
    #endif    
}

void filename_auto_ext(strong_cstr_t *out_filename, unsigned int cross_compile_for, unsigned int mode){
    if(mode == FILENAME_AUTO_PACKAGE){
        filename_append_if_missing(out_filename, ".dep");
        return;
    }

    if(mode == FILENAME_AUTO_EXECUTABLE){
        #if defined(__WIN32__)
            // Ignore unused variable 'cross_compile_for'
            (void) cross_compile_for;

            // Windows file extensions
            filename_append_if_missing(out_filename, ".exe");
            return;
        #else
            // MacOS / Linux / General Unix file extensions

            if(cross_compile_for == CROSS_COMPILE_WINDOWS)
                filename_append_if_missing(out_filename, ".exe");
            return;
        #endif
    }
}

void filename_append_if_missing(strong_cstr_t *out_filename, const char *addition){
    length_t length = strlen(*out_filename);
    length_t addition_length = strlen(addition);
    if(addition_length == 0) return;

    if(length < addition_length || strncmp( &((*out_filename)[length - addition_length]), addition, addition_length ) != 0){
        char *new_filename = malloc(length + addition_length + 1);
        memcpy(new_filename, *out_filename, length);
        memcpy(&new_filename[length], addition, addition_length + 1);
        free(*out_filename);
        *out_filename = new_filename;
    }
}

strong_cstr_t filename_without_ext(char *filename){
	length_t i;
    length_t filename_length = strlen(filename);
    maybe_null_strong_cstr_t without_ext = NULL;

    if(filename_length == 0) return strclone("");

    for(i = filename_length - 1 ; i != 0; i--){
        if(filename[i] == '.'){
            without_ext = malloc(i + 1);
            memcpy(without_ext, filename, i);
            without_ext[i] = '\0';
            break;
        } else if(filename[i] == '/' || filename[i] == '\\'){
            return strclone(filename);
        }
    }

	return (without_ext == NULL) ? strclone(filename) : without_ext;
}

void filename_prepend_dotslash_if_needed(strong_cstr_t *filename){
	length_t filename_length = strlen(*filename);
	if(filename_length < 2) return;
	
	if((*filename)[0] != '/' && !((*filename)[0] == '.' && (*filename)[1] == '/')){
		strong_cstr_t new_filename = malloc(2 + filename_length + 1);
        memcpy(&new_filename[0], "./", 2);
        memcpy(&new_filename[2], *filename, filename_length + 1);
		free(*filename);
        *filename = new_filename;
	}
}

