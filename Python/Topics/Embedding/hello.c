#ifdef MS_WINDOWS
#include <windows.h>
#endif

#include <stdio.h>
#include <Python.h>

int
main (int argc, char *argv[]) {

    printf("Beginning...\n");

    Py_SetProgramName(argv[0]);
    Py_Initialize();
    PyRun_SimpleString("print 'Hello, from Python!'");
    Py_Finalize();

    printf("Finished!\n");
    return 0;
}

/* EOF */