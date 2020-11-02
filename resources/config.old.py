import os
from resources.files.pathway import extensions
from py_code.enums import ConnectionTypes

### Running CADE ###
# ignore_warnings
# True - warnings will be displayed but the user will not be prompted to ask if they wish to continue.
# False - the user will not be prompted to ask if they wish to continue on any warning.
ignore_warnings = True
event_count_limit = 10000
# run_time_selections indicates how many options the user wishes to be presented with at run time. Exit option will be
# available at every prompt. Positive numbers will present more options as they increase. Negative numbers cawn be use
# for special case options (eg. a config setup option where every option is presented before running)
# 0 - no run time options are available. All variables must be set through the config. This is the default.
# 1 - Y/N questions only will be presented for config values not set TBD
# 2 - questions only will be presented for config values needed(Y/N, file locations) but not set TBD
# 3 - all Y/N questions will be presented in addition to option 2
# 4 - questions will be presented for all config values needed(Y/N, file locations)
# Yet to be implemented, leave as 0
run_time_selections = 0

informationItemsFile = "InformationItems.csv"
setAttributesFile = "AttributesSet.csv"

### Choose what will be executed
# population_gen_bool will indicate if a population is to be created in this run.
population_gen_bool = True
# population_gen_bool will indicate if a chosen set of pathways will be validated.
pathway_validation_bool = True
# execute_engine_bool will indicate if a simulation is to be executed this run.
# This implies that pathway validation will be run. Overrides pathwayValidation if false.
execute_engine_bool = True
# population_gen_bool will indicate if a visualisation is to be created in this run.
visualisation_bool = False
# visulisationDisplay not working currently - should be left as False
visualisation_display = False

current_dirname = os.path.dirname(__file__)
dirname = os.path.join(current_dirname, "../")

### Directories ###
# default_dir_location indicates where the resources directory is located.
default_dir_location = dirname
pathway_file_location = "resources/files/pathway/"


### py_logging ###
# language_file_location indicates where the language file to be used is located.
language_file_location = dirname + "py_code/py_logging/log_details.csv"
# message_set will be the header value of the set of messages to be used from the language file.
message_set = "message"
# individual_logs indicates whether the simulation will keep individual logs of patients at run time.
individual_logs = True
delete_logs = True


### Exhausts ###
# digitalExhaustDir indicates where the templates for a digital exhaust are located.
digital_exhaust_template_dir = dirname + "resources/files/exhaust_templates/"
# digital_exhaust_file will be the name of the file in the digitalExhaustDir location that details how the templates are
# to be used.
digital_exhaust_file = "ExhaustConfig.csv"
# digital exhaust directory
digital_exhaust_dirname = os.path.join(
    current_dirname, "../resources/outputs/exhaust/"
)
digital_exhaust_directory = digital_exhaust_dirname
# clear the exhaust directory
delete_exhaust = True
# number of seconds per tick
tick_value = 900


### Population creation ###
# population_size will indicate the desired number of persons. May end up off slightly
population_size = 50
# location of population file to load in
# population_file_path = 'resources/files/populations/start_population 2.csv'
population_file_path = (
    dirname + "resources/files/populations/start_population 50.csv"
)
# todo delete_end_population


### Execution engine ###
# Time between checks of the case for changed variables allowing sentries to be passed
# TBD: Only check case when change is made. This variable is a temporary fix.
caseTime = "Hours"


### visualisation ###
# Location of a list of nodes that will be used to filter the data shown in built figures
# TBD: Generate this list from pathway files with indicators on nodes of interest
nodes_list_file = dirname + "resources/files/visualisations/NodesList.csv"
# Log to be used for building the visualisations
vis_log = None

### FHIR exhaust ###

### FHIR exhaust  for kafka ###
# fhir_base = "http://localhost:8082/topics/"
# fhir_headers = {'Content-Type': 'application/vnd.kafka.json.v2+json'}
# if this is set to true then there will be a check to see if the FHIR server is available by
# checking for a connection to an endpoint in the fire server
# fhir_metadata_test = False
# this is is endpoint that is used to establish whether the FHIR resrver is up and available. This
# will be retried 10 times
# fhir_metadata_endpoint = "metadata"
# this is a default setting for whether item_id should be included at the end of the FHIR URL
# fhir_include_id = False
# this is to determine whether PUT or POST method request should be used (default to PUT)
# fhir_method_request = "POST"


##fhir_base = ""
## fhir_base = 'http://localhost:8080/baseDstu2/'
fhir_base = 'http://localhost:8186/ccri-fhir/STU3/'
## fhir_base = 'https://nhs.smilecdr.com/fhir-request/'
fhir_headers = {'Content-Type': 'application/json'}

# if this is set to true then there will be a check to see if the FHIR server is available by
# checking for a connection to an endpoint in the fire server
fhir_metadata_test = True
# this is is endpoint that is used to establish whether the FHIR resrver is up and available. This
# will be retried 10 times
fhir_metadata_endpoint = "metadata"
# this is a default setting for whether item_id should be included at the end of the FHIR URL
fhir_include_id = True
# this is to determine whether PUT or POST method request should be used (default to PUT)
fhir_method_request = "PUT"


eval_locals_extensions = {
    "random_line": extensions.random_line,
    "obs": extensions.obs,
    "mins": extensions.mins,
    "hours": extensions.hours,
    "smartonfhir": extensions.smartonfhir,
    "ccri": extensions.ccri,
    "getvalue": extensions.getvalue
}

default_server_type = ConnectionTypes.FHIR

is_running_connections = False
