#!/usr/bin/env RScript

# https://mran.microsoft.com/documents/rro/multithread
#http://blog.revolutionanalytics.com/2014/10/revolution-r-open-mkl.html

#
# This script has beed stolen from: https://gist.github.com/andrie/24c9672f1ea39af89c66
# but added bugs are mine
#

cat("Loading required packages...\n")

# used to set MKL threads if Revolution R Open or Revolution R Enterprise is available
require("RevoUtilsMath")

cat("Initializing test data...\n")

if(exists("setMKLthreads"))
    setMKLthreads(1)

# initializes random data
m <- 10000
n <-  5000
A <- matrix(runif(m*n), m, n)

cat("Trying to test with just one thread...\n")

if(exists("setMKLthreads"))
    setMKLthreads(1)

system.time(B1 <- crossprod(A))

if(exists("setMKLthreads"))
    setMKLthreads(2)

system.time(B2 <- crossprod(A))


if(exists("setMKLthreads"))
    setMKLthreads(3)

system.time(B3 <- crossprod(A))

# EOF