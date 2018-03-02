import os
import paramiko

paramiko.util.log_to_file('/tmp/paramiko.log')
paramiko.util.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))

host = 'localhost'
port = 22
username = 'user'

file = 'output.txt'
remote_images_path = '/Users/Ricardo/Desktop/'
local_path = '/Users/adriana/Documents/uni/EC/is/IS_Med/'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=host, port=port, username=username)
sftp = ssh.open_sftp()


file_remote = remote_images_path + file
file_local = local_path + file

print file_local + '>>>' + file_remote

sftp.put(file_local, file_remote)

sftp.close()
ssh.close()