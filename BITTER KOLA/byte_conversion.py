bytes = float(input("Enter a number in bytes: "))
kilobytes = bytes / 1024
megabytes = kilobytes / 1024
gigabytes = megabytes / 1024

print(f"Bytes: {bytes:.2f}\nKilobytes: {kilobytes:.2f}\nMegabytes: {megabytes:.2f}\nGigabytes: {gigabytes:.2f}")
