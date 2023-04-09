from subprocess import run
OATHPATH = ['python/oauth/oathplus']


def runOAuth(arguments: list):
    ArgumentList = OATHPATH + arguments
    Command = run(ArgumentList, capture_output=True, text=True)
    return Command.stdout
