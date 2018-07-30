#include "mogwai.h"
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <stdio.h>

#include "crypto/neoscrypt.h"
#include "crypto/neoscrypt_old.h"

void mogwai_hash(const char* input, int len, char* output)
{
    neoscrypt((unsigned char*)input, (unsigned char*)output, 0);
    //neoscrypt_old((unsigned char*)input, (unsigned char*)output);
}

