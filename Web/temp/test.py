# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re


test_str = ("=== UUID ===\n"
            "8029C39E-1963-E511-906E-0012795D9712\n"
            "=== HostName ===\n"
            "IncorpGWdev151\n"
            "=== TimeSync ===\n"
            "02 * * * * /usr/sbin/ntpdate -s 211.233.74.8\n"
            "=== UlimitConfig ===\n"
            "root             soft    nofile          8192\n"
            "root             hard    nofile          8192\n"
            "*               soft    nofile          1024000\n"
            "*               hard    nofile          1024000\n"
            "*               soft    stack           unlimited\n"
            "*               hard    stack           unlimited\n"
            "=== FilePermission ===\n"
            "/etc/passwd : 644\n"
            "/etc/group : 644\n"
            "/etc/hosts : 644\n"
            "/etc/rsyslog.conf : 640\n"
            "/var/spool/cron : 600\n"
            "/etc/at.deny : 600\n"
            "/etc/at.allow : File Not Found\n"
            "/etc/cron.deny : 600\n"
            "/etc/cron.allow : File Not Found\n"
            "/etc/crontab : 600\n"
            "/etc/login.defs : 600\n"
            "/etc/inittab : 600\n"
            "/etc/xinetd.d : 600\n"
            "/etc/shadow : 400\n"
            "/usr/bin/sudo : 4111\n"
            "/etc/rc.local : 777\n"
            "=== SetUID ===\n"
            "/usr/bin/newgrp : 0\n"
            "/sbin/unix_chkpwd : 0\n"
            "/usr/bin/at : 0\n"
            "=== KernelParameter ===\n"
            "net.ipv4.tcp_max_syn_backlog = 4096\n"
            "net.ipv4.conf.all.send_redirects = 0\n"
            "net.ipv4.conf.all.accept_redirects = 0\n"
            "net.ipv4.conf.all.accept_source_route = 0\n"
            "net.ipv4.conf.all.forwarding = 0\n"
            "net.ipv4.icmp_echo_ignore_broadcasts = 1\n"
            "=== FTPChroot ===\n"
            "chroot_list_enable=YES\n"
            "=== FTPConfig ===\n"
            "anonymous_enable=NO\n"
            "=== /etc/issue.net ===\n"
            "#\\S\n"
            "#Kernel \\r on an \\m\n\n"
            "Authorised access only!\n"
            "This system is the property of INTERPARK.\n"
            "Disconnect IMMEDIATELY if you are not an authorised user!\n"
            "All activity may be MONITERED and REPORTED..\n"
            "Contact  'domainadmin@interpark.com'\n"
            "=== /etc/banners/ftp.msg ===\n\n"
            "#------------------------------------------------------------#\n"
            "# Authorised access only!                                    #\n"
            "# This system is the property of INTERPARK.                  #\n"
            "# Disconnect IMMEDIATELY if you are not an authorised user!  #\n"
            "# All activity may be MONITERED and REPORTED..               #\n"
            "# Contact  'domainadmin@interpark.com'.                      #\n"
            "#------------------------------------------------------------#\n"
            "=== SSHRootDisable ===\n"
            "PermitRootLogin no\n"
            "=== UserLock ===\n"
            "avahi : /dev/null\n"
            "rpc : /dev/null\n"
            "mailnull : User Not Found\n"
            "smmsp : User Not Found\n"
            "nscd : User Not Found\n"
            "vcsa : User Not Found\n"
            "haldaemon : User Not Found\n"
            "rpcuser : /dev/null\n"
            "nfsnobody : /dev/null\n"
            "sshd : /dev/null\n"
            "pcap : User Not Found\n"
            "xfs : User Not Found\n"
            "ntp : /dev/null\n"
            "apache : User Not Found\n"
            "gdm : /dev/null\n"
            "=== PassWordPolicy ===\n"
            "PASS_MAX_DAYS	\n"
            "PASS_MIN_LEN	8\n"
            "=== UMASKConfig ===\n"
            "umask 022\n"
            "=== BackSpaceConfig ===\n"
            "stty erase ^H\n"
            "=== TimeOutConfig ===\n"
            "TMOUT=1800\n"
            "=== TCPWrapperDeny ===\n"
            "ALL:ALL\n"
            "=== Runlevel ===\n"
            "multi-user.target\n"
            "=== DisableDaemon ===\n"
            "NetworkManager.service                  disabled\n"
            "bluetooth.service                       disabled\n"
            "cups.service                            disabled\n"
            "atd.service                             disabled\n"
            "iscsi.service                           disabled\n"
            "iscsid.socket                           disabled\n"
            "iscsiuio.socket                         disabled\n"
            "firewalld.service                       disabled\n"
            "firstboot-graphical.service             disabled\n"
            "ModemManager.service                    disabled\n"
            "=== RunningApp ===\n"
            "App : nginx\n"
            "Directory : /webserver/web/nginx/sbin/nginx\n"
            "Version : nginx/1.12.0\n")

regex = r"== ([^ ]+) ===((:?.|\n)+?)(^=|\Z)"
M = re.findall(regex, test_str, re.MULTILINE)
for r in M:
    print(r[0], r[1].strip())
