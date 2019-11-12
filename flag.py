import argparse
def flag(n):
  """
  Return japanese flag
    input:
      int n : diametr of circle
    output:
      string: flag str with \n
  """
  if n < 2 or n % 2 != 0:
    raise argparse.ArgumentError(None, message='Not valid')
  width_area = 3*n
  height_area = 2*n 
  vertical_distance = n/2
  horizontal_distance = n
  result_string = ''

  # Iterate through the entire height flag by 1 row
  for i in range(height_area + 2):

    # if 1 or lasе row fill with 
    if i == 0 or i == height_area + 1:
      result_string += '#'*(width_area+2) + '\n'

    # else we're inside the flag
    else:

      # if we in area where the circle should be
      if i > vertical_distance and i < (height_area - vertical_distance + 1):
        # temp str for store row value
        temp_str = '#'
  
        # define the distance from the center
        dif = 0
        if horizontal_distance >= i:
          dif = horizontal_distance - i
        else:
          dif = abs(horizontal_distance + 1 - i)
        
        # define len of circle and spacece in row 
        circle_len = horizontal_distance - 2*dif
        space_len = horizontal_distance + dif

        # fill temp str with spaces
        temp_str += ' '*space_len
        # fill temp str with circle if > 2 fill with o in center
        if circle_len > 2:
          temp_str += '*' + 'o'*(circle_len-2) + '*'
        else:
          temp_str += '*'*circle_len

        # fill temp str last spaces
        temp_str += ' '*space_len
        # add # and \n
        temp_str += '#\n'
        # append to result string
        result_string += temp_str

      # else fill with the blanks
      else:
        result_string += '#' + ' '*width_area + '#\n'

  return result_string