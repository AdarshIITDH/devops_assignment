Question 1

Deploy a website on localhost using either apache2 or nginx. Create a DNS name for this website as ‘awesomeweb’. You can use any web template you want or can write your own simple html code. Write a detailed documentation with steps involved. 

Answer: Follow the redme.docx
https://github.com/AdarshIITDH/devops_class_assignment/blob/main/Networking%20and%20Servers/readme.docx

https://github.com/AdarshIITDH/devops_class_assignment/tree/main/Networking%20and%20Servers/question-1
![image](https://github.com/AdarshIITDH/devops_class_assignment/assets/60352729/8ac9bf34-cc95-4d39-99da-29484c80e54b)

Question 2

A website can have many subdomains and different services are running on them. Write a Python script to check the status of the subdomains which are up or down. The script should automatically check the status every min and should update it in tabular format on the screen. Write a detailed documentation of it.

Answer:

Requirements:

•	requests library: To make HTTP requests and check the status of subdomains.
•	tabulate library: To present the results in a tabular format.
•	time library: to check in 60sec
•	pip install requests tabulate

Functionality:

•	The script uses the requests library to make HTTP GET requests to the URLs of the subdomains to check their status.
•	The tabulate library is employed to display the results in a grid-based tabular format on the screen.
•	The script continuously checks the status of all subdomains every minute and updates the status table accordingly.
•	If a subdomain's service is up and responds with a status code of 200, the status will be marked as 'Up.' Otherwise, it will be marked as 'Down.'
•	To stop the script, simply press Ctrl+C.

Output:
![image](https://github.com/AdarshIITDH/devops_class_assignment/assets/60352729/7820d960-dcbd-46f5-9366-6f4d3daf8ec4)







