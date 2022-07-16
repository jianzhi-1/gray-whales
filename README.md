# Jane Street ETC 2022
Copy file from local machine to EC2 instance

scp /Users/jianzhiucb/gray-whales-local/sample-bot.py ubuntu@100.25.23.202:/home/ubuntu

scp -r /Users/jianzhiucb/gray-whales-local/sample-bot.py ubuntu@100.25.23.202:/home/ubuntu/jane

Running on production
# 3) Run in loop: while true; do ./bot.py --production; sleep 1; done

### Actual

```shell
ubuntu@bot-gray-whales:~$ host test-exch-gray-whales
```
```shell
nc test-gray-whales 20000
```


### From online


```shell
scp -i identity_file.pem source_file.extention username@public_ipv4_dns:/remote_path
```

Copy file from EC2 instance to local machine
```
scp -i identity_file.pem username@public_ipv4_dns:/remote_path/source_file.extension ~/destination_local_path
```
