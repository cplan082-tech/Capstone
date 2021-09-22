tool_trig_pin_val = 0
prev_val = 0

while True:

    if tool_trig_pin_val == 1:
        tool_trig_pin_val = 0
    elif tool_trig_pin_val == 0:
        tool_trig_pin_val = 1
    
    if (prev_val != tool_trig_pin_val):

        if tool_trig_pin_val:
        
            prev_val = 1
         
        elif ~tool_trig_pin_val:
            prev_val == 0

