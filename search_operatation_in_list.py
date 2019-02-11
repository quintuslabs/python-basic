city = ["bbsr", "ctc", "puri", "balu", "khurda"]
i = 0
count = 1

while count <= len(city):
    if "puri" in city[i]:
        city[i] = "found here"
        print(i)
        print(f"number of city {len(city)}")
    count += 1
    i += 1
print(city)