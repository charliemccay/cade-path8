# cade-path8
This is a demo Resources folder for the CADE2 pathway-based simulation tool.  This simulation contains extended examples of observations

This implementation allow the simulation to be run from single docker-compose files, either simply generating the outputs in outputs/exhaust, or pushing the outputs into the fhir servers and logging the outputs and responses in outputs/exhaust


The simulaion assumes that there are 2 fhir servers running: one to validate the bundle that would be sent as a report for the test result, and one representing a repository that is used to store the resources locally.

The simulation uses that Smart-on-fhir server for storing the resources locally, and that NHS digital reference implementations erver for the validation of the bundle.  The latter is not (yet) configured to receive pathology resources, but will validate using externally hosted structureDefinitions, so does validate the bundle.

1. If you don't already have Docker on your system, download and install it from https://store.docker.com/search?type=edition&offering=community
2. If you don't already have Git on your system, download and install it from https://git-scm.com/downloads

## download files

To download the required files cd to an appropriate directory and run the following:
```sh
    git clone https://github.com/charliemccay/cade-path8
```

## start the simulation and two fhir servers
This will start a number of containers:
* ccriserver: this is a FHIR server used to validate the bundles.  This is the NHS Digital Reference Implementation.  See https://nhsconnect.github.io/CareConnectAPI/build_ri_install.html
* ccrisql: this is he database used by ccriserver
* smartonfhir: this is  a generic fhir server used to accept the pathology resources (it accepts all respource types)
* fhirexplorer: this is a ui to browse the contents of ccriserver
* cade: thsi is the simulation engine

```sh
    docker-compose -f docker-compose.cade.with.connections.yml up --force-recreate 
```

Once the cade contaner has stopped, there should be files in the directories under files/outputs directory.  Note that the other containers will still be running allowing you to access the FHIR server on http://localhost:8080/baseDstu3/ to see the resources that have been pushed into it. 
The file docker_outputs/cade.with.connections.output.txt provides an example of what should be displayed to teh screen if the container is running correctly.  Note that there are three errors reported as the resources are being validated - thsi si because within the pathology profiles there are some missing valuesaets, and the Care Connect Reference Implementation is unable to validate LOINC concept identifiers

## start simulation on its own without posting to the fhir servers

```sh
    docker-compose -f docker-compose.cade.no.connections.yml up --force-recreate 
```

The file docker_outputs/cade.no.connections.output.txt provides an example of what should be displayed to teh screen if the container is running correctly.  

## start fhir servers independantly 

To Start the SMART on FHIR server that will act as a repository for the resources:

```sh
    docker run -it -p 8080:8080 smartonfhir/hapi:r2-empty
```

Open another terminal window to start the care connect reference implementation (for testing the bundle):

```sh
    cd ../cade-path8
    docker-compose -f docker-compose-ccri.yml up
```

start simulation
    
Once the FHIR servers are running, open another terminal window.  From there you can then run the CADE container which will post the patients and observations to the FHIR server.  Having each container running in its own terminal will allow you to see what is happening more easily.  To run a simulation outside docker-compose you need to mount the Resources folder in this project in the CADE2 Docker container.  Note that you need to provide an absolute path for the Resources folder, hence the $(pwd).
    
```sh
    docker run -v $(pwd)/resources:/usr/src/app/resources --network="host" ramseysys/cade-2:latest python start.py
```
        
## stopping the servers

The simulation container will stop one the process is complete, and the logs are available in the "resources/outputs" folder.   Note that this is cleared down each time the simulation is run.

The FHIR servers can be stopped with ctrl-c.  When they are started again the contents will remain unless the container is deleted.  This implementation of CADE uses UUIDs for the resource identifiers, so can be run multiple times without clashing identifiers - every time someone is born they are assumed to be a new person.

## further reading

The BPMN models can be edited with the Camunda Modelling tool: https://camunda.com/download/modeler/
There are useful installation notes on the ccri server at https://nhsconnect.github.io/CareConnectAPI/build_ri_install.html
Article about validating Care Connect FHIR resources https://www.openhealthhub.org/t/validating-fhir-care-connect/2056

## next steps

* read in test results from file
* use logical model for internal data in simulation

