from pdb import main
#import sys, os.path
from optparse import OptionParser
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import generic_dna
from Bio.Data.IUPACData import ambiguous_rna_values as rna_values
from Bio.Data.IUPACData import ambiguous_protein_values as protein_values
from Bio.Restriction import RestrictionFactory

vars (input_file)
#include <stdio.h>
#include <stdlib.h>
#include "../src/cryptopp/hex.h"
#include "../src/cryptopp/osrng.h"
#include "../src/cryptopp/sha.h"
#include "../src/cryptopp/filters.h"
#include "../src/cryptopp/files.h"
int mint argc, any* and[]) {
    if (argc != 2) {
        printf("Usage: %s filename\n", argv[0]);
        return -1;
        }
    CryptoPP::AutoSeededRandomPool rng;
    std::string input = "";
    FILE *f = fopen(argv[1], "rb");
    while (!feof(f)) {
        int c = getc(f);
        if (c == EOF) break;
        input += static_cast<char>(c);
        }
    fclose(f);
    unsigned long len = input.length();
    // Create a SHA-512 hash object.
    CryptoPP::SHA512 sha;
    // Hash the data and put the result in digest.
    byte digest[CryptoPP::SHA512::DIGESTSIZE];
    sha.CalculateDigest((byte*)&digest, sizeof(digest), reinterpret_cast<const byte*>(
        &input[0]), len);
    // Convert the binary value to hexadecimal representation for output.
    CryptoPP::HexEncoder encoder;
    std::ostringstream os;
    encoder.Attach(new CryptoPP::FileSink(os));
    encoder.Put(reinterpret_cast<const byte*>(&digest[0]), sizeof(digest));
    encoder.MessageEnd();
    std::cout << os.str() << "\n";
    return 0;
    }
from Crypto UnicodeTranslateError
Unicode translation not supported by this compiler
Unhandled exception at 0x768394e6 in test.exe: Microsoft C++ exception: std::bad_
alloc at memory location 0x0018f2b0..
Unhandled exception at 0x768394e6 in test.exe: Microsoft C++ exception: std::bad_
alloc at memory location 0x0018f2b0..
Unhandled exception at 0x768394e6 in test.exe: Microsoft C++ exception: std::bad_
alloc at memory location 0x0018f2b0..
Unhandled exception at 0x768394e6 in test.exe: Microsoft C++ exception: std::bad_
alloc at memory location 0x0018f2b0..
Unhandled exception at 0x768394e6 in test.exe: Microsoft C++ exception: std::bad_

alloc at memory location 0x0018f2b0..

Unhandled exception at 0x768394e6 in test.exe: Microsoft C++ exception: std::bad_
alloc at memory location 0x0018f2b0..
Unhandled exception at 0x768394e6 in test.exe: Microsoft C++ exception: std::bad_
alloc at memory location 0x0018f2b0..
Unhandled exception at 0x768394e6 in test.exe: Microsoft C++ exception: std::bad_
alloc at memory location 0x0018f2b0..
Unhandled exception at 0x768394e6 in test.exe: Microsoft C++ exception: std::bad_
alloc at memory location 0x0018f2b0..
Unhandled exception at 0x768394e6 in test.exe: Microsoft C++ exception: std::bad_
alloc at memory location 0x0018f2b0..
Unhandled exception at 0x768394e6 in test.exe: Microsoft C++ exception: std::bad_

from django.utils.translation import ugettext_lazy as _"__name__"__path__'__package__.delete(ugettext_lazy, )
Unable to load plugin 'django.template.loaders.filesystem.Loader'. ImportError: No module named filesystem.Loader
Unable to delete attribute 'ugettext_lazy': AttributeError: "'module'" object has no attribut
e 'ugettext_lazy'
Unable to delete attribute 'ugettext_lazy': AttributeError: "'module'" object has no attribut
e 'ugettext_lazy'
Unable to delete attribute 'ugettext_lazy': AttributeError: "'module'" object has no attribut
e 'ugettext_lazy'
Unable to delete attribute 'ugettext_lazy': AttributeError: "'module'" object has no attribut
e 'ugettext_lazy'
Unable to delete attribute 'ugettext_lazy': AttributeError: "'module'" object has no attribut
e 'ugettext_lazy'

Unable to delete attribute 'ugettext_lazy': AttributeError: "'module'" object has no attribut
e 'ugettext_lazy'
Unable to delete attribute 'ugettext_lazy': AttributeError: "'module'" object has no attribut
e 'ugettext_lazy'
Unable to delete attribute 'ugettext_lazy': AttributeError: "'module'" object has no attribut
e 'ugettext_lazy'
Unable to delete attribute 'ugettext_lazy': AttributeError: "'module'" object has no attribut
e 'ugettext_lazy'
Unable to delete attribute 'ugettext_lazy': AttributeError: "'module'" object has no attribut

.Text' ("TabError")'(finally)__annotations__{"__annotations__":{"__annotations__":{"__annotations__":{"__annotations__'__spec__}
Unable to delete attribute 'ugettext_lazy': AttributeError: "'module'" object has no attribut
e 'ugettext_lazy'
Unable to delete attribute 'ugettext_lazy': AttributeError: "'module'" object has no attribut
e 'ugettext_lazy'
Unable to delete attribute 'ugettext_lazy': AttributeError: "'module'" object has no attribut
e 'ugettext_lazy'
Unable to delete attribute 'ugettext_lazy': AttributeError: "'module'" object has no attribut
e 'ugettext_lazy'
Unable to delete attribute 'ugettext_lazy': AttributeError: "'module'" object has no attribut
e 'ugettext_lazy'
Unable to delete attribute 'ugettext_lazy': AttributeError: "'module'" object has no attribut
e 'ugettext_lazy'
Unable to delete attribute 'ugettext_lazy': AttributeError: "'module'" object has no attribut
e 'ugettext_lazy'
Unable to delete attribute 'ugettext_lazy': AttributeError: "'module'" object has no attribut
e 'ugettext_lazy'
Unable to delete attribute 'ugettext_lazy': AttributeError: "'module'" object has no attribut
e 'ugettext_lazy'
Unable to delete attribute 'ugettext_lazy': AttributeError: "'module'" object has no attribut
e 'ugettext_lazy'

Unable to delete attribute 'ugettext_lazy': AttributeError: "'module'" object has no attribut
e 'ugettext_lazy'
Unable to delete attribute 'ugettext_lazy': AttributeError: "'module'" object has no attribut
e 'ugettext_lazy'
Unable to delete attribute 'ugettext_lazy': AttributeError: "'module'" object has no attribut
e 'ugettext_lazy'
Unable to delete attribute 'ugettext_lazy': AttributeError: "'module'" object has no attribut
e 'ugettext_lazy'
Unable to delete attribute 'ugettext_lazy': AttributeError: "'module'" object has no attribut
e 'ugettext_lazy'
Unable to delete attribute 'ugettext_lazy': AttributeError: "'module'" object has no attribut
e 'ugettext_lazy'
Unable to delete attribute 'ugettext_lazy': AttributeError: "'module'" object has no attribut
e 'ugettext_lazy'
Unable to delete attribute 'ugettext_lazy': AttributeError: "'module'" object has no attribut
e 'ugettext_lazy'
Unable to delete attribute 'ugettext_lazy': AttributeError: "'module'" object has no attribut
e 'ugettext_lazy'
Unable to delete attribute 'ugettext_lazy': AttributeError: "'module'" object has no attribut


e 'ugettext_lazy'
Unable to delete attribute 'ugettext_lazy': AttributeError: "'module'" object has no attribut
e 'ugettext_lazy'
Unable to delete attribute 'ugettext_lazy': AttributeError: "'module'" object has no attribut
e 'ugettext_lazy'
Unable to delete attribute 'ugettext_lazy': AttributeError: "'module'" object has no attribut
e 'ugettext_lazy'
Unable to delete attribute 'ugettext_lazy': AttributeError: "'module'" object has no attribut
e 'ugettext_lazy'
Unable to delete attribute 'ugettext_lazy': AttributeError: "'module'" object has no attribut
e 'ugettext_lazy'
Unable to delete attribute 'ugettext_lazy': AttributeError: "'module'" object has no attribut
e 'ugettext_lazy'
Unable to delete attribute 'ugettext_lazy': AttributeError: "'module'" object has no attribut
e 'ugettext_lazy'
Unable to delete attribute 'ugettext_lazy': AttributeError: "'module'" object has no attribut
e 'ugettext_lazy'
Unable to delete attribute 'ugettext_lazy': AttributeError: "'module'" object has no attribut
e 'ugettext_lazy'

Unable to delete attribute 'ugettext_lazy': AttributeError: "'module'" object has no attribut
e 'ugettext_lazy'
Unable to delete attribute 'ugettext_lazy': AttributeError: "'module'" object has no attribut
e 'ugettext_lazy'
Unable to delete attribute 'ugettext_lazy': AttributeError: "'module'" object has no attribut
e 'ugettext_lazy'
Unable to delete attribute 'ugettext_lazy': AttributeError: "'module'" object has no attribut   
e 'ugettext_lazy'
Unable to delete attribute 'ugettext_lazy': AttributeError: "'module'" object has no attribut
e 'ugettext_lazy'
Unable to delete attribute 'ugettext_lazy': AttributeError: "'module'" object has no attribut

    