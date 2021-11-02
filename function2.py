import random

coords_1 - coords_0 - data_coordinates[i][1]

c.execute('Select Entity_ID, Size FROM Entities) Select(Entity_2 FROM Relationships_1_1 Where Sub_Relationship! = Branches')
data_coordinates = c.fetchall()

coord_1 = coord_0 - data_coordinates[i][1]

for i in range(0, len(data_coordinates)

    def initial_vertical_positions(data: list[str, int], axis_y_length=100) -> list[str, int, int]:
        data_coordinates = list()  # will contain the pair of entity and coordinates

    filled = 0  # will represent the filled amount in the y-axis, it is used to know where to put the next entity

for entity, size in data:
    coords_0 = axis_y_length - filled  # calculate the starting point
    coords_1 = coords_0 - size  # calculate the ending point
    filled += size + 1  # update the filled size
    data_coordinates.append((entity, coords_0, coords_1))
    return data_coordinates

if __name__ == '__main__':
    data = [(f'Entity-{x + 1}', random.randint(1, 10)) for x in range(10)]  # create test data
data_coordinates = initial_vertical_positions(data)  # get coordinates of each entity
print(data)
print(data_coordinates)
