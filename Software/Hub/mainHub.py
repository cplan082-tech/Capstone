# Main Hub Code

#import Classes.AWS_Class.Class_AWSIoT

from Classes.AWS_Class.Class_AWSIoT import AWSIoT

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Description: Main function
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

if __name__ == "__main__":

    # Topic rules
    

    # Create class
    aws = AWSIoT()

    # Connect to AWS
    aws.mqttConnect()

    
    aws.publishHubData()
    #aws.describe_thing()
    #aws.disable_topic_rule("RaspberryPi4Analytics_Rule")

    aws.mqttDisconnect()
    print("Closing Application")
    exit(0)
