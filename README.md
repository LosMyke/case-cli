## Summary
Simple python scipt that can be used to review open cases as and open new cases. This is not a full featured script and still a work in progress

## Requirments 
- AWS Python SDK Boto3 
	- https://boto3.readthedocs.org/en/latest/guide/quickstart.html#installation


## Install 
1. Clone the repo
2. Ensure your AWS IAM user has the approproate policy attached, "AWSSupportAccess"
3. Ensure you have setup your AWS authentication credentials
	- https://boto3.readthedocs.org/en/latest/guide/quickstart.html

## How to use 
1. Execute the file 'python aws-case-cli.py'
2. Note what severity level you want, to view a list select option 3
3. Identify the Servie Code and Category Code you want, to view a list select option 4
	- Output will save to file called 'describe-services.out'
	- For example If I want to open a case for Virtual Private Cloud (VPC) API's I'd look at 

   ``` 
   {
    "categories": [
    {
        "code": "apis",
        "name": "APIs"
    },
    {
        "code": "vpn-solutions",
        "name": "VPN Solutions"
    },
    {
        "code": "connection-issue",
        "name": "Connection Issue"
    },
    {
        "code": "general-guidance",
        "name": "General Guidance"
    }
    ],
        "code": "amazon-virtual-private-cloud",
        "name": "Virtual Private Cloud (VPC)"
    },
	``` 

 	ServiceCode: amazon-virtual-private-cloud
 	CategoryCode: apis
4. Now that you have your Severity, CategoryCode, and ServiceCode you're ready to open the case, select option 2 and fill out all information. 

#### Example
```
python aws-case-cli.py
AWS Support API CLI
This script will allow you to list and open cases.

Menu
 (1) View Open Cases
 (2) Open a Case
 (3) Describe severity levels
 (4) List Services
 (Q)uit
>>> 2
Subject: Test Case
Service Code: amazon-virtual-private-cloud
Severity Code: low
Category Code: apis
Communication Body: This is a test case and can be closed.
Issue Type (customer-service / technical): technical
CC Email Address: user@user.com
('Test Case', 'amazon-virtual-private-cloud', 'low', 'apis', 'This is a test case and can be closed.', 'technical')
{u'caseId': u'case-XXXXXXXXXXXX-xxxx-XXXX-XXXXXXXXXXXXXXXX', 'ResponseMetadata': {'HTTPStatusCode': 200, 'RequestId': 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'}}
```

## To do
1. Modify output from "View Open Cases" to only show 
	- displayId
	- subject
	- severityCode
	- timeCreated
	- submittedBy
	- status
1.1 Allow the user to expand on their view to see all corespondance. 
2. Add capability to update, modify status, and resolve from command line.
3. Modify output of "Describe severity levels" to make it more screen friendly.
	- Possibly move this option to only disply when opening a case.
4. Modify output of "List Services" from file dump to display on screen.
	- Would like to change this to menu driven where you select your Service Code first then select Category
	- Possibly move this option to only display when opening a case. 
