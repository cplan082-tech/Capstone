'''
Title : Publish data to AWS IoT Core using MQTT

'''

from awscrt import io, mqtt, auth, http
from awsiot import mqtt_connection_builder
import time
import json
import os
import time

import csv
from csv import DictReader

import Functions.AWS_Functions as functions
import Functions.Audio_Functions as audio

#import Functions.AWS_Functions as functions

import boto3


# Need these paths
csvFilePath = r'Memory/Hub_Memory.csv'
csvTmpPath = r'Memory/Tmp/Tmp_Hub_Memory.csv'
jsonFilePath = r'Memory/Hub_Memory.json'

#awsConnectSoundPath = "Sounds/MP3/AWS_Connected.mp3"
awsConnectSoundPath = "Sounds/WAV/AWS_Connected.wav"


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

    mqtt_connection = ""
    iotclient = boto3.client('iot')

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
        connect_future.result()
        audio.cliSound(awsConnectSoundPath)
        print("Connected!")
        print()

    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Description: End MQTT Connection
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    def mqttDisconnect(self):
        print('Closing connection')
        disconnect_future = self.mqtt_connection.disconnect()
        disconnect_future.result()

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
    Description: Main function
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''




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
