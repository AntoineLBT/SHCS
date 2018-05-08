def display_clothe(self):
    self.array_cursor_top = []
    for i in range(1, 14, 2):
        self.tick = Label(root, text='|')
        self.tick.grid(row=0, column=i)
        self.array_cursor_top.append(self.tick)
    self.clothe_id = Label(root, text='N°vêtement')