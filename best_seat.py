def bestSeat(seats):
    best_seat = -1
    empty_count = -1
    total_empty_count = -1
    for seat in range(1, len(seats) - 1):
        print(f"seat={seat}")
        if seats[seat] == 0:
            left_empties = check_left(seats, seat)
            right_empties = check_right(seats, seat)
            total_empties = left_empties + right_empties
            if left_empties > right_empties:
                empties = right_empties
            else:
                empties = left_empties
            if empties > empty_count or (empties == empty_count and total_empties > total_empty_count):
                best_seat = seat
                empty_count = empties
                total_empty_count = total_empties
    return best_seat

def check_left(seats, seat):
    left = seat - 1
    empties = 0
    while left > 0 and seats[left] == 0:
        empties += 1
        left -= 1
    return empties

def check_right(seats, seat):
    right = seat + 1
    empties = 0
    while right < len(seats) and seats[right] == 0:
        empties += 1
        right += 1
    return empties
