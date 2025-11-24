# DroneCAN Messages

The ARK Flow MR outputs data using the DroneCAN protocol\
[https://dronecan.github.io/Specification/1.\_Introduction/](https://dronecan.github.io/Specification/1._Introduction/)\
\
There are 3 onboard sensors with a corresponding message each. Optical Flow and Rangefinder data publishing is enabled by default. IMU data publishing must be enabled by setting the node parameter CANNODE\_PUB\_IMU.

* Optical Flow:  `com.hex.equipment.flow`
* Rangefinder:  `uavcan.equipment.range_sensor`
* IMU: `RawIMU`

There are also messages all Nodes emit:\
[https://dronecan.github.io/Specification/6.\_Application\_level\_functions/](https://dronecan.github.io/Specification/6._Application_level_functions/)

* NodeStatus: `NodeStatus`
* GetNodeInfo: `GetNodeInfo`

#### Messages

The DroneCAN messages can be found here:

{% embed url="https://dronecan.github.io/Specification/7._List_of_standard_data_types/" %}

***

### `com.hex.equipment.flow` <a href="#comhexequipmentflow" id="comhexequipmentflow"></a>

#### `Measurement` <a href="#measurement-1" id="measurement-1"></a>

Full name: `com.hex.equipment.flow.Measurement`

Default data type ID: 20200

```
float32 integration_interval    # Integration Interval in seconds
float32[2] rate_gyro_integral   # Integrated Gyro Data in radians
float32[2] flow_integral        # Integrated LOS Data in radians
uint8 quality                   # Flow Data Quality Lowest(0)-Highest(255) Unitless
```

***

### `uavcan.equipment.range_sensor` <a href="#uavcanequipmentrange_sensor" id="uavcanequipmentrange_sensor"></a>

#### `Measurement` <a href="#measurement" id="measurement"></a>

Full name: `uavcan.equipment.range_sensor.Measurement`

Default data type ID: 1050

```
#
# Generic narrow-beam range sensor data.
#

uavcan.Timestamp timestamp

uint8 sensor_id

uavcan.CoarseOrientation beam_orientation_in_body_frame

float16 field_of_view                # Radians

uint5 SENSOR_TYPE_UNDEFINED = 0
uint5 SENSOR_TYPE_SONAR     = 1
uint5 SENSOR_TYPE_LIDAR     = 2
uint5 SENSOR_TYPE_RADAR     = 3
uint5 sensor_type

uint3 READING_TYPE_UNDEFINED   = 0   # Range is unknown
uint3 READING_TYPE_VALID_RANGE = 1   # Range field contains valid distance
uint3 READING_TYPE_TOO_CLOSE   = 2   # Range field contains min range for the sensor
uint3 READING_TYPE_TOO_FAR     = 3   # Range field contains max range for the sensor
uint3 reading_type

float16 range                        # Meters
```

***

#### `RawIMU` <a href="#rawimu" id="rawimu"></a>

Full name: `uavcan.equipment.ahrs.RawIMU`

Default data type ID: 1003

```
#
# Raw IMU data with timestamps.
#
# THIS DEFINITION MAY BE CHANGED IN A NON-BACKWARD-COMPATIBLE WAY IN THE FUTURE.
#

#
# Data acquisition timestamp in the bus shared time base.
#
uavcan.Timestamp timestamp

#
# Integration interval, seconds.
# Set to a non-positive value if the integrated samples are not available
# (in this case, only the latest point samples will be valid).
#
float32 integration_interval

#
# Angular velocity samples in radian/second.
# The samples are represented in the body frame, the axes are ordered as follows:
#   1. angular velocity around X (roll rate)
#   2. angular velocity around Y (pitch rate)
#   3. angular velocity around Z (yaw rate)
#
float16[3] rate_gyro_latest                 # Latest sample, radian/second
float32[3] rate_gyro_integral               # Integrated samples, radian/second

#
# Linear acceleration samples in meter/(second^2).
# The samples are represented in the body frame, the axes are ordered as follows:
#   1. linear acceleration along X (forward positive)
#   2. linear acceleration along Y (right positive)
#   3. linear acceleration along Z (down positive)
#
float16[3] accelerometer_latest             # Latest sample, meter/(second^2)
float32[3] accelerometer_integral           # Integrated samples, meter/(second^2)

#
# Covariance matrix. The diagonal entries are ordered as follows:
#   1. roll rate                (radian^2)/(second^2)
#   2. pitch rate               (radian^2)/(second^2)
#   3. yaw rate                 (radian^2)/(second^2)
#   4. forward acceleration     (meter^2)/(second^4)
#   5. rightward acceleration   (meter^2)/(second^4)
#   6. downward acceleration    (meter^2)/(second^4)
#
float16[<=36] covariance
```

<br>
