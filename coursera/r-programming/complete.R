complete <- function(directory, id=1:332) {
  nobs <- integer(length(id))
  for (i in 1:length(id)) {
    nobs[i] <- sum(complete.cases(read.csv(file.path(directory, sprintf("%03i.csv", id[i])))))
  }
  data.frame(id=id,nobs=nobs)
}