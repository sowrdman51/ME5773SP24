MODULE searchutils
implicit none

contains


! Description: Function that finds the location (idx) of a value x
! in an array using the linear search algorithm.
!
! Find idx such that arr(idx) == x
!
FUNCTION linearSearch(arr, n, x) RESULT(idx)
   REAL(8), DIMENSION(n) :: arr(n)  ! Array to search
   INTEGER :: n       ! Number of elements in array.
   REAL(8) :: x       ! Value to search for in array.
   INTEGER :: idx     ! Result of the search. [arr(idx) == x]
   INTEGER :: i
   
   idx = -1  ! Initialize index to -1 (indicating not found)
   DO i = 1, n
        IF (arr(i) == x) THEN
           idx = i 
           EXIT 
        END IF
   END DO
END FUNCTION linearSearch


! Description: Function that finds the location (idx) of a value x
! in a sorted array using the binary search algorithm.
!
! Find idx such that arr(idx) == x
!
FUNCTION  binarySearch(arr, n, x) RESULT(idx)
   REAL(8), DIMENSION(n) :: arr(n)  ! Array to search
   INTEGER :: n       ! Number of elements in array.
   REAL(8) :: x       ! Value to search for in array.
   INTEGER :: idx     ! Result of the search. [arr(idx) == x]
   INTEGER :: low, high, mid      ! Indices for binary search
   
   idx  = -1 
   low  =  1    
   high =  n  
   
   DO WHILE (low <= high)
       mid = (low + high) / 2
       IF (arr(mid) == x) THEN
           idx = mid 
           EXIT       
       ELSE IF (arr(mid) < x) THEN
           low = mid + 1 
       ELSE
           high = mid - 1 
       END IF
   END DO
END FUNCTION binarySearch

END MODULE searchutils

