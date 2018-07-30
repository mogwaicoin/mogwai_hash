void neoscrypt_old(const unsigned char *input, unsigned char *output);

#define SCRYPT_BLOCK_SIZE 64
#define SCRYPT_HASH_BLOCK_SIZE 64
#define SCRYPT_HASH_DIGEST_SIZE 32

typedef uint8_t hash_digest[SCRYPT_HASH_DIGEST_SIZE];

#define ROTL32OLD(a,b) (((a) << (b)) | ((a) >> (32 - b)))
#define ROTR32OLD(a,b) (((a) >> (b)) | ((a) << (32 - b)))
