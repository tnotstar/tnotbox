#
# A benchmark for reading data from `base::readRDS` vs `feather::read_feather`
#

MY_BIGFILE_FN = "~/Resources/Documents/bigfile.csv"
N = 25

change_filename_ext <- function (fn, ext)
    file.path(dirname(fn), gsub(tools::file_ext(fn), ext, basename(fn)))

library(readr)
library(feather)

rs <- try({
    # read input data from a .csv file
    ds1 <- read_csv2(file=MY_BIGFILE_FN, col_types=strrep("c", 11))

    # open a file connection and writes data to

    conn1 <- file(change_filename_ext(MY_BIGFILE_FN, "rds"), "wb")
    saveRDS(ds1, conn1)
    close(conn1)

    # write data to a feather file
    write_feather(ds1, change_filename_ext(MY_BIGFILE_FN, "feather"))
})
stopifnot(class(rs) != "try-error")

st1 <- sapply(1:N, function(...) {
    system.time(readRDS(file(change_filename_ext(MY_BIGFILE_FN, "rds"), "rb")))
})

st2 <- sapply(1:N, function(...) {
    system.time(read_feather(change_filename_ext(MY_BIGFILE_FN, "feather")))
})

ds3 <- data.frame(readRDS=st1[3,], feather=st2[3,])

png(filename="feather-benchmark1.png", width=480, height=480)
boxplot(ds3, main="Comparativa de tiempos de carga\n`base::readRDS`, `base::readRDS*` vs `feather::read_feather`",
        xlab="Nombre del paquete", ylab="Tiempo (s)")
dev.off()

# EOF