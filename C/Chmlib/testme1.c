/*
 */

#include <stdio.h>
#include <stdlib.h>

#include "chm_lib.h"


/**
 */
int _print_uinfo(struct chmFile *hnd, struct chmUnitInfo *ui, void *ctx) {

    printf("> %d %d %d %s\n", ui->space, ui->start, ui->length, ui->path);
    return CHM_ENUMERATOR_CONTINUE;
}

/**
 */
int
do_something_useful_with(struct chmFile *handle) {

    int rs;

    rs = chm_enumerate(handle, CHM_ENUMERATE_ALL, _print_uinfo, NULL);
    if (CHM_ENUMERATOR_FAILURE == rs) {
        fprintf(stderr, "Oops: something's very wrong...\n");
        exit(3);
    }

    fprintf(stderr, "Info: finished!\n");
    return 0;
}

/**
 */
int
main (int argc, char *argv[]) {

    struct chmFile *handle;

    if (argc < 2) {
        fprintf(stderr, "Oops: nothing to do!\n");
        exit(1);
    }

    handle = chm_open(argv[1]);
    if (NULL == handle) {
        fprintf( stderr, "Oops: something's wrong...\n");
        exit(2);
    }

    do_something_useful_with(handle);
    
    chm_close(handle);

    return 0;
}

/* EOF */
