from diffractio import plt, np, um, mm
from diffractio.scalar_masks_X import Scalar_mask_X
from diffractio.scalar_sources_X import Scalar_source_X
from diffractio.scalar_fields_XZ import Scalar_field_XZ

from matplotlib import rcParams

import config

# um - standard diffractio units (not necessary)
# mm = 1000 * um

rcParams['figure.figsize'] = (config.picture_resolution_x, config.picture_resolution_y)
rcParams['figure.dpi'] = config.dpi

wavelength = config.wavelength
z_talbot = 2 * config.period ** 2 / wavelength
config.end_z_axic = int((z_talbot * 1.6 + 99) / 100) * 100  # pushing z axis to have enough space to picture z_talbot

x = np.linspace(config.start_x_axic, -config.start_x_axic, config.plot_resolution_x)
z = np.linspace(config.start_z_axic, config.end_z_axic, config.plot_resolution_y)

u0 = Scalar_source_X(x, wavelength)
u0.plane_wave(A=1)

t = Scalar_mask_X(x, wavelength)
t.ronchi_grating(x0=config.phase_shift, period=config.period, fill_factor=0.5)

talbot_effect = Scalar_field_XZ(x, z, wavelength)
talbot_effect.incident_field(u0 * t)
talbot_effect.BPM()

talbot_effect.draw(kind='intensity')
plt.title('Эффект Тальбота')
plt.xlabel("X (мк)")
plt.ylabel("Y (мк)")
plt.ylim(-config.plt_x_size, config.plt_x_size)  # in basic world Y axis goes up
# but here X axis go up and Z axis go right, so here can be misunderstanding

# Adding to plot a line and a text to show where is Talbot's length
if config.show_z_talbot:
    plt.axline((z_talbot, -config.plt_x_size), (z_talbot, config.plt_x_size), linestyle='--', color='w', marker='o')
    plt.annotate('длина Тальбота', color='w',
                 xytext=(z_talbot * 1.1, -config.plt_x_size * 0.8),
                 xy=(z_talbot, -config.plt_x_size * 0.95),
                 arrowprops=dict(arrowstyle="->", connectionstyle="angle3", color='w'),
                 )

plt.savefig(config.picture_name)
