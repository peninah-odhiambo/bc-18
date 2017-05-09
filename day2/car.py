class Car (object):
  

  def __init__ (self, name = None, model = None, vehicle_type = None):

    self.name = name
    self.model = model
    self.vehicle_type = vehicle_type
    self.speed = 0


    if self.name is None:
      return "General"
    else:
      return self.name

    if self.model is None:
      return "GM" 
    else:
      return self.model


    if self.name is 'Porshe'or 'Koenigsegg':
      self.num_of_doors = 2
    else:
      self.num_of_doors = 4

    if self.vehicle_type is 'Trailer':
      self.num_of_wheels = 8
    else:
      self.num_of_wheels = 4


  def is_saloon(self):
    if self.vehicle_type == saloon:
      return True
    elif self.vehicle_type != saloon:
      return "Trailer"
    else:
      return False

  def drive(self, moving_speed):
    if moving_speed == 3:
      self.speed = 1000
      
    elif moving_speed == 7:
      self.speed = 77

    return self