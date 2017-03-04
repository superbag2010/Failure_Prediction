from abc import ABC, abstractmethod
from eval_info import *

# abstract class to be used by machine learning class
class Model(ABC):
# db = Database()
# input_x = Dataframe()
# input_y = Dataframe()
  ev_inf = Eval_info() 

  @abstractmethod
  def __init__(self):
    pass

  @abstractmethod
  def create_model(self):
    pass
  
  @abstractmethod
  def restore(self):
    pass

  @abstractmethod
  def train(self):
    pass

  @abstractmethod
  def run(self):
    pass

  @abstractmethod
  def save(self):
    pass

  @abstractmethod
  def eval(self):
    pass