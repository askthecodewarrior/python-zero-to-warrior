# Practice 1: predict the output, then run it
# No network needed: these are numbers connect_ex() really gave back
# in the video (0 = it connected, 61 = connection refused on a Mac).
results = {22: 61, 3306: 0, 8000: 0, 8080: 61}

for port, code in results.items():
    print(port, code == 0, bool(code))
