## Auth

Make sure you are auth'd using:

`gcloud auth application-default login`

## Usage

- Create a new entity usage:

`./entity-uploader.py <entity name>`

- Update an entity usage:

`./entity-uploader.py <entity name> <entity ID>`

entity ID can be found when you click into an entity. It will be in the URL at the end:

`entityTypes?id=xxxxxxxx`
