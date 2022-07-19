#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <gpio/gpio.h>
#include <stdbool.h>

#ifdef __arm__
#include <bsp/bsp.h>
#endif

#define GPIO_PIN_NUM_IN1 12U
#define GPIO_PIN_NUM_IN2 13U
#define GPIO_PIN_NUM_ENA 6U
#define GPIO_PIN_NUM_IN4 20U
#define GPIO_PIN_NUM_IN3 21U
#define GPIO_PIN_NUM_ENB 26U
#define DELAY_S 2

#define HIGH 1
#define LOW 0

void back(GpioHandle* handle){
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
    GpioOut(*handle, GPIO_PIN_NUM_IN1, LOW);
    GpioOut(*handle, GPIO_PIN_NUM_IN2, HIGH);
    GpioOut(*handle, GPIO_PIN_NUM_IN3, LOW);
    GpioOut(*handle, GPIO_PIN_NUM_IN4, HIGH);
    GpioOut(*handle, GPIO_PIN_NUM_ENA, HIGH);
    GpioOut(*handle, GPIO_PIN_NUM_ENB, HIGH);

}

void left(GpioHandle* handle) {
    GpioOut(*handle, GPIO_PIN_NUM_IN1, LOW);
    GpioOut(*handle, GPIO_PIN_NUM_IN2, LOW);
    GpioOut(*handle, GPIO_PIN_NUM_IN3, HIGH);
    GpioOut(*handle, GPIO_PIN_NUM_IN4, LOW);
    GpioOut(*handle, GPIO_PIN_NUM_ENA, HIGH);
    GpioOut(*handle, GPIO_PIN_NUM_ENB, HIGH);
}

void right(GpioHandle* handle) {
    GpioOut(*handle, GPIO_PIN_NUM_IN1, HIGH);
    GpioOut(*handle, GPIO_PIN_NUM_IN2, LOW);
    GpioOut(*handle, GPIO_PIN_NUM_IN3, LOW);
    GpioOut(*handle, GPIO_PIN_NUM_IN4, LOW);
    GpioOut(*handle, GPIO_PIN_NUM_ENA, HIGH);
    GpioOut(*handle, GPIO_PIN_NUM_ENB, HIGH);
}

int main(int argc, const char *argv[])
{
    fprintf(stderr, "Start GPIO_output test\n");

#ifdef __arm__
    /*
      InitializeGPIO_PIN_NUM board support package (BSP) driver and set configuration
      for GPIO pins. It`s required for stdout by UART.
     */
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

    /* initialize and setup gpio0 port */
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


    forward(handle);
    sleep(3);
    usleep(300000);

    right(handle);
    usleep(500000);

    forward(handle);
    sleep(1);

    right(handle);
    usleep(550000);

    forward(handle);
    sleep(3);
    usleep(300000);

    right(handle);
    usleep(500000);

    forward(handle);
    sleep(1);

    stop(handle);

    if(GpioClosePort(handle))
    {
        fprintf(stderr, "GpioClosePort failed\n");
        return EXIT_FAILURE;
    }

    fprintf(stderr, "Test finished.\n");

    return EXIT_SUCCESS;
}
