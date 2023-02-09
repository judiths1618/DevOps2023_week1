# Swagger generated server

This server was generated by the [swagger-codegen](https://github.com/swagger-api/swagger-codegen) project. By using the
[OpenAPI-Spec](https://github.com/swagger-api/swagger-core/wiki) from a remote server, you can easily generate a server stub.  This
is an example of building a swagger-enabled Flask server.

This example uses the [Connexion](https://github.com/zalando/connexion) library on top of Flask.

Requirements
Python 3.5.2+

Usage
To run the server, please execute the following from the root directory:

```
pip3 install -r requirements.txt
python3 -m swagger_server
```

and open your browser to here:

```
http://localhost:8080/service-api/ui/
```

Your Swagger definition lives here:

```
http://localhost:8080/service-api/swagger.json
```

To launch the integration tests, use tox:
```
sudo pip install tox
tox
```

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t swagger_server .

# starting up a container
docker run -p 8080:8080 swagger_server
#� �w�e�e�k�2�l�a�b�_�v�3�
�
�
```
# Hints to give the students

## Week1
How to declare properties in OpenAPI Objects
```
components:
  schemas:
    Student:
      type: object
      properties:
        student_id:
          type: integer
          format: int64
```
How to reference to an item inside an array
```
    # Array of Pets
    type: array
    items:
      $ref: '#/components/schemas/Pet'
```
How to set float

https://swagger.io/docs/specification/data-models/data-types/





> **Note**
> 
> REGISTRY_USERNAME and REPO_NAME should be your Dockerhub username 

> **Warning**
> 
> Build action fails with COPY .. /usr/src/app
> 
> Should be COPY . /usr/src/app




