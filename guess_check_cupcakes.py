totalCupcakes = 28

for d in range (0,28):
    for e in range(0,28):
        for f in range(0,28):
            wantedResult = d + e + f
            if wantedResult == totalCupcakes and d*3 == f and e == d+3:
                print("Correct order is: \n ")
                print(f"David: {d}")
                print(f"Emma: {e}")
                print(f"Frank: {f}")
                break
