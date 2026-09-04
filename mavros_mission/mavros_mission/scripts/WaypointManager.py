from typing import ty
import rclpy
from mavros_msgs.msg import Waypoint, WaypointList, WaypointReached
from mavros_msgs.srv import SetMode, WaypointClear, WaypointPull, WaypointPush, WaypointSetCurrent, CommandBool, CommandTOL
from rclpy.node import Node, SrvTypeRequest
#from rclpy.qos import HistoryPolicy, QoSPresetProfiles, ReliabilityPolicy

HOME_SAFE_ALTITUDE = 5


class WaypointManager(Node):

    def __init__(self):
        if __name__ == "__main__":
            super().__init__("WaypointManager")

            #Service clients
            self.push_client = self.create_client(WaypointPush, '/mavros/mission/push') #send waypoint
            self.pull_client = self.create_client(WaypointPull, '/mavros/mission/pull') #request waypont
            self.clear_client = self.create_client(WaypointClear, '/mavros/mission/clear') #clear list of waypoint
            self.set_current_client = self.create_client(WaypointSetCurrent, '/mavros/mission/set_current')
            self.set_mode_client = self.create_client(SetMode, '/mavros/set_mode')
            self.arming_client = self.create_client(CommandBool, '/mavros/cmd/arming')
            self.takeoff_client = self.create_client(CommandTOL, 'mavros/cmd/takeoff')

            #subsribers

            self.waypoint_subscribers = self.create_subscription(WaypointList, '/mavros/mission/waypoints',
                                                                 self.waypoint_subscribers)

            #waypoint_list
            self.waypoints_list = []



    def set_waypoint(self, waypoint: int) -> bool:
        #Sets the current active waypoint

        request = WaypointSetCurrent.Request()
        request.wp_seq

    #Pushes waypoint list to be executed
    def push_waypoints(self, waypoints: ty.List[Waypoint]) -> bool:
        request = WaypointPush.Request()
        request.start_index = 0
        request.waypoints = waypoints

        self.get_logger().info("Pushing waypoints")
        async_request = self.push_client.call_async(request)
        rclpy.spin_until_future_complete(self, async_request, timeout_sec=5.0)

        if async_request.result() is not None:
            self.get_logger().info("Successly push waypoints")
        else:
            self.get_logger().info("Waypoint push failed")



    def clear_waypoints(self) -> bool:
        #"clear all given waypoints"

        request = WaypointClear.Request()

        self.get_logger().info("Clearing waypoints")

        async_req = self.clear_client.call_async(request)
        rclpy.spin_until_future_complete(self, async_req, timeout_sec=5.0)

        if async_req.result() is not None:
            response = async_req.result()
            self.get_logger().info("Successfully cleared waypoints")
        else:
            self.get_logger().info("Waypoint clearance failed")

    def arm_vehicle(self) -> bool:
        #Arm the client 
        request = CommandBool.Request()
        request.value = True

        async_request = self.arming_client.call_async(request)
        rclpy.spin_until_future_complete(self, async_request, timeout_sec=5.0)

        if async_request.result() is not None:
            self.get_logger().info("Vehicle armed")
        else:
            self.get_logger().info("Vehicle failed to arm. Service call failed")


    #begins the mission after pushing waypoints
    def set_auto_mode(self, mode: str = 'AUTO.MISSION') -> bool:
        request = SetMode.Request()
        request.custom_mode = mode

        self.get_logger().info("Setting flight mode to AUTO_MISSION")

        async_req = self.set_mode_client.call_async(request)
        rclpy.spin_until_future_complete(self, async_req, timeout_sec=5.0)

        if async_req.result() is not None:
            self.get_logger().info("AUTO MODE ACTIVATED")
        else:
            self.get_logger().info("AUTO MODE FAILED!")

    #Brings vehicle back to home
    def set_return_mode(self, mode: str = 'AUTO.RTL') -> bool:
        request = SetMode.Request()
        request.custom_mode = mode
    
        self.get_logger().info("Setting flight mode to AUTO")
    
        async_req = self.set_mode_client.call_async(request)
        rclpy.spin_until_future_complete(self, async_req, timeout_sec=5.0)
    
        if async_req.result() is not None:
            self.get_logger().info("AUTO_RTL MODE ACTIVATED")
        else:
            self.get_logger().info("AUTO_RTL MODE FAILED!")

    def call_takeoff(self, altitude : float = HOME_SAFE_ALTITUDE):
        request = CommandTOL.Request()
        request.altitude = altitude

        async_req = self.takeoff_client.call_async(request)
        rclpy.spin_until_future_complete(self, async_req, timeout_sec=5)

        if async_req is not None:
            self.get_logger().info


    def verifyMission():
        return 0

    def ExecuteMission():
        return 0

    def landMission():
        return 0


def main(args=None):
    rclpy.init(args=args)
    manager = WaypointManager

    rclpy.shutdown()





