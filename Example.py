import cv2
import sys
## Import AndroidCamFeed module
from AndroidCamFeed import AndroidCamFeed

def main():
    if not sys.argv[1] or len(sys.argv) > 2:
        print "Usage: \n\tpython Example.py <host>:<port>"
        return

    ## Set host
    host = sys.argv[1]
    cv2.namedWindow('feed', cv2.WINDOW_NORMAL)

    ## Create new AndroidCamFeed instance
    acf = AndroidCamFeed(host)

    ## While camera is open
    while acf.isOpened():
        ## Read frame
        ret, frame = acf.read()
        if ret:
            cv2.imshow('feed', frame)
        if cv2.waitKey(1) == ord('q'):
            break

    ## Must Release ACF instance
    acf.release()
    cv2.destroyAllWindows()
    return

if __name__ == '__main__':
    main()
