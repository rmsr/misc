## Week 3 R programming assignment
## Simulate object oriented programming using R lists

## Factory for a list of operations related to caching the inverse of a matrix
## (R's version of an object I guess. Reminds me of JavaScript only worse.
## Also, It's not correct to say it returns a 'specialized matrix', since the
## list cannot be directly substituted for a matrix.)
makeCacheMatrix <- function(m = matrix()) {
  i <- NULL
  # Yes I'm being a little cheesy here, skipping the intermediate local
  # variables for my method definitions.
  list(
    set = function(x) {
      m <<- x
      i <<- NULL
    },
    get = function() m,
    setinverse = function(x) i <<- x,
    getinverse = function() i
  )
}


## Return a cached matrix inverse or calculate and store it
## (We would normally implement this within getinverse(), where it has
## direct access to the member variables we need.)
cacheSolve <- function(x) {
  i <- x$getinverse()
  if (!is.null(i))
    return(i)
  i <- solve(x$get())
  x$setinverse(i)
  i
}
