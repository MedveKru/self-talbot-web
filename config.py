# --------------------------
# Static for user values

plt_x_size = 150            # height of a plot
start_x_axic = plt_x_size   # height of a picture on a plot
# Should be the same size as plt_x_size

start_z_axic = 0
end_z_axic = 10_000
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
wavelength = 0.6238          # virtually wave's length
period = 40                  # period of a grid
phase_shift = 0

picture_name = 'output.png'  # result picture's name