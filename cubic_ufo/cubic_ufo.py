import numpy as np

# return list of 3 Points of the centres of three non-pairwise-opposing faces
# when the cube is rotated to cast a shadow of given area
def get_face_points_for_shadow_area(area):
  # Set 1: 1 <= area <= 1.414213 (i.e. 1 <= area <= sqrt(2)). Can achieve by rotation about 1 axis.
  # Set 2: 1 <= area <= 1.732050 (i.e. 1 <= area <= sqrt(3)). Can achieve by rotation about 2 axes.

  # If we fall within bounds for Set 1, then we can just rotate in a fixed axis.
  # Let's rotate by theta about x axis.
  #         y
  #         |
  #       ______
  #      / p2  /|
  #     /_____/ |
  # z-p3| p1  | /
  #     |_____|/
  #       /
  #       x
  #
  # If we are in Set 2, then rotate by pi/4 around x axis, then rotate by theta about z axis.

  p1 = np.array([0.5, 0, 0])
  p2 = np.array([0, 0.5, 0])
  p3 = np.array([0, 0, 0.5])

  if area <= 1.414213:
    # Set 1:
    #
    #  area = 1 * (cos(theta) + sin(theta))
    #       = sqrt(2) * sin(theta + pi/4) [equate above with R * sin(theta + alpha) to work this out)
    #         [note max area is sqrt(2), i.e. max of Set 1]
    # theta = asin(area / sqrt(2)) - pi/4
    theta = np.arcsin(area / np.sqrt(2)) - (np.pi/4)

    # Calculate new points by using a x rotation matrix.
    c = np.cos(theta)
    s = np.sin(theta)
    rotx = np.array([[1, 0, 0], [0, c, s], [0, -s, c]])

    p1 = rotx.dot(p1)
    p2 = rotx.dot(p2)
    p3 = rotx.dot(p3)

  else:
    # Set 2:
    #
    #  area = sqrt(2) * cos(theta) + sin(theta) [draw a picture to work this out]
    #       = sqrt(3) * sin(theta + acos(1/sqrt(3)) [equate above with R * sin(theta + alpha) to work this out)
    #         [note max area is sqrt(3), i.e. max of Set 2]
    # theta = asin(area / sqrt(3)) - acos(1/sqrt(3))
    theta = np.arcsin(area / np.sqrt(3)) - np.arccos(1/np.sqrt(3))

    # Calculate new points.
    # First, rotate pi/4 about x axis.
    c = 1/np.sqrt(2)
    s = 1/np.sqrt(2)
    rotx = np.array([[1, 0, 0], [0, c, s], [0, -s, c]])

    # Then, rotate by theta about z axis.
    c = np.cos(theta)
    s = np.sin(theta)
    rotz = np.array([[c, s, 0], [-s, c, 0], [0, 0, 1]])

    p1 = rotz.dot(rotx).dot(p1)
    p2 = rotz.dot(rotx).dot(p2)
    p3 = rotz.dot(rotx).dot(p3)

  return [p1, p2, p3]

num_tests = int(input())
for i in range(1, num_tests+1):
  area = np.float64(input())
  face_centres = get_face_points_for_shadow_area(area)
  print("Case #{:d}:".format(i))
  for point in face_centres:
    print("{:.16f} {:.16f} {:.16f}".format(point[0], point[1], point[2]))
