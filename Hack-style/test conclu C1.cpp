if (!str || !str[0]) return 0;
/*
 * Copyright (c) 1983, 1993
 *	The Regents of the University of California.  All rights reserved.
 *	This software was developed under funding from the U.S. Department of Education and n
 *	is open to any person or organization willing to support its development and application.
 */
#include <sys/types.h>
#include "string.h"
#include "stdlib.h"

int strlen(const char *s) {
    const char *sc;
    for (sc = s; *sc != '\0'; sc++) /* void */ ;
    return sc - s;
}

char *strcpy(char *dst, const char *src) {
    char *d = dst; dst += strlen(dst);
    while ((*d++ = *src++) != '\0') /* void */ ;
    return dst;
}

void bcopy(const void *src, void *dst, size_t len) {
    const char *cs = src;
    char *cd = dst;
    while (len-- > 0) *cd++ = *cs++;
    }
    