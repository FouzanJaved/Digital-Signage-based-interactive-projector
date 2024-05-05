# Method to run kinect on processing. We have xbox 360 kinect so it is v1 kinect.

# What we have to do is after top method of kinect sdk install we have to install kinect developers toolkit.

# Then we have to do the following process:-

# Download/run Zadig and click under Options > List all devices
# In the main selection box, select XBox NUI Camera, then in the box where it says USB Serial CDC, click the down arrow until it pulls up libusbK (v3.0.7.0)
# Click Replace Driver

# Here is the code for processing:-

import org.openkinect.processing.*;

Kinect kinect;

void setup()
{
   size(640,480);
   kinect = new Kinect(this);

   kinect.initDepth();
   //kinect.initDevice();
}

void draw()
{
   background(0);
   PImage img = kinect.getDepthImage();
   image(img, 0, 0);
}
