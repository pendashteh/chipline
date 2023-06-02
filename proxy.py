import os
import datetime
import json
import hashlib

def proxy_function(original_function, *args, **kwargs):
    logs_directory = "logs"

    # Create the logs directory if it doesn't exist
    os.makedirs(logs_directory, exist_ok=True)

    # Generate a unique identifier for the function call using the hash of the arguments
    args_hash = hashlib.sha1(json.dumps((args, kwargs)).encode()).hexdigest()
    call_id = f"{original_function.__name__}_{args_hash}"

    # Check if there is a log file for the call_id
    log_file = os.path.join(logs_directory, f"log_{call_id}.txt")
    if os.path.isfile(log_file):
        # Read the response from the log file
        with open(log_file, "r") as file:
            lines = file.readlines()
            response_line = lines[-1]  # Assume the response is on the last line
            response = json.loads(response_line.strip())
        return response

    # Call the original function with the provided parameters
    response = original_function(*args, **kwargs)

    # Generate the log file path with a timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file = os.path.join(logs_directory, f"log_{call_id}.txt")

    # Log the parameters with timestamps
    with open(log_file, "a") as file:
        file.write("Parameters:\n")
        file.write(f"args: {args}\n")
        file.write(f"kwargs: {kwargs}\n")

    # Log the response with timestamps
    with open(log_file, "a") as file:
        file.write("Response:\n")
        file.write(json.dumps(response) + "\n")

    # Return the response
    return response

