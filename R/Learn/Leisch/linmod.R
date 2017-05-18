# linmod.R - code from `Leisch-CreatingPackages.pdf`

linmod <- function (x, ...)
	UseMethod("linmod")

linmod.default <- function(x, y, ...) {

	# try to cast params to espected classes
	x <- as.matrix(x)
	y <- as.numeric(y)

	# compute the QR-decomposition of X
	qx <- qr(x)

	# compute (X'X)^-1 X'y
	coef <- solve.qr(qx, y)

	# calculate degrees of freedom and standard desviation
	df <- nrow(x) - ncol(x)
	sigma2 <- sum((y - x %*% coef)^2)/df

	# compute sigma^2 * (X'X)^-1
	vcov <- sigma2 * chol2inv(qx$qr)
	colnames(vcov) <- rownames(vcov) <- colnames(x)

	estimate <- list(coefficients=coef, df=df, vcov=vcov, sigma=sqrt(sigma2))

	# put any additional computation right here
	estimate$fitted.values <- as.vector(x %*% estimate$coefficients)
	estimate$residuals <- y - estimate$fitted.values
	estimate$call <- match.call()

	# set the class for the calculated object
	class(estimate) <- "linmod"

	# return the default estimation
	return(estimate)
}

linmod.formula <- function (formula, data=list(), ...) {

	# create the model frame and extract its components
	m <- model.frame(formula=formula, data=data)
	x <- model.matrix(attr(m, "terms"), data=m)
	y <- model.response(m)

	# compute the default estimation
	estimate <- linmod.default(x, y, ...)
	estimate$call <- match.call()
	estimate$formula <- formula

	# return the formula estimation
	return(estimate)
}

print.linmod <- function (x, ...) {

	cat("Call (linmod):\n")
	print(x$call)

	cat("\nCoefficients:\n")
	print(x$coefficients)
}

predict.linmod <- function(model, newdata=NULL, ...) {

	if (is.null(newdata)) {
		y <- fitted(model)
	} else {
		if (!is.null(model$formula)) {
			x <- model.matrix(model$formula, newdata)
		} else {
			x <- newdata
		}

		y <- as.vector(x %*% coef(model))
	}

	return(y)
}

summary.linmod <- function(x, ...) {

	# compute the standard errors and `t` values
	se <- sqrt(diag(x$vcov))
	tval <- coef(x) / se

	tabular <- cbind(
		estimate = coef(x),
		stderr = se,
		t.value = tval,
		p.value = 2 * pt(-abs(tval), df=x$df)
	)

	results <- list(call=x$call, coefficients=tabular)
	class(results) <- "summary.linmod"

	return(results)
}

print.summary.linmod <- function (x, ...) {

	cat("Call (summary.linmod):\n")
	print(x$call)

	cat("\nCoefficients:\n")
	printCoefmat(x$coefficients, P.value=TRUE, has.Pvalue=TRUE)
}


data(cats, package="MASS")

x <- cbind(Const=1, Bwt=cats$Bwt)
y <- cats$Hwt

cat("\nPrinting the estimated model:\n")
cat("----------------------------\n")
mod1 <- linmod(x, y)
print(mod1)

cat("\nPrinting summary from given model:\n")
cat("---------------------------------\n")
print(summary(mod1))

cat("\nCoefficients (outside):\n")
cat("----------------------\n")
print(coef(mod1))

cat("\nFitted values (outside):\n")
cat("-----------------------\n")
print(fitted(mod1))

cat("\nResiduals (outside):\n")
cat("-------------------\n")
print(resid(mod1))

cat("\nNow estimate a model from given formula:\n")
cat("---------------------------------------\n")
mod2 <- linmod(Hwt ~ Bwt * Sex, data=cats)
print(summary(mod2))

cat("\nPredictions (outside):\n")
cat("---------------------\n")
newdata <- data.frame(Sex=sample(c('F', 'M'), size=100, replace=TRUE),
		Bwt=runif(100, min(cats$Bwt), max(cats$Bwt)),
		Hwt=rep(0, 100))
print(predict(mod2, newdata))

# EOF
