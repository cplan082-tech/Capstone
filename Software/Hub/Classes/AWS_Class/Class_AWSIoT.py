'''
Title : Publish data to AWS IoT Core using MQTT

'''

from awscrt import io, mqtt, auth, http
from awsiot import mqtt_connection_builder
#import time
import json
import os

#import csv
from csv import DictReader

import Functions.AWS_Functions as functions
import Functions.Audio_Functions as audio
import time


#import Functions.AWS_Functions as functions

import boto3
import threading

received_count = 0
received_all_event = threading.Event()
received_all_event_timed = threading.Event()


# Need these paths
csvFilePathOld = r'Memory/Hub_Memory_Old.csv'

csvFilePath = r'Memory/Hub_Memory.csv'
csvTmpPath = r'Memory/Tmp/Tmp_Hub_Memory.csv'
jsonFilePath = r'Memory/Hub_Memory.json'

#awsConnectSoundPath = "Sounds/MP3/AWS_Connected.mp3"
awsConnectSoundPath = "Sounds/WAV/AWS_Connected.wav"

'''
INCOMPLETE

Purpose: Function called when we get a message from AWS

INCOMPLETE
'''

# Callback when the subscribed topic receives a message
def on_message_received(topic, payload, dup, qos, retain, **kwargs):
    print("Received message from topic '{}': {}".format(topic, payload))
    global received_count
    received_count += 1
    if received_count == specific_count:
        received_all_event.set()

# Callback when the subscribed topic receives a message
def on_message_received_timed(topic, payload, dup, qos, retain, **kwargs):
    print("Received message from topic '{}': {}".format(topic, payload))
    global received_count
    received_count += 1
    #if received_count == specific_count:
    #    received_all_event_timed.set()
    time.sleep(1)
    received_all_event_timed.set()





class AWSIoT(object):
    PATH_TO_CONFIG = "Config/config.json"
    ENDPOINT = ""
    CLIENT_ID = ""
    PATH_TO_CERT = ""
    PATH_TO_KEY = ""
    PATH_TO_ROOT = ""
    MESSAGE = ""
    TOPIC = "test/testing"
    THING_NAME = ""
    COUNT = 1 # We expect 1 package from AWS

    mqtt_connection = ""
    iotclient = boto3.client('iot', region_name='us-east-2')
    sqsclient = boto3.client('sqs', region_name='ca-central-1')
    snsclient = boto3.client('sns', region_name='us-east-2')
    check = 0
    def __init__(self):
        print("Initializing AWS MQTT ")
        self.setVariables()
        
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Description : Parse json config file and set the variables
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def setVariables(self):
        configData = {}
        if os.path.exists(self.PATH_TO_CONFIG):
            with open(self.PATH_TO_CONFIG) as fp:
                configData = json.load(fp)
            self.ENDPOINT = configData["ENDPOINT"]
            self.CLIENT_ID = configData["CLIENT_ID"]
            self.PATH_TO_CERT = configData["PATH_TO_CERT"]
            self.PATH_TO_KEY = configData["PATH_TO_KEY"]
            self.PATH_TO_ROOT = configData["PATH_TO_ROOT"]
            self.TOPIC = configData["TOPIC"]
            self.THING_NAME = configData["THING_NAME"]
        else:
            print("ERROR : config file not found")
            exit(-1)

    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Description : Connect to AWS Endpoint and Start MQTT connection
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def mqttConnect(self):
        event_loop_group = io.EventLoopGroup(1)
        host_resolver = io.DefaultHostResolver(event_loop_group)
        client_bootstrap = io.ClientBootstrap(event_loop_group, host_resolver)
        self.mqtt_connection = mqtt_connection_builder.mtls_from_path(
                    endpoint=self.ENDPOINT,
                    cert_filepath=self.PATH_TO_CERT,
                    pri_key_filepath=self.PATH_TO_KEY,
                    client_bootstrap=client_bootstrap,
                    ca_filepath=self.PATH_TO_ROOT,
                    client_id=self.CLIENT_ID,
                    clean_session=False,
                    keep_alive_secs=6
                    )
        print("Connecting to {} with client ID '{}'...".format(
                self.ENDPOINT, self.CLIENT_ID))
        connect_future = self.mqtt_connection.connect()
        #connect_future.result()
        #connection = bool(connect_future.result())
        #if connection == True:
        #    audio.cliSound(awsConnectSoundPath)
        #    print("Connected!")
        #    print()
            #functions.aws_connection_led(connection)
        #elif connection == False:
        #    print("Unable to connect. Please try again.")
            #functions.aws_connection_led(connection)
        #else:
        #    print("Connection error!")

    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Description: End MQTT Connection
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    def mqttDisconnect(self):
        print('Closing connection')
        disconnect_future = self.mqtt_connection.disconnect()
        #disconnect_future.result()

    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Description: Publish CSV file in chunks in JSON format
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''' 

    def publishHubData(self):
        with open(csvFilePath, 'r') as read_obj:
            # pass the file object to DictReader() to get the DictReader object
            csv_dict_reader = DictReader(read_obj)
            # iterate over each line as a ordered dictionary
            for row in csv_dict_reader:
                # row variable is a dictionary that represents a row in csv
                print(row)
                # Write the row into a temporary CSV file
                fieldnames = functions.csv_get_fieldnames(csvFilePath)
                functions.write_to_csv_file(csvTmpPath, row, fieldnames)
                # For each row convert to json
                functions.csv_to_json(csvTmpPath, jsonFilePath)
                json_file = open(jsonFilePath)
                json_load = json.load(json_file)
                json_file.close()
                json_string = json.dumps(json_load[0]) # Convert to json format  
                # Publish the smaller JSON format string
                self.mqtt_connection.publish(topic=self.TOPIC, payload=json_string, qos=mqtt.QoS.AT_LEAST_ONCE)
               #time.sleep(0.5)
                print("Published: '" + json_string + "' to the topic: " + self.TOPIC)

    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Description: Give details about aws thing 
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''' 

    def describe_thing(self):
        print("\nThing description:\n")
        print(self.iotclient.describe_thing(thingName = self.THING_NAME))
        print()
        
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Description: Disable topic rule
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''' 

    def disable_topic_rule(self, rule_name):
        self.iotclient.disable_topic_rule(ruleName = rule_name)

    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Description: Enable topic rule
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''' 

    def enable_topic_rule(self, rule_name):
        self.iotclient.enable_topic_rule(ruleName = rule_name)

    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Description : Return the expected count
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    def getCount(self):
        return (self.COUNT)

    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Description: Send message to SNS topic
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    @staticmethod
    def publish_message_sns(topic_arn = 'arn:aws:sns:us-east-2:423730035441:ToolAlert', message = "Tool Alert! Possible stolen tool!"):
        """
        Publishes a message to a topic. Subscriptions can be filtered
        based on message attributes so that a subscription receives messages only
        when specified attributes are present.

        :param topic: The topic to publish to.
        :param message: The message to publish.
        """
        snsclient = boto3.client('sns', region_name='us-east-2')
        # Publish to topic
        snsclient.publish(TopicArn=topic_arn,
                    Message=message,
                    Subject="Force Field Alert",
                    MessageStructure='string')
        print("Alert Sent!")


    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Description: Listen to AWS for any incomming packets
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


    def listen_to_aws(self, specific_count=0):
        if specific_count != 0:
            # Subscribe
            print("Subscribing to topic '{}'...".format(self.TOPIC))
            subscribe_future, packet_id = self.mqtt_connection.subscribe(
                topic=self.TOPIC,
                qos=mqtt.QoS.AT_LEAST_ONCE,
                callback=on_message_received)

            subscribe_result = subscribe_future.result()
            print("Subscribed with {}".format(str(subscribe_result['qos'])))

            # Wait for all messages to be received.
            # This waits forever if count was set to 0.
            if self.COUNT != 0 and not received_all_event.is_set():
                print("Waiting for all messages to be received...")
            received_all_event.wait()
            print("{} message(s) received.".format(received_count))

        else:
            print("Search for messages for 10 seconds")
            # Subscribe
            print("Subscribing to topic '{}'...".format(self.TOPIC))
            subscribe_future, packet_id = self.mqtt_connection.subscribe(
                topic=self.TOPIC,
                qos=mqtt.QoS.AT_LEAST_ONCE,
                callback=on_message_received_timed)

            subscribe_result = subscribe_future.result()
            print("Subscribed with {}".format(str(subscribe_result['qos'])))

            # Wait for messages, if any.
            # This waits 5 seconds
            if self.COUNT != 0 and not received_all_event_timed.is_set():
                print("Waiting for all messages to be received... If any...")
                # Wait 5 seconds for messages
                time.sleep(5)
                print("Times up")
            received_all_event_timed.wait()
            print("{} message(s) received.".format(received_count))  # Wait for all messages to be received.


    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Description : Return 1 message from SQS if any
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    def get_sqs_messages(self, queue_url):

        maxWait = 4

        print(self.check)
        # Check if there are any messages in the queue
        queueAttributes = self.sqsclient.get_queue_attributes(
            QueueUrl=queue_url,
            AttributeNames=['ApproximateNumberOfMessages']
        )

        msgNumQueue = int(queueAttributes['Attributes']['ApproximateNumberOfMessages'])

        if msgNumQueue > 0 and self.check >= 0 and self.check < maxWait:
            self.check = self.check + 1
            message = "NO MESSAGES WAITING"
            print(self.check)
            return message
        elif msgNumQueue == 0 and self.check == maxWait:
            self.check = 0
            message = "NO MESSAGES WAITING"
            print(self.check)
            return message
        if msgNumQueue > 0 and self.check == maxWait:
            self.check = 0
            print(str(msgNumQueue) + " messages waiting")
            print("Fetching first message")
            response = self.sqsclient.receive_message(
                QueueUrl=queue_url,
                AttributeNames=['SentTimestamp'],
                MaxNumberOfMessages=1,
                MessageAttributeNames=['All'],
                VisibilityTimeout=0,
                WaitTimeSeconds=0
            )

            message = response['Messages'][0]['Body']
            receipt_handle = response['Messages'][0]['ReceiptHandle']

            # Delete received message from queue
            self.sqsclient.delete_message(
                QueueUrl=queue_url,
                ReceiptHandle=receipt_handle
            )
            return message
        else:
            print(str(msgNumQueue) + " messages waiting")

        message = "NO MESSAGES WAITING"
        return message






#if __name__ == "__main__":

    # Need these paths
#    csvFilePath = r'Memory/Hub_Memory.csv'
#    csvTmpPath = r'Memory/Tmp/Tmp_Hub_Memory.csv'
#    jsonFilePath = r'Memory/Hub_Memory.json'

    # Topic rules
    

    # Create class
#    aws = AWSIoT()

    # Connect to AWS
#    aws.mqttConnect()

    
#    aws.publishHubData()
#    aws.describe_thing()
#    aws.disable_topic_rule("RaspberryPi4Analytics_Rule")

#    aws.mqttDisconnect()
#    print("Closing Application")
#    exit(0)
