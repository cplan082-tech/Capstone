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

    # Loop forever, or until keyboard interrupt (CTRL-C)
    try:
        while True:

            '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
            Description: Publish data to AWS if any, then listen for message from AWS
            '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

            # Connecting to AWS
            # Connect to AWS through mqtt connection
            aws.mqttConnect()

            # We are now connected to AWS
            # We can do our actions

            # If there is sensor data, publish to AWS
            # =============================== ALERT =================================
            newSensorData = True    # This will be removed later... Just for testing now
            # =======================================================================
            if newSensorData == True:
                aws.publishHubData()

            # Set specific count to an integer other than 0 if you want the program to wait until
            # the specified number of messages arrive.
            # Set specific_count to 0 if you want it to wait a time period (This is better)
            # The hub main loop will loop through checking for bluetooth and checking incoming messages
            # Right now there is no queue so if we are not looking for messages exactly when it comes in we miss it
            # We can use SQS to solve this problem!

            ######## UNCOMMENT
            #specific_count = 0 # It will wait 5 seconds for messages
            #aws.listen_to_aws(specific_count)
            ########

            queue_url = 'https://sqs.ca-central-1.amazonaws.com/423730035441/two-way-sms'
            message = aws.get_sqs_messages(queue_url)
            if message == "NO MESSAGES WAITING":
                print("There were no messages... Continuing")
            else:
                print("The message is: " + message)

            
            # aws.describe_thing()
            # aws.disable_topic_rule("RaspberryPi4Analytics_Rule")

            aws.mqttDisconnect()

            time.sleep(10)
            #print("Closing Application")
            #exit(0)S

            '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
            Description: Check for connection to Transponder
            '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

            # Try to connect...





    except KeyboardInterrupt:
        print("Press Ctrl-C to terminate while statement")
        pass



