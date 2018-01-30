#!/usr/bin/env Rscript

require("RODBC")

odbcDriverConnect("FILEDSN=TD_Trusted_Production.dsn") -> connection
odbcClose(connection)

# EOF