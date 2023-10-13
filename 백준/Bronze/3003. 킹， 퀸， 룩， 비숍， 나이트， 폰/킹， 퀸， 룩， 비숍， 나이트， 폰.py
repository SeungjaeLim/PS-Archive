king, queen, rook, bishop, knight, phone = map(int, input().split())
king = 1 - king
queen = 1 - queen
rook = 2 - rook
bishop = 2 - bishop
knight = 2 - knight
phone = 8 - phone
print(king, queen, rook, bishop, knight, phone)