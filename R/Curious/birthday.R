#
# birthday.R: a recursive way to solve the Birthday Problem
# original idea from: http://efgh.com/math/birthday.htm
#

different.birthdays <- function(people) {
	ifelse(people == 1, 1.0, different.birthdays(people - 1) * (365.0 - (people - 1))/365.0)
}

birthday.problem <- function(people) 1.0 - different.birthdays(people)

for(n in 1:25) {
	cat(sprintf("%3d: %g\n", n, birthday.problem(n)))
}

# EOF