import asyncio
 
import websockets
import json
import logging
import sys

from textselect import * # imports python script to process client msg and choose text
from compareInput import *

# create websocket handler for each connection websocket
 
async def websocket_handler(websocket, path):

    # handler is always waiting for client messages

    while True: 
        
        # Read websocket message from client (JSON format)

        data = await websocket.recv() 
        logging.info("Received: %s", data)

        # Process client message

        print("print data: ", data, " -------------------")

        data_json = json.loads(data)

        if "textlength" in data_json:
            (retrieved_text, retrieved_title) = retrieve_text(data_json.get('textlength'), data_json.get('textgenre'))
            print("textselect returned: ", retrieved_text)
            print("textselect title: ", retrieved_title)
            test_text = str(retrieved_text)
            # Send response to client for selected text and corresponding title
            response = {"TestText":retrieved_text, "Title":retrieved_title}
        
        if "user_input" in data_json:
            (num_errors, index_errors) = testCorrections(data_json.get('user_input'), test_text)
            # Send response to client with received user input
            response = {"NumErrors":num_errors, "ErrorIndices":index_errors}

        # Send response to client (hardcoded JSON response for now)

        reply = json.dumps(response)
        await websocket.send(reply)
        logging.info("Sent message to websocket client: %s", reply)
 
def main():

    # test_text is GLOBAL and shared across multiple users, add user handling to accomodate
    test_text = None # Declares var to hold retrieved text so that it can be accessed upon user_input

    # set up logger to pump logs to console

    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)      # set this to DEBUG will spill a lot more websocket debug messages
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    root.addHandler(handler)

    # configure websocket to listen on a port
    start_server = websockets.serve(websocket_handler, "localhost", 8081)
    
    # start server
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
    main()

