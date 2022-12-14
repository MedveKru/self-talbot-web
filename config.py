# --------------------------
# Static for user values

plt_x_size = 150            # height of a plot
start_x_axis = plt_x_size   # height of a picture on a plot
# Should be the same size as plt_x_size

start_z_axis = 0
end_z_axis = 10_000
# Weight of a picture on a plot

picture_resolution_x = 7
picture_resolution_y = 5
dpi = 125
# Some kostili for rcParams

plot_resolution_x = int((picture_resolution_x * dpi) / 2) * 2
plot_resolution_y = int((picture_resolution_y * dpi) / 2) * 2
# Same for x and z axes

# --------------------------
# Modifying for user values
wavelength = 10               # virtually wave's length (0 - 1000)
period = 40                  # period of a grid (1 - 100)
phase_shift = 0  # (0 - 1000)
show_z_talbot = True
z_indent = 50                  # for front image: how many MK go through Z axis to get cut (0 - 1000)

image_folder = 'static/'
picture_name = 'output.png'              # result picture's name
picture_front_name = 'front_output.png'  # result picture's name
