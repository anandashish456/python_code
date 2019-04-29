from paramiko import SSHClient, AutoAddPolicy


def ssh_remote_files(host, user, srcfile, destfile, action):
    ssh_client = SSHClient()
    ssh_client.set_missing_host_key_policy(AutoAddPolicy())
    ssh_client.connect(hostname=host, username=user)
    ftp_client = ssh_client.open_sftp()

    if action == "import":
        ftp_client.get(srcfile, destfile)
    else:
        ftp_client.put(srcfile, destfile)

    ftp_client.close()

