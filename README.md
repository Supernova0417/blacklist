# What is the BLACKLIST?

A script-package to Manage Emails, IPs, IP Ranges, ASNs in the CUSTOM LISTS tab on https://proxycheck.io/dashboard/

# How to set it up?

1. Clone this to a directory of your own machine.

2. Make sure that Python3.x, pip, and modules(request, logging, etc.) are already installed.
> On the CMD, or CLI  
: sudo apt-get install python3 python3-pip  
When done, then  
: pip3 install request logging  
Now it's ready to run the blacklist.py!  
: python blacklist.py

3. Check if it creates blacklists well.

4. Synchronize the list on your machine with the one of proxycheck.io.
> There are ways to set up web services such as Nginx and Apache on your machine so that the list can be viewed directly by proxycheck.io,  
or to upload the list to a third platform using API and connect it to proxycheck.io

# Why did you upload your ASN & IP detection lists in a public repository?

This repository is a script package but also my __personal-use__ repository. I'm updating them together with the script,  
because I think the records I've used and tested myself will __help new users and develop the package__.

However, the ASN and IP listed in this repository are my __personal detections__,  
which other users __can only be _referenced_, and are _different_ from professional ISP & IP reputation detections__.

Nevertheless, if you would like certain logs to be deleted from the list,  
please contact **Discord DM: Supernova#0417**.  
(I don't really check other platforms or messengers.)

# An Example Actually Applied!
![proxycheck io_dashboard_202404011](https://github.com/Supernova0417/blacklist/assets/74053211/4117db89-2139-48df-9f74-dbbfa90ebf7a)

