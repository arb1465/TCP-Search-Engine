import socket

dictionary = {
    "network": "A network consists of two or more computers or devices connected together to share resources.",
    "protocol": "A set of rules that defines how data is formatted and transmitted on a network.",
    "TCP": "Transmission Control Protocol - A connection-oriented protocol that provides reliable, ordered, and error-checked delivery of data.",
    "UDP": "User Datagram Protocol - A connectionless protocol that provides faster but less reliable delivery of data.",
    "IP": "Internet Protocol - A protocol responsible for addressing and routing packets across networks.",
    "router": "A networking device that forwards data packets between computer networks. It operates at the OSI network layer.",
    "switch": "A networking device that connects devices together within a local area network (LAN). It operates at the OSI data link layer.",
    "firewall": "A security device or software that monitors and controls incoming and outgoing network traffic based on predetermined security rules.",
    "subnet": "A portion of a network that shares a common address component. Devices within the same subnet can communicate directly with each other.",
    "DNS": "Domain Name System - A hierarchical decentralized naming system for computers, services, or other resources connected to the Internet.",
    "LAN": "Local Area Network - A network that connects computers and devices in a limited geographical area, such as a home, office, or school.",
    "WAN": "Wide Area Network - A network that spans a large geographical area, often connecting multiple LANs together.",
    "HTTP": "Hypertext Transfer Protocol - A protocol used for transmitting hypertext documents on the World Wide Web.",
    "HTTPS": "Hypertext Transfer Protocol Secure - An extension of HTTP that uses encryption to secure the data transmitted between the client and server.",
    "FTP": "File Transfer Protocol - A standard network protocol used to transfer files from one host to another over a TCP-based network.",
    "IPv4": "Internet Protocol version 4 - The fourth version of the Internet Protocol, which uses a 32-bit address scheme.",
    "IPv6": "Internet Protocol version 6 - The most recent version of the Internet Protocol, which uses a 128-bit address scheme to address the IPv4 address exhaustion issue.",
    "subnet mask": "A bitmask used to divide an IP address into network and host portions. It determines which part of the IP address is the network identifier and which part is the host identifier.",
    "gateway": "A network node that serves as an entry and exit point for another network. It typically connects a LAN to the Internet or another WAN.",
    "packet": "A unit of data transmitted over a packet-switched network. It consists of a header and payload containing the actual data being transmitted.",
    "TCP/IP": "Transmission Control Protocol/Internet Protocol - The suite of protocols used for communication over the Internet. It includes TCP, IP, and other protocols.",
    "DNS server": "A server responsible for translating domain names into IP addresses and vice versa.",
    "subnetting": "The process of dividing a large network into smaller subnetworks, or subnets, to improve performance and security.",
    "ARP": "Address Resolution Protocol - A protocol used to map IP addresses to MAC addresses on a local network.",
    "DHCP": "Dynamic Host Configuration Protocol - A network management protocol used to automatically assign IP addresses and other network configuration parameters to devices on a network.",
    "router": "A device that connects multiple computer networks and routes data packets between them. It operates at the network layer of the OSI model.",
    "NAT": "Network Address Translation - A process that translates private IP addresses to public IP addresses and vice versa to enable communication between devices on different networks.",
    "VPN": "Virtual Private Network - A secure encrypted connection established over a public network, typically the Internet, to ensure secure data transmission.",
    "traceroute": "A diagnostic tool used to trace the route that packets take to reach a destination host on an IP network.",
    "ping": "A network utility tool used to test the reachability of a host on an Internet Protocol (IP) network and measure the round-trip time for packets sent to the host.",
    "port": "A communication endpoint identified by a numerical value within the header of a data packet. It allows multiple networked services to operate on a single device.",
    "TCP handshake": "The process of establishing a TCP connection between two devices. It involves a three-way handshake where SYN, SYN-ACK, and ACK packets are exchanged between the client and server.",
    "bandwidth": "The maximum rate of data transfer across a network path, usually measured in bits per second (bps), kilobits per second (kbps), or megabits per second (Mbps).",
    "latency": "The time it takes for a data packet to travel from the source to the destination across a network. It is typically measured in milliseconds (ms).",
    "OSI model": "Open Systems Interconnection model - A conceptual framework that standardizes the functions of a telecommunication or computing system into seven abstraction layers.",
    "MAC address": "Media Access Control address - A unique identifier assigned to network interfaces for communications on the physical network segment.",
    "LAN cable": "A physical cable used to connect devices within a local area network (LAN) for data transmission. Common types include Ethernet cables (e.g., Cat5e, Cat6).",
    "Wi-Fi": "A wireless networking technology that uses radio waves to provide high-speed internet and network connections to devices within a limited range.",
    "Ethernet": "A widely used networking protocol for wired local area networks (LANs). It defines how data is transmitted over copper wires, optical fibers, or wireless connections.",
    "ISP": "Internet Service Provider - A company that provides access to the Internet and related services such as web hosting, email hosting, and domain registration."
}


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 3000)
print('Starting server on {}:{}'.format(*server_address))
server_socket.bind(server_address)

server_socket.listen(10)

while True:
    
    print('Waiting for a connection...')
    connection, client_address = server_socket.accept()

    print('Client connected:', client_address)

    data = connection.recv(1024)
    if data:
        keyword = data.decode().strip()
        print('Received from client:', keyword)

        if keyword in dictionary:
            description = dictionary[keyword]
            connection.sendall(description.encode() + b'\r\n')
        else:
            connection.sendall(b'Description not found!\r\n')
    else:
        print('No more data from client')
        break

    connection.close()
