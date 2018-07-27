#
# A benchmark for reading .CSV data with `readr::read:csv` vs `base::read.csv`.
#

MY_BIGFILE_FN = "~/Resources/Documents/bigfile.csv"
N = 24

system(paste("cmd /c dir", gsub("/", "\\", path.expand(MY_BIGFILE_FN), fixed=TRUE)))

st1 <- sapply(1:N, function(...) {
    system.time(read.csv(file=MY_BIGFILE_FN, header=TRUE, sep=";", dec=",", quote="\""))
})

library(readr)

st2 <- sapply(1:N, function(...) {
    system.time(read_csv2(file=MY_BIGFILE_FN, col_types=strrep("c", 11)))
})

ds3 <- data.frame(base=st1[3,], readr=st2[3,])

png(filename="readr-benchmark1.png", width=480, height=480)
boxplot(ds3, main="Comparativa de tiempos de carga\n`base::read.csv` vs `readr::read_csv`",
        xlab="Nombre del paquete", ylab="Tiempo (s)")
dev.off()

# EOF