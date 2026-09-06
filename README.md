# android-wireless-launcher
A lightweight Python utility to automatically discover and connect to wireless Android devices via Wi-Fi using ADB. It features an interactive menu to instantly launch scrcpy in Standard Mirroring, Samsung DeX desktop mode, or a 1920x1080 Virtual Display workspace, complete with robust multi-device support and CLI arguments.

A lightweight Python utility that automatically discovers and connects to wireless Android devices over Wi-Fi via ADB. It features an interactive menu to instantly launch `scrcpy` in **Standard Mirroring** (to seamlessly control your phone directly from your laptop) or **Virtual Display** mode, complete with multi-device support and custom CLI arguments.

---

## 🖥️ Display Modes & Visuals

### 1. Standard Mirroring (Option 1)


Clones and displays your physical phone screen on your computer, allowing you to fully control your device using your laptop's mouse and keyboard. Like this


<img width="320" height="719" alt="Screenshot 2026-09-06 at 7 28 15 PM" src="https://github.com/user-attachments/assets/1d93bdeb-ae43-4afb-8dc3-3811040b2cc0" />



### 2. Virtual Display (Option 2)

Creates a separate, clean 1920x1080 canvas workspace on your device that streams independently to your computer. Like this


<img width="1232" height="719" alt="Screenshot 2026-09-06 at 7 29 25 PM" src="https://github.com/user-attachments/assets/512734a9-8264-4521-af96-22f8250ecfd9" />


---

## ✨ Features

* **Automatic Wi-Fi Discovery:** Scans your local network via ADB and mDNS to automatically detect active wireless debugging connections without manual IP typing.
* **Multi-Device Support:** Seamlessly handles multiple wireless connections and prompts you to choose the target device.
* **Interactive Menu & CLI:** Run interactively for a simple prompt experience or use command-line arguments for scripts and automation.
* **Robust Error Handling:** Built-in Python logging, safe shell subprocess execution, and pre-flight ADB server resets.

---

## 🛠️ Prerequisites

Ensure you have the following tools installed and added to your system's PATH:

* **Python 3.x**
* **ADB (Android Debug Bridge)** — part of Android SDK Platform-Tools
* **scrcpy** — client for displaying and controlling Android devices

---

## 🚀 Installation & Usage

1. Clone the repository:
```bash
  git clone https://github.com/your-username/wireless-android-manager.git
  cd wireless-android-manager

```


2. Turn on **Wireless Debugging** in your phone's *Developer Options* and ensure your computer is connected to the same Wi-Fi network.
3. Run the script:
```bash
python main.py

```

## Notes

 This works when you install the 'scrcpy' check if there is 'scrcpy' in your Device

 Turn on the Wireless debugging in your Phone

 <img width="325" height="726" alt="Screenshot 2026-09-06 at 7 44 59 PM" src="https://github.com/user-attachments/assets/14eb10d6-e1a8-44d6-9562-492e038f270d" />



