# BlockChain

**Install the required packages in requirments.txt**

**Activate the virtual environment**

```source blockchain-env/bin/activate```
**Install all packages**

```pip3 install -r requirements.txt```
**Run the tests**

**Make sure to activate the virtual environment.**

```python3 -m pytest backend/tests```
**Run the application and API**

**Make sure to activate the virtual environment.**

```python3 -m backend.app```
**Run a peer instance**

**Make sure to activate the virtual environment.**

Mac and Linux
```export PEER=True```
Windows Command prompt
```set PEEER=True```
Windows Powershell
```$Env:PEER = "True"```
```python3 -m backend.app```
**Run the frontend**

**In the frontend directory:**

```npm run start```
**Seed the backend with data**

**Make sure to activate the virtual environment.**

Mac and Linux
```export SEED_DATA=True```
indows Command prompt
```set SEED_DATA=True```
Windows Powershell
```$Env:SEED_DATA = "True"```
```python3 -m backend.app```