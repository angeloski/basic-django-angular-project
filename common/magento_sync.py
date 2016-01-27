from django.conf import settings
from magento import MagentoAPI


def magento_connect():
    
    # host = '{0}:{1}@{2}'.format(settings.MAGENTO_HTTP_AUTH_USERNAME,
    #                             settings.MAGENTO_HTTP_AUTH_PASSWORD,
    #                             settings.MAGENTO_URL)

    magento_api_instance = MagentoAPI(http_method=settings.MAGENTO_PROTOCOL,
                         http_username=settings.MAGENTO_HTTP_AUTH_USERNAME,
                         http_pass=settings.MAGENTO_HTTP_AUTH_PASSWORD,
                         host=settings.MAGENTO_URL,
                         port=settings.MAGENTO_PORT,
                         api_user=settings.MAGENTO_API_USERNAME,
                         api_key=settings.MAGENTO_API_KEY,
                         path=settings.MAGENTO_PATH)
    return magento_api_instance

#magento_api_instance = magento_connect()