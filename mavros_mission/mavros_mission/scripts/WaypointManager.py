import rclpy
from mavros_msgs.msg import Waypoint, WaypointList, WaypointReached
from mavros_msgs.srv import SetMode, WaypointClear, WaypointPull, WaypointPush, WaypointSetCurrent
from rclpy.node import Node
#from rclpy.qos import HistoryPolicy, QoSPresetProfiles, ReliabilityPolicy

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

            #subsribers

            self.waypoint_subscribers = self.create_subscription(WaypointList, '/mavros/mission/waypoints',
                                                                 self.waypoint_subscribers)

            #waypoint_list
            self.waypoints_list = []


    def pushWaypoints():
        

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





