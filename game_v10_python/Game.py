from typing import Tuple
import random
import copy

class Game:
    SHIFT_INDEXES = ((0,0),(0,1),(1,1),(1,0))


    def __getitem__(self, indices: Tuple[int, int]):
        return self.__cells[indices[0]][indices[1]]

    @staticmethod
    def get_neighbor_cells(cells, _i, _j):
        for c in ((0,1),(1,0),(0,-1),(-1,0)):
            i = _i+c[0]
            j = _j+c[1]
            if i>=0 and j>=0 and i<len(cells) and j<len(cells[i]):
                yield i, j

    @staticmethod
    def get_same_neighbor_cells(cells, _i, _j, result=None):
        if result is None:
            result = []
        if (_i, _j) in result:
            return result

        if cells[_i][_j] is None:
            return result

        result.append((_i, _j))
        val = cells[_i][_j]

        for c in Game.get_neighbor_cells(cells, _i, _j):
            val2 = cells[c[0]][c[1]]
            if val2 is not None and val == val2:
                Game.get_same_neighbor_cells(cells, c[0], c[1], result)
        return result

    def __fill_cells(self):
        self.__cells = [[None for i in range(self.__size)] for j in range(self.__size )]
        for i in range(self.__size):
            for j in range(self.__size):
                #Подбор возможных значений ячейки
                a_colors = [0]*self.__count_colors
                for c in Game.get_neighbor_cells(self.__cells, i, j):
                    color_num = self.__cells[c[0]][c[1]]
                    if color_num is None:
                        continue
                    a_colors[color_num] += len(Game.get_same_neighbor_cells(self.__cells, c[0],c[1]))
                a_colors = [i for i, item in enumerate(a_colors) if item < self.__min_count_destroy_figures-1]
                if len(a_colors) == 0:
                    return False
                self.__cells[i][j] = a_colors[random.randrange(len(a_colors))]
        return True



    def __init__(self, size, count_colors, min_count_destroy_figures):
        self.__size = size
        self.__count_colors = count_colors
        self.__min_count_destroy_figures = min_count_destroy_figures
        self.new_game()

    def new_game(self):
        self.__score = 0
        is_fill_cells = False
        while not is_fill_cells:
            is_fill_cells = self.__fill_cells()

    @staticmethod
    def rotate(cells, i, j, shift_indexes=SHIFT_INDEXES):
        shift_indexes_r = shift_indexes[-1:] + shift_indexes[:-1]
        x = [cells[i+shift_index[0]][j+shift_index[1]] for shift_index in shift_indexes_r]

        for ii, val in enumerate(x):
            shift_index = shift_indexes[ii]
            cells[i + shift_index[0]][j + shift_index[1]] = val

    @property
    def size(self):
        return self.__size

    @property
    def count_colors(self):
        return self.__count_colors

    @property
    def min_count_destroy_figures(self):
        return self.__min_count_destroy_figures

    @property
    def score(self):
        return self.__score

    # Верхний левый угол _i _j
    def step(self, _i, _j):
        result_state = []
        def _save_state():
            result_state.append({"cells": copy.deepcopy(self.__cells), "score": self.__score })

        if _i < 0 or _j < 0 or _i > self.__size - 1 or _j > self.__size - 1:
            raise IndexError()

        Game.rotate(self.__cells, _i, _j)
        _save_state()

        start_positions = set()
        for shift_index in Game.SHIFT_INDEXES:
            start_positions.add((_i+shift_index[0],_j+shift_index[1]))

        destroy_positions = set()
        while len(start_positions)>0 or len(destroy_positions)>0:
            if len(start_positions)>0:
                start_position = start_positions.pop()
                neighbors_positions = Game.get_same_neighbor_cells(self.__cells,start_position[0],start_position[1])
                if len(neighbors_positions)>=self.__min_count_destroy_figures:
                    self.__score += len(neighbors_positions) * (len(neighbors_positions) + 1 - self.__min_count_destroy_figures)
                    destroy_positions.update(neighbors_positions)
                    for neighbors_position in neighbors_positions:
                        self.__cells[neighbors_position[0]][neighbors_position[1]] = None
                        if neighbors_position in start_positions:
                            start_positions.remove(neighbors_position)
                    _save_state()

            elif len(destroy_positions)>0:
                for destroy_position in sorted(destroy_positions):
                    j = destroy_position[1]
                    for i in range(destroy_position[0],0,-1):
                        self.__cells[i][j] = self.__cells[i-1][j]
                        start_positions.add((i,j))
                    self.__cells[0][j] = random.randrange(self.__count_colors)
                    start_positions.add((0, j))
                destroy_positions.clear()
                _save_state()
        return result_state

"""
g = Game(10,5,3)
r = g.step(1,1)
print(g[0,1])
"""
