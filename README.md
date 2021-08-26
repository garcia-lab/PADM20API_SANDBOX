# Tripp Lite PADM20 API Sandbox

Chances are you're reading this because you're interested in Tripp Lite's PADM 20 platform and our new RESTful API. Nothing you find here will be ready for production use as-is, but you may find some useful examples or docs that help. Feel free to reach out to me directly if you have questions. 

With that out of the way, below is a running list of what I have going.

## Documentation

PowerAlert Device Manager (PADM) docs can be found in the **Documentation & Videos** section at the following location:

- [PowerAlert Device Manager (PADM)](https://www.tripplite.com/products/power-alert-device-manager)

Some basic examples of using Postman:

- [PADM20 API Examples (Beta)](https://documenter.getpostman.com/view/6407998/TVt17Pi2)
  - Includes methods such as login, load 1 off, get load 1 details, and logout
- [Device Variables Data Points (Beta)](https://documenter.getpostman.com/view/6407998/TzY3BbAP)
  - Includes methods such as login and get token, get device info, and get variable(s)

## Example

See [`load1off.py`](/load1off.py) for a Python script that takes user input, uses it to login, read info on load 1, and turn load 1 off.

Feel free to reach out to me here or at david_zomaya AT tripplite DOT com.
