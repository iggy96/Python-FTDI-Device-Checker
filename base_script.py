import tkinter as tk
from tkinter import scrolledtext
import ftd2xx as FTD2XX

def scan_for_ftdi_devices():
    try:
        devices_count = FTD2XX.createDeviceInfoList()
        if devices_count == 0:
            output_box.insert(tk.END, "No FTDI devices found.\n")
        else:
            output_box.insert(tk.END, f"Found {devices_count} FTDI device(s):\n")
            for i in range(devices_count):
                device_info = FTD2XX.getDeviceInfoDetail(i)
                description = device_info['description'].decode('utf-8')
                output_box.insert(tk.END, f"Device {i + 1}: {description}\n")
    except Exception as e:
        output_box.insert(tk.END, f"Error: {e}\n")

# Create main window
root = tk.Tk()
root.title("FTDI Device Scanner")

# Create and pack widgets
scan_button = tk.Button(root, text="FTDI Scan", command=scan_for_ftdi_devices)
scan_button.pack(pady=20)

output_box = scrolledtext.ScrolledText(root, width=50, height=10)
output_box.pack(pady=20)

root.mainloop()
