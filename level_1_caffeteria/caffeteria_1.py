from typing import List
# Write any import statements here

def freeIslands(Space: int, Seats: List[int], Occupied: List[int], Islands: List[int]) -> List[List[int]]:
  #print("Seats: ", Seats, ", Occupied: ", Occupied, ", Islands: ", Islands)
  if len(Occupied) == 0:
    return Islands + [Seats]

  occupantIndex = Seats.index(Occupied[0])
  leftIslandEnd = max(0, occupantIndex - Space)
  rightIslandStart = min(len(Seats), occupantIndex + Space + 1)
  leftIsland = Seats[0:leftIslandEnd]
  rightIsland = Seats[rightIslandStart:len(Seats)]
  #print("Occ i: ", occupantIndex,
  #      ", L end: ", leftIslandEnd,
  #      ", L isl: ", leftIsland,
  #      ", R start: ", rightIslandStart,
  #      ", R isl: ", rightIsland)
  if len(leftIsland) > 0:
    newIslands = [leftIsland]
  else:
    newIslands = []
  return freeIslands(Space, rightIsland, Occupied[1:], Islands + newIslands)

def numFree(Space: int, Islands: List[int], NumSeats) -> int:
  #print("Space: ", Space, ", Islands: ", Islands)
  if len(Islands) == 0:
    return NumSeats

  island = Islands[0]
  if len(island) == 0:
    return numFree(Space, Islands[1:], NumSeats)

  NumSeats += 1
  remainingIsland = island[Space + 1:]

  if len(remainingIsland) > 0:
    remainingIslands = [remainingIsland] + Islands[1:]
  else:
    remainingIslands = Islands[1:]

  return numFree(Space, remainingIslands, NumSeats)

# Cannot change this line
#############################################################################
def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
#############################################################################

  # Write your code here
  numSeats = N
  if numSeats == 0:
    return 0
  seats = [i for i in range(1, numSeats + 1)]
  occupied = S
  list.sort(occupied)
  minFreeSeats = K
  freeIslands_ = freeIslands(minFreeSeats, seats, occupied, [])
  numFree_ = numFree(minFreeSeats, freeIslands_, 0)
  return numFree_
