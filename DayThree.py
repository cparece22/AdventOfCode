
grid = [None] * 10000
pathOne = [1997,4543,2529,4916,1855,4705,2159,3444,1234,3639,2178,4682,2836,3333,1571,4906,2583,3872,2733,3815,2484,4641,1649,3378,226,366,2659,427,14,3325,2264,4711,2837,4986,238,3623,2830,4369,2469,4704,2302,3143,2771,3170,1237,3477,2251,4100,1561,4889,1857,4780,1258,4299,2975,4481,2692,4894,1847,4416,1670,4658,2537,3748,1468,4304,2263,4884,1806,413,1288,3933,14,3291,2809,4242,1669,450,1106,4510,1409,3311,1101,4232,1370,4490,2762,4805,2981,4637,2987,3403,1965,3724,2404,4664,2687,3868,2808,4174,2363,4241,254,4238,1444,375,1683,3712,2759,4569,1349,4378,2576,3437,1137,4822,121,4595,2602,3147,1959,3350,1964,3625,2718,3331,2252,4386,2251,3371,1973,4709,1915,4837,27,3727,2501,4520,2626,3161,2287,4224,2821,3555,2312,3234,2335,4572,2113,3673,2615,4919,1925,316,1211,377,1630,3786,1850,4221,1939,3559,1887,3779,2222,4482,2252,4682,2904,3568,1317,4453,1689,4917,1845,3260,169,3613,1528,4447,2791,4119,2268,3215,2806,3786,1465,4787,2792,4823,1526,4709,2362,4748,2518,3115,2898,3784,1893,3911,198,3215,1828,4100,1153,3496,2938,4403,1886,4317,2849,459,1156,427,264,4771,1956,3880,1313,4244,2483,417,172,3467,2475,4444,1554,4781,1524,4152,2771,3435,2622,4601,1733,4478,2686,412,2525,4467,2302,4948,2966,3572,2303,3914,154,4417,1635,4425,1640,4703,117,4187,2195,359,1166,4616,2557,3458,2743,4166,1328,4640,1908,4775,2151,4216,2964,4202,2534,4239,1998,3167,2604,4812,2527,3526,2640,393,2733,4980,1607,4879,2593,4721,1454,3137,1683,4343,238,4398,281,3392,1821,3247,2361,4208,1763,4771,2515]

pathTwo = [21000,4189,2867,3824,2193,412,1704,383,1371,4858,2970,456,1877,4448,1962,3239,1641,4198,2840,4413,1586,4920,1650,3919,1375,4540,2150,3995,154,4200,161,4974,1249,3893,1319,3930,1658,3680,1286,4186,1963,3553,2256,3629,2554,3576,1887,3595,1629,4680,2684,3556,2302,3348,1825,4252,2684,3705,2258,472,1907,3702,2518,3440,1239,3258,1825,327,2580,4613,1357,4468,1519,3833,2415,4822,2798,3904,1812,376,186,3252,1427,3637,2896,3147,2294,3381,1306,3423,2688,4336,1648,3677,2750,4218,2649,4360,1710,464,1317,3232,1261,4167,249,4138,2431,4505,2535,3294,2553,3969,2144,3227,1437,4397,1359,3848,248,4992,1169,4580,2219,4525,1552,3546,1849,4722,1894,4735,2182,3570,1274,4349,1312,3430,1441,3183,1645,4308,2416,3333,2687,3202,2973,4736,1382,3260,2176,4207,1706,352,2142,4746,2328,4413,1879,4429,2679,4695,2224,4462,1358,4124,2515,4629,2873,4759,2763,328,1765,4426,293,3927,2395,3243,2393,4488,2729,3100,1488,483,147,392,2871,4410,1405,4993,1537,410,279,4218,2686,4563,231,3885,2784,4462,2160,3345,1204,3275,1162,3164,1843,4578,1255,4456,2398,3470,2576,4973,2337,4971,1205,3264,1707,3975,260,3270,11,3808,1844,4884,2952,4435,2144,4374,1389,4741,1404,4398,1282,4807,2316,3136,2504,3720,1859,4925,2711,3343,2535,4978,1578,3636,2447,4298,1574,3590,2142,4802,2846,4617,2838,3362,1812,3295,2328,3162,2617,4857,2759,4251,2343,3394,1721,3320,1836,3726,2950,4612,1129,3549,2970,487,2341,4269,2659,3550,1835,4318,2189,3278,1871,462,1703,3807,2389,3824,1521,4175,2698,3313,2942,4810,2498,318,1168,4111,1607]
# To Prevent having to make a string, at the start of each number, 1 wi11 be right, 2 wi11 be left, 3 wi11 be up, and 4 wi11 be down. 6 means end of line
#Idea: Use the first digit to tell direction. Right will move positive by 1, Left will be negative by 1, Up will be postive by 1000, left will be negative by 1000

def moveRight(line, grid, start= 0, distance):
    blocksNeeded = distance + 1
    gridUpdate = grid
    if start == 0:
        startPoint = grid.index(6)
    else:
        startPoint = start
    if line == 1:
        for path in range(startPoint,blocksNeeded):
            if gridUpdate[path] == 6:
                gridUpdate[path] = 1
            elif gridUpdate[path] == None:
                gridUpdate[path] = 1
            elif gridUpdate[path] == 1:
                gridUpdate[path] = 2
            elif path == blocksNeeded:
                gridUpdate[path] = 6

            else:
                print("error? at 16")
    elif line == 2:
        for path in range(startPoint,blocksNeeded):
            if gridUpdate[path] == 6:
                gridUpdate[path] = 1
            elif gridUpdate[path] == None:
                gridUpdate[path] = 1
            elif gridUpdate[path] == 1:
                gridUpdate[path] = 2
            elif path == blocksNeeded:
                gridUpdate[path] = 6
    return gridUpdate
def moveLeft(line, grid,start= 0, distance):
    blocksNeeded = distance * -1 - 1
    if start == 0:
        startPoint = grid.index(6)
    else:
        startPoint = start
    if line == 1:
        for path in range(startPoint,blocksNeeded):
            if grid[path] == 6:
                grid[path] = 1
            elif grid[path] == None:
                grid[path] = 1
            elif grid[path] == 1:
                grid[path] = 2
            elif path == blocksNeeded:
                grid[path] = 6
            else:
                print("error? at 16")

    elif line == 2:
        for path in range(startPoint,blocksNeeded):
            if grid[path] == 6:
                grid[path] = 1
            elif grid[path] == None:
                grid[path] = 1
            elif grid[path] == 1:
                grid[path] = 2
            elif path == blocksNeeded:
                grid[path] = 6

def moveUp(line, grid, start= 0, distance):
    blocksNeeded = distance * -1000 - 1
    if start == 0:
        startPoint = grid.index(6)
    else:
        startPoint = start
    if line == 1:
        for path in range(startPoint,blocksNeeded):
            if grid[path] == 6:
                grid[path] = 1
            elif grid[path] == None:
                grid[path] = 1
            elif grid[path] == 1:
                grid[path] = 2
            elif path == blocksNeeded:
                grid[path] = 6
            else:
                print("error? at 16")
    elif line == 2:
        for path in range(startPoint,blocksNeeded):
            if grid[path] == 6:
                grid[path] = 1
            elif grid[path] == None:
                grid[path] = 1
            elif grid[path] == 1:
                grid[path] = 2
            elif path == blocksNeeded:
                grid[path] = 6

def moveDown(line, grid, start= 0, distance):
    blocksNeeded = distance * 1000 + 1
    if start == 0:
        startPoint = grid.index(6)
    else:
        startPoint = start
    if line == 1:
        for path in range(startPoint,blocksNeeded):
            if grid[path] == 6:
                grid[path] = 1
            elif grid[path] == None:
                grid[path] = 1
            elif grid[path] == 1:
                grid[path] = 2
            elif path == blocksNeeded:
                grid[path] = 6
            else:
                print("error? at 16")
    elif line == 2:
        for path in range(startPoint,blocksNeeded):
            if grid[path] == 6:
                grid[path] = 1
            elif grid[path] == None:
                grid[path] = 1
            elif grid[path] == 1:
                grid[path] = 2
            elif path == blocksNeeded:
                grid[path] = 6

def wireOne(pathData):
    grid = [None] * 10000
    startPoint = 4999
    for move in pathData:
        moveString = str(move)
        fixedMove = moveString[1:]
        if move == pathData[0]:
            print("checking",move, pathData[0])
            if moveString[0] == 1:
                grid = moveRight(1, grid, startPoint, fixedMove)
            elif moveString[0] == 2:
                grid = moveLeft(1, grid, startPoint, fixedMove)
            elif moveString[0] == 3:
                grid = moveUp(1, grid, startPoint, fixedMove)
            elif moveString[0] == 4:
                grid = moveDown(1, grid, startPoint, fixedMove)
        else:
            if moveString[0] == 1:
                grid = moveRight(1, grid, fixedMove)
            elif moveString[0] == 2:
                grid = moveLeft(1, grid, fixedMove)
            elif moveString[0] == 3:
                grid = moveUp(1, grid, fixedMove)
            elif moveString[0] == 4:
                grid = moveDown(1, grid, fixedMove)
    return grid

def wireTwo(grid, pathData):




print(wireOne(pathOne))
