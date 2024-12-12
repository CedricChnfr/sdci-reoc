import curses
import npyscreen
import subprocess
import psutil

import monitoring

npyscreen.disableColor()
def main():
    app = App()
    app.run()

class App(npyscreen.NPSApp):
    def main(self):
        form = npyscreen.FormBaseNew(name="SDCI Controller")
        choices = ["Monitoring", "Adaptation", "Topologie", "Mode auto."]
        port_choices = ["Local", "Output", "Z1", "Z2", "Z3"]

        widget_choice = form.add(
            npyscreen.MultiSelect,
            name="CHOICE",
            relx=2,
            rely=3,
            max_width=20,
            values=choices,
        )

        widget_port_choice = form.add(
            npyscreen.SelectOne,
            name="PORT CHOICE",
            relx=26,
            rely=3,
            values=port_choices,
            hidden=True
        )

        widget_debug = form.add(
            npyscreen.BoxTitle,
            name="DEBUG",
            relx=40,
            rely=10,
            editable=False,
        )

        widget_monitor = form.add(
            npyscreen.BoxTitle,
            name="MONITORING",
            relx=40,
            rely=2,
            max_height=8,
            editable=False,
        )

        def update(*args, **kwargs):
            choice = widget_choice.value
            # 0 -> Monitor
            if 0 in choice:
                widget_port_choice.hidden = False
            if not 0 in choice:
                widget_port_choice.hidden = True
            #1 -> Adaptation
            #2 -> Topologie
            #3 -> Mode Auto.

            # Checking for any monitoring
            if not is_process_running("topology_sdn.py") and len(choice)>0:
                widget_debug.values=["Error: topology_sdn.py is not running."]
            form.display()

        quit_handlers = {
            "^Q": self.exit_func,
            "^C": self.exit_func,
            "^Z": self.exit_func,
            curses.ascii.ESC: self.exit_func,
        }
        widget_choice.add_handlers(quit_handlers)
        widget_port_choice.add_handlers(quit_handlers)

        widget_choice.when_value_edited = update
        widget_port_choice.when_value_edited = lambda *args, **kwargs: monitoring.update_port(widget_port_choice, widget_monitor, form)

        form.edit()

    def exit_func(*args, **kwargs):
        monitoring.stop_thread()
        exit(0)

def is_process_running(process_name):
    for process in psutil.process_iter(['name', 'cmdline']):
        try:
            if process_name in process.info['name'] or process_name in ' '.join(process.info['cmdline']):
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

if __name__ == "__main__":
    if not is_process_running("topology_sdn.py"):
        print("Warning: Topology SDN is not launched.")
        result = subprocess.run(["bash", "docker/clear.sh"], check=True, text=True, capture_output=True)
        print(result.stdout)
        result = subprocess.run(["bash", "docker/create.sh"], check=True, text=True, capture_output=True)
        print(result.stdout)
    main()