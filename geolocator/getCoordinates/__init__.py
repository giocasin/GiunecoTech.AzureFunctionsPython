import logging
import json

import azure.functions as func

from .geo import getCoordinates


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    spot = req.params.get('spot')

    coordinates = getCoordinates(spot)

    headers = {
        "Content-type": "application/json",
        "Access-Control-Allow-Origin": "*"
    }

    return func.HttpResponse(json.dumps(coordinates), headers = headers)
    
