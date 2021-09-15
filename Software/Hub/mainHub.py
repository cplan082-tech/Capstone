# Main Hub Code

#import Classes.AWS_Class.Class_AWSIoT

from Classes.AWS_Class.Class_AWSIoT import AWSIoT
import time
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Description: Main function
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

if __name__ == "__main__":

    # Variables
    newSensorData = False

    # Initialize Classes
    aws = AWSIoT() # AWS Class

    try:
        while True:
            # Connecting to AWS
            # Connect to AWS through mqtt connection
            aws.mqttConnect()

            # We are now connected to AWS
            # We can do our actions

            # If there is sensor data, publish to AWS
            # =============================== ALERT =================================
            newSensorData = True    # This will be removes later... Just for testing now
            # =======================================================================
            if newSensorData == True:
                aws.publishHubData()


            # aws.describe_thing()
            # aws.disable_topic_rule("RaspberryPi4Analytics_Rule")

            aws.mqttDisconnect()

            time.sleep(10)
            #print("Closing Application")
            #exit(0)

    except KeyboardInterrupt:
        print("Press Ctrl-C to terminate while statement")
        pass



