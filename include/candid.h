#ifndef CANDID_H
#define CANDID_H

#define BUFFSIZE 67
#define MAX_INTERFACE_NAME_LENGTH 8

char *get_line(char* buff);
struct candump_line *proc_line(char* line);

struct candump_line {
    char interface[MAX_INTERFACE_NAME_LENGTH];
    int header;
    int dlc;
    int *payload;
};

#endif