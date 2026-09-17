func searchMatrix(matrix [][]int, target int) bool {
	results := make(chan bool, len(matrix))
	for i := 0; i < len(matrix); i++ {
		go func(row []int) {
			results <- searchArray(row, target)
		}(matrix[i])
	}
	for i := 0; i < len(matrix); i++ {
		found := <-results
		if found {
			return true
		}
	}
	return false
}
func searchArray(row []int, target int) bool {
	left := 0
    right := len(row) -1
    midpoint := 0
    for left <= right{
        midpoint = (left + right) / 2 //int division so floored#
        if row[midpoint] == target{
            return true
        }else if row[midpoint] < target{
           left = midpoint + 1 
        } else{
            right = midpoint - 1 
        }
}
return false
}