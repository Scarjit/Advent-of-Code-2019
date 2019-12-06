import time
import copy

import math


class Day_1:
    def __init__(self, module_mass_str):
        self.module_masses_str = module_mass_str
        self.module_masses = self.module_masses_str.split("\n")
        self.total_fuel = 0
        self.recursive_total_fuel = 0

    def get_fuel_from_mass(self, mass):
        if mass < 0:
            raise Exception("Wrong universe mass may never be negative")
        fuel = int(mass / 3) - 2
        return fuel

    def get_raw_total_fuel(self):
        self.total_fuel = 0
        for m_str in self.module_masses:
            self.total_fuel += self.get_fuel_from_mass(int(m_str))
        return self.total_fuel

    def get_recursive_total_fuel(self):
        self.recursive_total_fuel = 0
        for m_str in self.module_masses:
            self.recursive_total_fuel += self.get_recursive_fuel_from_mass(int(m_str))
        return self.recursive_total_fuel

    def get_recursive_fuel_from_mass(self, module_mass):
        raw_fuel_module = self.get_fuel_from_mass(module_mass)

        def recursive_fuel(mass):
            raw_fuel = int(mass / 3) - 2
            if raw_fuel <= 0:
                return 0
            fuel = raw_fuel + recursive_fuel(raw_fuel)
            return fuel

        return raw_fuel_module + recursive_fuel(raw_fuel_module)


def solve_day_1():
    spaceship = Day_1("129561\n"
                      "125433\n"
                      "97919\n"
                      "93037\n"
                      "73254\n"
                      "96511\n"
                      "115676\n"
                      "95032\n"
                      "69369\n"
                      "145385\n"
                      "111145\n"
                      "64368\n"
                      "83462\n"
                      "95765\n"
                      "133284\n"
                      "136563\n"
                      "67439\n"
                      "69311\n"
                      "147720\n"
                      "92632\n"
                      "142940\n"
                      "100610\n"
                      "106538\n"
                      "80025\n"
                      "121672\n"
                      "125386\n"
                      "126601\n"
                      "67943\n"
                      "120022\n"
                      "95914\n"
                      "132721\n"
                      "105831\n"
                      "138493\n"
                      "57649\n"
                      "72843\n"
                      "81754\n"
                      "103116\n"
                      "148993\n"
                      "139042\n"
                      "145929\n"
                      "61039\n"
                      "126034\n"
                      "74187\n"
                      "60750\n"
                      "99048\n"
                      "131776\n"
                      "123137\n"
                      "113098\n"
                      "107571\n"
                      "117050\n"
                      "108649\n"
                      "117455\n"
                      "147443\n"
                      "121863\n"
                      "104952\n"
                      "103465\n"
                      "128718\n"
                      "61795\n"
                      "121049\n"
                      "112010\n"
                      "74403\n"
                      "56153\n"
                      "136161\n"
                      "76872\n"
                      "94156\n"
                      "131477\n"
                      "91769\n"
                      "90744\n"
                      "118647\n"
                      "135791\n"
                      "98914\n"
                      "104988\n"
                      "62070\n"
                      "82308\n"
                      "71964\n"
                      "91477\n"
                      "63733\n"
                      "84412\n"
                      "127000\n"
                      "65449\n"
                      "67976\n"
                      "51400\n"
                      "56045\n"
                      "82951\n"
                      "101119\n"
                      "143015\n"
                      "99388\n"
                      "51796\n"
                      "93467\n"
                      "63220\n"
                      "124459\n"
                      "136330\n"
                      "130535\n"
                      "144270\n"
                      "88616\n"
                      "63626\n"
                      "139954\n"
                      "92191\n"
                      "117618\n"
                      "110422")

    print("total Fuel = ", spaceship.get_raw_total_fuel())

    print("total Fuel with recursive fuel = ", spaceship.get_recursive_total_fuel())


class Day_2:
    def __init__(self, codes):
        self.codes = codes
        self.initial_codes = copy.deepcopy(codes)

    def reset_codes(self):
        self.codes = copy.deepcopy(self.initial_codes)

    def execute_codes(self):

        def execute_from_position(position):
            operation = self.codes[position]

            if operation == 1:
                self.codes[self.codes[position + 3]] = self.codes[self.codes[position + 1]] + self.codes[
                    self.codes[position + 2]]
                return True, 4
            elif operation == 2:
                self.codes[self.codes[position + 3]] = self.codes[self.codes[position + 1]] * self.codes[
                    self.codes[position + 2]]
                return True, 4
            elif operation == 99:
                return False, 1
            else:
                print("can not execute ", self.codes[position], "at", position)
                raise Exception("Operation can not be executed")

        start_position = 0
        current_position = start_position
        while True:
            continue_execution, increment = execute_from_position(current_position)
            current_position += increment
            if not continue_execution:
                break


def solve_day_2():
    computer = Day_2(
        [1, 12, 2, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 1, 10, 19, 2, 6, 19, 23, 1, 23, 5, 27, 1, 27, 13, 31, 2, 6,
         31, 35, 1, 5, 35, 39, 1, 39, 10, 43, 2, 6, 43, 47, 1, 47, 5, 51, 1, 51, 9, 55, 2, 55, 6, 59, 1, 59, 10, 63, 2,
         63, 9, 67, 1, 67, 5, 71, 1, 71, 5, 75, 2, 75, 6, 79, 1, 5, 79, 83, 1, 10, 83, 87, 2, 13, 87, 91, 1, 10, 91, 95,
         2, 13, 95, 99, 1, 99, 9, 103, 1, 5, 103, 107, 1, 107, 10, 111, 1, 111, 5, 115, 1, 115, 6, 119, 1, 119, 10, 123,
         1, 123, 10, 127, 2, 127, 13, 131, 1, 13, 131, 135, 1, 135, 10, 139, 2, 139, 6, 143, 1, 143, 9, 147, 2, 147, 6,
         151, 1, 5, 151, 155, 1, 9, 155, 159, 2, 159, 6, 163, 1, 163, 2, 167, 1, 10, 167, 0, 99, 2, 14, 0, 0])
    result_found = False
    for noun in range(100):
        for verb in range(100):
            computer.reset_codes()
            computer.codes[1] = noun
            computer.codes[2] = verb
            try:
                computer.execute_codes()
                print("result = ", computer.codes[0], " for inputs ", noun, verb, "Answer = ", 100 * noun + verb)
                if computer.codes[0] == 19690720:
                    result_found = True
                    break
            except Exception as _e:
                if _e.args[0] == "Operation can not be executed":
                    pass
        if result_found:
            break


class Day_3:

    def __init__(self, route1, route2):
        self.route1 = route1.split(",")
        self.route2 = route2.split(",")
        self.grid = {}
        self.origin = (0, 0)
        self.intersections = []

    def add_route_to_grid(self, route, prime):
        def get_full_entry_direction(path_instruction):  # 0 achse = x achse. 1 achse = y achse
            return {"R": lambda v: (int(v), 0),
                    "L": lambda v: (-int(v), 0),
                    "U": lambda v: (0, int(v)),
                    "D": lambda v: (0, -int(v))}[path_instruction[0]](path_instruction[1:])

        current_position = list(copy.deepcopy(self.origin))
        current_step = 0

        def add_position_to_grid(position, identifier, c_step):
            line_step = copy.deepcopy(c_step)
            grid_step = copy.deepcopy(c_step)
            if position not in self.grid:
                self.grid[position] = identifier, grid_step
            else:  # line is in grid
                if self.grid[position][0] % identifier == 0:  # get's triggered when selfe intersection occurs
                    line_step = self.grid[position][1]
                    grid_step = self.grid[position][1]
                else:  # get's triggered when 2 different lines meet for the first time on any tile
                    grid_step = self.grid[position][1] + line_step
                self.grid[position] = self.grid[position][
                                          0] * identifier, grid_step  # TODO maybe Broken  for step length of self intersection
            return line_step

        for segment in route:
            s = list(get_full_entry_direction(segment))
            while s[0] != 0 or s[1] != 0:
                current_step += 1
                if s[0] != 0:
                    current_position[0] += int(s[0] / abs(s[0]))
                    current_step = add_position_to_grid(tuple(current_position), prime, current_step)
                    s[0] -= int(s[0] / abs(s[0]))
                elif s[1] != 0:
                    current_position[1] += int(s[1] / abs(s[1]))
                    current_step = add_position_to_grid(tuple(current_position), prime, current_step)
                    s[1] -= int(s[1] / abs(s[1]))
                else:
                    print(s)

    def check_for_intersections(self, identifiers):
        intersections = []
        for pair in self.grid.items():
            check = True
            for prime in identifiers:
                check = pair[1][0] % prime == 0 and check
            if check:
                intersections.append(pair)
        intersections.sort(key=lambda inter: abs(inter[0][0]) + abs(inter[0][1]))
        self.intersections = intersections

    def get_closest_intersection(self):
        min_distance = 10 ** 10
        closest_intersection = ((0, 0), 0)
        for inter in self.intersections:
            manhattan_distance = abs(inter[0][0]) + abs(inter[0][1])
            if manhattan_distance < min_distance:
                min_distance = manhattan_distance
                closest_intersection = inter
        return min_distance, closest_intersection

    def get_shortest_intersection(self):
        min_distance = 10 ** 10
        shortest_intersection = ((0, 0), (0, 0))
        for inter in self.intersections:
            if inter[1][1] < min_distance:
                min_distance = inter[1][1]
                shortest_intersection = inter
        return min_distance, shortest_intersection


def solve_day_3():
    grid = Day_3("R993,U847,R868,D286,L665,D860,R823,U934,L341,U49,R762,D480,R899,D23,L273,D892,R43,U740,L940,U502,"
                 "L361,U283,L852,D630,R384,D758,R655,D358,L751,U970,R72,D245,L188,D34,R355,U373,L786,U188,L304,D621,"
                 "L956,D839,R607,U279,L459,U340,R412,D901,L929,U256,R495,D462,R369,D138,R926,D551,L343,U237,L434,"
                 "U952,R421,U263,L663,D694,R687,D522,L47,U8,L399,D930,R928,U73,L581,U452,R80,U610,L998,D797,R584,"
                 "U772,L521,U292,L959,U356,L940,D894,R774,U957,L813,D650,L891,U309,L254,D271,R791,D484,L399,U106,"
                 "R463,D39,L210,D154,L380,U86,L136,D228,L284,D267,R195,D727,R739,D393,R395,U703,L385,U483,R433,U222,"
                 "L945,D104,L605,D814,L656,U860,L474,D672,L812,U789,L29,D256,R857,U436,R927,U99,R171,D727,L244,D910,"
                 "L347,U789,R49,U598,L218,D834,L574,U647,L185,U986,L273,D363,R848,U531,R837,U433,L795,U923,L182,D915,"
                 "R367,D347,R867,U789,L776,U568,R969,U923,L765,D589,R772,U715,R38,D968,L845,D327,R721,D928,R267,U94,"
                 "R763,U799,L946,U130,L649,U521,L569,D139,R584,D27,L823,D918,L450,D390,R149,U237,L696,U258,L757,U810,"
                 "L216,U202,L966,U157,R702,D623,R740,D560,R932,D587,L197,D56,R695,U439,R655,U576,R695,D176,L800,D374,"
                 "R806,U969,L664,U216,L170,D415,R485,U188,L444,D613,R728,U508,L644,U289,R831,D978,R711,U973,R3,U551,"
                 "R377,U114,L15,U812,R210,D829,L536,D883,L843,D427,L311,D680,R482,D69,R125,D953,L896,D85,R376,D683,"
                 "R374,U415,L3,U843,L802,D124,R299,U345,L696,D276,L87,D98,R619,D321,R348,D806,L789,U657,R590,D747,"
                 "L477,U251,R854,D351,L82,D982,R906,D94,R285,U756,L737,D377,L951,U126,L852,D751,L946,U696,L44,D709,"
                 "R851,D364,R222", "L1002,D658,L695,U170,L117,U93,R700,D960,L631,U483,L640,D699,R865,U886,L59,D795,"
                                   "R265,U803,R705,D580,R519,U685,R126,D888,R498,U934,L980,U734,L91,D50,R805,U197,"
                                   "R730,U363,R337,U594,L666,U702,L237,D140,L72,U980,L167,U598,L726,U497,L340,D477,"
                                   "L304,U945,R956,U113,L43,D4,R890,D316,R916,D644,R704,D398,L905,U361,R420,U31,L317,"
                                   "U338,R703,D211,R27,D477,L746,U813,R705,U191,L504,D434,R697,D945,R835,D374,L512,"
                                   "U269,L299,U448,R715,U363,R266,U720,L611,U672,L509,D983,L21,U895,L340,D794,R528,"
                                   "U603,R154,D610,L582,U420,L696,U599,R16,U610,L134,D533,R156,D338,L761,U49,L335,"
                                   "D238,R146,U97,L997,U545,L896,D855,L653,D789,R516,D371,L99,D731,R868,D182,R535,"
                                   "D35,R190,D618,R10,D694,L567,D17,R356,U820,R671,D883,R807,U218,L738,U225,L145,"
                                   "D954,R588,U505,R108,U178,R993,D788,R302,D951,R697,D576,L324,U930,R248,D245,R622,"
                                   "U323,R667,U876,L987,D411,L989,U915,R157,D67,L968,U61,R274,D189,L53,D133,R617,"
                                   "D958,L379,U563,L448,D412,R940,U12,R885,U121,R746,U215,R420,U346,L469,D839,R964,"
                                   "D273,R265,D3,L714,D224,L177,U194,L573,U511,L795,U299,L311,U923,R815,U594,L654,"
                                   "U326,L547,U547,R467,D937,L174,U453,R635,D551,L365,U355,R658,U996,R458,D623,R61,"
                                   "U181,R340,U163,L329,D496,L787,D335,L37,D565,R318,U942,R198,U85,R328,D826,R817,"
                                   "D118,R138,D29,L434,D427,R222,D866,L10,D152,R822,D779,L900,D307,R723,D363,L715,"
                                   "D60,R661,U680,R782,U789,R311,D36,R425,U498,L910,D546,R394,D52,R803,D168,L6,U769,"
                                   "R856,D999,L786,U695,R568,U236,R472,U291,L530,U314,L251,D598,R648,D475,L132,D236,"
                                   "L915,D695,L700,U378,L685,D240,R924,D977,R627,U824,L165")

    grid1 = Day_3("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7")
    grid2 = Day_3("U62,R66,U55,R34,D71,R55,D58,R83", "R75,D30,R83,U83,L12,D49,R71,U7,L72")
    grid3 = Day_3(
        "L1002,D658,L695,U170,L117,U93,R700,D960,L631,U483,L640,D699,R865,U886,L59,D795,R265,U803,R705,D580,R519,U685,R126,D888,R498,U934,L980,U734,L91,D50,R805,U197,R730,U363,R337,U594,L666,U702,L237,D140,L72,U980,L167,U598,L726,U497,L340,D477,L304,U945,R956,U113,L43,D4,R890,D316,R916,D644,R704,D398,L905,U361,R420,U31,L317,U338,R703,D211,R27,D477,L746,U813,R705,U191,L504,D434,R697,D945,R835,D374,L512,U269,L299,U448,R715,U363,R266,U720,L611,U672,L509,D983,L21,U895,L340,D794,R528,U603,R154,D610,L582,U420,L696,U599,R16,U610,L134,D533,R156,D338,L761,U49,L335,D238,R146,U97,L997,U545,L896,D855,L653,D789,R516,D371,L99,D731,R868,D182,R535,D35,R190,D618,R10,D694,L567,D17,R356,U820,R671,D883,R807,U218,L738,U225,L145,D954,R588,U505,R108,U178,R993,D788,R302,D951,R697,D576,L324,U930,R248,D245,R622,U323,R667,U876,L987,D411,L989,U915,R157,D67,L968,U61,R274,D189,L53,D133,R617,D958,L379,U563,L448,D412,R940,U12,R885,U121,R746,U215,R420,U346,L469,D839,R964,D273,R265,D3,L714,D224,L177,U194,L573,U511,L795,U299,L311,U923,R815,U594,L654,U326,L547,U547,R467,D937,L174,U453,R635,D551,L365,U355,R658,U996,R458,D623,R61,U181,R340,U163,L329,D496,L787,D335,L37,D565,R318,U942,R198,U85,R328,D826,R817,D118,R138,D29,L434,D427,R222,D866,L10,D152,R822,D779,L900,D307,R723,D363,L715,D60,R661,U680,R782,U789,R311,D36,R425,U498,L910,D546,R394,D52,R803,D168,L6,U769,R856,D999,L786,U695,R568,U236,R472,U291,L530,U314,L251,D598,R648,D475,L132,D236,L915,D695,L700,U378,L685,D240,R924,D977,R627,U824,L165",
        "R993,U847,R868,D286,L665,D860,R823,U934,L341,U49,R762,D480,R899,D23,L273,D892,R43,U740,L940,U502,L361,U283,L852,D630,R384,D758,R655,D358,L751,U970,R72,D245,L188,D34,R355,U373,L786,U188,L304,D621,L956,D839,R607,U279,L459,U340,R412,D901,L929,U256,R495,D462,R369,D138,R926,D551,L343,U237,L434,U952,R421,U263,L663,D694,R687,D522,L47,U8,L399,D930,R928,U73,L581,U452,R80,U610,L998,D797,R584,U772,L521,U292,L959,U356,L940,D894,R774,U957,L813,D650,L891,U309,L254,D271,R791,D484,L399,U106,R463,D39,L210,D154,L380,U86,L136,D228,L284,D267,R195,D727,R739,D393,R395,U703,L385,U483,R433,U222,L945,D104,L605,D814,L656,U860,L474,D672,L812,U789,L29,D256,R857,U436,R927,U99,R171,D727,L244,D910,L347,U789,R49,U598,L218,D834,L574,U647,L185,U986,L273,D363,R848,U531,R837,U433,L795,U923,L182,D915,R367,D347,R867,U789,L776,U568,R969,U923,L765,D589,R772,U715,R38,D968,L845,D327,R721,D928,R267,U94,R763,U799,L946,U130,L649,U521,L569,D139,R584,D27,L823,D918,L450,D390,R149,U237,L696,U258,L757,U810,L216,U202,L966,U157,R702,D623,R740,D560,R932,D587,L197,D56,R695,U439,R655,U576,R695,D176,L800,D374,R806,U969,L664,U216,L170,D415,R485,U188,L444,D613,R728,U508,L644,U289,R831,D978,R711,U973,R3,U551,R377,U114,L15,U812,R210,D829,L536,D883,L843,D427,L311,D680,R482,D69,R125,D953,L896,D85,R376,D683,R374,U415,L3,U843,L802,D124,R299,U345,L696,D276,L87,D98,R619,D321,R348,D806,L789,U657,R590,D747,L477,U251,R854,D351,L82,D982,R906,D94,R285,U756,L737,D377,L951,U126,L852,D751,L946,U696,L44,D709,R851,D364,R222")
    grid.add_route_to_grid(grid.route1, 3)
    grid.add_route_to_grid(grid.route2, 2)
    grid.check_for_intersections((2, 3))

    grid1.add_route_to_grid(grid1.route1, 3)
    grid1.add_route_to_grid(grid1.route2, 2)
    grid1.check_for_intersections((2, 3))

    grid2.add_route_to_grid(grid2.route1, 3)
    grid2.add_route_to_grid(grid2.route2, 2)
    grid2.check_for_intersections((2, 3))

    grid3.add_route_to_grid(grid3.route1, 3)
    grid3.add_route_to_grid(grid3.route2, 2)
    grid3.check_for_intersections((2, 3))

    print("grid")
    print(grid.get_closest_intersection())
    print(grid.get_shortest_intersection())

    print("testgrid 1 Target 135,410")
    print(grid1.get_closest_intersection())
    print(grid1.get_shortest_intersection())

    print("testgrid 2Target 159,610")
    print(grid2.get_closest_intersection())
    print(grid2.get_shortest_intersection())

    print("testgrid : Target eqaul to grid")
    print(grid3.get_closest_intersection())
    print(grid3.get_shortest_intersection())


class Day_4:
    def __init__(self, lower, upper):
        if lower > upper:
            _x = upper
            upper = lower
            lower = _x
        self.lower_boundary = lower
        self.upper_boundary = upper
        self.possibilities = range(lower, upper + 1)
        self.valid_options = set()
        self.valid_options_found = 0
        self.digits = self.digit_detector()

    def digit_detector(self):
        current_digits = 1
        while True:
            if 0 == math.floor(self.upper_boundary / (10 ** current_digits)):
                break
            current_digits += 1
        return current_digits

    def filter_options(self):
        for option in self.possibilities:
            if self.check_option(option):
                self.valid_options.add(option)
                self.valid_options_found += 1

    def filter_options_no_set(self):
        for option in self.possibilities:
            if self.check_option(option):
                self.valid_options_found += 1

    def filter_options_no_set_stage_2(self):
        for option in self.possibilities:
            if self.check_option_stage_2(option):
                self.valid_options_found += 1

    def filter_options_stage_2(self):
        for option in self.possibilities:
            if self.check_option_stage_2(option):
                self.valid_options.add(option)
                self.valid_options_found += 1

    def check_option_stage_2(self, option):
        def get_digits(number):
            """

            :param number:
            :return: list(int) list with digits, dominant digit in first position
            """
            digits = []
            for _i in range(self.digits):
                power = self.digits - _i - 1
                digit = (math.trunc(number / (10 ** power)))
                number = number - digit * 10 ** power
                digits.append(digit)
            return digits

        def raise_check(_digits):
            """

            :param _digits:
            :return:bool true if no declining digits
            """
            for _i in range(1, len(_digits)):
                if _digits[_i] < _digits[_i - 1]:
                    return False
            return True

        def dubs_check(_digits):
            """

            :param _digits:
            :return:bool True if dubs in number
            """
            dubs = False
            earlydubs = False
            current_row = 1
            for _i in range(len(_digits) - 1):
                if _digits[_i] == _digits[_i + 1]:
                    current_row += 1
                    dubs = True
                    if current_row > 2:
                        dubs = False
                else:
                    if dubs:
                        earlydubs = True
                    current_row = 1
            return dubs or earlydubs

        digits = get_digits(option)
        if raise_check(digits):
            if dubs_check(digits):
                return True
        return False

    def check_option(self, option):
        def get_digits(number):
            """

            :param number:
            :return: list(int) list with digits, dominant digit in first position
            """
            digits = []
            for _i in range(self.digits):
                power = self.digits - _i - 1
                digit = (math.trunc(number / (10 ** power)))
                number = number - digit * 10 ** power
                if digit != 0:
                    digits.append(digit)
            return digits

        def raise_check(_digits):
            """

            :param _digits:
            :return:bool true if no declining digits
            """
            for _i in range(1, len(_digits)):
                if _digits[_i] < _digits[_i - 1]:
                    return False
            return True

        def dubs_check(_digits):
            """

            :param _digits:
            :return:bool True if dubs in number
            """
            for _i in range(len(_digits) - 1):
                if _digits[_i] == _digits[_i + 1]:
                    return True
            return False

        digits = get_digits(option)
        if raise_check(digits):
            if dubs_check(digits):
                return True
        return False


def solve_day_4():
    start = time.time()
    l = 1
    u = 10000000
    test1 = Day_4(l, u)
    test2 = Day_4(l, u)

    print("calculating stage 1")
    start_filter_1 = time.time()
    test1.filter_options_no_set()
    end_filter_1 = time.time()
    print("completed filter in ", end_filter_1 - start_filter_1, " s")
    print("calculating stage 2")
    start_filter_2 = time.time()
    test2.filter_options_no_set_stage_2()
    end_filter_2 = time.time()
    print("completed filter in ", end_filter_2 - start_filter_2, " s")
    print("Test stage 1 options : ", test1.valid_options_found)
    print("Test stage 2 options : ", test2.valid_options_found)


class Day_5(Day_2):

    def execute_codes(self):
        def execute_from_position(position):
            def get_operation(full_operation_code):
                _operation = full_operation_code % 100
                _op_code = int(full_operation_code / 100)
                return _op_code, _operation

            def addition(input_1, input_2, output_index):
                self.codes[output_index] = input_1 + input_2
                return True, 4

            def multiplication(input_1, input_2, output_index):
                # print("output index", output_index)
                self.codes[output_index] = input_1 * input_2
                return True, 4

            def my_in(index_for_input):
                self.codes[index_for_input] = int(input("enter input\n"))
                return True, 2

            def my_out(output):
                print("output = ", output)
                return True, 2

            def jump_if_true(boolean, target):
                if boolean != 0:
                    return False, target
                else:
                    return True, 3

            def jump_if_false(boolean, target):
                if boolean == 0:
                    return False, target
                else:
                    return True, 3

            def less_than(first_input, second_input, output_index):
                if first_input < second_input:
                    self.codes[output_index] = 1
                else:
                    self.codes[output_index] = 0
                return True, 4

            def equal(first_input, second_input, output_index):
                if first_input == second_input:
                    self.codes[output_index] = 1
                else:
                    self.codes[output_index] = 0
                return True, 4

            def halt():
                return False, -1

            op_code, operation = get_operation(self.codes[position])
            # print(op_code, operation)
            input_params = {1: 2,
                            2: 2,
                            3: 0,
                            4: 1,
                            5: 2,
                            6: 2,
                            7: 2,
                            8: 2,
                            99: 0}
            output_params = {1: 1,
                             2: 1,
                             3: 1,
                             4: 0,
                             5: 0,
                             6: 0,
                             7: 1,
                             8: 1,
                             99: 0}
            n_params = input_params[operation] + output_params[operation]
            modes = [0] * input_params[operation]
            for _i in range(input_params[operation]):
                digit = int(op_code / (10 ** _i)) % 10
                if not (digit == 1 or digit == 0):
                    raise Exception("invalid opcode")
                modes[_i] = digit
            params = [0] * n_params
            for _i in range(input_params[operation]):  # input parameters
                # print("input param ", _i, "of", input_params[operation])
                if modes[_i] == 0:  # adds value of register to params
                    # print(self.codes[position+1 + _i], self.codes[position + _i])
                    params[_i] = self.codes[self.codes[position + _i + 1]]
                elif modes[_i] == 1:
                    params[_i] = self.codes[position + _i + 1]
                else:
                    raise Exception("invalid opcode", op_code, operation, "at", position)
            for _i in range(output_params[operation]):
                params[input_params[operation] + _i] = self.codes[position + input_params[operation] + _i + 1]
            # print("modes = ",modes," operation = ", operation," parameters = ", params)
            return {1: addition,
                    2: multiplication,
                    3: my_in,
                    4: my_out,
                    5: jump_if_true,
                    6: jump_if_false,
                    7: less_than,
                    8: equal,
                    99: halt}[operation](*params)

        start_position = 0
        current_position = start_position

        while True:
            # print(self.codes)
            continue_execution, increment = execute_from_position(current_position)
            current_position += increment
            # print(continue_execution, increment,current_position)
            # print(current_position)
            # print(self.codes)
            if not continue_execution:
                if increment == -1:
                    break
                else:
                    current_position = increment


def solve_day_5():
    test_programm = Day_5([3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
                           1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
                           999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99])
    test_programm = Day_5(
        [3, 225, 1, 225, 6, 6, 1100, 1, 238, 225, 104, 0, 1002, 43, 69, 224, 101, -483, 224, 224, 4, 224, 1002, 223, 8,
         223, 1001, 224, 5, 224, 1, 224, 223, 223, 1101, 67, 60, 225, 1102, 5, 59, 225, 1101, 7, 16, 225, 1102, 49, 72,
         225, 101, 93, 39, 224, 101, -98, 224, 224, 4, 224, 102, 8, 223, 223, 1001, 224, 6, 224, 1, 224, 223, 223, 1102,
         35, 82, 225, 2, 166, 36, 224, 101, -4260, 224, 224, 4, 224, 102, 8, 223, 223, 101, 5, 224, 224, 1, 223, 224,
         223, 102, 66, 48, 224, 1001, 224, -4752, 224, 4, 224, 102, 8, 223, 223, 1001, 224, 2, 224, 1, 223, 224, 223,
         1001, 73, 20, 224, 1001, 224, -55, 224, 4, 224, 102, 8, 223, 223, 101, 7, 224, 224, 1, 223, 224, 223, 1102, 18,
         41, 224, 1001, 224, -738, 224, 4, 224, 102, 8, 223, 223, 101, 6, 224, 224, 1, 224, 223, 223, 1101, 68, 71, 225,
         1102, 5, 66, 225, 1101, 27, 5, 225, 1101, 54, 63, 224, 1001, 224, -117, 224, 4, 224, 102, 8, 223, 223, 1001,
         224, 2, 224, 1, 223, 224, 223, 1, 170, 174, 224, 101, -71, 224, 224, 4, 224, 1002, 223, 8, 223, 1001, 224, 4,
         224, 1, 223, 224, 223, 4, 223, 99, 0, 0, 0, 677, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1105, 0, 99999, 1105, 227,
         247, 1105, 1, 99999, 1005, 227, 99999, 1005, 0, 256, 1105, 1, 99999, 1106, 227, 99999, 1106, 0, 265, 1105, 1,
         99999, 1006, 0, 99999, 1006, 227, 274, 1105, 1, 99999, 1105, 1, 280, 1105, 1, 99999, 1, 225, 225, 225, 1101,
         294, 0, 0, 105, 1, 0, 1105, 1, 99999, 1106, 0, 300, 1105, 1, 99999, 1, 225, 225, 225, 1101, 314, 0, 0, 106, 0,
         0, 1105, 1, 99999, 1007, 226, 226, 224, 1002, 223, 2, 223, 1006, 224, 329, 1001, 223, 1, 223, 1007, 226, 677,
         224, 102, 2, 223, 223, 1006, 224, 344, 1001, 223, 1, 223, 108, 677, 677, 224, 102, 2, 223, 223, 1005, 224, 359,
         1001, 223, 1, 223, 1007, 677, 677, 224, 1002, 223, 2, 223, 1006, 224, 374, 101, 1, 223, 223, 8, 677, 226, 224,
         1002, 223, 2, 223, 1006, 224, 389, 101, 1, 223, 223, 7, 226, 226, 224, 1002, 223, 2, 223, 1005, 224, 404, 101,
         1, 223, 223, 7, 677, 226, 224, 102, 2, 223, 223, 1005, 224, 419, 1001, 223, 1, 223, 8, 226, 677, 224, 1002,
         223, 2, 223, 1005, 224, 434, 101, 1, 223, 223, 1008, 226, 677, 224, 102, 2, 223, 223, 1006, 224, 449, 1001,
         223, 1, 223, 7, 226, 677, 224, 1002, 223, 2, 223, 1006, 224, 464, 1001, 223, 1, 223, 108, 677, 226, 224, 102,
         2, 223, 223, 1005, 224, 479, 101, 1, 223, 223, 108, 226, 226, 224, 1002, 223, 2, 223, 1006, 224, 494, 101, 1,
         223, 223, 8, 226, 226, 224, 1002, 223, 2, 223, 1005, 224, 509, 1001, 223, 1, 223, 1107, 677, 226, 224, 102, 2,
         223, 223, 1005, 224, 524, 1001, 223, 1, 223, 1107, 226, 226, 224, 102, 2, 223, 223, 1005, 224, 539, 1001, 223,
         1, 223, 1108, 677, 677, 224, 1002, 223, 2, 223, 1006, 224, 554, 101, 1, 223, 223, 107, 226, 677, 224, 102, 2,
         223, 223, 1005, 224, 569, 1001, 223, 1, 223, 1108, 226, 677, 224, 1002, 223, 2, 223, 1005, 224, 584, 1001, 223,
         1, 223, 1107, 226, 677, 224, 1002, 223, 2, 223, 1005, 224, 599, 1001, 223, 1, 223, 1008, 226, 226, 224, 1002,
         223, 2, 223, 1005, 224, 614, 101, 1, 223, 223, 107, 226, 226, 224, 102, 2, 223, 223, 1006, 224, 629, 1001, 223,
         1, 223, 1008, 677, 677, 224, 1002, 223, 2, 223, 1006, 224, 644, 101, 1, 223, 223, 107, 677, 677, 224, 1002,
         223, 2, 223, 1005, 224, 659, 101, 1, 223, 223, 1108, 677, 226, 224, 1002, 223, 2, 223, 1006, 224, 674, 1001,
         223, 1, 223, 4, 223, 99, 226])

    test_programm.execute_codes()
    if len(test_programm.codes) < 15:
        print(test_programm.codes)


if __name__ == '__main__':
    solve_day_5()
