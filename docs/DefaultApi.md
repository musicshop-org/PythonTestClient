# openapi_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_albums_to_cart**](DefaultApi.md#add_albums_to_cart) | **POST** /api/albums/addAlbumsToCart | 
[**add_songs_from_album_to_cart**](DefaultApi.md#add_songs_from_album_to_cart) | **POST** /api/albums/addSongsFromAlbumToCart | 
[**add_songs_to_cart**](DefaultApi.md#add_songs_to_cart) | **POST** /api/albums/addSongsToCart | 
[**buy_product**](DefaultApi.md#buy_product) | **POST** /api/shoppingCart/buyProducts | 
[**clear_shopping_cart**](DefaultApi.md#clear_shopping_cart) | **GET** /api/shoppingCart/clear | 
[**display_shopping_cart**](DefaultApi.md#display_shopping_cart) | **GET** /api/shoppingCart/display | 
[**find_album_by_album_id**](DefaultApi.md#find_album_by_album_id) | **GET** /api/album/{albumId} | 
[**find_albums_by_song_title_physical**](DefaultApi.md#find_albums_by_song_title_physical) | **GET** /api/albums/{songTitle} | 
[**login**](DefaultApi.md#login) | **POST** /api/login | 
[**login_web**](DefaultApi.md#login_web) | **POST** /api/loginWeb | 
[**welcome**](DefaultApi.md#welcome) | **GET** /api | 


# **add_albums_to_cart**
> bool add_albums_to_cart()



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.album_dto import AlbumDTO
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    cart_uuid = "CartUUID_example" # str |  (optional)
    album_dto = AlbumDTO(
        title="title_example",
        image_url="image_url_example",
        price=3.14,
        stock=1,
        medium_type="CD",
        release_date="release_date_example",
        album_id=AlbumId(
            album_id="album_id_example",
        ),
        label="label_example",
        songs=[
            SongDTO(
                song_id=1,
                title="title_example",
                price=3.14,
                stock=1,
                medium_type="CD",
                release_date="release_date_example",
                genre="genre_example",
                artists=[
                    ArtistDTO(
                        name="name_example",
                    ),
                ],
                in_album=[
                    AlbumDTO(),
                ],
            ),
        ],
        quantity_to_add_to_cart=1,
    ) # AlbumDTO |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.add_albums_to_cart(cart_uuid=cart_uuid, album_dto=album_dto)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->add_albums_to_cart: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_uuid** | **str**|  | [optional]
 **album_dto** | [**AlbumDTO**](AlbumDTO.md)|  | [optional]

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_songs_from_album_to_cart**
> bool add_songs_from_album_to_cart()



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.album_dto import AlbumDTO
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    cart_uuid = "CartUUID_example" # str |  (optional)
    album_dto = AlbumDTO(
        title="title_example",
        image_url="image_url_example",
        price=3.14,
        stock=1,
        medium_type="CD",
        release_date="release_date_example",
        album_id=AlbumId(
            album_id="album_id_example",
        ),
        label="label_example",
        songs=[
            SongDTO(
                song_id=1,
                title="title_example",
                price=3.14,
                stock=1,
                medium_type="CD",
                release_date="release_date_example",
                genre="genre_example",
                artists=[
                    ArtistDTO(
                        name="name_example",
                    ),
                ],
                in_album=[
                    AlbumDTO(),
                ],
            ),
        ],
        quantity_to_add_to_cart=1,
    ) # AlbumDTO |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.add_songs_from_album_to_cart(cart_uuid=cart_uuid, album_dto=album_dto)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->add_songs_from_album_to_cart: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_uuid** | **str**|  | [optional]
 **album_dto** | [**AlbumDTO**](AlbumDTO.md)|  | [optional]

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_songs_to_cart**
> bool add_songs_to_cart()



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.song_dto import SongDTO
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    cart_uuid = "CartUUID_example" # str |  (optional)
    song_dto = [
        SongDTO(
            song_id=1,
            title="title_example",
            price=3.14,
            stock=1,
            medium_type="CD",
            release_date="release_date_example",
            genre="genre_example",
            artists=[
                ArtistDTO(
                    name="name_example",
                ),
            ],
            in_album=[
                AlbumDTO(
                    title="title_example",
                    image_url="image_url_example",
                    price=3.14,
                    stock=1,
                    medium_type="CD",
                    release_date="release_date_example",
                    album_id=AlbumId(
                        album_id="album_id_example",
                    ),
                    label="label_example",
                    songs=[
                        SongDTO(),
                    ],
                    quantity_to_add_to_cart=1,
                ),
            ],
        ),
    ] # [SongDTO] |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.add_songs_to_cart(cart_uuid=cart_uuid, song_dto=song_dto)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->add_songs_to_cart: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_uuid** | **str**|  | [optional]
 **song_dto** | [**[SongDTO]**](SongDTO.md)|  | [optional]

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buy_product**
> bool buy_product()



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.invoice_line_item_dto import InvoiceLineItemDTO
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str |  (optional)
    invoice_line_item_dto = [
        InvoiceLineItemDTO(
            medium_type="CD",
            name="name_example",
            quantity=1,
            price=3.14,
            returned_quantity=1,
        ),
    ] # [InvoiceLineItemDTO] |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.buy_product(authorization=authorization, invoice_line_item_dto=invoice_line_item_dto)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->buy_product: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional]
 **invoice_line_item_dto** | [**[InvoiceLineItemDTO]**](InvoiceLineItemDTO.md)|  | [optional]

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clear_shopping_cart**
> bool clear_shopping_cart()



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    cart_uuid = "CartUUID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.clear_shopping_cart(cart_uuid=cart_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->clear_shopping_cart: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_uuid** | **str**|  | [optional]

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **display_shopping_cart**
> ShoppingCartDTO display_shopping_cart()



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.shopping_cart_dto import ShoppingCartDTO
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    cart_uuid = "CartUUID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.display_shopping_cart(cart_uuid=cart_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->display_shopping_cart: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_uuid** | **str**|  | [optional]

### Return type

[**ShoppingCartDTO**](ShoppingCartDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_album_by_album_id**
> AlbumDTO find_album_by_album_id(album_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.album_dto import AlbumDTO
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    album_id = "albumId_example" # str | 
    authorization = "Authorization_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.find_album_by_album_id(album_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->find_album_by_album_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.find_album_by_album_id(album_id, authorization=authorization)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->find_album_by_album_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **album_id** | **str**|  |
 **authorization** | **str**|  | [optional]

### Return type

[**AlbumDTO**](AlbumDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_albums_by_song_title_physical**
> [AlbumDTO] find_albums_by_song_title_physical(song_title)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.album_dto import AlbumDTO
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    song_title = "songTitle_example" # str | 
    authorization = "Authorization_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.find_albums_by_song_title_physical(song_title)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->find_albums_by_song_title_physical: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.find_albums_by_song_title_physical(song_title, authorization=authorization)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->find_albums_by_song_title_physical: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **song_title** | **str**|  |
 **authorization** | **str**|  | [optional]

### Return type

[**[AlbumDTO]**](AlbumDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login**
> str login()



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.user_data_dto import UserDataDTO
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    user_data_dto = UserDataDTO(
        email_address="email_address_example",
        password="password_example",
    ) # UserDataDTO |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.login(user_data_dto=user_data_dto)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->login: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_data_dto** | [**UserDataDTO**](UserDataDTO.md)|  | [optional]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_web**
> str login_web()



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.user_data_dto import UserDataDTO
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    user_data_dto = UserDataDTO(
        email_address="email_address_example",
        password="password_example",
    ) # UserDataDTO |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.login_web(user_data_dto=user_data_dto)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->login_web: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_data_dto** | [**UserDataDTO**](UserDataDTO.md)|  | [optional]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **welcome**
> str welcome()



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.welcome()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->welcome: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

