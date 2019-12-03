import requests
from loguru import logger

from .errors import RequestError, raise_error


def session_request(session, url, **kwargs):
    """Do HTTP/S request and return response as a string."""
    try:
        response = session(url, **kwargs)

        response.raise_for_status()

        return response.text

    except requests.exceptions.HTTPError as errh:
        logger.debug(f'{response}, {errh}')
        raise_error(response.status_code)

    except requests.exceptions.ConnectionError as errc:
        logger.debug(f'{errc}')
        raise RequestError(f'Connection error: {errc}')

    except requests.exceptions.Timeout as errt:
        logger.debug(f'{errt}')
        raise RequestError(f'Timeout: {errt}')

    except requests.exceptions.RequestException as err:
        logger.debug(f'{err}')
        raise RequestError(f'Unknown error: {err}')
