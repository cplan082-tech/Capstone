# Main Hub Code

#import Classes.AWS_Class.Class_AWSIoT

from Classes.AWS_Class.Class_AWSIoT import AWSIoT
from Functions.Misc_Functions import is_tool_missing, findTimeSum
import time
import os
from datetime import datetime
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Description: Main function
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

if __name__ == "__main__":

    # Variables
    newSensorData = False
    csvFilePath = r'Memory/Hub_Memory.csv'
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

            if os.path.exists(csvFilePath):
                newSensorData = True
            else:
                newSensorData = False

            # If there is sensor data, publish to AWS
            # =======================================================================
            #newSensorData = False
            # =======================================================================
            if newSensorData == True:

                # Find the time sum in minutes
                findTimeSum(csvFilePath)

                # If there is new sensor data (the Hub_Memory.csv file got updated)
                # First check if a tool has been stolen

                ######### Checking if tool has suspisious behaviour #################
                topic = 'arn:aws:sns:us-east-2:423730035441:ToolAlert'
                Alert, lastDate, lastTime, toolId, dateChecked, timeChecked = is_tool_missing(3)

                # =======================================================================
                #Alert = True # For testing so I dont get constant messages remove later
                # =======================================================================

                # Data was corrupted (date or time recorded in csv is later than the time checked)
                if Alert == 'Data Corrupted':
                    message = "\n\nData is corrupted.\nLast known tool time/date is later than today's time.\nTool # " + toolId + "\n\nLast recorded time:\n" + lastDate + " at " + lastTime + '\n\nTime checked:\n' + dateChecked + " at " + timeChecked
                    aws.publish_message_sns(topic, message)
                # The last known time of the tool is later than the threshold of three hours
                elif Alert == True:
                    message = "\n\nPossible stolen tool!\nPlease check inventory.\nTool # " + toolId + "\n\nLast recorded time:\n" + lastDate + " at " + lastTime + '\n\nTime checked:\n' + dateChecked + " at " + timeChecked
                    aws.publish_message_sns(topic, message)
                # No suspicious behaviour noted
                else:
                    print("Tool is not lost were good!")

                ################# Publish data to the hub #############################
                aws.publishHubData()

                ################# Remove csv file here... #############################
                newSensorData = False
                if os.path.exists(csvFilePath):
                    os.remove(csvFilePath)


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


            # This is where we would send an alert if a tool is stolen
            # The alert will be of the form of sms or email depending on who is subscribed in the AWS SNS topic (ToolAlert)
            # Below is the variable that will trigger the alert






            aws.mqttDisconnect()
            ##########################################################################################################
            # Remove this timer delay for real device... This is just done for testing
            time.sleep(2)
            #print("Closing Application")
            #exit(0)S

            '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
            Description: Check for connection to Transponder
            '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

            # Try to connect...





    except KeyboardInterrupt:
        print("Press Ctrl-C to terminate while statement")
        pass



