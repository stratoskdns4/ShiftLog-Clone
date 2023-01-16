# ShiftLog-Clone

This is clone of ShiftLog made with python and tkinter.

## Installing

Download the repository
```sh
$ git clone https://github.com/stratoskdns4/ShiftLog-Clone.git
$ cd ShiftLog-Clone
```

Install dependencies using pip
```sh
$ pip3 install -r requirments.txt
```

## Run the app

To run the app, just execute ```app.py```.
```sh
$ python3 app.py
```

## Adding new frames

The app follows a tab-based design.
To add a new tab, follow these steps:

1. Create a new python file, using snake case notation for your frame name. Example: ```my_new_frame.py```
2. Start your new Frame using this code snippet. Replace ```MyNewFrame``` with your frame name.:
```py
import tkinter as tk


class MyNewFrame(tk.Frame):

    def __init__(self, root, **options):
        super().__init__(root, **options)

        # Place your wigdets here

    def refresh(self):
        """On re-render hook"""


# Use this to test your frame as a single app
if __name__ == "__main__":
    from single_frame_runner import single_frame_runner

    single_frame_runner(MyNewFrame)

```

3. Subscribe your new frame into the main app tab manager, by instanciating your frame into the
```pages``` dict. Example:
```py
pages = {
    # other tabs
    'my_new_page': MyNewFrame(notebook)
}
```

4. Done!