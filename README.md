# 3D-Reconstruction-with-Structured-Light
This repo is to illustrate how a simple camera can obtain the depth of the scene with structured light with so called active triangulation method. In most of the cases, camera and the laser pointer are built together. Here, I demonstrate the case when the laser pointer is not aligned with the camera.

![alt text](assets/structured_light.png?raw=true)

The laser pointer location is known with respect to the camera location. The laser pointer is located `z` distance from the camera and `b` distance to the right of the camera. In addition to `z` and `b` parameters, camera focal length `f` and `x` coordinate in image pixel should be stated.

We have two equations with two unknowns X and Z coordinates of point P:
```
1) x/f = X/Z (perspective projection equation -  projection of a scene point onto the image plane)
2) tan(θ) = (Z - z) / b + X
   cot(θ) = b + X / (Z - z)
```

Solve for X and Z:

Replace X value in the second equation with X value in the first equation and find Z:
```
cot(θ)(Z - z) = b + x*f/Z
Z*f*cot(θ) - cot(θ)*z*f - b*f - x*Z = 0     
Z(cot(θ)*f - x) = cot(θ)*z*f + bf
Z = [cot(θ)*z*f + bf] / [cot(θ)*f - x]
```

You can get the Z value by calling `main.py` script:
```
usage: main.py [-h] z b f theta x

Find the depth to the point in the scene

positional arguments:
  z           distance from camera to the laser pointer by Z-axis
  b           distance from camera to the laser pointer by X-axis
  f           camera focal length
  theta       angle of the laser pointer
  x           x coordinate of P in the image buffer
```
```
python main.py z b f theta x
```
