#!/usr/bin/python
# -*- coding: utf-8 -*-

import paramiko

TRANSMISSION_RETRIES = 10

class SSHUtility:

    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password
        self.connect_ssh(self.host, self.username, self.password)
        pass

    def connect_ssh(self, host, username, password):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(host, username=username, password=password)

    def execute_cmd(self, cmd, show_output=False, show_error=False):
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        stdin.close()

        if show_output:
            for line in stdout.read().splitlines():
                print('%s: %s' % (str(self.host), str(line)))
        stdout.close()

        if show_error:
            for line in stderr.read().splitlines():
                print('%s: %s' % (str(self.host), str(line) + "\n"))
        stderr.close()

    def close(self):
        self.ssh.close()