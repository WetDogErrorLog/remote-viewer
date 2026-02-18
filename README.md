# remote-viewer

### Overview
Framework:
- BE: Flask
- FE: simple html

#### Main/Home
- List all available hosts and their cameras, based on a local config
- Display if each of those is 'awake' (and maybe the last time it was up?)
- upon selection, display the camera using the adapter specified in config (all impl of same interface, but available features will need to depend on the selected camera)

#### Config
##### List: Camera
- name
- features/settings
- 

#### Test Enviornment
For a test enviornment I could set up a network of docker clusters and flip around between them as targets. This will help build the foundations for some future projects, while also preventing me from needing to load the scripts onto pi's to test them. (long term testing could add latency or flakeyness)
