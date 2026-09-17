import(
    "sync"
)
func searchMatrix(matrix [][]int, target int) bool {

    found := make(chan struct{}, 1)
    done := make(chan struct{})

    var wg sync.WaitGroup

    for i := 0; i < len(matrix); i++ {

        wg.Add(1)

        go func(row []int) {
            defer wg.Done()

            if searchArray(row, target) {

                select {
                case found <- struct{}{}:
                default:
                }

            }

        }(matrix[i])
    }

    go func() {
        wg.Wait()
        close(done)
    }()

    select {
    case <-found:
        return true
    case <-done:
        return false
    }
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