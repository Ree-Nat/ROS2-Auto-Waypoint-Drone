from mavros_msgs.msg import Waypoint 
class WaypointBuilder:
    def __init__(self, param1 : float = 0, param2 : float = 0, 
                param3: float = 0, param4 : float = 0, 
                x_lat: float = 0, y_long:float = 0, z_alt:float = 0):
        self.frame : int = 0
        self.command : int = 16
        self.is_current:bool = False
        self.autocontinue: bool = True 
        self.param1 = param1
        self.param2 = param2
        self.param3 = param3
        self.param4 = param4
        self.x_lat = x_lat
        self.y_long = y_long
        self.z_alt = z_alt

        def convert_to_mav_waypoint(self) -> Waypoint:
            wp = Waypoint()
            wp.frame = self.frame
            wp.command = self.command
            wp.param1 = self.param1
            wp.param2 = self.param2
            wp.param3 = self.param3
            wp.param4 = self.param4
            wp.x_lat = self.x_lat
            wp.y_long = self.y_long
            wp.z_alt = self.z_alt
            return wp
        
    
