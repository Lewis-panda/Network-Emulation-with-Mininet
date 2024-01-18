# Project README

## Table of Contents
1. [Background](#background)
2. [Network Topology](#network-topology)
   - [Mininet Command-Line Interface (CLI)](#mininet-command-line-interface-cli)
3. [iPerf](#iperf)
4. [Wireshark](#wireshark)

## Background
This project aims to explore and implement methods for network simulation and performance testing using 
- Mininet
- iPerf
- Wireshark
Below is a brief introduction to these tools and some basic operations.

## Network Topology
With Mininet, we can create a realistic virtual network running real kernel, switch, and application code on a single machine (VM, cloud, or native). This includes running a collection of endpoints, switches, routers, and links on a single Linux kernel.
Reference: [Mininet Official Website](https://mininet.org/)

### Mininet Command-Line Interface (CLI)
Mininet provides a powerful command-line interface for easy manipulation of the virtual network. Here are some commonly used CLI commands:

```bash
# Start a simple minimal topology and enter the CLI
$ sudo mn
mininet> help

# Show information of all nodes
mininet> nodes

# Show all links in the network
mininet> links

# Show the network topology
mininet> net

# Show all ports on every switch
mininet> ports

# Show all network interfaces
mininet> intfs

# Dump information about all nodes
mininet> dump

# Test connectivity of all hosts
mininet> pingall

# Test TCP connection of two hosts with iPerf
mininet> iperf

# Leave the CLI mode
mininet> exit
```
Note: After exiting Mininet, use "sudo mn -c" to clean up the environment; otherwise, you may encounter errors, such as "File Exists Error."


# iPerf

iPerf is a tool for active measurements of the maximum achievable bandwidth in IP networks. It supports tuning various parameters related to timing, buffers, and protocols (TCP, UDP, SCTP with IPv4 and IPv6).

iPerf Command line options: [iPerf Official Documentation](https://iperf.fr/iperf-doc.php)

# Wireshark

Wireshark is a widely-used network protocol analyzer with the following features:

- Deep inspection of hundreds of protocols
- Live capture and offline analysis
- Most powerful display filter
- Read/write many different capture file formats

Wireshark Official Website: [Wireshark](https://www.wireshark.org/)
