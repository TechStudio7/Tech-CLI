from rich import print
from rich.console import Console
import platform
import socket
import os

# Your ASCII art
BANNER = """                                            
░██████████                      ░██             ░██████  ░██         ░██████
    ░██                          ░██            ░██   ░██ ░██           ░██  
    ░██     ░███████   ░███████  ░████████     ░██        ░██           ░██  
    ░██    ░██    ░██ ░██    ░██ ░██    ░██    ░██        ░██           ░██  
    ░██    ░█████████ ░██        ░██    ░██    ░██        ░██           ░██  
    ░██    ░██        ░██    ░██ ░██    ░██     ░██   ░██ ░██           ░██  
    ░██     ░███████   ░███████  ░██    ░██      ░██████  ░██████████ ░██████
                                                                             
                                                                             
                                                                             
                                                        
                                                                                                                                                                                     
"""

def show_banner():
    console = Console()
    # Define your rainbow spectrum
    rainbow_colors = ["red", "orange1", "yellow", "green", "cyan", "blue", "magenta"]
    
    # Split the banner into individual lines
    lines = BANNER.strip().split('\n')
    
    # Print each line with a cycling color
    for i, line in enumerate(lines):
        color = rainbow_colors[i % len(rainbow_colors)]
        console.print(f"[{color}]{line}[/{color}]")
    
    print("[green]Type 'info', 'os info', or 'device name'. Type 'exit' to quit.[/green]\n")

def run_cli():
    show_banner()
    
    while True:
        command = input(f"tech-cli > ").strip().lower()

        if command == "exit":
            print("Goodbye!")
            break
        elif command == "info":
            print("You are currently using: [bold magenta]Tech CLI[/bold magenta]")
        elif command == "os info":
            print(f"OS: [bold green]{platform.system()} {platform.release()}[/bold green]")
            print(f"Device Name: [bold cyan]{socket.gethostname()}[/bold cyan]")
            print(f"Account Name: [bold red]{os.getlogin()}[/bold red]")

        elif command == "commands" or command == "help":
            print("[bold white]Available Commands:[/bold white]")
            print("  [cyan]info[/cyan]        - Displays application info")
            print("  [cyan]os info[/cyan]     - Displays operating system details")
            print("  [cyan]device name[/cyan] - Displays the hostname of the machine")
            print("  [cyan]exit[/cyan]        - Closes the application")
            print("  [cyan]help, commands[/cyan] - Displays available commands")
            print("  [green]ralsei[/green] - Displays ASCII art of Ralsei")
        elif command == "ralsei":
            print("""
        &&&&      &&&&        
      &$Xx&&&&&&& &&xX$&&     
    &&+;x&&X+::::&& &x;+$&    
    &&;;x&&+......+&&x;;$&    
    &&;;:.;:.;:......:;;$&    
   &X+:...:::;;::.......+x&   
   &;....................;&   
 &&.......+$&&;;&&$+.......&& 
 &&...::+XX$&.::.&&XX+:::..&& 
 &&....+;..x&.;+.&X..;+....&& 
 &&.....:+...+::+...+;.....&& 
 &&....&X;+++....+++;X&....&& 
 &&....;+$.+$..:$:..$x;....&& 
   &;...:xx;.&&$..:xx;...;&   
   &;.....xxxxxxxxxx.....;&   
   X&&X;+xxxxxxxxxxxxxxX&&X   
 XX&&&xxxx&&&&&&&&&XXXX&&&&XX 
X$&&&&xxxx&X++$&++++XXX&&&&&&X
X$&&xxxxX&+$&&&&&&$++xX&&&&&&X
XXX&&&&&$x+xx&&&&xx+++xX&&&$XX
   &$XXXx+++++$&+++++++XXX&   
   &$XX++++++++++++++++XXX&   
&&$Xxx++++++++++++++++++xxX$$&
 &&&x++++++++++++++++++++x&&& 
    &&&Xx++++++++++++xX&&&    
       &&&$$$$&&$$$$&&&       
        XX....xx....XX        
        XX....xx....XX        
     XXX+.....xx.....+XXX     
    Xx.+;.+;.+xx+.:+.;+.xX    
     XXXXXXXX    XXXXXXXX    
              hi 
                  """)
        elif command == "c" or command == "C":
            print("""
             ======+             
          =============          
      =====================      
   =========:.......:=========   
=========.             .========+
=======..                .===*###
======.      .:===:.     :+######
=====.     .=========::##########
====:     :=======+*#############
====:     -====+#################
====:     :=*#%%%%%##############
=====.     :%%%%%%%%%:.*#########
======.      .=*#*=.     .-######
==+%%%#..                .#%%%###
%%%%%%%%#:             .#%%%%%%%%
   %%%%%%%%#=.......-#%%%%%%%%   
      %%%%%%%%%%%%%%%%%%%%%      
          %%%%%%%%%%%%%          
             %%%%%%%             
             """)
        elif command == "i hate ralsei":
            for _ in range(60):
                print("[red]SHUT THE FUCK UP[/red]")
        elif command:
            print(f"[red]Unknown command:[/red] '{command}'")

if __name__ == "__main__":
    run_cli()