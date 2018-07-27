# From: https://developer.teradata.com/blog/odbcteam/2016/02/r-with-teradata-odbc

MY_TESTQUERY_SQL = "
    SELECT DatabaseName
         , TableName
         , ColumnName
         , CommentString
      FROM DBC.Columns
     ORDER
        BY DatabaseName
         , TableName
         , ColumnName;
"
N = 24

library(RODBC)

dbc1 <- RODBC::odbcDriverConnect("FILEDSN=TD_Trusted_Production.dsn")
st1 <- sapply(1:N, function(...) {
    system.time(sqlQuery(dbc1, MY_TESTQUERY_SQL))
})
odbcClose(dbc1)

library(DBI)

dbc2 <- dbConnect(odbc::odbc(), filedsn="TD_Trusted_Production.dsn")
st2 <- sapply(1:N, function(...) {
    system.time(dbGetQuery(dbc2, MY_TESTQUERY_SQL))
})
dbDisconnect(dbc2)

ds3 <- data.frame(RODBC=st1[3,], odbc=st2[3,])

png(filename="odbc-benchmark1.png", width=480, height=480)
boxplot(ds3, main="Comparativa de tiempos de carga\n`RODBC::sqlQuery` vs `odbc::dbGetQuery`",
        xlab="Nombre del paquete", ylab="Tiempo (s)")
dev.off()

# EOF