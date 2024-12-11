import curses
import sys
import npyscreen
from monitoring import update_port  # Importer les fonctions de monitoring

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
        port_choices = ["Port 1", "Port 2", "Port 3", "Port 4", "Port 5"]
        
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

        widget_port_choice = form.add(
            npyscreen.SelectOne,
            name="PORT CHOICE",
            relx=24,  # Adjusted to be next to the "Monitoring" option
            rely=2,
            max_width=20,
            max_height=column_height,
            values=port_choices,
            hidden=True  # Initially hidden
        )

        widget_debug = form.add(
            npyscreen.BoxTitle,
            name="DEBUG",
            relx=46,  # Adjusted to make space for the port choices
            rely=2,
            max_height=column_height,
        )

        # Define the event handler for when the user selects a choice
        def update(*args, **kwargs):
            if len(widget_choice.value) > 0:
                choice = choices[widget_choice.value[0]]
                if choice == "Monitoring":
                    widget_port_choice.hidden = False
                    form.display()  # Redraw the form to show the port choice
                else:
                    widget_port_choice.hidden = True
                    widget_debug.values = [f"You chose {choice}"]
                    form.display()  # Redraw the form with the updated debug box

        widget_choice.when_value_edited = update
        widget_port_choice.when_value_edited = lambda *args, **kwargs: update_port(widget_port_choice, widget_debug, form)

        form.edit()


class ExitButton(npyscreen.ButtonPress):
    def whenPressed(self):
        sys.exit(0)  # Gracefully exit the application

if __name__ == "__main__":
    main()