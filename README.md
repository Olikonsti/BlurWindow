I WONT WORK ON THIS ANY LONGER (IT WORKS BUT NOT GREAT)

# BlurWindow
 Python class for creating tkinter windows with blurred background
 
 dark title bar: https://gist.github.com/Olikonsti/879edbf69b801d8519bf25e804cec0aa
 
 ![ezgif com-gif-maker (1)](https://user-images.githubusercontent.com/68354546/150221194-316ae8b9-c14f-4b0e-b4e5-fabc4f36c2e9.gif)

 ![image](https://user-images.githubusercontent.com/68354546/150221245-80e0fbaa-f55e-40ec-9a66-3b540fb6ad14.png)
 
 # Known Bugs:
- Window sometimes not resizable
- Ghost titlebar after window maximize
- Support for only one main Monitor

# How it works
- BlurWindow will create a second window without a title bar behind the root window.
- A blurred image of the Screen gets placed on the back window
- You just specify a color, which will become transparent in the root window thus showing the blurred background 
