/**
 * Copyright (c) 2016, Antonio Alvarado Hernández
 * All rights reserved
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may
 * not use this file except in compliance with the License. You may obtain
 * a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 * License for the specific language governing permissions and limitations
 * under the License.
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
