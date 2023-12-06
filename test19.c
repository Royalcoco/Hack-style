#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>

// Function to convert string to int
int string_to_int(char* str) {
    int res = 0;
    while (*str) {
        res = res * 10 + (*str - '0');
        str++;
    }
    return res;
}

// Function to convert string to ip
unsigned int string_to_ip(char* str) {
    unsigned int ip = 0;
    char *token = strtok(str, ".");
    ip = string_to_int(token);
    ip = ip << 8;
    token = strtok(NULL, ".");
    ip += string_to_int(token);
    ip = ip << 8;
    token = strtok(NULL, ".");
    ip += string_to_int(token);
    ip = ip << 8;
    token = strtok(NULL, ".");
    ip += string_to_int(token);
    return ip;
}

// Function to convert string to port
unsigned short string_to_port(char* str) {
    unsigned short port = 0;
    char *token = strtok(str, ":");
    token = strtok(NULL, ":");
    port = string_to_int(token);
    return htons(port);
}

int main(int argc, char* argv[]) {
    int sockfd;
    struct sockaddr_in servaddr;
    char message[1000] = "Encrypted message goes here...";

    // Create socket
    sockfd = socket(AF_INET, SOCK_DGRAM, 0);
    if (sockfd < 0) {
        perror("socket creation failed");
        exit(EXIT_FAILURE);
    }

    memset(&servaddr, 0, sizeof(servaddr));
    servaddr.sin_family = AF_INET;
    servaddr.sin_port = string_to_port(argv[1]);
    servaddr.sin_addr.s_addr = string_to_ip(argv[2]);

    sendto(sockfd, message, strlen(message), 0, (const struct sockaddr *) &servaddr, sizeof(servaddr));
    close(sockfd);

    return 0;
}