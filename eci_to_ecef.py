# eci_to_ecef.py
#
# Usage: python3 eci_to_ecef.py year month day hour minute second eci_x_km eci_y_km eci_z_km
#  Convert from ECI coordinates to ECEF using the date
# Parameters:
# year = year for the date
# month = month in year
# day = day in month
# hour = hour in day
# minute = minute in hour
# second = second in minute
# eci_x_km = ECI x coordinate in km
# eci_y_km = ECI y coordinate in km
# eci_z_km = ECI z coordinate in km

# Output:
#  Script will output ECEF x,y,z coordinates in km
#
# Written by Anushka Devarajan
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
import math # math module
import sys # argv

# "constants"
R_E_KM = 6378.137
w=7.292115 * 10**(-5) #rad/s

# helper functions

## function description
# def calc_something(param1, param2):
#   pass

# initialize script arguments
year = float('nan') 
month = float('nan') 
day = float('nan') 
hour = float('nan')
minute = float('nan')
second = float('nan')
eci_x_km = float('nan')
eci_y_km = float('nan')
eci_z_km = float('nan')

# parse script arguments
if len(sys.argv)==10:
  year = float(sys.argv[1])
  month = float(sys.argv[2])
  day = float(sys.argv[3])
  hour = float(sys.argv[4])
  minute = float(sys.argv[5])
  second = float(sys.argv[6])
  eci_x_km= float(sys.argv[7])
  eci_y_km= float(sys.argv[8])
  eci_z_km= float(sys.argv[9])
else:
  print(\
   'Usage: '\
   'python3 eci_to_ecef.py year month day hour minute second eci_x_km eci_y_km eci_z_km'\
  )
  exit()

# write script below this line
if month <= 2:
    year -= 1
    month += 12

A = year // 100
B = 2 - A +(A // 4)

# fractional Julian Date
jd_frac = math.floor(365.25 * (year + 4716)) + math.floor(30.6001 * (month + 1)) + day + B - 1524.5 + hour/24 + minute/1440 + second/86400
jd= day- 32075 + 1461 *(year+4800+(month-14)/12)/4+367*(month-2-(month-14)/12*12)/12-3*((year+4900+(month-14)/12)/100)/4
t_ut1=(jd-2451545.0)/(36525)
theta_GMST = 67310.54841+(876600*60*60+8640184.812866)*t_ut1 + 0.093104*math.pow(t_ut1, 2) + math.pow(-6.2,-6)*math.pow(t_ut1,3)
# GMST in radians
GMST_mod=math.fmod(theta_GMST,360)*w
GMST_rad = math.fmod(theta_GMST*(2*math.pi/86400), (2*math.pi))-GMST_mod

#z-rotation matrix
ecef_x_km= (eci_x_km*math.cos(-GMST_rad)-eci_y_km*math.sin(-GMST_rad))
ecef_y_km=(eci_x_km*math.sin(-GMST_rad)+eci_y_km*math.cos(-GMST_rad))
ecef_z_km=(eci_z_km)

print(ecef_x_km)
print(-ecef_y_km)
print(ecef_z_km)
