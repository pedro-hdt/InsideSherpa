"""
JPMC Virtual SEP - InsideSherpa - Module 1
Pedro Teixeira - O734271

Core logic of the alerts package
"""

import re

class AlertService:
    """
    Implements a simple interface for generating the alert messages according 
    to the input utilization tuple:

    alert_me(entry) takes a single utilization tuple and returns the alert/no 
    alert message
    """

    RULE_CPU = "CPU_UTILIZATION VIOLATED"
    RULE_MEM = "MEMORY_UTILIZATION VIOLATED"
    RULE_DSK = "DISK_UTILIZATION VIOLATED"

    NO_ALERT = "No Alert"
    ALERT = "Alert"

    def __init__(self, cpu_limit=85, mem_limit=75, disk_limit=60):
        self.cpu_limit = cpu_limit
        self.mem_limit = mem_limit
        self.disk_limit = disk_limit

    def _parse(self, entry: str):
        """
        Extracts the fields in the format below from an input string into a 
        tuple (structured) format.

        Format: (SERVER_ID, CPU_UTILIZATION, MEMORY_UTILIZATION, 
            DISK_UTILIZATION)
        """ 

        # separate values by a comma surrounded by any number of whitespace chars
        pattern = re.compile(r"\s*,\s*")

        # extract data to useful format
        server, cpu, mem, disk = pattern.split(entry.strip("()\n"))       

        # strip ends of server id and round utilization to nearest int 
        return (server.strip(), 
                round(float(cpu)), 
                round(float(mem)), 
                round(float(disk)))


    def _validate(self, server: str, cpu: int, mem: int, disk: int):
        """
        Validates utilization data according to the limits provided on 
        object construction, to check for over utilization of cpu, mem
        or disk.
        """
        rules_violated = []

        # check for rule violations
        if cpu > self.cpu_limit:
            rules_violated.append(self.RULE_CPU)
        if mem > self.mem_limit:
            rules_violated.append(self.RULE_MEM)
        if disk > self.disk_limit:
            rules_violated.append(self.RULE_DSK)

        if len(rules_violated) > 0:
            out = (self.ALERT, server, *rules_violated)
        else:
            out = (self.NO_ALERT, server)

        # apply proper format to result
        return f"({', '.join(out)})"


    def alert_me(self, entry):
        """
        Generates the appropriate alert/no alert message for the given entry
        """
        server, cpu, mem, disk = self._parse(entry)
        return self._validate(server, cpu, mem, disk)

    