# telnet_checker
Script to check credentials against telnet servers

## Usage: 
To run this program, just create a creds file and put the information inside.
```
$ ls -l
total 276
-rwxrwxr-x 1 bigfucker bigfucker   1163 Jan 25 20:24 checker.py
-rw-rw-r-- 1 bigfucker bigfucker 666 Jan 25 20:24 creds
```
Then run:

```
chmod +x checker.py
./checker.py
```


## Creds File
The creds file must be in the follow format:
```
IP:username:password
xxx.xx.xx.xxx:username:password
xxx.xxx.xx.xx:root:password
```

