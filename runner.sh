#!/bin/bash

echo " run "

python cli_testing_dssANDhelp.py > dssANDhelp.log
python cli_testing_vpc.py > vpc.log
python cli_testing_compute.py > compute.log
python cli_testing_iam.py > iam.log

echo " complete "

