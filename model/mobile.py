class MobileModel:

    def __init__(self, mAh, clock_speed, dual_sim, frontal_camera,
                 gb_intern_memory, primary_camera, height, width, ram):
        self.mAh = mAh
        self.clock_speed = clock_speed
        self.dual_sim = dual_sim
        self.frontal_camera = frontal_camera
        self.gb_intern_memory = gb_intern_memory
        self.primary_camera = primary_camera
        self.height = height
        self.width = width
        self.ram = ram

    def set_mAh(self, mAh):
        self.mAh = mAh

    def set_clock_speed(self, clock_speed):
        self.clock_speed = clock_speed

    def set_dual_sim(self, dual_sim):
        self.dual_sim = dual_sim

    def set_frontal_camera(self, frontal_camera):
        self.frontal_camera = frontal_camera

    def set_intern_memory(self, gb_intern_memory):
        self.gb_intern_memory = gb_intern_memory

    def set_primary_camera(self, primary_camera):
        self.primary_camera = primary_camera

    def set_height(self, height):
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_ram(self, ram):
        self.ram = ram
