corr <- function(directory, threshold = 0) {
  corrs <- numeric()
  for (id in 1:332) {
    data <- read.csv(file.path(directory, sprintf("%03i.csv", id)))
    if (sum(complete.cases(data)) <= threshold) {
      next
    }
    data <- data[complete.cases(data),]
    corrs <- c(corrs, cor(data$sulfate, data$nitrate))
  }
  corrs
}