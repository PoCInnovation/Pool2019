import sys


FLAG = (14 * 18 + 1) * 678 * 49

def main(argc, argv):
  if argc < 2:
    sys.stderr.write('Il me faut un argument...\n')
    return -1

  userInput = argv[1]
  if str(FLAG) == userInput:
    sys.stdout.write('Bravo !\n')
    return 0

  sys.stdout.write('Ce n\'est pas bon...\n')
  return 1


if __name__ == '__main__':
  ret = main(len(sys.argv), sys.argv)
  sys.exit(ret)

# python -m compileall -f . ; mv bin06.pyc bin06 ; chmod +x bin06
