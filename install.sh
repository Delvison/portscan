cp portscan.py /usr/bin/portscan
chmod +x /usr/bin/portscan
echo "Successfully installed."
echo "Usage: portscan -s [IP_address] [start_port] [end_port]"
echo "       portscan -m [start_IP_address] [end_IP_address] [start_port] [end_port]"
echo "Args:"
echo " -s: indicates single IP mode."
echo " -m: indicates multiple IP mode"
