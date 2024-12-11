import curses
import sys
import npyscreen
npyscreen.disableColor()

def main():
    app = App()
    app.run()

class App(npyscreen.NPSApp):
    def main(self):
        global i
        # Create the form and get terminal size
        form = npyscreen.FormBaseNew(name="SDCI Controller")
        stdscr = curses.initscr()  # Initialize curses screen once
        column_height = stdscr.getmaxyx()[0] - 4
        choices = ["Monitoring", "Adaptation", "Topologie", "Mode auto."]
        
        # Create widgets (column for choice and debug)
        widget_choice = form.add(
            npyscreen.SelectOne,
            name="CHOICE",
            relx=2,
            rely=2,
            max_width=20,
            max_height=column_height,
            values=choices
        )

        widget_debug = form.add(
            npyscreen.BoxTitle,
            name="DEBUG",
            relx=23,
            rely=2,
            max_height=column_height,
        )
        
        # Define the event handler for when the user selects a choice
        def update(*args, **kwargs):
            if len(widget_choice.value) > 0:
                widget_debug.values = [f"You choose {choices[widget_choice.value[0]]}"];
            form.display()  # Redraw the form with the updated debug box

        # Set max height of widget_choice
        widget_choice.when_value_edited = update

        form.edit()


class ExitButton(npyscreen.ButtonPress):
    def whenPressed(self):
        sys.exit(0)  # Gracefully exit the application

if __name__ == "__main__":
    main()
