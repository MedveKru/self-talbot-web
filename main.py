from diffractio import plt, np, um, mm, degrees, num_max_processors
from diffractio.scalar_masks_X import Scalar_mask_X
from diffractio.scalar_masks_XZ import Scalar_mask_XZ
from diffractio.scalar_sources_X import Scalar_source_X
from diffractio.scalar_fields_XZ import Scalar_field_XZ

from diffractio.utils_multiprocessing import (_pickle_method, _unpickle_method,
                                              execute_multiprocessing)

from matplotlib import rcParams

rcParams['figure.figsize'] = (7, 5)
rcParams['figure.dpi'] = 125

x = np.linspace(-350 * um, 350 * um, 2048)
z = np.linspace(0 * um, 10 * mm, 512)
wavelength = 0.6238 * um
period = 40 * um
z_talbot = 2 * period ** 2 / wavelength

u0 = Scalar_source_X(x, wavelength)
u0.plane_wave(A=1)

t = Scalar_mask_X(x, wavelength)
t.ronchi_grating(x0=0 * um, period=40 * um, fill_factor=0.5)

talbot_effect = Scalar_field_XZ(x, z, wavelength)
talbot_effect.incident_field(u0 * t)
talbot_effect.BPM()

talbot_effect.draw(kind='intensity')
plt.ylim(-150 * um, 150 * um)

plt.savefig('aboba.png')
