# Airflow, selenium and docker
This project is designed to automate selenium scripts.

## Specification
* Airflow 2.3.3 
* Python 3.9 
* Selenium image "standalone-chrome"

Parsed data will be save in remote mongo database.
### Step 1. Up preparing
```
docker-compose build
docker-compose up
```
## TODO: 
### **Finish base**
- [ ] Airflow MongoDB
- [ ] Data persistence
- [ ] Selenium Scripts