import time
from plyer import notification 
import random


formulas = [
    "angular_velocity = omega = Delta_theta / Delta_t",
    "linear_velocity = v = r * omega",
    "centripetal_acceleration = a_c = v**2 / r",
    "centripetal_force = F_c = m * a_c",
    "period = T = 2 * pi / omega",
    "frequency = f = 1 / T",
    "angular_momentum = L = I * omega",
    "kinetic_energy_rotational = KE_r = 0.5 * I * omega**2"
    "sin(3x) = 3sin(x) - 4sin^3(x)",
    "cos(3x) = 4cos^3(x) - 3cos(x)",
    "tan(3x) = (3tan(x) - tan^3(x)) / (1 - 3tan^2(x))",
    "sin(2x) = 2sin(x)cos(x) = 2tan(x) / (1 + tan^2(x))",
    "cos(2x) = cos^2(x) - sin^2(x) = (1 - tan^2(x)) / (1 + tan^2(x)) = 2cos^2(x) - 1 = 1 - 2sin^2(x)",
    "tan(2x) = 2tan(x) / (1 - tan^2(x))",
    "sec(2x) = sec^2(x) / (2 - sec^2(x))",
    "cosec(2x) = (sec(x)cosec(x)) / 2",
    "sin(x + y) = sin(x)cos(y) + cos(x)sin(y)",
    "cos(x + y) = cos(x)cos(y) - sin(x)sin(y)",
    "tan(x + y) = (tan(x) + tan(y)) / (1 - tan(x)tan(y))",
    "sin(x - y) = sin(x)cos(y) - cos(x)sin(y)",
    "cos(x - y) = cos(x)cos(y) + sin(x)sin(y)",
    "tan(x - y) = (tan(x) - tan(y)) / (1 + tan(x)tan(y))",
    "sin(90° - x) = cos(x)",
    "cos(90° - x) = sin(x)",
    "tan(90° - x) = cot(x)",
    "cot(90° - x) = tan(x)",
    "sec(90° - x) = cosec(x)",
    "cosec(90° - x) = sec(x)"
]


while True:
    a = random.choice(formulas)
    notification.notify(title="formula",message=a,timeout=5)
    time.sleep(300)


