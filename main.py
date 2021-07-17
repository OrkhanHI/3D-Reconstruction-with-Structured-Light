import argparse
import numpy as np

def main(args):
    ''' 
        Given z, b, f and theta: 
            With respect to the camera coordinate system:
                z - offset distance from camera to the laser pointer by Z-axis
                b - offset distance from camera to the laser pointer by X-axis
            f - focal length of the camera
            theta - setup angle of the laser pointer
            x - value of P point in the image buffer
        finds the depth to the point of the 3D object
    '''
    angle_to_radian = np.radians(args.theta)
    cot_theta = np.arctan(np.tan(angle_to_radian))
    
    Z = (cot_theta*args.z*args.f + args.b*args.f) / (cot_theta*args.f - args.x)
    return Z

if __name__ == "__main__":
    PARSER = argparse.ArgumentParser(description="Find the depth to the point in the scene")
    PARSER.add_argument("z", help="distance from camera to the laser pointer by Z-axis")
    PARSER.add_argument("b", help="distance from camera to the laser pointer by X-axis")
    PARSER.add_argument("f", help="camera focal length")
    PARSER.add_argument("theta", help="angle of the laser pointer")
    PARSER.add_argument("x", help="x coordinate of P in the image buffer")
    ARGS = PARSER.parse_args()
    main(ARGS)
