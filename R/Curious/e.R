#!/usr/bin/env Rscript

##
# calculate the number `e` after `n` iterations
#
e <- function (n) {
	e <- p <- 1;
	for (i in 2:n) {
		e <- e + 1/p
		p <- p * i
	}
	return(e)
}

print(e(10))

# EOF
