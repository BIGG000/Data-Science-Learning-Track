RPA Fraud Detection
Reputable Product Agency (RPA) has started receiving complaints from their credit card processor about fraudulent transactions. Help your finance department identify potentially risky transactions before they finish processing.

This dataset contains a single table, transaction_data.

The schema of this table is available here.

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Help“ to see a project walkthrough video.

1.
Start by getting a feel for the transaction_data table:

SELECT *
FROM transaction_data
LIMIT 10;
What are the column names?

2.
The finance department noted that some of the fraudulent transactions were recorded as coming from Smokey Bear’s zip code (20252).

You agree this is suspicious, it’s unlikely that the fire prevention mascot is using Reputable Company’s services.

Find the full_names and emails of the transactions listing 20252 as the zip code.


3.
Finance has also noticed a number of pseudonyms associated with fraudulent transactions.

The fraudsters thought it would be funny to use ‘Art Vandelay’ for their full name or add a ‘der’ for their middle name.

Use a query to find the names and emails associated with these transactions.

4.
There are some irregularities in the IP addresses where transactions are originating from.

For example, any IP address beginning with ‘10.’ is reserved for internal use.

We shouldn’t see IP addresses like this accessing Reputable Company’s service.

Find the ip_addresses and emails listed with these transactions.

5.
Users are making fraudulent transactions using a temporary email address service. These services provide a short-lived email that can be verified and then self-destructs.

Find the emails in transaction_data with ‘temp_email.com’ as a domain.

6.
The finance department is looking for a specific transaction. They know that the transaction occurred from an ip address starting with ‘120.’ and their full name starts with ‘John’.

Can you find the transaction?
