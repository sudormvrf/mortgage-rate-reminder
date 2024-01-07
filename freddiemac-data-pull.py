from datetime import datetime
import subprocess
import os
import time

# current_date = date.today()

def runcmd (cmd, verbose = False, *args, **kargs):
	process = subprocess.Popen(
		cmd,
		stdout = subprocess.PIPE,
		stderr = subprocess.PIPE,
		text = True,
		shell = True
	)
	std_out, std_err = process.communicate()
	if verbose:
		print(std_out.strip(), std_err)
	pass

runcmd(f"wget -P xlsx_files/ https://freddiemac.com/pmms/docs/historicalweeklydata.xlsx", verbose = True)

mtime = os.path.getmtime('xlsx_files/historicalweeklydata.xlsx')
ts = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d')

runcmd(f"mv xlsx_files/historicalweeklydata.xlsx xlsx_files/{ts}-mortgate-data.xlsx", verbose = True)

