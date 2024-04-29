! This module contains search algorithms.
MODULE searchutils
    USE omp_lib  ! Corrected from INCLUDE
    IMPLICIT NONE

CONTAINS

    FUNCTION linearSearch(arr, n, x) RESULT(idx)
        REAL(8), INTENT(IN) :: arr(n)
        INTEGER, INTENT(IN) :: n
        REAL(8), INTENT(IN) :: x
        INTEGER :: idx, i
        LOGICAL :: found

        idx = -1
        found = .FALSE.

        ! Parallelize this loop
        !$OMP PARALLEL DO PRIVATE(i, idx) SHARED(arr, n, x, found)
        DO i = 1, n
            IF (arr(i) == x .AND. .NOT. found) THEN
                !$OMP CRITICAL
                IF (.NOT. found) THEN
                    idx = i
                    found = .TRUE.
                END IF
                !$OMP END CRITICAL
            END IF
        END DO
        !$OMP END PARALLEL DO

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
