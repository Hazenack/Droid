# "c:/Users/hazen/OneDrive/Code/Python/Droid solution - winc.py"
class droid():
  pass

C3PO = droid()
R2D2 = droid()
IG88 = droid()

def comparing_droids(droid1, droid2):
    if droid1 == droid2:
      print("Here they are! Don't move, rebel scum!")
    else:  
      print("These are not the droids we are looking for.")
      
comparing_droids(C3PO, R2D2)
comparing_droids(R2D2, R2D2)