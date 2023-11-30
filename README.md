# fluid
client for fluid

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v0.1
- Package version: 0.1
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import fluid
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import fluid
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function

import time
import fluid
from fluid.rest import ApiException
from pprint import pprint

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------


## Documentation For Models

 - [APIGatewayStatus](docs/APIGatewayStatus.md)
 - [AlluxioCompTemplateSpec](docs/AlluxioCompTemplateSpec.md)
 - [AlluxioFuseSpec](docs/AlluxioFuseSpec.md)
 - [AlluxioRuntime](docs/AlluxioRuntime.md)
 - [AlluxioRuntimeList](docs/AlluxioRuntimeList.md)
 - [AlluxioRuntimeSpec](docs/AlluxioRuntimeSpec.md)
 - [CacheableNodeAffinity](docs/CacheableNodeAffinity.md)
 - [CleanCachePolicy](docs/CleanCachePolicy.md)
 - [Condition](docs/Condition.md)
 - [Data](docs/Data.md)
 - [DataBackup](docs/DataBackup.md)
 - [DataBackupList](docs/DataBackupList.md)
 - [DataBackupSpec](docs/DataBackupSpec.md)
 - [DataLoad](docs/DataLoad.md)
 - [DataLoadList](docs/DataLoadList.md)
 - [DataLoadSpec](docs/DataLoadSpec.md)
 - [DataMigrate](docs/DataMigrate.md)
 - [DataMigrateList](docs/DataMigrateList.md)
 - [DataMigrateSpec](docs/DataMigrateSpec.md)
 - [DataProcess](docs/DataProcess.md)
 - [DataProcessList](docs/DataProcessList.md)
 - [DataProcessSpec](docs/DataProcessSpec.md)
 - [DataRestoreLocation](docs/DataRestoreLocation.md)
 - [DataToMigrate](docs/DataToMigrate.md)
 - [Dataset](docs/Dataset.md)
 - [DatasetCondition](docs/DatasetCondition.md)
 - [DatasetList](docs/DatasetList.md)
 - [DatasetSpec](docs/DatasetSpec.md)
 - [DatasetStatus](docs/DatasetStatus.md)
 - [DatasetToMigrate](docs/DatasetToMigrate.md)
 - [EFCCompTemplateSpec](docs/EFCCompTemplateSpec.md)
 - [EFCFuseSpec](docs/EFCFuseSpec.md)
 - [EFCRuntime](docs/EFCRuntime.md)
 - [EFCRuntimeList](docs/EFCRuntimeList.md)
 - [EFCRuntimeSpec](docs/EFCRuntimeSpec.md)
 - [EncryptOption](docs/EncryptOption.md)
 - [EncryptOptionSource](docs/EncryptOptionSource.md)
 - [ExternalEndpointSpec](docs/ExternalEndpointSpec.md)
 - [ExternalStorage](docs/ExternalStorage.md)
 - [GooseFSCompTemplateSpec](docs/GooseFSCompTemplateSpec.md)
 - [GooseFSFuseSpec](docs/GooseFSFuseSpec.md)
 - [GooseFSRuntime](docs/GooseFSRuntime.md)
 - [GooseFSRuntimeList](docs/GooseFSRuntimeList.md)
 - [GooseFSRuntimeSpec](docs/GooseFSRuntimeSpec.md)
 - [HCFSStatus](docs/HCFSStatus.md)
 - [InitFuseSpec](docs/InitFuseSpec.md)
 - [InitUsersSpec](docs/InitUsersSpec.md)
 - [JindoCompTemplateSpec](docs/JindoCompTemplateSpec.md)
 - [JindoFuseSpec](docs/JindoFuseSpec.md)
 - [JindoRuntime](docs/JindoRuntime.md)
 - [JindoRuntimeList](docs/JindoRuntimeList.md)
 - [JindoRuntimeSpec](docs/JindoRuntimeSpec.md)
 - [JobProcessor](docs/JobProcessor.md)
 - [JuiceFSCompTemplateSpec](docs/JuiceFSCompTemplateSpec.md)
 - [JuiceFSFuseSpec](docs/JuiceFSFuseSpec.md)
 - [JuiceFSRuntime](docs/JuiceFSRuntime.md)
 - [JuiceFSRuntimeList](docs/JuiceFSRuntimeList.md)
 - [JuiceFSRuntimeSpec](docs/JuiceFSRuntimeSpec.md)
 - [Level](docs/Level.md)
 - [MasterSpec](docs/MasterSpec.md)
 - [Metadata](docs/Metadata.md)
 - [MetadataSyncPolicy](docs/MetadataSyncPolicy.md)
 - [Mount](docs/Mount.md)
 - [OSAdvise](docs/OSAdvise.md)
 - [OperationRef](docs/OperationRef.md)
 - [OperationStatus](docs/OperationStatus.md)
 - [PodMetadata](docs/PodMetadata.md)
 - [Processor](docs/Processor.md)
 - [Runtime](docs/Runtime.md)
 - [RuntimeCondition](docs/RuntimeCondition.md)
 - [RuntimeManagement](docs/RuntimeManagement.md)
 - [RuntimeStatus](docs/RuntimeStatus.md)
 - [ScriptProcessor](docs/ScriptProcessor.md)
 - [SecretKeySelector](docs/SecretKeySelector.md)
 - [TargetDataset](docs/TargetDataset.md)
 - [TargetDatasetWithMountPath](docs/TargetDatasetWithMountPath.md)
 - [TargetPath](docs/TargetPath.md)
 - [ThinCompTemplateSpec](docs/ThinCompTemplateSpec.md)
 - [ThinFuseSpec](docs/ThinFuseSpec.md)
 - [ThinRuntime](docs/ThinRuntime.md)
 - [ThinRuntimeList](docs/ThinRuntimeList.md)
 - [ThinRuntimeProfile](docs/ThinRuntimeProfile.md)
 - [ThinRuntimeProfileList](docs/ThinRuntimeProfileList.md)
 - [ThinRuntimeProfileSpec](docs/ThinRuntimeProfileSpec.md)
 - [ThinRuntimeSpec](docs/ThinRuntimeSpec.md)
 - [TieredStore](docs/TieredStore.md)
 - [User](docs/User.md)
 - [VersionSpec](docs/VersionSpec.md)
 - [VineyardCompTemplateSpec](docs/VineyardCompTemplateSpec.md)
 - [VineyardRuntime](docs/VineyardRuntime.md)
 - [VineyardRuntimeList](docs/VineyardRuntimeList.md)
 - [VineyardRuntimeSpec](docs/VineyardRuntimeSpec.md)
 - [VineyardSockSpec](docs/VineyardSockSpec.md)
 - [VolumeSource](docs/VolumeSource.md)
 - [WaitingStatus](docs/WaitingStatus.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author


