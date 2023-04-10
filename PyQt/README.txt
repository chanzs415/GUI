Before running the script, have to modify some directories for now.

3 directories in the functions to change:
1. def runCommand(self):
 - Put the docker compose directory to yours

2. def stopCommand(self):
 - Put the docker compose directory to yours

3. def getData(self):
- Run the following line below to create the hadoop_namenode/ volume first
 -> docker cp sparkcontainer:/app/ hadoop_namenode/
- Weather API doesnt run yet, so take the combined_csv.csv and put it in the volume first
- Then change the first directory in the command = r'.....' to the combined_csv.csv file directory in the volume

The UI is currently a separate thing from docker, so it doesnt run inside any of the containers.
Need to download PyQt5 along with python in your pc before the UI can run. (pip install pyqt5, pip install pyqt5-tools)

Run the script for the UI to appear
-> python testui.py