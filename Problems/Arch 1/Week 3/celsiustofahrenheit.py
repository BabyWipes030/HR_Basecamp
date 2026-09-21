def celciusFahrenheitConverter():
    print("°C °F")
    for increase in range(10, 101, 10):
        print(increase, (int(increase* 1.8) + 32))

celciusFahrenheitConverter()