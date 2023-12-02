import psutil

cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
cpu_freq = psutil.cpu_freq(percpu=True)

print("CPU usage per core:")
for i, (percent, freq) in enumerate(zip(cpu_percent, cpu_freq), start=1):
    print(f"Core{i}:{percent}% Frequency: {freq.current} MHz")

virtual_men = psutil.virtual_memory()
swap = psutil.swap_memory()

print("\nVirtual Memory:")
print(f"Total: {virtual_men.total / (1024 ** 3):.2f} GB")
print(f"Used: {virtual_men.used / (1024 ** 3):.2f} GB")
print(f"Swap Total: {swap.total / (1024 ** 3):.2f} GB")
print(f"Swap Used: {swap.used / (1024 ** 3):.2f} GB")

network = psutil.net_io_counters()
print("\nNetwork Information: ")
print(f"Bytes received: {network.bytes_recv}")
print(f"Bytes sent:{network.bytes_sent}")

try:
    temperatures = psutil.sensors_temperatures()
    if temperatures:
        print("\nTemperatures:")
        for name, entries in temperatures.items():
            for entry in entries:
                print(f"{name}: {entry.current}ºC")
    else:
        print("\ninfomação de Temperatura indisponivel")
except AttributeError:
    print("\nTemperature information unavailable.")

#Battery information (if it's a laptop)
battery = psutil.sensors_battery()
if battery:
    plugged = "Plugged in" if battery.power_plugged else "Not plugged in"
    print(f"\nBattery status: {plugged}, {battery.percent}%")
else:
    print("\nBattery information unavailable.")

disk = psutil.disk_usage('/')
print("\nDisk information:")
print(f"Total Disk Space: {disk.total / (1024 ** 3):.2f} GB")
print(f"Total Disk Used: {disk.used / (1024 ** 3):.2f} GB")
print(f"Free Disk Space: {disk.free / (1024 ** 3):.2f} GB")

