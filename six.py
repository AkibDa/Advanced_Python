def myfunction(myparameter: int) -> str:
  return f"The parameter is: {myparameter}"
  
def otherfunction(otherparameter: str) -> int:
  return len(otherparameter)
  
myfunction("Hello") # This will raise a type warning in static type checkers

def dosth(param: list[int]) -> None:
  for item in param:
    print(item)
    
dosth([1, 2, 3, 4])