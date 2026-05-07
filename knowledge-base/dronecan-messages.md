---
description: >-
  Reference for the DroneCAN messages published and subscribed by ARK CANnode
  products, plus the protocol-level messages every node emits.
---

# DroneCAN Messages

ARK CANnode products communicate using the [DroneCAN protocol](https://dronecan.github.io/Specification/1._Introduction/) on top of [CAN Bus](can-bus.md). See the [DroneCAN GUI Tool Guide](dronecan-gui-tool-guide.md) for inspecting messages on a live bus.

This page documents the subset of DroneCAN messages that ARK products use. The complete catalog of standard data types lives in the official spec:

{% embed url="https://dronecan.github.io/Specification/7._List_of_standard_data_types/" %}

The DSDL definitions below are reproduced from the spec for convenience. If anything here disagrees with the spec, the spec wins.

***

## Common Node Messages

Every DroneCAN node — including all ARK CANnode products — implements the protocol-level messages below. They let the flight controller detect the node, monitor its health, and identify its firmware and hardware version.

For more on the application-level functions these messages belong to, see the [DroneCAN application-level functions spec](https://dronecan.github.io/Specification/6._Application_level_functions/).

### `uavcan.protocol.NodeStatus` <a href="#nodestatus" id="nodestatus"></a>

Periodic heartbeat broadcast by every node so other participants on the bus can detect that it is online and observe its current health and mode.

Default data type ID: 341

```
#
# Abstract node status information.
#
# All UAVCAN nodes are required to publish this message periodically.
#

#
# Publication period may vary within these limits.
# It is NOT recommended to change it at run time.
#
uint16 MAX_BROADCASTING_PERIOD_MS = 1000
uint16 MIN_BROADCASTING_PERIOD_MS = 2

#
# If a node fails to publish this message in this amount of time, it should be considered offline.
#
uint16 OFFLINE_TIMEOUT_MS = 3000

#
# Uptime counter should never overflow.
# Other nodes may detect that a remote node has restarted when this value goes backwards.
#
uint32 uptime_sec

#
# Abstract node health.
#
uint2 HEALTH_OK         = 0     # The node is functioning properly.
uint2 HEALTH_WARNING    = 1     # A critical parameter went out of range or the node encountered a minor failure.
uint2 HEALTH_ERROR      = 2     # The node encountered a major failure.
uint2 HEALTH_CRITICAL   = 3     # The node suffered a fatal malfunction.
uint2 health

#
# Current mode.
#
uint3 MODE_OPERATIONAL      = 0         # Normal operating mode.
uint3 MODE_INITIALIZATION   = 1         # Initialization is in progress; this mode is entered immediately after startup.
uint3 MODE_MAINTENANCE      = 2         # E.g. calibration, the bootloader is running, etc.
uint3 MODE_SOFTWARE_UPDATE  = 3         # New software/firmware is being loaded.
uint3 MODE_OFFLINE          = 7         # The node is no longer available.
uint3 mode

#
# Not used currently, keep zero when publishing, ignore when receiving.
#
uint3 sub_mode

#
# Optional, vendor-specific node status code, e.g. a fault code or a status bitmask.
#
uint16 vendor_specific_status_code
```

### `uavcan.protocol.GetNodeInfo` <a href="#getnodeinfo" id="getnodeinfo"></a>

Service that returns full information about a node — its current status plus its software version, hardware version, and human-readable name. Used by the flight controller and tools like the [DroneCAN GUI Tool](dronecan-gui-tool-guide.md) to identify nodes on the bus.

Default data type ID: 1

```
#
# Full node info request.
# Note that all fields of the response section are byte-aligned.
#

---

#
# Current node status
#
NodeStatus status

#
# Version information shall not be changed while the node is running.
#
SoftwareVersion software_version
HardwareVersion hardware_version

#
# Human readable non-empty ASCII node name.
# Node name is a reversed internet domain name (like Java packages),
# e.g. "com.manufacturer.project.product".
#
uint8[<=80] name
```

The `SoftwareVersion` and `HardwareVersion` nested types are defined in the [official spec](https://dronecan.github.io/Specification/7._List_of_standard_data_types/#getnodeinfo).

***

## GNSS Messages

### `uavcan.equipment.gnss.Fix2` <a href="#fix2" id="fix2"></a>

Primary GNSS navigation solution — position, velocity, fix status, and uncertainty. Published by every ARK GPS module.

Default data type ID: 1063

```
#
# GNSS ECEF and LLA navigation solution with uncertainty.
#

#
# Global network-synchronized time, if available, otherwise zero.
#
uavcan.Timestamp timestamp

#
# Time solution.
# The method and number of leap seconds which were in use for deriving the timestamp are
# defined in the fields below.
#
uavcan.Timestamp gnss_timestamp

uint3 GNSS_TIME_STANDARD_NONE = 0  # Time is unknown
uint3 GNSS_TIME_STANDARD_TAI  = 1
uint3 GNSS_TIME_STANDARD_UTC  = 2
uint3 GNSS_TIME_STANDARD_GPS  = 3
uint3 gnss_time_standard

void13   # Reserved space

#
# Accumulated one-second adjustments applied to UTC since 1972.
#
uint8 NUM_LEAP_SECONDS_UNKNOWN = 0
uint8 num_leap_seconds

#
# Position and velocity solution
#
int37 longitude_deg_1e8            # Longitude degrees multiplied by 1e8 (approx. 1 mm per LSB)
int37 latitude_deg_1e8             # Latitude degrees multiplied by 1e8 (approx. 1 mm per LSB on equator)
int27 height_ellipsoid_mm          # Height above ellipsoid in millimeters
int27 height_msl_mm                # Height above mean sea level in millimeters

float32[3] ned_velocity            # NED frame (north-east-down) in meters per second

#
# Fix status
#
uint6 sats_used

uint2 STATUS_NO_FIX    = 0
uint2 STATUS_TIME_ONLY = 1
uint2 STATUS_2D_FIX    = 2
uint2 STATUS_3D_FIX    = 3
uint2 status

#
# GNSS Mode
#
uint4 MODE_SINGLE      = 0
uint4 MODE_DGPS        = 1
uint4 MODE_RTK         = 2
uint4 MODE_PPP         = 3
uint4 mode

#
# GNSS Sub mode
#
uint6 SUB_MODE_DGPS_OTHER    = 0
uint6 SUB_MODE_DGPS_SBAS     = 1

uint6 SUB_MODE_RTK_FLOAT     = 0
uint6 SUB_MODE_RTK_FIXED     = 1

uint6 sub_mode

#
# Precision
#
float16[<=36] covariance    # Position and velocity covariance. Units are
                            # m^2 for position, (m/s)^2 for velocity and
                            # m^2/s for position/velocity.

float16 pdop

#
# Position and velocity solution in ECEF, if available
#
ECEFPositionVelocity[<=1] ecef_position_velocity
```

### `uavcan.equipment.gnss.Auxiliary` <a href="#gnss-auxiliary" id="gnss-auxiliary"></a>

Lower-priority GNSS metrics — DOP values and visible/used satellite counts. Published alongside [`Fix2`](#fix2) by every ARK GPS module.

Default data type ID: 1061

```
#
# GNSS low priority auxiliary info.
# Unknown DOP parameters should be set to NAN.
#

float16 gdop
float16 pdop
float16 hdop
float16 vdop
float16 tdop
float16 ndop
float16 edop

uint7 sats_visible                    # All visible sats of all available GNSS (e.g. GPS, GLONASS, etc)
uint6 sats_used                       # All used sats of all available GNSS
```

### `ardupilot.gnss.RelPosHeading` <a href="#relposheading" id="relposheading"></a>

GPS-derived heading from a moving-baseline solution. Published by GPS modules that support dual-antenna heading (e.g. the ARK G5H RTK Heading GPS, and an ARK RTK GPS pair configured as base + rover).

This is an ArduPilot-vendor message rather than a `uavcan.equipment.*` standard type.

Default data type ID: 20006

```
# timestamp on the gps message
uavcan.Timestamp timestamp

bool    reported_heading_acc_available
float32 reported_heading_deg
float32 reported_heading_acc_deg
float16 relative_distance_m
float16 relative_down_pos_m
```

***

## AHRS Messages

### `uavcan.equipment.ahrs.RawIMU` <a href="#rawimu" id="rawimu"></a>

Raw 6-DoF IMU samples — gyroscope and accelerometer — with timestamps and an optional integration interval. Published by ARK CANnode products that have an onboard IMU when `CANNODE_PUB_IMU` is set on the node.

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

### `uavcan.equipment.ahrs.MagneticFieldStrength2` <a href="#magneticfieldstrength2" id="magneticfieldstrength2"></a>

Magnetometer reading in Gauss, in body frame. The `2` variant carries a `sensor_id` so a single node can publish multiple magnetometers. This is the message ARK products publish; the older `MagneticFieldStrength` (without `sensor_id`) is deprecated.

Default data type ID: 1002

```
#
# Magnetic field readings, in Gauss, in body frame.
# SI units are avoided because of float16 range limitations.
#

uint8 sensor_id

float16[3] magnetic_field_ga
float16[<=9] magnetic_field_covariance
```

### `uavcan.equipment.ahrs.MagneticFieldStrength` (deprecated) <a href="#magneticfieldstrength" id="magneticfieldstrength"></a>

Older single-sensor variant. Listed here for completeness; ARK products publish [`MagneticFieldStrength2`](#magneticfieldstrength2) instead.

Default data type ID: 1001

```
#
# Magnetic field readings, in Gauss, in body frame.
# This message is deprecated. Use the newer 1002.MagneticFieldStrength2.uavcan message.
#

float16[3] magnetic_field_ga
float16[<=9] magnetic_field_covariance
```

***

## Air Data Messages

### `uavcan.equipment.air_data.StaticPressure` <a href="#staticpressure" id="staticpressure"></a>

Barometric static pressure reading. Published by ARK GPS modules that include an onboard barometer.

Default data type ID: 1028

```
#
# Static pressure.
#

float32 static_pressure                 # Pascal
float16 static_pressure_variance        # Pascal^2
```

### `uavcan.equipment.air_data.StaticTemperature` <a href="#statictemperature" id="statictemperature"></a>

Static air temperature. Published alongside [`StaticPressure`](#staticpressure) by ARK GPS modules with an onboard barometer.

Default data type ID: 1029

```
#
# Static temperature.
#

float16 static_temperature              # Kelvin
float16 static_temperature_variance     # Kelvin^2
```

***

## Range Sensor Messages

### `uavcan.equipment.range_sensor.Measurement` <a href="#range-sensor-measurement" id="range-sensor-measurement"></a>

Generic narrow-beam range sensor reading with sensor type, beam orientation, field of view, and validity flags. Published by ARK rangefinder products and the rangefinder on combined sensors like the ARK Flow.

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

## Optical Flow Messages

### `com.hex.equipment.flow.Measurement` <a href="#flow-measurement" id="flow-measurement"></a>

Optical-flow measurement — integrated gyro and line-of-sight rates over the integration interval, plus a quality byte. Vendor message originally defined by Hex/CUAV; published by ARK Flow products.

Default data type ID: 20200

```
float32 integration_interval    # Integration Interval in seconds
float32[2] rate_gyro_integral   # Integrated Gyro Data in radians
float32[2] flow_integral        # Integrated LOS Data in radians
uint8 quality                   # Flow Data Quality Lowest(0)-Highest(255) Unitless
```

***

## Actuator and ESC Messages

The ARK CANnode subscribes to the messages below when used as a [PWM expander](../sensor/ark-cannode/px4-instructions.md#cannode-as-pwm-expander).

### `uavcan.equipment.esc.RawCommand` <a href="#esc-rawcommand" id="esc-rawcommand"></a>

Raw ESC throttle commands for up to 20 motors, normalized to the range \[-8192, 8191].

Default data type ID: 1030

```
#
# Raw ESC command normalized into [-8192, 8191]; negative values indicate reverse rotation.
# The ESC should normalize the setpoint into its effective input range.
# Non-zero setpoint value below minimum should be interpreted as min valid setpoint for the given motor.
#

int14[<=20] cmd
```

### `uavcan.equipment.actuator.ArrayCommand` <a href="#actuator-arraycommand" id="actuator-arraycommand"></a>

Array of actuator (servo) commands — up to 15 per message. Each entry references one of up to 256 actuators.

Default data type ID: 1010

```
#
# Actuator commands.
# The system supports up to 256 actuators; up to 15 of them can be commanded with one message.
#

Command[<=15] commands
```

The nested `Command` type is defined in the [official spec](https://dronecan.github.io/Specification/7._List_of_standard_data_types/#arraycommand).

***

## Messages by Product

| Product | Publishes | Subscribes |
|---------|-----------|------------|
| All ARK CANnodes | [`NodeStatus`](#nodestatus), [`GetNodeInfo`](#getnodeinfo) | — |
| [ARK CANnode](../sensor/ark-cannode/) | [`RawIMU`](#rawimu) (when `CANNODE_PUB_IMU=1`) | [`RawCommand`](#esc-rawcommand), [`ArrayCommand`](#actuator-arraycommand) (PWM expander mode) |
| [ARK Flow](../sensor/ark-flow/) / [ARK Flow MR](../sensor/ark-flow-mr/) | [`flow.Measurement`](#flow-measurement), [`range_sensor.Measurement`](#range-sensor-measurement), [`RawIMU`](#rawimu) (optional) | — |
| [ARK MAG](../sensor/ark-mag/) | [`MagneticFieldStrength2`](#magneticfieldstrength2) | — |
| [ARK DIST](../sensor/ark-dist/) | [`range_sensor.Measurement`](#range-sensor-measurement) | — |
| [ARK GPS](../gps/ark-gps/) | [`Fix2`](#fix2), [`Auxiliary`](#gnss-auxiliary), [`MagneticFieldStrength2`](#magneticfieldstrength2), [`StaticPressure`](#staticpressure), [`StaticTemperature`](#statictemperature), [`RawIMU`](#rawimu) (optional) | — |
| [ARK RTK GPS](../gps/ark-rtk-gps/) | [`Fix2`](#fix2), [`Auxiliary`](#gnss-auxiliary), [`MagneticFieldStrength2`](#magneticfieldstrength2), [`RawIMU`](#rawimu) (optional); [`RelPosHeading`](#relposheading) on the rover when configured for moving-baseline heading | — |
| [ARK MOSAIC-X5 RTK GPS](../gps/ark-mosaic-x5-rtk-gps/) | [`Fix2`](#fix2), [`Auxiliary`](#gnss-auxiliary), [`MagneticFieldStrength2`](#magneticfieldstrength2), [`RawIMU`](#rawimu) (optional) | — |
| [ARK G5 RTK GPS](../gps/ark-g5-rtk-gps/) | [`Fix2`](#fix2), [`Auxiliary`](#gnss-auxiliary), [`MagneticFieldStrength2`](#magneticfieldstrength2), [`RawIMU`](#rawimu) (optional) | — |
| [ARK G5H RTK Heading GPS](../gps/ark-g5-rtk-heading-gps/) | [`Fix2`](#fix2), [`Auxiliary`](#gnss-auxiliary), [`MagneticFieldStrength2`](#magneticfieldstrength2), [`RawIMU`](#rawimu) (optional); [`RelPosHeading`](#relposheading) when dual-antenna heading is enabled | — |
| [ARK X20 RTK GPS](../gps/ark-x20-rtk-gps.md) | [`Fix2`](#fix2), [`Auxiliary`](#gnss-auxiliary), [`RawIMU`](#rawimu) (optional) | — |
| [ARK TESEO GPS](../gps/ark-teseo-gps/) | [`Fix2`](#fix2), [`Auxiliary`](#gnss-auxiliary), [`MagneticFieldStrength2`](#magneticfieldstrength2), [`StaticPressure`](#staticpressure), [`StaticTemperature`](#statictemperature), [`RawIMU`](#rawimu) (optional) | — |
