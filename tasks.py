from invoke import Collection, task, exceptions
@task
##(comport=None,filePath=None,address=0,blPath=None,phyInitPath=None,mainPath=None,partPath=None,clean=True)
def setup(c,**kwargs):
    
    if not kwargs["comport"]:
    	return exceptions.Failure(result="comport is needed to use this command ", reason=exceptions.AmbiguousEnvVar)
    if clean and comport:
        c.run("esptool --port %s erase_flash" % comport)
    # ... setup things here ...
    if filePath and not (blPath or phyInitPath or mainPath or partPath):
    	c.run("esptool ")

@task(pre=[setup])
def build(c):
    c.run("build, accounting for leftover files...")

def clean_build(c):
    c.run("build, assuming clean slate...")