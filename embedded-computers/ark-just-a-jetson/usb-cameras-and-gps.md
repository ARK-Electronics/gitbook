# USB Cameras and GPS

USB cameras pose a unique challenge on drone platforms due to electromagnetic interference (EMI). USB 3.0 signaling is a well-documented source of GPS interference, emitting broadband EMI that overlaps with GPS frequencies across the L1, L2, and L5 bands. This interference can significantly elevate the noise floor, effectively burying the weak GPS signals and degrading or completely preventing GPS lock.

#### Mitigation Strategy

Ensuring your camera uses USB 2.0 signalling is one method to eliminate interference. If USB 2.0 is not an option you may need to use faraday tape to shield your cables and connectors.

Before flight testing, verify that USB EMI impact is minimal:

1. **Measure the interference**: Use a GPS receiver with spectrum monitoring capability or a spectrum analyzer to observe the noise floor across GPS bands with the USB camera active.
2. **Apply shielding if needed**: If EMI is severe, wrap the entire USB cable, connectors, and any exposed portions in faraday/EMI shielding tape.
3. **Verify effectiveness**: Re-measure to confirm the noise floor returns to acceptable levels.

Checkout this X post from Alex Klimaj \
[https://x.com/ArkElectron/status/1752197126120189962](https://x.com/ArkElectron/status/1752197126120189962)
