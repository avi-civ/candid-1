#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <candid.h>
#include <string.h>

int main () {
    char buff[BUFFSIZE];

    /* Read from stdin */
    while (1) {
        struct candump_line *cdl = proc_line(buff);
        printf("Got: %s\n", cdl->interface);
        free(cdl);
    }

    return 0;
}

char *get_line(char* buff) {
    return fgets(buff, BUFFSIZE, stdin);
}

struct candump_line *proc_line(char* buff) {
    struct candump_line *line = malloc(sizeof(struct candump_line));
    if (get_line(buff) == NULL) {
        return NULL;
    }

    memcpy(line->interface, buff, 4);
    line->interface[4] = '\0';
    return line;
}