#!/usr/bin/python
import os
import sys
from tabulate import tabulate
import paramiko

class Status: 

    def __init__(self, argv):
        self.table = []
        self.username = 'farooqh1'
        self.pw = 'mkonjibh'
        self.machines = ['khaki', 'olive', 'fluffy', 'berovo', 'mayday']
        #self.machines = ['olive']
        self.headers = ["Machine","File", "Analysis","Voltage Range","Model", "PID"]
        self.sweep_machines()

        print tabulate(self.table, headers=self.headers)

    def sweep_machines(self):
        for machine in self.machines:
            
            #connect to machine
            self.current_machine = machine
        
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            #client.load_system_host_keys()
            client.connect(machine, username=self.username, password=self.pw)

            
            sftp_client = client.open_sftp()
            #remote_file = sftp_client.open('panic.log', 'rb').read()

            self.read_procs(sftp_client)




    def read_procs(self, sftp_client):

        pids = [pid for pid in sftp_client.listdir('/proc') if pid.isdigit()]

        atk_procs = []
        for pid in pids:
            try:
                proc_str = sftp_client.open (os.path.join('/proc', pid, 'cmdline'), 'rb').read()
                if 'atkpython_exec' in proc_str:
                    proc_str = proc_str.encode("string-escape")
                    proc_str = proc_str.replace ("\\x00", " ")
                    proc_str = str(pid) + ' ' + proc_str 
                    
                    atk_procs.append(proc_str)
            except IOError: #proc has already been terminated
                continue


        

        self.print_status (atk_procs)
    def print_status (self, atk_procs):
        
        #no procs running
        if not atk_procs:
            atk_procs = ['']
            
            

        for proc in atk_procs:
            ifile = ''
            analysis=''
            gate_v=''
            model=''
            vds=''
            pid=''

            if proc:
                werds = proc.split('--')
                pid = werds[0].split(' ')[0]
                #ignore the first argument, it contains PID
                werds = werds[1:]

                
                

                args = [w.strip() for w in werds]
                for arg in args:
                    if ('ifile' in arg):
                        ifile = arg.split('=')[1]
                    elif ('analysis' in arg):
                        analysis = arg.split('=')[1]
                    elif ('gate_v' in arg):
                        gate_v = arg.split('=')[1]
                    elif ('vds' in arg):
                        vds = arg.split('=')[1]
                    elif ('model' in arg):
                        model = arg.split('=')[1]

            
            table_row = []
            table_row.append(self.current_machine)
            table_row.append(ifile)
            table_row.append(analysis)
            table_row.append(gate_v)
            table_row.append(vds)
            table_row.append(model)
            table_row.append(pid)

            self.table.append(table_row)

if __name__ == "__main__":

        statusObj = Status(sys.argv[1:])
 
