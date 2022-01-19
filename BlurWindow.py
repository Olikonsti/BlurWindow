from tkinter import *
import pyautogui
from PIL import ImageTk, ImageFilter, ImageEnhance
from PIL import ImageGrab
from functools import partial
#ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

class BlurWindow(Toplevel):
    def __init__(self, window, color):
        super().__init__(window)
        self.overrideredirect(True)
        self.window = window
        self.enabled = True
        self.freeze = False
        self.transparent_color = color
        def handle_focus(event=None):
            window.focus_set()
        self.bind("<FocusIn>", handle_focus)
        def upd(hide=False):
            if hide:
                self.withdraw()
                self.window.withdraw()
            ss = pyautogui.screenshot(region=(0, 0, 4000, 4000))

            if hide:
                self.deiconify()
                self.window.deiconify()
            blurImage = ss.filter(ImageFilter.GaussianBlur(radius=80))
            filter = ImageEnhance.Brightness(blurImage)
            brightImage = filter.enhance(0.75)
            brightImage = brightImage.filter(ImageFilter.SMOOTH_MORE())
            return brightImage

        self.upd = upd

        self.frame = Frame(self)
        self.ss = upd()
        # root.state('zoomed')
        self.picture = ImageTk.PhotoImage(self.ss)
        image1 = Label(self.frame, image=self.picture)
        image1.image = self.picture
        self.image1 = image1
        self.frame.config(bg="black")
        self.frame.pack(expand="true", fill=BOTH)



        self.window.bind("<Configure>", self.update_task)
        self.window.bind("<F5>", self.update_image)
        self.window.bind("<Unmap>", lambda e:self.withdraw())
        self.window.bind("<Map>", self.unminimize)

        self.last_width = self.window.winfo_width()
        self.last_height = self.window.winfo_height()
        self.last_x = self.window.winfo_x()
        self.last_y = self.window.winfo_y()

        self.after(1, self.disable)
        self.update()
        image1.place(x=self.window.winfo_x() * -1 -2, y=self.window.winfo_y() * -1)

    def lift_bg(self, event=None):
        self.deiconify()
        self.window.deiconify()

    def unminimize(self, event=None):
        if self.enabled:
            self.deiconify()
            self.lift_bg()


    def enable(self):
        self.enabled = True
        def lift_bg(event=None):
            self.deiconify()
            self.window.deiconify()
        self.window.bind("<FocusIn>", lift_bg)
        self.window.bind("<Configure>", self.update_task)
        self.update_task()
        self.window.wm_attributes("-transparentcolor", self.transparent_color)
        self.change_geometry_width(1)
        self.change_geometry_width(-1)
        self.after(10, lift_bg)

    def disable(self):
        self.enabled = False
        self.window.wm_attributes("-transparentcolor", "")
        self.kill()
        self.withdraw()

    def change_geometry_width(self, pixels):
        try:
            width = self.window.winfo_width()
            height = self.window.winfo_height()
            self.window.geometry(f"{width+pixels}x{height}")
        except:
            pass


    def update_image(self, event=None):
        self.ss = self.upd()

    def kill(self):
        self.window.bind("<Configure>", lambda e:print)
        self.window.bind("<FocusIn>", lambda e:print)

    def update_task(self, event=None, repeat=True):
        if not self.freeze:
            self.width = self.window.winfo_width()
            self.height = self.window.winfo_height()
            self.x = self.window.winfo_x()
            self.y = self.window.winfo_y()
            self.update()

            if (self.x != self.last_x or self.y != self.last_y or self.height != self.last_height or self.width != self.last_width) :

                self.freeze = True
                self.image1 = Label(self.frame, image=self.picture)
                self.image1.image = self.picture
                self.image1.place(x=self.winfo_x() * -1-2 , y=self.winfo_y() * -1 )
                #self.image1 = image1

                self.geometry(f"{self.window.winfo_width()-1}x{self.window.winfo_height()}+{self.window.winfo_x() + 8}+{self.window.winfo_y() + 30}")


                self.last_width = self.width
                self.last_height = self.height
                self.last_x = self.x
                self.last_y = self.y

                self.after(80, self.unfreeze)

            #self.after(10, self.update_task)


    def unfreeze(self):
        self.freeze = False
        self.update_task()