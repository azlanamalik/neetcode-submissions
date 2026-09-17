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
	for i := 0; i < len(row); i++ {
		if row[i] == target {
			return true
		}
	}

	return false
}