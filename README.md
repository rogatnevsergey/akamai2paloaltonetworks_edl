# akamai2paloaltonetworks_edl

This project is to automate PaloAltoNetworks firewall EDL creation from Akamai Shield. 

## Quick Start

The script takes "akamai.txt" file as input.
And generates "akamai-edl.html" file that could be used as a EDL source.

Downloading the files is done using a git clone command or a direct download of the repo as a zip file.

```
https://github.com/sergeyrogatnev/akamai2paloaltonetworks_edl.git
```

## To Do

1. Fetch Akamai Shield prefix list from Akamai,
2. Once script run, verify all IP in the list are valid IPv4 prefixes,
3. Published the new generated EDL to web site,
4. Send email to provide status.
