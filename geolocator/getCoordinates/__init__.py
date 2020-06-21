import logging
import json

import azure.functions as func

from .geo import getCoordinates


def localize(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Received an HttpRequest.')

    spot = req.params.get('spot')

    headers = {
            "Content-type": "application/json",
            "Access-Control-Allow-Origin": "*"
        }

    if not spot:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            print(req_body)
            spot = req_body.get('spot')
    if spot:
        logging.info(f'Searching coordinates of: <{spot}>')
        coordinates = getCoordinates(spot)
        if coordinates != -1:
            logging.info(f'<{coordinates}>')
            return func.HttpResponse(json.dumps(coordinates), headers=headers)
        else:
            message = spot + ' not found!'
            logging.info(message)
            return func.HttpResponse(message, headers=headers)
    else:
        logging.error('no <spot> parameter passed!')
        return func.HttpResponse(
             "Please pass a spot on the query string or in the request body",
             headers=headers, status_code=400
        )
    
