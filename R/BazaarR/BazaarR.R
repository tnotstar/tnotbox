# BazaarR.R - random stuff to work with BazaarVoice's reports

require("XLConnect", quietly=TRUE)
require("tm", quietly=TRUE)

readReviews <- function(filename, cleanup_data=TRUE) {

    # read raw data from the input file
    reviews <- readWorksheetFromFile(filename, "All Reviews Report",
        startRow=3, rownames=FALSE)

    # cleaning up and data conversions
    if(cleanup_data) {
        # clean up column values and data types
        reviews$Review.ID <- as.character(reviews$Review.ID)
        reviews$Moderation.Status <- as.factor(reviews$Moderation.Status)
        reviews$Published.Date <- reviews$Initial.Publish.Date
        reviews$User.ID <- as.factor(reviews$User.ID)
        reviews$User.Location <- as.factor(tolower(reviews$User.Location))
        reviews$Product.ID <- as.factor(reviews$Product.ID)
        reviews$Product.Name <- as.factor(reviews$Product.Name)
        reviews$Product.Brand <- as.factor(reviews$Product.Brand)
        reviews$Category.ID <- as.factor(reviews$Category.ID)
        reviews$Category.Name <- as.factor(reviews$Category)
        reviews$Category.Hierarchy <- as.factor(reviews$Category.Hierarchy)
        reviews$Top.Level.Category.ID <- as.factor(reviews$Top.Level.Category.ID)
        reviews$Top.Level.Category.Name <- as.factor(reviews$Top.Level.Category)
        reviews$Rating <- as.numeric(reviews$Overall.Rating)
        reviews$Title <- as.character(tolower(reviews$Review.Title))
        reviews$Review <- as.character(tolower(reviews$Review.Text))

        # select columns to build a subset
        columns <- c(
            "Review.ID",
            "Moderation.Status",
            "Submission.Date",
            "Published.Date",
            "User.ID",
            "User.Location",
            "Product.ID",
            "Product.Name",
            "Product.Brand",
            "Category.ID",
            "Category.Name",
            "Category.Hierarchy",
            "Top.Level.Category.ID",
            "Top.Level.Category.Name",
            "Rating",
            "Title",
            "Review"
        )
        reviews <- subset(reviews, Moderation.Status != "PENDING", columns)
    }

    # return the cleaned up data frame
    return(reviews)
}

saveReviews <- function(datafile, reviews) {

    # save the given data frame to a file in native format
    save(reviews, file=datafile, compress=TRUE)
}

loadReviews <- function(datafile) {

    # load the file with given name into the current environment
    load(datafile)

    # just return the object named `reviews`
    return(reviews)
}

createReviewsCorpus <- function(reviews, cleanup_data=FALSE) {

    # create the base corpus from given review texts
    corpus <- Corpus(VectorSource(reviews[,"Review"]))

    # cleaning up and data conversions
    if(cleanup_data) {
        # pre-processes the base corpus
        corpus <- tm_map(corpus, tolower)
        corpus <- tm_map(corpus, removePunctuation)
        corpus <- tm_map(corpus, removeWords, stopwords("spanish"))
        corpus <- tm_map(corpus, stripWhitespace)
    }

    # return the pre-processed corpus
    return(corpus)
}

createReviewsTDM <- function(corpus) {

    # make a control list for pre-processing
    control <- list()
}

# EOF
