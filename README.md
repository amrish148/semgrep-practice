# semgrep-practice
semgrep rules definitions

reference repo:
java: https://github.com/Rohak-Thakur/Java-MySQL-Connectivity
c#: https://github.com/kitkav/C-Web-Api
python spotify: https://github.com/4GeeksAcademy/ginappedrosa-interacting-with-api-python-project-tutorial 
python DB: https://github.com/imleoos/Python-SQLite-Client


curl -X POST http://localhost:8000/scan/ -F "code_path=/Users/amrish/Work/Projects/github/Java-MySQL-Connectivity" -F "config_path=/Users/amrish/Work/Projects/github/semgrep-practice/java-mysql-conn-rules.yaml" 

#Curl output to a json file -o result.json