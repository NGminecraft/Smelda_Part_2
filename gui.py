import pygame
from copy import deepcopy


class Gui:
    def __init__(self, screen, items, special_flag=None, special_flag_surface=None, special_flag_location=None,
                 show_money=True):
        self.screen = screen
        self.show_money = show_money
        if type(items) == dict:
            self.items = list(items.keys())
        else:
            self.items = items
        if special_flag:
            self.special_flag = special_flag
            self.special_flag_surface = special_flag_surface
            self.special_flag_location = special_flag_location
        else:
            self.special_flag = False
        # Create basic variables for GUI
        self.gui_height = self.screen.get_height() // 2
        self.width = self.screen.get_width()
        self.gui_rows = 2
        self.gui_layout = []

    def gui(self, screen, sufficent_money=True, money=0, text_function=None, order=None):
        if not self.items:
            back = pygame.surface.Surface((screen.get_width(), screen.get_height()))
            back.fill((0, 0, 0, 220))
            back.set_alpha(220)
            screen.blit(back, (0, 0))
            return
        self.gui_layout = []
        for i in range(self.gui_rows):
            self.gui_layout.append([])
        if len(self.items) % self.gui_rows != 0:
            overflow = len(self.items) % self.gui_rows
        else:
            overflow = 0
        keys = deepcopy(self.items)
        length = len(keys)
        num = 0
        for num in range(self.gui_rows):
            self.gui_layout[num] = keys[0:length // self.gui_rows + overflow]
            del keys[0:length // self.gui_rows + overflow]
            overflow = max(overflow - 1, 0)
        self.side_length = min(self.gui_height / self.gui_rows, self.width / len(self.gui_layout[0]))
        back = pygame.surface.Surface((screen.get_width(), screen.get_height()))
        back.fill((0, 0, 0, 220))
        back.set_alpha(220)
        screen.blit(back, (0, 0))
        self.gui_buttons = {}
        for index, value in enumerate(self.gui_layout):
            dif = abs(len(value) - len(self.gui_layout[max(index - 1, 0)]))
            for i, v in enumerate(value):
                self.gui_buttons[v] = screen.blit(
                    pygame.transform.scale(v(name="Demo").image, (self.side_length, self.side_length)), (
                        (self.width / len(value)) * i + self.side_length / 6 * dif,
                        (screen.get_height() // 2) + self.side_length * index))
        if self.special_flag:
            self.gui_buttons[self.special_flag] = screen.blit(self.special_flag_surface, self.special_flag_location)
        if text_function and order:
            text_function(screen, str(order), (0, 0))
        if self.show_money and text_function:
            color = (255, 255, 255)
            if not sufficent_money:
                color = (255, 0, 0)
            text_function(screen, f"${str(money)}", (screen.get_width() - (len(str(money)) + 1) * 15, 50), color)

    def check_gui_click(self, pos):
        try:
            for i in list(self.gui_buttons.keys()):
                if self.gui_buttons[i].collidepoint(pos):
                    return i
        except AttributeError:
            pass
