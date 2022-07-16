#include <stdio.h>
#include <stddef.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>

#include <stdlib.h>
//#include <gpio/gpio.h>
#include <stdbool.h>

#include <platform/platform.h>
#include <kos_net.h>

#ifdef __arm__
#include <bsp/bsp.h>
#endif

/*#define GPIO_PIN_NUM_IN1 12U
#define GPIO_PIN_NUM_IN2 13U
#define GPIO_PIN_NUM_ENA 6U
#define GPIO_PIN_NUM_IN4 20U
#define GPIO_PIN_NUM_IN3 21U
#define GPIO_PIN_NUM_ENB 26U
#define DELAY_S 2

#define HIGH 1
#define LOW 0


void back(GpioHandle* handle){
    fprintf(stderr, "forward\n");
     GpioOut(*handle, GPIO_PIN_NUM_IN1, HIGH);
    GpioOut(*handle, GPIO_PIN_NUM_IN2, LOW);
    GpioOut(*handle, GPIO_PIN_NUM_IN3, HIGH);
    GpioOut(*handle, GPIO_PIN_NUM_IN4, LOW);
    GpioOut(*handle, GPIO_PIN_NUM_ENA, HIGH);
    GpioOut(*handle, GPIO_PIN_NUM_ENB, HIGH);
}

void stop(GpioHandle* handle) {
    GpioOut(*handle, GPIO_PIN_NUM_IN1, LOW);
    GpioOut(*handle, GPIO_PIN_NUM_IN2, LOW);
    GpioOut(*handle, GPIO_PIN_NUM_IN3, LOW);
    GpioOut(*handle, GPIO_PIN_NUM_IN4, LOW);
    GpioOut(*handle, GPIO_PIN_NUM_ENA, LOW);
    GpioOut(*handle, GPIO_PIN_NUM_ENB, LOW);
}

void forward(GpioHandle* handle) {
    fprintf(stderr, "backward\n");
    GpioOut(*handle, GPIO_PIN_NUM_IN1, LOW);
    GpioOut(*handle, GPIO_PIN_NUM_IN2, HIGH);
    GpioOut(*handle, GPIO_PIN_NUM_IN3, LOW);
    GpioOut(*handle, GPIO_PIN_NUM_IN4, HIGH);
    GpioOut(*handle, GPIO_PIN_NUM_ENA, HIGH);
    GpioOut(*handle, GPIO_PIN_NUM_ENB, HIGH);

}

void left(GpioHandle* handle) {
    fprintf(stderr, "left\n");
    GpioOut(*handle, GPIO_PIN_NUM_IN1, LOW);
    GpioOut(*handle, GPIO_PIN_NUM_IN2, LOW);
    GpioOut(*handle, GPIO_PIN_NUM_IN3, HIGH);
    GpioOut(*handle, GPIO_PIN_NUM_IN4, LOW);
    GpioOut(*handle, GPIO_PIN_NUM_ENA, HIGH);
    GpioOut(*handle, GPIO_PIN_NUM_ENB, HIGH);
}

void right(GpioHandle* handle) {
     fprintf(stderr, "right\n");
    GpioOut(*handle, GPIO_PIN_NUM_IN1, HIGH);
    GpioOut(*handle, GPIO_PIN_NUM_IN2, LOW);
    GpioOut(*handle, GPIO_PIN_NUM_IN3, LOW);
    GpioOut(*handle, GPIO_PIN_NUM_IN4, LOW);
    GpioOut(*handle, GPIO_PIN_NUM_ENA, HIGH);
    GpioOut(*handle, GPIO_PIN_NUM_ENB, HIGH);
}

*/

int main() {
  /*
  printf(stderr, "Start GPIO_output test\n");

  #ifdef __arm__
    
    // * InitializeGPIO_PIN_NUM board support package (BSP) driver and set configuration
     //* for GPIO pins. It`s required for stdout by UART.
     
    {
        BspError rc = BspInit(NULL);
        if (rc != BSP_EOK)
        {
            fprintf(stderr, "Failed to initialize BSP\n");
            return EXIT_FAILURE;
        }

        rc = BspSetConfig("gpio0", "raspberry_pi4b.default");
        if (rc != BSP_EOK)
        {
            fprintf(stderr, "Failed to set mux configuration for gpio0 module\n");
            return EXIT_FAILURE;
        }
    }
  #endif

    if (GpioInit())
    {
        fprintf(stderr, "GpioInit failed\n");
        return EXIT_FAILURE;
    }

    // initialize and setup gpio0 port 
    GpioHandle handle = NULL;
    if (GpioOpenPort("gpio0", &handle) || handle == GPIO_INVALID_HANDLE)
    {
        fprintf(stderr, "GpioOpenPort failed\n");
        return EXIT_FAILURE;
    }

  GpioSetMode(handle, GPIO_PIN_NUM_IN1, GPIO_DIR_OUT);
  GpioSetMode(handle, GPIO_PIN_NUM_IN2, GPIO_DIR_OUT);
  GpioSetMode(handle, GPIO_PIN_NUM_IN3, GPIO_DIR_OUT);
  GpioSetMode(handle, GPIO_PIN_NUM_IN4, GPIO_DIR_OUT);
  GpioSetMode(handle, GPIO_PIN_NUM_ENA, GPIO_DIR_OUT);
  GpioSetMode(handle, GPIO_PIN_NUM_ENB, GPIO_DIR_OUT);
  */


  int sock, listener;
  struct sockaddr_in addr;
  char buf[1024];
  int bytes_read;

  printf("Start KOS server\n");
  perror(DEFAULT_INTERFACE "app point 0 \n");


#if PLATFORM_OS(KOS)
#define server_addr "10.0.2.2"
    /* Add network interface. */
    if (!configure_net_iface(DEFAULT_INTERFACE, "10.0.2.10", DEFAULT_MASK, DEFAULT_GATEWAY, DEFAULT_MTU)) {

        perror(DEFAULT_INTERFACE ": network iface configuration failed\n");
        return EXIT_FAILURE;
    }

    if (!list_network_ifaces()) {
        perror("listing of host network interfaces failes\n");
        return EXIT_FAILURE;
    }

#else
#define server_addr "localhost"
#endif

  listener = socket(AF_INET, SOCK_STREAM, 0);

  if(listener < 0) { perror("socket"); return 1;}
    addr.sin_family = AF_INET;
    addr.sin_port = htons(3425);
    addr.sin_addr.s_addr = htonl(INADDR_ANY);
    if(bind(listener, (struct sockaddr *)&addr, sizeof(addr)) < 0) {
      perror("bind"); 
      return 1;
    }
    listen(listener, 1);
    while(1) {
      sock = accept(listener, NULL, NULL);
      if(sock < 0) {
        perror("accept"); 
        return 1;
      }
      while(1) {
        bytes_read = recv(sock, buf, 1024, 0);
        if(bytes_read <= 0)
          break;
        printf("Receive message: %s\n", buf);
        /*if (buf=='forward')
        {
          forward(p_handle);
          sleep(2);
          stop(p_handle);
        }
        else
        {
          back(p_handle);
          sleep(2);
          stop(p_handle);
        }*/
      }
      close(sock);
   }
   close(listener);
}

