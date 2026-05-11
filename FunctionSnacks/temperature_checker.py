def checkTemperature(temp,unit):
    
    unit_error_message = 'Invalid Unit'
    
    
    if  unit == 'C':

        fahrenhit_converter = ((float(temp) * (9/5)) + 32)

        final_temperature = round(fahrenhit_converter,2)

        final_temperature_as_string = str(round(fahrenhit_converter,2)) + ' F'
        hot = 68.0 
        cold = 20.0        
        
        if final_temperature <= cold:

            threshold_message = 'Cold advisory'

        elif final_temperature >= hot:

            threshold_message = 'Heat alert'              
            

        return final_temperature_as_string, threshold_message

    elif unit == 'F':

        celsius_converter = ((float(temp) - 32) * (5/9))

        final_temperature = round(celsius_converter,2)

        final_temperature_as_string = str(round(celsius_converter,2)) + ' C'

        hot = 30

        cold = 20

        if final_temperature <= cold:

            threshold_message = 'Cold advisory'

        elif final_temperature >= 30:
        
            threshold_message = 'Heat alert'


        return final_temperature_as_string, threshold_message

    elif unit == ' ':

        fahrenhit_converter = ((float(temp) * (9/5)) + 32)

        final_temperature = round(fahrenhit_converter,2)

        final_temperature_as_string = str(round(fahrenhit_converter,2)) + ' F'
        hot = 68.0 
        cold = 20.0        
        
        if final_temperature <= cold:

            threshold_message = 'Cold advisory'

        elif final_temperature >= hot:

            threshold_message = 'Heat alert'              
            

        return final_temperature_as_string, threshold_message

    return unit_error_message
