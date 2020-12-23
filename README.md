# Documentation

## Installation
Download the project from `git@github.com:alex4u2nv/monitor-fs.git`
Navigate to the folder and install by running the following commands
```shell
python3 -m venv my-python-environment
source my-python-environment
git clone git@github.com:alex4u2nv/monitor-fs.git
pip3 install monitor-fs
pip3 show monitor-fs
my-python-environment/bin/monitor --help # for usage data

```

### Usage Data
```shell
usage: monitor-fs [-h] -q QUEUE_URL -f FOLDER

Monitor a folder and write events to SQS

optional arguments:
  -h, --help            show this help message and exit
  -q QUEUE_URL, --queue_url QUEUE_URL
                        Path to ACS. For example https://sqs.us-east-1.amazonaws.com/accountid/myqueue
  -f FOLDER, --folder FOLDER
                        path to folder to monitor
```