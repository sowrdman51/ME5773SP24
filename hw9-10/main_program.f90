PROGRAM main_program



  IMPLICIT NONE


  INTEGER, PARAMETER :: N2 = 10000000
  REAL(8), dimension(10) :: arr_test=[1.d0,2.d0,4.d0,5.d0,6.d0,7.d0,9.d0,10.d0,11.d0,15.d0]
  REAL(8) :: arr2(N2)
  REAL(8) :: x, t_start, t_end
  INTEGER :: idx, n
  
  

  n = size(arr_test,1) ! Number of elements in the array.
  x = 7.d0        ! Search for value 7.0 in the array.
  idx = linearsearch(arr_test,n,x)
  print*, "Index computed with linear search: ", idx

  idx = binarySearch(arr_test,n,x)
  print*, "Index computed with binary search: ", idx




  ! ! Uncomment lines 27-54 to check the behavior with sorted arrays.

  ! ! Use here these two cases to evaluate performance.
  ! print*, " -------------------------- "
  ! print*, "Testing on a sorted array"

  !   ! Call the fillSortedArray subroutine to fill arr2 with sorted values.


  ! x = arr2(N2-1)   ! Value of interest: Second to last element.
  ! n = SIZE(arr2,1)

  ! ! Measure the CPU time of this linearsearch function.
  ! CALL CPU_TIME(t_start) ! Start measuring time here
  ! idx = linearsearch(arr2,n,x)
  ! ! Complete the CPU TIME measrurement 
  
  ! ! Idx must be the second to last elemetn.
  ! print*, "Index computed with linear search: ", idx , N2-1
  ! print*, "was the value found?: ", arr2(idx)==x

  ! ! Measure the CPU time of this binarysearch function.
  ! CALL CPU_TIME(t_start) ! Start measuring time here
  ! idx = binarysearch(arr2,n,x)
  ! ! Complete the CPU TIME measrurement 

  ! print*, "Index computed with binary search: ", idx, N2-1
  ! print*, "was the value found?: ", arr2(idx)==x
  


  ! ! Uncomment lines 56-71 to the behavior with unsorted arrays.

  ! print*, " -------------------------- "
  ! print*, "Testing on an unsorted array"

  
  ! ! Call the fillUnsortedArray subroutine to fill arr2 with unsorted values.


  ! x = arr2(N2/2-1) ! Value of interest: midle element -1.
  ! n = SIZE(arr2,1)

  ! idx = linearsearch(arr2,n,x)

  ! print*, "Index computed with linear search: ", idx
  ! print*, "was the value found?: ", arr2(idx)==x

CONTAINS
  
  ! Fill an array with sorted values.
  SUBROUTINE fillSortedArray(array)
    
    IMPLICIT NONE

    REAL(8):: array(:)

    INTEGER :: i

    DO i=1,SIZE(array,1)
      array(i) = (i*3.d0)
    END DO

  END SUBROUTINE fillSortedArray

  ! Fill an array with unsorted values.
  SUBROUTINE fillUnsortedArray(array)
    
    IMPLICIT NONE

    REAL(8):: array(:)

    INTEGER :: i

    DO i=1,SIZE(array,1)
      array(i) = (-1.d0)**(i) * i*2.d0
    END DO

  END SUBROUTINE fillUnsortedArray


END PROGRAM main_program
