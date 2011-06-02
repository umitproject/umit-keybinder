default: all

all:
	cd bind; python setup.py build_ext -f -b ../
	cp *.py umit/libkeybinder/
	cp *.so umit/libkeybinder/
clean:
	rm -rf *.so
