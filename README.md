# Jane Street ETC 2022
Copy file from local machine to EC2 instance

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
