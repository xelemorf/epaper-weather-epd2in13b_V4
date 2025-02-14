# ePaper-Weather-epd2in13b_V4

## Description

![showcase](https://github.com/xelemorf/epaper-weather-epd2in13b_V4/assets/979681/0ba047d8-bf32-45f6-825e-cebcf3c97c2e)

A program to display weather and other useless information you could get by looking at the window.
This is based on Nerstak's project, I modified it to epd2in13b_V4 Black-White-Red display using black colors only for now and removed the DHT22 sensor requirement.

Please find Nerstak's original project here (from which this was forked): https://github.com/nerstak/epaper-weather

### Technologies used

Software:

- Python3
- Waveshare epd2in13b_V4 e-paper lib included (Source: https://github.com/waveshare/e-Paper/blob/master/RaspberryPi_JetsonNano/python/lib/)

Hardware (you are not required to use the exact same one, but you'll need to adapt the program):

- Raspberry Pi 3A+, Raspberry Pi Zero 2 WH (Recommended), Raspberry Pi 4B
- Waveshare epd2in13b_V4 display: https://www.waveshare.com/wiki/2.13inch_e-Paper_HAT_(B)_Manual (you can find it on AliExpress)

### Features

- Display current weather (temperature, humidity, rain)
- Display 24hours forecast
- Display sunrise and sunset time

## Usage

### Installation

#### OpenWeather

Go to [OpenWeather](https://openweathermap.org/price#current), create an account and create a key for the Professional
Collection Free Tier. This tier **does not** require a credit card.

#### ePaper Weather

Download the `lib` folder
from [waveshare repository](https://github.com/waveshare/e-Paper/tree/master/RaspberryPi_JetsonNano/python/lib/waveshare_epd),
and put it at the root of the project

#### config.yaml

Copy the file `config.example.yaml` and name the new file `config.yaml`. Inside, you will need to configure the
following elements:

- `API_KEY`: The OpenWeather key you created just before. This **your** personal key, it won't leave you device
- `unit`: `metric` or `imperial`
- `coordinates`: Coordinates of the place you want to track the weather of. Use this website for
  help: [LatLong.net](https://www.latlong.net/)
- `refresh_period_min`: How often to refresh the data or the screen in minutes (`data` being lower than `screen` will
  have no effect)
- `city`: Name of the location of the place you are tracking the weather of. OpenWeather API does not always give a
  relevant city name
- `metrics`: If you wish to monitor data. Set `record_metrics` to `false` or `true`. Set `database_url`
  and `database_name` to the one setup during InfluxDB installation.

Run `pip install -Ur requirements.txt`, `sudo apt-get install libgpiod2`

#### Service (auto-run)

Copy the file `systemd/epaper-weather.example.service` and name the new file `systemd/epaper-weather.service`. Inside, you will need to configure the
following elements:
- `User`: Put your own user
- `PATH_TO_PROJECT`: Path of your project location

```
sudo cp systemd/epaper-weather.service /etc/systemd/system
sudo systemctl daemon-reload
sudo systemctl enable epaper-weather
sudo systemctl start epaper-weather
```

#### Tested with
- `Hardware`: Raspberry Pi Zero 2 WH (Recommended)
- `OS`: Raspbian GNU/Linux 11 (bullseye) x86; Raspbian GNU/Linux 12 (bookworm) x86

## Related projects

- [epaper-weather](https://github.com/nerstak/epaper-weather): This project was forked from
- [inkyWeather](https://github.com/xenOs76/inkyWeather): a similar project with Inky pHAT. I borrowed some graphical
  parts to speed up the development process
- [E-paper Weather Display](https://github.com/AbnormalDistributions/e_paper_weather_display): a similar project with a
  bigger screen
