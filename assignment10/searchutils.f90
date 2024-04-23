MODULE searchutils
use omp_lib        
implicit none

contains


! Description: Function that finds the location (idx) of a value x
! in an array using the linear search algorithm.
!
! Find idx such that arr(idx) == x

FUNCTION linearSearch(arr, n, x) RESULT(idx)
   REAL(8) :: arr(n)  ! Array to search
   INTEGER :: n       ! Number of elements in array.
   REAL(8) :: x       ! Value to search for in array.
   INTEGER :: idx     ! Result of the search. [arr(idx) == x]
   INTEGER :: i
   
   idx = -1  ! Initialize index to -1 (indicating not found)
   !$omp parallel do shared(arr, n, x) private(i)
   DO i = 1, n
      IF (arr(i) == x) THEN
	 !$omp atomic write
         idx = i
      END IF
   END DO
   !$omp end parallel do

END FUNCTION linearSearch


!!!FUNCTION linearSearch(arr, n, x) RESULT(idx)
!!    REAL(8), INTENT(IN) :: arr(n)  ! Array to search
!!    INTEGER, INTENT(IN) :: n       ! Number of elements in the array.
!    REAL(8), INTENT(IN) :: x       ! Value to search for.
!    INTEGER :: idx                 ! Result of the search. [arr(idx) == x]
!    INTEGER :: i
!    LOGICAL :: found               ! Flag to indicate if x has been found
!
!    idx = -1                       ! Initialize index to -1 (indicating not found)
!    found = .FALSE.
!
!    !$omp parallel private(i) shared(arr, n, x, idx, found)
!    !$omp do
!    DO i = 1, n
!        IF (.NOT.found .AND. arr(i) == x) THEN
!            !$omp atomic write
!            idx = i
!            !$omp flush(found)
!            found = .TRUE.
!            !$omp flush(found)
!        END IF
!        IF (found) EXIT  ! Exit loop once found is set (not part of OpenMP, normal Fortran EXIT)
!    END DO
!    !$omp end do
!    !$omp end parallel
!
!    RETURN
!END FUNCTION linearSearch



! Description: Function that finds the location (idx) of a value x
! in a sorted array using the binary search algorithm.
!
! Find idx such that arr(idx) == x
!
FUNCTION  binarySearch(arr, n, x) RESULT(idx)
   REAL(8) :: arr(n)  ! Array to search
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

