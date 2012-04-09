#!/usr/bin/env python
import freenect
import cv
import frame_convert
import sys

cv.NamedWindow('Depth')
cv.NamedWindow('Video')
print('Press any key in window to stop')

#print dir( freenect )
#print find_depth_mode(freenect_resolution res, freenect_depth_format fmt);
#freenect.set_video_mode( freenect.RESOLUTION_HIGH, freenect.VIDEO_RGB );
#sys.exit( 0 )

def grayscale_cv(depth):

    image = cv.CreateImageHeader((depth.shape[1], depth.shape[0]),
                                 cv.IPL_DEPTH_8U,
                                 1)
    cv.SetData(image, depth.tostring(),
               depth.dtype.itemsize * depth.shape[1])
    return image

def get_depth():
    return frame_convert.pretty_depth_cv(freenect.sync_get_depth()[0])


def get_video():
    return grayscale_cv(freenect.sync_get_video(index=0, format=freenect.VIDEO_IR_8BIT)[0])


while 1:
    #cv.ShowImage('Depth', get_depth())
    cv.ShowImage('Video', get_video())
    if cv.WaitKey(10) != -1:
        break
