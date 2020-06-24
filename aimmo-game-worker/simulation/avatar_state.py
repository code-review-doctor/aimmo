from simulation.location import Location


class BasicAvatarState(object):
    def __init__(self, location, health, score, id, orientation):
        self.location = Location(**location)
        self.health = health
        self.score = score
        self.id = id
        self.orientation = orientation


class Worksheet2AvatarState(BasicAvatarState):
    def __init__(self, location, health, score, id, orientation, backpack):
        super().__init__(location, health, score, id, orientation)

        self.backpack = backpack


def avatar_state_factory(worksheet_id, location, player):
    if worksheet_id == 1:
        return BasicAvatarState(
            {"x": location.x, "y": location.y},
            player["health"],
            player["score"],
            player["id"],
            player["orientation"],
        )
    elif worksheet_id == 2:
        return Worksheet2AvatarState(
            {"x": location.x, "y": location.y},
            player["health"],
            player["score"],
            player["id"],
            player["orientation"],
            player["backpack"],
        )
    else:
        raise Exception("Worksheet not recognised.")
