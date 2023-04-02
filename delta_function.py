def delta(x):
    if -0.05< x-0.5 < 0.05:
        return 1-abs(1-2*x)
    else: return 0