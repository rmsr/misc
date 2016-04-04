pollutantmean <- function(directory, pollutant, id = 1:332) {
  # @directory: location of csv files
  # @pollutant: one of 'sulfate' or 'nitrate'
  # @id: which stations to process

  total <- 0
  count <- 0
  for (i in id) {
    data <- read.csv(file.path(directory, sprintf("%03i.csv", i)))[pollutant]
    data <- data[!is.na(data)]
    total <- total + sum(data)
    count <- count + length(data)
  }
  total / count
}