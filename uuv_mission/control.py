class Controller:
    def __init__(self, kp: float = 0.15, kd: float = 0.6):
        """
        Initializes PD controller for submarine in the cave.

        Parameters:
        - kp: Proportional gain (default is 0.15)
        - kd: Derivative gain (default is 0.6)
        """
        self.kp = kp
        self.kd = kd
        self.previous_error = 0  

    def get_action(self, reference: float, current_depth: float) -> float:
        """
        Computes the control action based on the reference and current depth.

        Parameters:
        - reference: Target depth
        - current_depth: Current depth of the submarine

        Returns:
        - Control action to be applied (force in y-direction)
        """
        error = reference - current_depth  
        derivative = error - self.previous_error  
        control_action = self.kp * error + self.kd * derivative

        self.previous_error = error
        return control_action