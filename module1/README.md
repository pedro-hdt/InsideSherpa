# JPMC Summer Internship SEP: InsideSherpa Module 1
## Real Time Alerting

### Task

As described ont he InisdeSherpa platform:

Reusable Python/Java Classes which can used to generate an alert against given 
list of rules and returns with Alert or No Alert with server id and violated 
rules list as comma separated values on terminal or rest endpoint,
Output from the code like (Alert, SERVER_ID,RULE(S) VIOLATED) or 
(No Alert, SERVER_ID)
e.g.(Alert,1234, CPU_UTILIZATION VIOLATED, DISK_UTILIZATION VOILATED) or 
(No Alert,2234) 

Expected Input:
Server resource parameters through command line argument or build a simple 
rest endpoint in Python/Java
Input Like (SERVER_ID, CPU_UTILIZATION, MEMORY_UTILIZATION, DISK_UTILIZATION)
Eg. (1234,89,69,65) or . (2234,81,62,55)

Bonus:
- Use a rest API for I/O rather than just having CLI
- Write unit tests
- Investigate Apache Kafka for input 

### Solution

Used Python 3 for the core logic and the Flask library to implement the REST 
API. For unittests the standard Python unittest mdoule was chosen. Kafka was 
not used.

The code is structured as a package (`alerts`) that provides a single class 
(`AlertService`) with a single method to be used externally (`alert_me()`).
The utilization limits are taken in as constructor arguments and cannot be 
subsequently changed so the`AlertService` object works with the same limits 
for its entire lifetime.

The CLI is implemented externally to the package in `cli_client.py`.

The REST API is very simple Flask app with a single method that handles post 
requests that should include the tuples as raw data.

Unit test are provided for the core logic only in `test_alerts.py`.

TODO how to set limnits in rest???

### Assumptions

Due to a lack of clarification on the specification, the following assumptions 
were made about the desired behavior of the solution:

* Only the 3 mentioned utilization values are supported: CPU, memory and disk. 
No configuration of this is supported
* Utilization values can be taken in as floats but will be rounded to the 
nearest integer
* Server IDs can contain any alphanumeric character
* The input format is comma-separated and may or may not have parentheses 
surrounding each entry.
* The utilization limits for the rules are passed in to the AlertService 
constructor. For direct CLI usage these can be passed as arguments (see 
`--help` flag).
* The REST API defines a single POST mapping (to the root URL) with the input 
taken as raw data from the request body
* The CLI terminates on the first empty line, EOF or keyboard interrupt that 
it receives as input

### How to use

For the command line interface:

```
./cli_client.py [--cpu=<cpu_limit>] [--mem=<mem_limit>] [--disk=<disk_limit>] 
[ < inputfile ]
```

For the REST API (this starts a development server only but that seems enough 
for the purpose of the exercise):

```
./rest_api.py
```

#### Running tests

```
python -m unittest test_alerts.py
```
