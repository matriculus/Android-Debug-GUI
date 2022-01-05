from configparser import ConfigParser

config_object = ConfigParser()

if path.exists("config.ini"):
    pass
else:
    config_object["Windows"] = {
        "BACKGROUND": "light green",
        "FONT": "Arial",
        "FONTSIZE": 12
    }
    with open("config.ini", "w") as conf:
        config_object.write(conf)

# Read config.ini file
config_object.read("config.ini")