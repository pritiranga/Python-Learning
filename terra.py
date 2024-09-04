import subprocess

def terraform_run(command):
        # Run the command and capture output
        process = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(process.stdout.decode())

dir=r"C:\Users\Priti Ranga\Documents\Python Workshop\terraform-automation" # Use a raw string "r" for the directory path to avoid escaping issues
#command=f'terraform -chdir="{dir}" init'  
command=f'terraform -chdir="{dir}" apply --auto-approve'

terraform_run(command)
