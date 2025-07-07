n = 4  # Size of the board (4x4)
x = {}  # Dictionary to store queen positions

def place(k, i):
    # Check if column i is already occupied
    if i in x.values():
        return False
    # Check diagonal conflicts
    for j in range(1, k):
        if abs(x[j] - i) == abs(j - k):
            return False
    return True

def clear_blocks(k):
    # Clear all future rows starting from k
    for i in range(k, n + 1):
        x[i] = None

def Nqueens(k):
    for i in range(1, n + 1):
        clear_blocks(k)
        if place(k, i):
            x[k] = i
            if k == n:
                # All queens are placed successfully
                for j in range(1, n + 1):
                    print(f"Place Queen at row {j}, column {x[j]}")
                print("----------")
            else:
                Nqueens(k + 1)

# Driver code
Nqueens(1)
