# IMX93-GW8016 Document screenshot description

This directory is used to store screenshot files required in the IMX93-GW8016 product documentation.

## Required screenshot list

### Gateway login related
- `gateway-login.png` - Gateway login page, showing username and password input boxes
- `lan-connection.png` - Diagram of connecting the gateway via LAN
- `wifi-hotspot-connection.png` - WiFi hotspot connection interface (displays the hotspot name in WiFi-10_XXXXXX format)
- `wan-remote-access.png` - Schematic diagram of accessing the gateway through WAN port IP

### WAN port static IP configuration
- `network-interfaces-list.png` - Network->Interfaces page, showing multiple network interface lists of the gateway
- `edit-wan-interface.png` - WAN port interface editing page
- `change-to-static-ip.png` - drop-down selection box to change the WAN port from DHCP to static IP
- `static-ip-configuration.png` - Static IP configuration interface, showing IP address, subnet mask, gateway, and DNS configuration
- `save-and-apply.png` - Save and apply configuration button
- `verify-network-config.png` - Network status confirmation page after the configuration takes effect

### LoRa communication method configuration
- `udp-gwmp-config.png` - UDP GWMP protocol configuration page, showing server address and port
- `mqtt-forwarder-config.png` - Configuration page for MQTT connection to external NS
- `chirpstack-mqtt-forwarder-config.png` - chirpstack-mqtt-forwarder protocol configuration
- `lns-protocol-config.png` - LNS protocol configuration page (connected to chirpstack/helium)
- `cups-protocol-config.png` - CUPS protocol configuration page (connect to AWS)

### Built-in NS data forwarding configuration
- `builtin-ns-mqtt-push-config.png` - MQTT push configuration for built-in NS
- `builtin-ns-mqtt-subscribe-config.png` - Built-in NS MQTT subscription configuration
- `builtin-ns-http-push-config.png` - HTTP push configuration for built-in NS
- `builtin-ns-modbus-tcp-config.png` - Modbus TCP configuration for built-in NS
- `builtin-ns-bacnet-config.png` - BACnet BIP configuration for built-in NS

### Chirpstack Device Management
- `chirpstack-login.png` - Chirpstack login page
- `add-device-profile.png` - Create device profile page
- `device-profile-general.png` - Basic information of device profile
- `device-profile-join.png` - device configuration file network access parameters
- `device-profile-codec.png` - Device profile codec configuration
- `enter-application.png` - Enter the application page
- `add-device-button.png` - Add device button
- `device-basic-info.png` - Device basic information configuration
- `device-otaa-keys.png` - Device OTAA key configuration

### TSL object model configuration
- `tsl-model-tab.png` - TSL object model tab page
- `add-tsl-property.png` - Add TSL property interface
- `tsl-property-list.png` - TSL property list

### Modbus and BACnet configuration
- `device-modbus-tcp-config.png` - Device Modbus TCP configuration (port and Slave ID)
- `device-bacnet-config.png` - Device BACnet configuration (device object ID)

### View device data
- `device-status.png` - Device status page
- `device-data.png` - device data display page
- `lorawan-frames.png` - LoRaWAN frame data viewing page
- `device-events.png` - Device event log

## Screenshot requirements

1. **Resolution**: 1920x1080 or higher resolution recommended
2. **Format**: PNG format, ensuring clarity
3. **Content**: Ensure that interface elements are clearly visible and important configuration items are highlighted.
4. **Language**: Chinese interface screenshot
5. **Privacy**: Hide or obscure sensitive information (such as real IP address, device ID, etc.), you can use sample data

## Snipping tool suggestions

- Windows: Snipping Tool, Greenshot
- macOS: Command+Shift+4
- Linux: GNOME Screenshot, Flameshot

## Notes

- All screenshot file names must be exactly the same as those cited in the document
- Screenshots should accurately reflect the current software version (openwrt-24.10, chirpstack V4.15)
- For complex configurations, arrows or labels can be added to illustrate key configuration items