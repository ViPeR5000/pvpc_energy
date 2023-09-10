import datetime
import time
import requests
import logging

_LOGGER = logging.getLogger(__name__)


def get(url, headers):
    return requests.get(url, headers=headers)

class REE:
    token = "20dada670614470c2f0cd1ff9042018bbedd5ab3796b1f96fd56d0dc209f4480"
    url_indicators = "https://api.esios.ree.es/indicators/1001?geo_ids[]=8741&start_date={start_date}&end_date={end_date}"

    def getHeaders():
        headers = {
            'Accept': 'application/json; application/vnd.esios-api-v2+json',
            'Content-Type': 'application/json',
            'Host': 'api.esios.ree.es',
            'x-api-key': REE.token
        }
        return headers

    async def pvpc(start_date, end_date, hass):
        _LOGGER.debug(f"START - REE.pvpc(start_date={start_date.isoformat()}, end_date={end_date.isoformat()})")
        
        result = {}
        url = REE.url_indicators.format(start_date=start_date.strftime('%Y-%m-%d'), end_date=end_date.strftime('%Y-%m-%dT23%%3A00%%3A00'))
        response = None
        _LOGGER.info(f"REE.get_prices(start_date={start_date.isoformat()}, end_date={end_date.isoformat()})")
        r = await hass.async_add_executor_job(get, url, REE.getHeaders())
        if r.status_code == 200:
            response = r.json()
        if response is not None and len(response['indicator']['values']) > 0:
            for value in response['indicator']['values']:
                timestamp = int(time.mktime(time.strptime(value['datetime'][:13], '%Y-%m-%dT%H')))
                result[timestamp] = round(value['value'] / 1000, 5)
        _LOGGER.debug(f"END - REE.pvpc: len(result)={len(result)}")
        return result
