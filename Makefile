CC       = nuitka3
CC_FLAGS = --onefile --disable-console --output-filename=Rezi-PBP.exe
FILE     = Rezi-PBP.py
DEPS     = requirements.txt
PM       = pip

rezi:
	$(CC) --quiet $(CC_FLAGS) $(FILE)

rezi-verb:
	$(CC) --verbose $(CC_FLAGS) $(FILE)

deps:
	$(PM) install -r $(DEPS)