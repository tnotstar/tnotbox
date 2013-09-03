# BazaarR.R - random stuff to work with BazaarVoice's reports

require("RODBC", quietly)

read.reviews <- function (filename) {
    channel <- odbcConnectExcel(filename)
    reviews <- sqlFetch(channel, "All Reviews Report")
    close(channel)
    return(reviews)
}

# EOF
