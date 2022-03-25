# Python-Autoclicker
A simple autoclicker made with Python using threading

## Setup
After downloading *main.py* and *requirements.txt*, in your terminal, execute:
```
pip install -r requirements.txt 
```

## Usage
- Set the *key* variable to any hotkey you want to use to activate the autoclicker
- The time.sleep() statement denotes the delay between each click. Set it to 0 for maximum performance (insanely fast, may crash computer), or values like 0.05 or 0.03 for more controlled clicking. You can experiment with this to find what suits your computer.
- To run, run the program as administrator on windows. For MacOS, type sudo python3 main.py in your terminal.

## Screenshots
#### Performance with time delay at 0:
<img width="780" alt="Screen Shot 2022-03-25 at 11 47 16 AM" src="https://user-images.githubusercontent.com/75612147/160077183-14dc0ede-99c0-4f12-acfc-b6edfa966b0d.png">

#### Performance with delay at 0.01:
<img width="781" alt="Screen Shot 2022-03-25 at 11 48 13 AM" src="https://user-images.githubusercontent.com/75612147/160077300-9522f358-763d-46fb-942d-141095830451.png">

#### Performance with delay at 0.05:
<img width="781" alt="Screen Shot 2022-03-25 at 11 47 39 AM" src="https://user-images.githubusercontent.com/75612147/160077343-ee5f351d-d2f4-44b8-8d32-9f82eff5a0f4.png">

## WARNING
Setting time delay to 0 creates an insanely huge amounts of clicks in a second. This may cause your computer to crash. Use at your own risk.
