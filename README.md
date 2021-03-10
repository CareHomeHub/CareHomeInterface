# CareHomeInterface


## CareHomeHub API
   To build :  docker build -t chi_api .
   
   To run : docker run -d --name chi_api_contaner -p 7000:7000 chi_api


## CareHomeHub Web App
   To build :  docker build -t chi_web:v0.0.1 .
   
   To run : docker run -d --name chi_web_contaner -p 5000:5000 chi_web:v0.0.1
