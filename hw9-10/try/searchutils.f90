! This module contains search algorithms.
MODULE searchutils
    IMPLICIT NONE
CONTAINS

    ! Linear search algorithm
    FUNCTION linearSearch(arr, n, x) RESULT(idx)
        REAL(8), INTENT(IN) :: arr(n)
        INTEGER, INTENT(IN) :: n
        REAL(8), INTENT(IN) :: x
        INTEGER :: idx, i

        idx = -1  ! Default to -1 if not found
        DO i = 1, n
            IF (arr(i) == x) THEN
                idx = i
                EXIT
            END IF
        END DO
    END FUNCTION linearSearch

    ! Binary search algorithm
    FUNCTION binarySearch(arr, n, x) RESULT(idx)
        REAL(8), INTENT(IN) :: arr(n)
        INTEGER, INTENT(IN) :: n
        REAL(8), INTENT(IN) :: x
        INTEGER :: idx, low, high, mid

        low = 1
        high = n
        idx = -1  ! Default to -1 if not found

        DO WHILE (low <= high)
            mid = (low + high) / 2
            IF (arr(mid) == x) THEN
                idx = mid
                EXIT
            ELSEIF (arr(mid) < x) THEN
                low = mid + 1
            ELSE
                high = mid - 1
            END IF
        END DO
    END FUNCTION binarySearch

END MODULE searchutils
