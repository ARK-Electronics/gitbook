#!/usr/bin/env python3
"""Send gripper open/close command via MAVLink."""

import argparse
import glob
import sys
from pymavlink import mavutil


def find_ark_port():
    """Auto-detect an ARK device in /dev/serial/by-id/."""
    matches = sorted(glob.glob("/dev/serial/by-id/*ARK*-if00"))
    if not matches:
        return None
    return matches[0]


def main():
    parser = argparse.ArgumentParser(description="Send gripper open/close command")
    parser.add_argument("action", choices=["open", "close"], help="Gripper action")
    parser.add_argument("--port", default=None, help="Serial port (auto-detects ARK device if omitted)")
    args = parser.parse_args()

    port = args.port or find_ark_port()
    if port is None:
        print("No ARK device found. Specify --port manually.")
        sys.exit(1)

    # GRIPPER_ACTION: 0 = release, 1 = grab
    gripper_action = 0 if args.action == "open" else 1

    print(f"Using port: {port}")
    conn = mavutil.mavlink_connection(port)
    conn.wait_heartbeat()
    print(f"Connected to system {conn.target_system}, component {conn.target_component}")

    conn.mav.command_long_send(
        conn.target_system,
        conn.target_component,
        mavutil.mavlink.MAV_CMD_DO_GRIPPER,
        0,       # confirmation
        1,       # param1: gripper instance
        gripper_action,  # param2: 0=release, 1=grab
        0, 0, 0, 0, 0,
    )

    ack = conn.recv_match(type="COMMAND_ACK", blocking=True, timeout=3)
    if ack and ack.command == mavutil.mavlink.MAV_CMD_DO_GRIPPER:
        if ack.result == mavutil.mavlink.MAV_RESULT_ACCEPTED:
            print(f"Gripper {args.action} OK")
        else:
            print(f"Gripper command rejected (result={ack.result})")
            sys.exit(1)
    else:
        print("No ACK received")
        sys.exit(1)

if __name__ == "__main__":
    main()
