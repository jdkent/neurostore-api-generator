# neurostore-sdk
Create studysets for meta-analysis

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0
- Package version: 0.0.1
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://github.com/jdkent](https://github.com/jdkent)

## Requirements.

Python >=3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import neurostore_sdk
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import neurostore_sdk
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import neurostore_sdk
from pprint import pprint
from neurostore_sdk.api import analyses_api
from neurostore_sdk.model.analysis import Analysis
from neurostore_sdk.model.analysis_list import AnalysisList
from neurostore_sdk.model.analysis_return import AnalysisReturn
from neurostore_sdk.model.inline_response404 import InlineResponse404
from neurostore_sdk.model.inline_response422 import InlineResponse422
# Defining the host is optional and defaults to http://localhost:80/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurostore_sdk.Configuration(
    host = "http://localhost:80/api"
)



# Enter a context with an instance of the API client
with neurostore_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analyses_api.AnalysesApi(api_client)
    search = "imagin" # str | search for entries that contain the substring (optional)
sort = "created_at" # str | Parameter to sort results on (optional) (default to "created_at")
page = 0 # int | page of results (optional)
desc = True # bool | sort results by descending order (as opposed to ascending order) (optional)
page_size = 1 # int | number of results to show on a page (optional)
name = "name_example" # str | search the name field for a term (optional)
description = "description_example" # str | search description field for a term (optional)
nested = True # bool | whether to show the URI to a resource (false) or to embed the object in the response (true) (optional)

    try:
        # GET list of analyses
        api_response = api_instance.analyses_get(search=search, sort=sort, page=page, desc=desc, page_size=page_size, name=name, description=description, nested=nested)
        pprint(api_response)
    except neurostore_sdk.ApiException as e:
        print("Exception when calling AnalysesApi->analyses_get: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:80/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AnalysesApi* | [**analyses_get**](docs/AnalysesApi.md#analyses_get) | **GET** /analyses/ | GET list of analyses
*AnalysesApi* | [**analyses_id_delete**](docs/AnalysesApi.md#analyses_id_delete) | **DELETE** /analyses/{id} | DELETE an analysis
*AnalysesApi* | [**analyses_id_get**](docs/AnalysesApi.md#analyses_id_get) | **GET** /analyses/{id} | GET an analysis
*AnalysesApi* | [**analyses_id_put**](docs/AnalysesApi.md#analyses_id_put) | **PUT** /analyses/{id} | PUT/update an analysis
*AnalysesApi* | [**analyses_post**](docs/AnalysesApi.md#analyses_post) | **POST** /analyses/ | POST/create an analysis
*AnnotationsApi* | [**annotations_get**](docs/AnnotationsApi.md#annotations_get) | **GET** /annotations/ | Your GET endpoint
*AnnotationsApi* | [**annotations_id_delete**](docs/AnnotationsApi.md#annotations_id_delete) | **DELETE** /annotations/{id} | DELETE an annotation
*AnnotationsApi* | [**annotations_id_get**](docs/AnnotationsApi.md#annotations_id_get) | **GET** /annotations/{id} | Your GET endpoint
*AnnotationsApi* | [**annotations_id_put**](docs/AnnotationsApi.md#annotations_id_put) | **PUT** /annotations/{id} | Update an annotation
*AnnotationsApi* | [**annotations_post**](docs/AnnotationsApi.md#annotations_post) | **POST** /annotations/ | Post Annotation
*ConditionsApi* | [**conditions_get**](docs/ConditionsApi.md#conditions_get) | **GET** /conditions/ | GET Conditions
*ConditionsApi* | [**conditions_id_delete**](docs/ConditionsApi.md#conditions_id_delete) | **DELETE** /conditions/{id} | DELETE a condition
*ConditionsApi* | [**conditions_id_get**](docs/ConditionsApi.md#conditions_id_get) | **GET** /conditions/{id} | GET a condition
*ConditionsApi* | [**conditions_id_put**](docs/ConditionsApi.md#conditions_id_put) | **PUT** /conditions/{id} | PUT/update a condition
*ConditionsApi* | [**conditions_post**](docs/ConditionsApi.md#conditions_post) | **POST** /conditions/ | POST/Create a condition
*ImagesApi* | [**images_get**](docs/ImagesApi.md#images_get) | **GET** /images/ | GET a list of images
*ImagesApi* | [**images_id_delete**](docs/ImagesApi.md#images_id_delete) | **DELETE** /images/{id} | DELETE an image
*ImagesApi* | [**images_id_get**](docs/ImagesApi.md#images_id_get) | **GET** /images/{id} | GET an image
*ImagesApi* | [**images_id_put**](docs/ImagesApi.md#images_id_put) | **PUT** /images/{id} | PUT/update an image
*ImagesApi* | [**images_post**](docs/ImagesApi.md#images_post) | **POST** /images/ | POST/create an image
*PointsApi* | [**points_get**](docs/PointsApi.md#points_get) | **GET** /points/ | Get Points
*PointsApi* | [**points_id_delete**](docs/PointsApi.md#points_id_delete) | **DELETE** /points/{id} | DELETE a point
*PointsApi* | [**points_id_get**](docs/PointsApi.md#points_id_get) | **GET** /points/{id} | GET a point
*PointsApi* | [**points_id_put**](docs/PointsApi.md#points_id_put) | **PUT** /points/{id} | PUT/update a point
*PointsApi* | [**points_post**](docs/PointsApi.md#points_post) | **POST** /points/ | POST Points
*StudiesApi* | [**studies_get**](docs/StudiesApi.md#studies_get) | **GET** /studies/ | GET a list of studies
*StudiesApi* | [**studies_id_delete**](docs/StudiesApi.md#studies_id_delete) | **DELETE** /studies/{id} | DELETE a study
*StudiesApi* | [**studies_id_get**](docs/StudiesApi.md#studies_id_get) | **GET** /studies/{id} | GET a study
*StudiesApi* | [**studies_id_put**](docs/StudiesApi.md#studies_id_put) | **PUT** /studies/{id} | PUT/update a study
*StudiesApi* | [**studies_post**](docs/StudiesApi.md#studies_post) | **POST** /studies/ | POST/create a study
*StudysetsApi* | [**studysets_get**](docs/StudysetsApi.md#studysets_get) | **GET** /studysets/ | GET a list of studysets
*StudysetsApi* | [**studysets_id_delete**](docs/StudysetsApi.md#studysets_id_delete) | **DELETE** /studysets/{id} | DELETE a studyset
*StudysetsApi* | [**studysets_id_get**](docs/StudysetsApi.md#studysets_id_get) | **GET** /studysets/{id} | GET a studyset
*StudysetsApi* | [**studysets_id_put**](docs/StudysetsApi.md#studysets_id_put) | **PUT** /studysets/{id} | PUT/update a studyset
*StudysetsApi* | [**studysets_post**](docs/StudysetsApi.md#studysets_post) | **POST** /studysets/ | POST/create a studyset
*UserApi* | [**users_get**](docs/UserApi.md#users_get) | **GET** /users/ | Your GET endpoint
*UserApi* | [**users_id_get**](docs/UserApi.md#users_id_get) | **GET** /users/{id} | Individual User Profile
*UserApi* | [**users_id_put**](docs/UserApi.md#users_id_put) | **PUT** /users/{id} | Update Individual Profile
*UserApi* | [**users_post**](docs/UserApi.md#users_post) | **POST** /users/ | 


## Documentation For Models

 - [Analysis](docs/Analysis.md)
 - [AnalysisList](docs/AnalysisList.md)
 - [AnalysisReturn](docs/AnalysisReturn.md)
 - [Annotation](docs/Annotation.md)
 - [AnnotationExport](docs/AnnotationExport.md)
 - [AnnotationList](docs/AnnotationList.md)
 - [AnnotationNote](docs/AnnotationNote.md)
 - [AnnotationReturn](docs/AnnotationReturn.md)
 - [Condition](docs/Condition.md)
 - [ConditionList](docs/ConditionList.md)
 - [ConditionReturn](docs/ConditionReturn.md)
 - [Image](docs/Image.md)
 - [ImageList](docs/ImageList.md)
 - [ImageReturn](docs/ImageReturn.md)
 - [InlineResponse404](docs/InlineResponse404.md)
 - [InlineResponse422](docs/InlineResponse422.md)
 - [JsonLd](docs/JsonLd.md)
 - [JsonLdContext](docs/JsonLdContext.md)
 - [Metadata](docs/Metadata.md)
 - [Point](docs/Point.md)
 - [PointList](docs/PointList.md)
 - [PointReturn](docs/PointReturn.md)
 - [PointValue](docs/PointValue.md)
 - [ReadOnly](docs/ReadOnly.md)
 - [Study](docs/Study.md)
 - [StudyList](docs/StudyList.md)
 - [StudyReturn](docs/StudyReturn.md)
 - [Studyset](docs/Studyset.md)
 - [StudysetList](docs/StudysetList.md)
 - [StudysetReturn](docs/StudysetReturn.md)
 - [User](docs/User.md)
 - [UserList](docs/UserList.md)


## Documentation For Authorization


## JSON-Web-Token

- **Type**: Bearer authentication


## Author

jamesdkent21@gmail.com


## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in neurostore_sdk.apis and neurostore_sdk.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from neurostore_sdk.api.default_api import DefaultApi`
- `from neurostore_sdk.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import neurostore_sdk
from neurostore_sdk.apis import *
from neurostore_sdk.models import *
```
