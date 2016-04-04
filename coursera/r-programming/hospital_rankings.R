best <- function(state, outcome) {
  data <- read.csv("outcome-of-care-measures.csv", colClasses = "character")
  outcome_map <- list(
    "pneumonia"=23,
    "heart attack"=11,
    "heart failure"=17
  )

  if (!(state %in% data$State))
    stop("invalid state")
  
  if (!(outcome %in% names(outcome_map)))
    stop("invalid outcome")
  
  outcome_idx <- outcome_map[[outcome]]
  state_data <- data[data$State == state,]
  state_data[, outcome_idx] <- suppressWarnings(as.numeric(state_data[,outcome_idx]))
  state_ordered <- state_data[order(state_data[outcome_map[[outcome]]], state_data$Hospital.Name),]
  head(state_ordered, 1)$Hospital.Name
  # return hospital in state with lowest 30-day death rate for outcome and lowest alpha
}

rankhospital <- function(state, outcome, num="best") {
  outcomes <- read.csv("outcome-of-care-measures.csv", colClasses = "character")
  outcome_map <- list(
    "pneumonia"=23,
    "heart attack"=11,
    "heart failure"=17
  )
  
  if (!(state %in% outcomes$State))
    stop("invalid state")
  
  if (!(outcome %in% names(outcome_map)))
    stop("invalid outcome")
  
  outcome_idx <- outcome_map[[outcome]]
  state_data <- outcomes[outcomes$State == state,]
  state_data[, outcome_idx] <- suppressWarnings(as.numeric(state_data[,outcome_idx]))
  state_data <- state_data[!is.na(state_data[outcome_idx]),]
  state_data <- state_data[order(state_data[outcome_idx], state_data$Hospital.Name),]
  
  if (num == "worst") {
    tail(state_data, 1)$Hospital.Name
  } else {
    if (num == "best") {
      num <- 1
    }
    state_data[num,]$Hospital.Name
  }
}

rankall <- function(outcome, num="best") {
  outcomes <- read.csv("outcome-of-care-measures.csv", colClasses = "character")
  outcome_map <- list(
    "pneumonia"=23,
    "heart attack"=11,
    "heart failure"=17
  )
  
  if (!(outcome %in% names(outcome_map)))
    stop("invalid outcome")
  
  outcome_idx <- outcome_map[[outcome]]
  
  outcomes[, outcome_idx] <- suppressWarnings(as.numeric(outcomes[,outcome_idx]))
  outcomes <- outcomes[!is.na(outcomes[outcome_idx]),]
  outcomes <- outcomes[order(outcomes[outcome_idx], outcomes$Hospital.Name),]
  hospitals = character(50)
  states <- unique(outcomes$State)
  states <- states[order(states)]
  for (i in 1:length(states)) {
    state_outcomes <- outcomes[outcomes$State == states[i],]
    
    if (num == "worst") {
      hospitals[i] <- tail(state_outcomes, 1)$Hospital.Name
    } else {
      if (num == "best") {
        num <- 1
      }
      hospitals[i] <- state_outcomes[num,]$Hospital.Name
    }
  }
  data.frame(hospital=hospitals, state=states)
}