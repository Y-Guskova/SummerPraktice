#include <cstring>
#include <exception>
#include <iostream>
#include <memory>

#include <kos_net.h>

#include "general.h"
#include "publisher.h"

namespace consts {
constexpr int DefaultMqttUnencryptedPort = 1883;
constexpr int PublicationIntervalInSec = 5;
} // namespace consts

int main(int argc, char *argv[])
{
    if (!wait_for_network())
    {
        std::cerr << app::AppTag << "Error: Wait for network failed!"
                  << std::endl;
        return EXIT_FAILURE;
    }

    mosqpp::lib_init();

    const std::string brokerAddress = getenv("MQTT_BROKER_ADDRESS");
    const int brokerPort = []() -> int {
        try
        {
            return std::stoi(getenv("MQTT_BROKER_PORT"));
        }
        catch (const std::invalid_argument &ex)
        {
            std::cerr
                << app::AppTag
                << "Failed to get MQTT broker port. Using default 1883 port."
                << std::endl;
            return consts::DefaultMqttUnencryptedPort;
        }
    }();

    std::unique_ptr<Publisher> pub(
        new Publisher("publisher", brokerAddress.c_str(), brokerPort));

    while (true)
    {
        sleep(consts::PublicationIntervalInSec);
        pub->send_time();
    }

    mosqpp::lib_cleanup();
    return EXIT_SUCCESS;
}