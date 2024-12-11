import curses
import sys
import npyscreen
import threading

import monitor

npyscreen.disableColor()
def main():
    app = App()
    app.run()

def thread_monitor(wpc, wd, f):
    while 1:
        port_no = wpc.value[0]
        port_stats = monitor.get_port_stats(port_no)
        if isinstance(port_stats, dict):
            wd.values = [
                f"Port {port_no + 1} Statistics:",
                "",
                f"  packet_reçu: {port_stats['rx_packets']}",
                f"  packet_envoyé: {port_stats['tx_packets']}",
                f"  octets_reçu: {port_stats['rx_bytes']}",
                f"  octets_envoyé: {port_stats['tx_bytes']}",
                f"  paquet_perdu_reçu: {port_stats['rx_dropped']}",
                f"  paquet_perdu_envoyé: {port_stats['tx_dropped']}",
                f"  erreurs_reçu: {port_stats['rx_errors']}",
                f"  erreurs_envoyé: {port_stats['tx_errors']}"
            ]
        else:
            wd.values = [port_stats]
        f.display()
        

class App(npyscreen.NPSApp):
    def main(self):
        global i

        form = npyscreen.FormBaseNew(name="SDCI Controller")
        stdscr = curses.initscr()
        column_height = stdscr.getmaxyx()[0] - 4
        choices = ["Monitoring", "Adaptation", "Topologie", "Mode auto."]
        # 4: Z1
        port_choices = ["Port 1", "Port 2", "Port 3", "Port 4", "Port 5"]
        

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
            relx=24,
            rely=2,
            max_width=20,
            max_height=column_height,
            values=port_choices,
            hidden=True
        )

        widget_debug = form.add(
            npyscreen.BoxTitle,
            name="DEBUG",
            relx=46,
            rely=2,
            max_height=column_height,
        )

        def update(*args, **kwargs):
            if len(widget_choice.value) > 0:
                choice = choices[widget_choice.value[0]]
                if choice == "Monitoring":
                    widget_port_choice.hidden = False
                    widget_debug.name="MONITORING"
                    form.display()
                else:
                    widget_port_choice.hidden = True
                    widget_debug.values = [f"You chose {choice}"]
                    form.display()

        def update_port(*args, **kwargs):
            if len(widget_port_choice.value) > 0:
                thread = threading.Thread(target=thread_monitor, args=(widget_port_choice, widget_debug, form))
                thread.start()

        widget_choice.when_value_edited = update
        widget_port_choice.when_value_edited = update_port

        form.edit()


class ExitButton(npyscreen.ButtonPress):
    def whenPressed(self):
        sys.exit(0)  # Gracefully exit the application

if __name__ == "__main__":
    main()