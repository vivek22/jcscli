#!/bin/bash

echo " running cli tests please wait !  "

python cli_testing_dssANDhelp.py > dssANDhelp.log
python cli_testing_vpc.py > vpc.log
python cli_testing_compute.py > compute.log
python cli_testing_iam.py > iam.log
python cli_testing_rds.py > rds.log

echo " complete "

