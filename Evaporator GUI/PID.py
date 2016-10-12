import numpy

class PID:
    """
    Discrete PID control
    """
    def __init__(self, P=0.0, I=0.0, D=0.0, Integrator_max=500, Integrator_min=-500, v_max = 0.7, v_off = 0.45):
        self.Kp=P
        self.Ki=I
        self.Kd=D
        self.previous_time = None
        self.previous_error = 0
        self.Integrator = 0
        self.Integrator_max=Integrator_max
        self.Integrator_min=Integrator_min
        self.v_max = v_max
        self.v_off = v_off

        self.set_point=0.0
        self.error=0.0

    def update(self,current_value):
        """
        Calculate PID output value for given reference input and feedback. Input current_value
        should be a tuple of the form (time, deposition rate)
        """

        #Set current error and time. 
        self.error = self.set_point - float(current_value[0,1])
        self.time = float(current_value[0,0])

        # Proportional contribution is Kp * error
        self.P_value = self.Kp * self.error 

        # Derivative contribution is Kd * (current error - previous error) / time step (approximate
        # instantaneous derivative). Cannot do this until the second data point. 
        if self.previous_time != None:
            self.D_value = self.Kd * (self.error - self.previous_error) / (self.time - self.previous_time)
            
            self.Integrator = self.Integrator + self.error*(self.time - self.previous_time)
        else:
            self.D_value = 0
            self.Integrator = 0
        # Set the integrator to be the currently integrated value plus the current error
        # times the step size (approximate integration)
        
        if self.Integrator > self.Integrator_max:
            self.Integrator = self.Integrator_max
        elif self.Integrator < self.Integrator_min:
            self.Integrator = self.Integrator_min

        # Set the integral contribution to be the integrated value times Ki
        self.I_value = self.Integrator * self.Ki

        val = self.P_value + self.I_value + self.D_value + self.v_off

        # Always return a positive voltage or 0. 
        if val <0:
            val = 0
        #Limit to maximum output voltage. 
        elif val > self.v_max:
            val = self.v_max

        # Set current error and time to now be previous error and time. 
        self.previous_error = self.error
        self.previous_time = self.time
        
        return val

    def setPoint(self,set_point):
        """
        Initilize the setpoint of PID. 
        """
        self.set_point = set_point

    def setIntegrator(self, Integrator):
        self.Integrator = Integrator

    def setKp(self,P):
        self.Kp=P

    def setKi(self,I):
        self.Ki=I
        
    def setIntMax(self,intMax):
        self.Integrator_max=intMax
        
    def setIntMin(self,intMin):
        self.Integrator_min=intMin
        
    def setKd(self,D):
        self.Kd=D
        
    def setVMax(self,V):
        self.v_max=V
        
    def setVOff(self,V):
        self.v_off=V
        
    def resetPoint(self):
        self.previous_time = None
        self.previous_error = 0

    def getPoint(self):
        return self.set_point

    def getError(self):
        return self.error

    def getIntegrator(self):
        return self.Integrator

    def getDerivator(self):
        return self.Derivator
        
    def getTimeStep(self):
        return self.step_size