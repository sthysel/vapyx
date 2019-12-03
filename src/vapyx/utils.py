import requests
from loguru import logger

from .errors import RequestError, raise_error


def session_request(session, url, **kwargs):
    """Do HTTP/S request and return response as a string."""
    try:
        response = session(url, **kwargs)
        response.raise_for_status()
        return response.text
    except requests.exceptions.HTTPError as e:
        logger.debug(f'{response}, {e}')
        raise_error(response.status_code)
    except requests.exceptions.ConnectionError as e:
        logger.debug(e)
        raise RequestError(f'Connection error: {e}')
    except requests.exceptions.Timeout as e:
        logger.debug(e)
        raise RequestError(f'Timeout: {e}')
    except requests.exceptions.RequestException as e:
        logger.debug(e)
        raise RequestError(f'Unknown error: {e}')
