import configparser

config = configparser.ConfigParser()

config["DEFAULT"] = {"KEY":"VALUE",
                     "DJF":"LIUDANDAN"
                     }

with open("example.ini","w") as f:
    config.write(f)