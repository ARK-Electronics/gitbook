# UART / MAVLink

There is no proprietary raw UART protocol. The UART port streams standard [MAVLink 2](https://mavlink.io/en/).

## Link

| Setting | Value |
|---------|-------|
| Connector | **UART** 6-pin JST-GH (not Debug) |
| Baud | 115200 8N1 |
| Flow control | Optional RTS/CTS (auto by default) |
| Init sequence | None — streams after boot |
| Default sysid / compid | 158 / 158 |

The Debug connector is NSH console + SWD only.

## Messages

| Message | ID | Rate |
|---------|----|------|
| `HEARTBEAT` | 0 | 1 Hz |
| [`DISTANCE_SENSOR`](https://mavlink.io/en/messages/common.html#DISTANCE_SENSOR) | 132 | One per range sample |

## `DISTANCE_SENSOR` fields

| Field | Unit | Notes |
|-------|------|-------|
| `current_distance` | cm | `uint16` |
| `min_distance` / `max_distance` | cm | `uint16` |
| `type` | enum | Laser |
| `orientation` | enum | Default downward |
| `signal_quality` | 0–100 | 0 unknown, 1 invalid |

## Rate

UART rate matches the rangefinder sample rate (same data path as DroneCAN). Defaults are typically about **5–25 Hz** depending on short/long range mode.

## Node configuration

No parameters need to be set on the ARK DIST for UART MAVLink output. Stock firmware enables MAVLink on the UART port automatically.
